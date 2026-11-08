#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate.py — Kiểm tra tính toàn vẹn của Leadership Knowledge Base.

Thực hiện các kiểm tra ở CLAUDE.md §10.

Phân biệt hai mức:
  ERROR   — phải sửa trước khi commit (CLAUDE.md §12).
  WARNING — ghi nhận, không chặn commit. Dùng cho trạng thái hợp lệ của kho
            chưa hoàn thiện (chưa có chunk, topic chưa xử lý, tài liệu mới
            chưa đưa vào kho).

Chạy:  python3 scripts/validate.py
Mã thoát: 0 nếu không có ERROR, 1 nếu có.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "kb")
INDEX = os.path.join(KB, "00_index")
RAW = os.path.join(ROOT, "raw")

CHUNK_DIRS = {
    "CON": "01_concepts",
    "FW": "02_frameworks",
    "PRB": "03_problems",
    "PB": "04_playbook",
    "TOP": "05_topics",
    "CASE": "06_cases",
}

VALID_LEVELS = {"SELF", "TEAM", "ORG"}
VALID_TYPES = {"concept", "principle", "framework", "problem",
               "playbook", "topic", "case", "tool", "exercise"}
VALID_SOURCE_TYPES = {"course", "external", "inferred", "mixed"}
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_STATUS = {"verified", "needs_review", "deprecated"}

REQUIRED_FIELDS = ["id", "type", "title_vi", "keywords", "courses",
                   "source", "source_type", "confidence", "status",
                   "last_updated"]

VAGUE_PHRASES = ["như trên", "mô hình này", "phần trước", "nói trên",
                 "framework này", "ở trên", "bên trên"]

ID_RE = re.compile(r"^(CON|FW|PRB|PB|CASE)-\d{3}(-\d{2})?$|^TOP-[A-Z0-9]+-\d{2}$")

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


# ---------------------------------------------------------------- frontmatter

def parse_frontmatter(text, path):
    """Trả về dict thô của khối YAML frontmatter. Parser tối giản, đủ cho schema
    ở CLAUDE.md §6 (giá trị vô hướng hoặc list dạng [a, b, c] / ["a", "b"])."""
    if not text.startswith("---"):
        err("%s: thiếu frontmatter (file không bắt đầu bằng '---')" % path)
        return None
    end = text.find("\n---", 3)
    if end == -1:
        err("%s: frontmatter không được đóng bằng '---'" % path)
        return None
    block = text[3:end]
    fm = {}
    for line in block.split("\n"):
        line = line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        if line[0] in " \t":           # dòng nối tiếp, bỏ qua
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.split(" #")[0].strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            items = []
            if inner:
                for it in re.findall(r'"[^"]*"|\'[^\']*\'|[^,]+', inner):
                    it = it.strip().strip('"').strip("'").strip()
                    if it:
                        items.append(it)
            fm[key] = items
        else:
            fm[key] = val.strip('"').strip("'")
    return fm


def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


# ---------------------------------------------------------------- thu thập

def collect_chunks():
    chunks = {}
    for prefix, sub in CHUNK_DIRS.items():
        d = os.path.join(KB, sub)
        if not os.path.isdir(d):
            err("thiếu thư mục kb/%s/" % sub)
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md"):
                continue
            path = os.path.join(d, name)
            rel = os.path.relpath(path, ROOT)
            text = open(path, encoding="utf-8").read()
            fm = parse_frontmatter(text, rel)
            if fm is None:
                continue
            cid = fm.get("id", "")
            if not cid:
                err("%s: thiếu trường 'id'" % rel)
                continue
            if name[:-3] != cid:
                err("%s: id '%s' không khớp tên file" % (rel, cid))
            if not cid.startswith(prefix + "-"):
                err("%s: id '%s' nằm sai thư mục (kỳ vọng tiền tố %s)"
                    % (rel, cid, prefix))
            if not ID_RE.match(cid):
                err("%s: id '%s' sai định dạng" % (rel, cid))
            if cid in chunks:
                err("id trùng lặp '%s': %s và %s"
                    % (cid, chunks[cid]["rel"], rel))
                continue
            body = text[text.find("\n---", 3) + 4:]
            chunks[cid] = {"fm": fm, "rel": rel, "body": body,
                           "prefix": prefix}
    return chunks


def read_index(name):
    p = os.path.join(INDEX, name)
    if not os.path.isfile(p):
        err("thiếu kb/00_index/%s" % name)
        return ""
    return open(p, encoding="utf-8").read()


# ---------------------------------------------------------------- kiểm tra

def check_frontmatter(chunks):
    for cid, c in chunks.items():
        fm, rel = c["fm"], c["rel"]
        for f in REQUIRED_FIELDS:
            if f not in fm:
                err("%s: thiếu trường bắt buộc '%s'" % (rel, f))
        t = fm.get("type", "")
        if t and t not in VALID_TYPES:
            err("%s: type '%s' không hợp lệ" % (rel, t))
        st = fm.get("source_type", "")
        if st and st not in VALID_SOURCE_TYPES:
            err("%s: source_type '%s' không hợp lệ" % (rel, st))
        cf = fm.get("confidence", "")
        if cf and cf not in VALID_CONFIDENCE:
            err("%s: confidence '%s' không hợp lệ" % (rel, cf))
        stt = fm.get("status", "")
        if stt and stt not in VALID_STATUS:
            err("%s: status '%s' không hợp lệ" % (rel, stt))
        if stt == "deprecated" and not fm.get("replaced_by"):
            warn("%s: status deprecated nhưng chưa có replaced_by" % rel)
        d = fm.get("last_updated", "")
        if d and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(d)):
            err("%s: last_updated '%s' phải dạng YYYY-MM-DD" % (rel, d))


def check_levels(chunks, topic_levels):
    for cid, c in chunks.items():
        if c["prefix"] == "CASE":
            continue
        lv = as_list(c["fm"].get("levels"))
        if not lv:
            err("%s: thiếu 'levels' (bắt buộc với mọi chunk trừ CASE)"
                % c["rel"])
            continue
        bad = [x for x in lv if x not in VALID_LEVELS]
        if bad:
            err("%s: levels không hợp lệ %s (chỉ SELF, TEAM, ORG)"
                % (c["rel"], bad))
        if c["prefix"] == "TOP" and cid in topic_levels:
            want = topic_levels[cid]
            if set(lv) != want:
                err("%s: levels %s không khớp topic_map.md %s"
                    % (c["rel"], sorted(lv), sorted(want)))


def check_links(chunks, course_codes):
    ids = set(chunks)
    for cid, c in chunks.items():
        fm, rel = c["fm"], c["rel"]
        for field in ("related_ids", "problems_addressed", "topics"):
            for ref in as_list(fm.get(field)):
                if ref not in ids:
                    err("%s: %s trỏ tới ID không tồn tại '%s'"
                        % (rel, field, ref))
        rb = fm.get("replaced_by")
        if rb and rb not in ids:
            err("%s: replaced_by trỏ tới ID không tồn tại '%s'" % (rel, rb))
        for code in as_list(fm.get("courses")):
            if code not in course_codes:
                err("%s: mã khóa '%s' không có trong courses.md" % (rel, code))


def check_fw_prb(chunks):
    fws = [c for c in chunks.values() if c["prefix"] == "FW"]
    prbs = [c for c in chunks.values() if c["prefix"] == "PRB"]
    for c in fws:
        if not as_list(c["fm"].get("problems_addressed")):
            err("%s: FW phải liên kết ít nhất một PRB qua problems_addressed"
                % c["rel"])
    referenced = set()
    for c in fws:
        referenced.update(as_list(c["fm"].get("problems_addressed")))
    for c in prbs:
        pid = c["fm"].get("id")
        rel_ids = as_list(c["fm"].get("related_ids"))
        has_fw = any(r.startswith("FW-") for r in rel_ids)
        if pid not in referenced and not has_fw:
            err("%s: PRB chưa được FW nào trỏ tới và cũng không trỏ tới FW nào"
                % c["rel"])


def check_body(chunks):
    for cid, c in chunks.items():
        body = c["body"]
        words = len(body.split())
        if words > 800:
            warn("%s: %d từ, vượt 800 — cân nhắc tách chunk con" % (c["rel"], words))
        low = body.lower()
        found = [p for p in VAGUE_PHRASES if p in low]
        if found:
            warn("%s: chứa cụm mơ hồ %s — chunk phải tự đứng được"
                 % (c["rel"], found))


def check_catalog(chunks, catalog_text):
    if not chunks:
        if "0 chunk" not in catalog_text and "chưa có" not in catalog_text:
            warn("catalog.md không ghi nhận trạng thái kho rỗng")
        return
    for cid in sorted(chunks):
        if cid not in catalog_text:
            err("catalog.md thiếu chunk '%s'" % cid)


def check_raw(course_dirs, topic_map_text, inventory_text):
    if not os.path.isdir(RAW):
        warn("không có thư mục raw/ — bỏ qua kiểm tra tài liệu gốc")
        return
    for entry in sorted(os.listdir(RAW)):
        p = os.path.join(RAW, entry)
        if not os.path.isdir(p) or entry.startswith("."):
            continue
        if entry not in course_dirs:
            warn("có tài liệu mới chưa xử lý: thư mục raw/%s/ chưa có trong "
                 "courses.md — chạy lệnh \"Lập inventory %s\"" % (entry, entry))
            continue
        for fn in sorted(os.listdir(p)):
            if fn.startswith(".") or os.path.isdir(os.path.join(p, fn)):
                continue
            if fn not in topic_map_text:
                warn("có tài liệu mới chưa xử lý: raw/%s/%s chưa có trong "
                     "topic_map.md" % (entry, fn))
            if fn not in inventory_text:
                warn("có tài liệu mới chưa xử lý: raw/%s/%s chưa có trong "
                     "slide_inventory.md" % (entry, fn))


def check_coverage(topic_status, coverage_text):
    for tid, (status, files) in topic_status.items():
        if status != "đã xử lý":
            continue
        for fn in files:
            if fn not in coverage_text:
                err("%s đã xử lý nhưng file '%s' không có trong "
                    "coverage_matrix.md" % (tid, fn))


# ---------------------------------------------------------------- đọc index

def parse_course_codes(text):
    """Mã khóa lấy từ cột đầu của bảng khóa học, thư mục lấy từ cột `raw/.../`
    của chính dòng đó — không quét cả file, để không nhầm tên pillar hay level
    thành mã khóa."""
    codes, dirs = set(), set()
    for line in text.split("\n"):
        m = re.match(r"^\|\s*`([A-Z][A-Z0-9_]*)`\s*\|", line)
        if not m:
            continue
        codes.add(m.group(1))
        d = re.search(r"`raw/([^/`]+)/`", line)
        if d:
            dirs.add(d.group(1))
    return codes, dirs


def parse_topic_map(text):
    """Trả về (levels theo TOP id, trạng thái + file theo TOP id)."""
    levels, status = {}, {}
    for line in text.split("\n"):
        if not line.startswith("| `TOP-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 9:
            continue
        tid = cells[0].strip("`")
        lv = {x.strip() for x in re.split(r"[+,]", cells[4]) if x.strip()}
        lv = {x for x in lv if x in VALID_LEVELS}
        fn = cells[5].strip("`")
        st = cells[7].replace("*", "").strip()
        if tid in levels:
            levels[tid] |= lv
            status[tid][1].append(fn)
        else:
            levels[tid] = lv
            status[tid] = (st, [fn])
    return levels, status


# ---------------------------------------------------------------- main

def main():
    for sub in ["00_index"] + list(CHUNK_DIRS.values()):
        if not os.path.isdir(os.path.join(KB, sub)):
            err("thiếu thư mục kb/%s/" % sub)
    for d in ("export", "scripts"):
        if not os.path.isdir(os.path.join(ROOT, d)):
            warn("thiếu thư mục %s/" % d)

    courses_text = read_index("courses.md")
    topic_map_text = read_index("topic_map.md")
    inventory_text = read_index("slide_inventory.md")
    catalog_text = read_index("catalog.md")
    for n in ("README.md", "problem_index.md", "glossary.md",
              "coverage_matrix.md", "changelog.md", "open_questions.md"):
        read_index(n)
    coverage_text = read_index("coverage_matrix.md")

    course_codes, course_dirs = parse_course_codes(courses_text)
    topic_levels, topic_status = parse_topic_map(topic_map_text)

    chunks = collect_chunks()

    check_frontmatter(chunks)
    check_levels(chunks, topic_levels)
    check_links(chunks, course_codes)
    check_fw_prb(chunks)
    check_body(chunks)
    check_catalog(chunks, catalog_text)
    check_raw(course_dirs, topic_map_text, inventory_text)
    check_coverage(topic_status, coverage_text)

    if not chunks:
        warn("kho chưa có chunk nào (hợp lệ sau bước inventory) — "
             "chạy \"Xử lý <khóa> topic X–Y\" để bắt đầu")

    n_done = sum(1 for s, _ in topic_status.values() if s == "đã xử lý")
    print("=" * 62)
    print("VALIDATE — Leadership Knowledge Base")
    print("=" * 62)
    print("Chunk:   %d" % len(chunks))
    print("Khóa:    %d (%s)" % (len(course_codes), ", ".join(sorted(course_codes))))
    print("Topic:   %d, đã xử lý %d" % (len(topic_status), n_done))
    print("-" * 62)

    for w in warnings:
        print("WARNING  %s" % w)
    for e in errors:
        print("ERROR    %s" % e)

    print("-" * 62)
    print("%d ERROR, %d WARNING" % (len(errors), len(warnings)))
    if errors:
        print("Không được commit khi còn ERROR (CLAUDE.md §12).")
    else:
        print("Không có ERROR.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
