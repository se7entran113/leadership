# changelog.md — Lịch sử cập nhật kho

Mới nhất ở trên cùng.

---

## 2026-11-08 — MEGROW Topic 04, 08, 09: thêm 19 chunk (tổng 67)

**Lệnh:** `Xử lý megrow topic 4, 8, 9` (CLAUDE.md §9)

Ba topic cùng đợt vì cùng phục vụ **vấn đề ưu tiên số 6** — feedback, coaching và trao đổi về hiệu suất.

### Chunk đã tạo (19)

**Framework (11):** `FW-023` AMO · `FW-024` SAIL · `FW-025` NOTICE→CONVERSE→COACH→HOLD ACCOUNTABLE · `FW-025-01` Ma trận Support × Accountability · `FW-026` 5-Impact Test · `FW-027` Bốn kiểu quản lý · `FW-028` Năm lăng kính chẩn đoán · `FW-029` Thang mức sẵn sàng phát triển · `FW-030` Lộ trình D–R–C · `FW-031` EDGE và VRIFA · `FW-032` Connector Manager

**Khái niệm (4):** `CON-010` Phép thử camera · `CON-011` Ba cấp độ lắng nghe · `CON-012` Vấn đề tổ chức khoác áo vấn đề nhân viên · `CON-013` Tự nhận thức và tự quản lý

**Vấn đề (1):** `PRB-006` Feedback, coaching và trao đổi về hiệu suất

**Topic (3):** `TOP-MEGROW-04` · `TOP-MEGROW-08` · `TOP-MEGROW-09`

### Quyết định đáng ghi
- **`FW-023` AMO và `FW-028` năm lăng kính để riêng, không gộp.** Chúng là hai bản chẩn đoán khác độ chi tiết: AMO ba nhánh cho hội thoại về *hiệu suất chưa đạt*; năm lăng kính tách Knowledge khỏi Skills và thêm nhánh **Career** cho hội thoại về *phát triển*. Mục "Phân biệt với framework gần giống" của cả hai ghi rõ khác biệt này.
- **Tách `FW-025-01`** (ma trận Support × Accountability) khỏi `FW-025` để chunk chính không vượt ngưỡng.
- **`FW-031` để `needs_review`**: slide 37–38 ghi nguồn là *"Dr Quyen Dang through experience and knowledge from different models"* — khung tổng hợp của giảng viên, không có tài liệu gốc đối chiếu. VRIFA nhiều khả năng phỏng theo VRIN của Topic 17.
- **Cập nhật ngược:** `PRB-004` (thêm `CON-013`), `PRB-005` (thêm `FW-028`, `FW-029`, `FW-031`), `PRB-007` (thêm Topic 09), `PRB-010` (thêm `FW-026`, `CON-010`), `CON-002`.
- **`CON-014` đổi số thành `CON-013`** trước khi commit để không để trống ID trong dãy.
- **OQ-002 được củng cố:** Topic 04 slide 10 nhắc *"audited mindset"* của Topic 03, và Topic 03 slide 28 nói rõ hai buổi diễn ra cùng ngày (sáng Topic 03, chiều Topic 04) — xác nhận thứ tự theo tên file.

### Index đã cập nhật
`catalog.md` (67 chunk, sinh bằng `gen_catalog.py`) · `coverage_matrix.md` (375/805 trang, 46.6%, 9/20 topic) · `topic_map.md` · `problem_index.md` · `glossary.md` (thêm 20 thuật ngữ, 2 nhóm mới) · `open_questions.md`

---

## 2026-11-08 — MEGROW Topic 12, 19, 14: thêm 22 chunk (tổng 48)

**Lệnh:** `Xử lý megrow topic 12, 19, 14` (CLAUDE.md §9)

Ba topic chọn cùng đợt vì cùng phục vụ **vấn đề ưu tiên Cao số 2** — làm việc với stakeholder khi không có quyền chỉ đạo.

### Chunk đã tạo (22)

**Framework (13):** `FW-011` Stakeholder Theory · `FW-012` Power–Interest Matrix · `FW-013` The Leadership Challenge · `FW-014` Sources of Social Power · `FW-015` Influence Without Authority · `FW-016` Thomas–Kilmann · `FW-017` Kotter Coalitions · `FW-018` SCQA · `FW-019` Pyramid Principle & MECE · `FW-019-01` Action titles · `FW-020` Ladder of Inference · `FW-021` Inquiry before Advocacy · `FW-022` chuỗi sáu chặng MAP→ACT

**Khái niệm (3):** `CON-007` Pre-wiring · `CON-008` Đừng tranh cãi với mục tiêu của họ · `CON-009` Mời góp ý và vẫn giữ quyền chốt

**Vấn đề (3):** `PRB-002` (Cao, người dùng nêu đích danh) · `PRB-008` · `PRB-010`

**Topic (3):** `TOP-MEGROW-12` · `TOP-MEGROW-19` · `TOP-MEGROW-14`

### Quyết định đáng ghi
- **`FW-012` Power–Interest Matrix gộp hai nguồn** (Topic 12 slide 8–11 và Topic 19 slide 24–25) thành MỘT chunk, ghi rõ mỗi topic bổ sung góc nhìn gì.
- **`FW-022`** được tạo riêng cho chuỗi sáu chặng của Topic 12 vì nó là điểm vào truy xuất cho câu hỏi "làm việc với stakeholder bắt đầu từ đâu".
- **Tách `FW-019-01`** (action title, skim test) khỏi `FW-019` để chunk chính không vượt ngưỡng độ dài.
- **Hai case reading đã xử lý cùng topic chủ:** Microsoft → Topic 12 (`FW-013`), BCPC → Topic 14 (`FW-020`, `TOP-MEGROW-14`). Không tạo chunk `CASE` — loại đó dành cho tình huống thực tế của người dùng.
- **Cập nhật ngược chunk cũ:** `FW-006` (liên kết `CON-009`), `PRB-003` (thêm Topic 14), `PRB-011` (thêm Kotter từ Topic 12).
- Thêm **OQ-009**: Topic 12 ghi chặng TRUST dựa trên Edmondson nhưng không có slide nào giải thích.

### Index đã cập nhật
`catalog.md` (48 chunk) · `coverage_matrix.md` (231/805 trang, 28.7%, chi tiết từng slide cho 6 topic) · `topic_map.md` (6 topic `đã xử lý`) · `problem_index.md` · `glossary.md` (thêm 36 thuật ngữ, 3 nhóm mới) · `open_questions.md`

### Công cụ mới
`scripts/gen_catalog.py` — sinh lại các bảng chunk trong `catalog.md` từ frontmatter, kèm `scripts/catalog_summaries.txt` giữ tóm tắt một dòng biên tập tay. Trước đó catalog phải sửa tay và đã sót chunk.

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
