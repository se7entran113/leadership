# changelog.md — Lịch sử cập nhật kho

Mới nhất ở trên cùng.

---

## 2026-11-07 — Khởi tạo kho + inventory MEGROW

**Lệnh:** `Lập inventory megrow` (CLAUDE.md §9)

### Hạ tầng
- Cài `poppler` qua Homebrew để đọc PDF: `pdftotext` (trích text theo trang, giữ layout) và `pdftoppm` (render trang thành ảnh cho việc đọc bằng thị giác). Đáp ứng CLAUDE.md §8.
- Tạo khung thư mục: `kb/00_index/`, `kb/01_concepts/`, `kb/02_frameworks/`, `kb/03_problems/`, `kb/04_playbook/`, `kb/05_topics/`, `kb/06_cases/`, `export/`, `scripts/`.
- Viết `scripts/validate.py` và `scripts/export.py` theo CLAUDE.md §10.

### Đăng ký khóa học
- Thêm khóa `MEGROW` — me.grow (2026) L2 Leadership Development Program, The Business School RMIT University Vietnam × Zalo — vào `courses.md`.
- Ánh xạ pillar → level theo taxonomy người dùng duyệt: P1 `LEAD_SELF` = Topic 1–5 (SELF), P2 `LEAD_PEOPLE_AND_TEAMS` = Topic 6–11 (TEAM), P3 `LEAD_ACROSS_ORGANISATION` = Topic 12–20 (ORG). Nhãn `[SUY LUẬN — người dùng duyệt]`, không phải cấu trúc RMIT chính thức đã kiểm chứng.

### Inventory
- Quét `raw/megrow/`: **22 tài liệu, 805 trang** (20 deck topic + 2 case reading).
- Lập `topic_map.md`: 20 topic, mỗi topic có ID `TOP-MEGROW-NN`, pillar, level chính + level phụ, file, số trang, trạng thái `chưa xử lý`.
- Lập `slide_inventory.md`: chủ đề của cả 805 trang ở mức tiêu đề.
  - 668 trang trích được text bằng `pdftotext`.
  - 137 trang không trích được text (slide dạng ảnh, chủ yếu ở Topic 5: 65/78 trang và Topic 6: 49/69 trang) — đã **đọc bằng thị giác** và mô tả, đánh dấu `[HÌNH]`.
  - Không có trang nào phải gắn `[KHÓ ĐỌC]`.
- Khởi tạo `catalog.md`, `coverage_matrix.md`, `glossary.md` ở trạng thái rỗng-có-cấu-trúc.
- Dựng sẵn `problem_index.md` với 11 vấn đề ưu tiên của người dùng (CLAUDE.md §2) kèm danh sách framework ứng viên `[SUY LUẬN]` nhận diện từ tiêu đề trang.
- Mở 5 mục trong `open_questions.md` (OQ-001 … OQ-005).

### Chưa làm (đúng theo §9.7)
- **Không tạo chunk kiến thức nào.** Kho hiện có 0 chunk.
- Không chạy export.
