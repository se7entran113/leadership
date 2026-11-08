#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_catalog.py — Sinh lại các bảng chunk trong kb/00_index/catalog.md từ frontmatter.

Giữ nguyên phần đầu (tiêu đề, bảng đếm) và phần cuối (bộ đếm ID, bảng đặt chỗ PRB);
chỉ thay sáu bảng ở giữa. Tóm tắt một dòng lấy từ dòng `summary:` trong frontmatter
nếu có, nếu không thì lấy từ bảng SUMMARY bên dưới (biên tập tay).

Chạy: python3 scripts/gen_catalog.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "kb")
CAT = os.path.join(KB, "00_index", "catalog.md")

SECTIONS = [
    ("01_concepts", "Khái niệm & nguyên tắc (CON)"),
    ("02_frameworks", "Framework (FW)"),
    ("03_problems", "Vấn đề (PRB)"),
    ("04_playbook", "Playbook (PB)"),
    ("05_topics", "Topic (TOP)"),
    ("06_cases", "Tình huống thực tế (CASE)"),
]

EMPTY_NOTE = {
    "04_playbook": '_(chưa có — viết ở bước "Rà soát tổng thể" sau khi xử lý xong các topic)_',
    "06_cases": '_(chưa có — tạo bằng lệnh "Thêm case")_',
}


def fm(path):
    t = open(path, encoding="utf-8").read()
    head = t[3:t.find("\n---", 3)]
    d = {}
    for line in head.split("\n"):
        if ":" not in line or line[:1] in " \t":
            continue
        k, _, v = line.partition(":")
        d[k.strip()] = v.split(" #")[0].strip().strip('"')
    return d


def sortkey(cid):
    m = re.match(r"^([A-Z]+)(?:-([A-Z0-9]+))?-(\d+)(?:-(\d+))?$", cid)
    if not m:
        return (cid, 0, 0)
    return (m.group(1) + (m.group(2) or ""), int(m.group(3)), int(m.group(4) or 0))


def main():
    # tóm tắt một dòng, biên tập tay — key là id
    summaries = {}
    for line in open(os.path.join(ROOT, "scripts", "catalog_summaries.txt"),
                     encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        cid, _, s = line.partition("\t")
        summaries[cid.strip()] = s.strip()

    counts, blocks = {}, []
    missing = []
    for sub, title in SECTIONS:
        d = os.path.join(KB, sub)
        rows = []
        ids = []
        for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if not n.endswith(".md"):
                continue
            ids.append(n[:-3])
        for cid in sorted(ids, key=sortkey):
            f = fm(os.path.join(d, cid + ".md"))
            vi, en = f.get("title_vi", ""), f.get("title_en", "")
            name = "%s (%s)" % (vi, en) if en and en.lower() != vi.lower() else vi
            lv = f.get("levels", "").strip("[]")
            co = f.get("courses", "").strip("[]")
            st = f.get("status", "")
            tag = "" if st == "verified" else " `%s`" % st
            s = summaries.get(cid)
            if s is None:
                missing.append(cid); s = "_(chưa có tóm tắt)_"
            rows.append("| `%s` | %s%s | %s | %s | %s | %s |"
                        % (cid, name, tag, f.get("type", ""), lv, co, s))
        counts[sub] = len(rows)
        body = ("| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |\n"
                "|---|---|---|---|---|---|\n")
        if rows:
            body += "\n".join(rows)
        else:
            body += "| %s | | | | | |" % EMPTY_NOTE.get(sub, "_(chưa có)_")
        blocks.append("## %s\n\n%s" % (title, body))

    if missing:
        print("THIẾU tóm tắt cho:", ", ".join(missing))
        return 1

    total = sum(counts.values())
    t = open(CAT, encoding="utf-8").read()
    head_end = t.index("\n---\n\n## ")
    tail_start = t.index("\n---\n\n## Bộ đếm ID tiếp theo")
    head, tail = t[:head_end], t[tail_start:]

    head = re.sub(r"\*\*Trạng thái kho: \d+ chunk\.\*\*",
                  "**Trạng thái kho: %d chunk.**" % total, head)
    for sub, label in [("01_concepts", "`CON` Khái niệm & nguyên tắc"),
                       ("02_frameworks", "`FW` Framework"),
                       ("03_problems", "`PRB` Vấn đề"),
                       ("04_playbook", "`PB` Playbook"),
                       ("05_topics", "`TOP` Topic"),
                       ("06_cases", "`CASE` Tình huống thực tế")]:
        head = re.sub(r"\| %s \| *\d+ \|" % re.escape(label),
                      "| %s | %d |" % (label, counts[sub]), head)
    head = re.sub(r"\| \*\*Tổng\*\* \| \*\*\d+\*\* \|",
                  "| **Tổng** | **%d** |" % total, head)

    open(CAT, "w", encoding="utf-8").write(head + "\n---\n\n"
                                           + "\n\n".join(blocks) + tail)
    print("catalog.md: %d chunk (%s)" % (total, ", ".join(
        "%s=%d" % (s.split('_')[1], counts[s]) for s, _ in SECTIONS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
