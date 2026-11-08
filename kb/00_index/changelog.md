# changelog.md — Lịch sử cập nhật kho

Mới nhất ở trên cùng.

---

## 2026-11-08 — MEGROW Topic 01, 06, 10: 26 chunk đầu tiên

**Lệnh:** `Xử lý megrow topic 1, 10, 6` (CLAUDE.md §9)

Ba topic được chọn cùng đợt vì cả ba cùng dạy Situational Leadership — xử lý chung để gộp thành MỘT chunk `FW` ngay từ đầu thay vì phải gộp lại về sau.

### Chunk đã tạo (26)

**Framework (12):** `FW-001` Situational Leadership · `FW-001-01` Skill × Will Matrix · `FW-001-02` Ba biến thể trong MEGROW · `FW-002` Five Myths of the New Manager · `FW-003` First 90 Days & STARS · `FW-004` Four Stages of Contribution · `FW-005` Leadership Grid · `FW-006` Vroom–Yetton–Jago · `FW-007` Transformation Design Framework · `FW-008` Socium 7 đòn bẩy · `FW-009` Psychological Ownership · `FW-010` HAI

**Khái niệm (6):** `CON-001` Chuyển dịch IC → quản lý · `CON-002` Ba cái bẫy · `CON-003` Responsibility/accountability/decision rights · `CON-004` Giao kết quả không giao đầu việc · `CON-005` Có tầm nhìn mà không kiểm soát · `CON-006` Tải nhận thức

**Vấn đề (5):** `PRB-003` · `PRB-004` · `PRB-005` · `PRB-007` · `PRB-011`

**Topic (3):** `TOP-MEGROW-01` · `TOP-MEGROW-06` · `TOP-MEGROW-10`

### Quyết định đáng ghi
- **Gộp Situational Leadership thành một chunk** với ba nguồn (Topic 01 s15, Topic 06 s60, Topic 10 s24–27), tách chunk con `FW-001-01` (công cụ Skill × Will) và `FW-001-02` (đối chiếu ba biến thể) vì chunk chính vượt ngưỡng độ dài.
- **Đặt chỗ `PRB-001`…`PRB-011`** khớp đúng 11 vấn đề ưu tiên ở CLAUDE.md §2; chỉ tạo 5 chunk có nội dung thật từ ba topic này, sáu ID còn lại giữ nguyên chỗ.
- **`PRB-003`, `PRB-007`, `PRB-011` để `needs_review`** vì mới phủ được một phần góc nhìn; phần còn lại nằm ở các topic chưa xử lý.
- **`FW-007`, `FW-008`, `FW-009`, `TOP-MEGROW-06` để `confidence: medium`** vì Topic 06 gần như không có slide văn bản — xem OQ-008.

### Index đã cập nhật
`catalog.md` (25 chunk + bảng đặt chỗ PRB) · `coverage_matrix.md` (132/805 trang, 16.4%, chi tiết từng slide cho 3 topic) · `topic_map.md` (3 topic sang `đã xử lý`) · `problem_index.md` (điền ID chunk, xác nhận framework ứng viên) · `glossary.md` (36 thuật ngữ chuyên môn, chia 4 nhóm) · `open_questions.md` (thêm OQ-006, OQ-007, OQ-008)

### Sửa script
`scripts/validate.py` — parser `parse_topic_map` bỏ dấu `**` trong cột trạng thái, và `parse_course_codes` chỉ đọc cột đầu bảng khóa học thay vì quét cả file (trước đó nhặt nhầm tên pillar và level thành mã khóa).

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
