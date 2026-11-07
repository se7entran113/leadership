#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export.py — Gộp kho tri thức thành các file để upload lên Claude Project.

Theo CLAUDE.md §10. Tên file export cố định, không đổi khi thêm khóa học:

  KB_00_index.md    README, courses, topic_map, catalog, problem_index, glossary
  KB_01_concepts.md
  KB_02_frameworks.md
  KB_03_problems.md
  KB_04_playbook.md
  KB_05_topics.md
  KB_06_cases.md
  QUICK_REFERENCE.md

Mỗi chunk giữ nguyên frontmatter, ngăn cách bằng dòng '====='.
Bỏ qua chunk có status: deprecated.
Không đưa slide_inventory.md, coverage_matrix.md, changelog.md,
open_questions.md vào export.

Chạy:  python3 scripts/export.py
In ra danh sách file trong export/ có nội dung thay đổi so với lần trước
(đó là các file cần upload lại lên Claude Project).
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "kb")
INDEX = os.path.join(KB, "00_index")
EXPORT = os.path.join(ROOT, "export")

SEP = "\n\n=====\n\n"

INDEX_PARTS = [
    ("README.md", "Hướng dẫn sử dụng kho"),
    ("courses.md", "Danh mục khóa học"),
    ("topic_map.md", "Bản đồ topic ↔ tài liệu"),
    ("catalog.md", "Danh mục mọi chunk"),
    ("problem_index.md", "Vấn đề → nguyên nhân → framework"),
    ("glossary.md", "Thuật ngữ Việt–Anh"),
]

CHUNK_EXPORTS = [
    ("01_concepts", "KB_01_concepts.md", "Khái niệm và nguyên tắc (CON)"),
    ("02_frameworks", "KB_02_frameworks.md", "Framework (FW)"),
    ("03_problems", "KB_03_problems.md", "Vấn đề (PRB)"),
    ("04_playbook", "KB_04_playbook.md", "Playbook (PB)"),
    ("05_topics", "KB_05_topics.md", "Topic (TOP)"),
    ("06_cases", "KB_06_cases.md", "Tình huống thực tế (CASE)"),
]


def is_deprecated(text):
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    head = text[3:end]
    return bool(re.search(r"^status:\s*deprecated\s*$", head, re.M))


def build_index():
    parts = [
        "# KB_00_index — Chỉ mục kho tri thức Leadership",
        "",
        "Bản gộp tự động bởi `scripts/export.py`. Không sửa trực tiếp file này;"
        " sửa các file nguồn trong `kb/00_index/` rồi chạy lại export.",
    ]
    for name, title in INDEX_PARTS:
        p = os.path.join(INDEX, name)
        if not os.path.isfile(p):
            parts.append("## %s\n\n_(thiếu file `kb/00_index/%s`)_" % (title, name))
            continue
        parts.append("<!-- nguồn: kb/00_index/%s -->\n\n%s"
                     % (name, open(p, encoding="utf-8").read().rstrip()))
    return SEP.join(parts) + "\n"


def build_chunks(subdir, title):
    d = os.path.join(KB, subdir)
    head = ("# %s\n\nBản gộp tự động bởi `scripts/export.py`."
            " Mỗi chunk giữ nguyên frontmatter, ngăn cách bằng `=====`."
            " Chunk `deprecated` đã bị loại." % title)
    parts = [head]
    n_kept = n_skipped = 0
    if os.path.isdir(d):
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md"):
                continue
            text = open(os.path.join(d, name), encoding="utf-8").read().rstrip()
            if is_deprecated(text):
                n_skipped += 1
                continue
            parts.append(text)
            n_kept += 1
    if n_kept == 0:
        parts.append("_(chưa có chunk nào thuộc nhóm này)_")
    return SEP.join(parts) + "\n", n_kept, n_skipped


def build_quickref():
    p = os.path.join(KB, "QUICK_REFERENCE.md")
    if os.path.isfile(p):
        return open(p, encoding="utf-8").read().rstrip() + "\n"
    return ("# QUICK_REFERENCE\n\n"
            "_(chưa có — sẽ được viết ở bước \"Rà soát tổng thể\" sau khi "
            "xử lý xong các topic.)_\n")


def write_if_changed(path, content):
    old = None
    if os.path.isfile(path):
        old = open(path, encoding="utf-8").read()
    if old == content:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    if not os.path.isdir(KB):
        print("ERROR: không tìm thấy thư mục kb/")
        return 1
    os.makedirs(EXPORT, exist_ok=True)

    outputs = [("KB_00_index.md", build_index(), None, None)]
    for subdir, fname, title in CHUNK_EXPORTS:
        content, kept, skipped = build_chunks(subdir, title)
        outputs.append((fname, content, kept, skipped))
    outputs.append(("QUICK_REFERENCE.md", build_quickref(), None, None))

    changed = []
    print("=" * 62)
    print("EXPORT — Leadership Knowledge Base")
    print("=" * 62)
    for fname, content, kept, skipped in outputs:
        did = write_if_changed(os.path.join(EXPORT, fname), content)
        if did:
            changed.append(fname)
        detail = ""
        if kept is not None:
            detail = "  (%d chunk%s)" % (kept, ", bỏ %d deprecated" % skipped
                                         if skipped else "")
        print("%-22s %-11s %s" % (fname, "ĐÃ ĐỔI" if did else "không đổi", detail))

    print("-" * 62)
    if changed:
        print("Cần upload lại lên Claude Project (%d file):" % len(changed))
        for f in changed:
            print("  - export/%s" % f)
    else:
        print("Không file nào thay đổi — không cần upload lại.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
