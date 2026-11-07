# Leadership Knowledge Base — Hướng dẫn sử dụng

Kho tri thức Markdown thống nhất cho mọi khóa học Leadership mà người dùng tham gia. Một kho chung, **không** chia kho theo khóa học.

Phục vụ hai nhóm:
- **Người dùng (con người):** tra cứu nhanh, áp dụng ngay. Bắt đầu từ `QUICK_REFERENCE.md` hoặc `problem_index.md`.
- **Agent khác (Claude Project, RAG):** truy xuất chính xác từng chunk mà không cần đọc cả kho.

## 1. Cách tra cứu

| Bạn muốn | Mở file |
|---|---|
| Tổng quan nhanh theo level | `../QUICK_REFERENCE.md` |
| "Tôi đang gặp vấn đề X, dùng framework nào?" | `problem_index.md` |
| Danh sách mọi chunk trong kho | `catalog.md` |
| Khóa học nào, cấu trúc ra sao | `courses.md` |
| Topic nào nằm ở file nào, đã xử lý chưa | `topic_map.md` |
| Trang slide nào nói về cái gì | `slide_inventory.md` |
| Trang slide đã được đưa vào chunk nào | `coverage_matrix.md` |
| Thuật ngữ Việt–Anh | `glossary.md` |
| Điều gì còn chưa chắc chắn | `open_questions.md` |
| Lịch sử cập nhật kho | `changelog.md` |

## 2. Quy ước ID

| Tiền tố | Loại | Thư mục | Cách đánh số |
|---|---|---|---|
| `CON` | Khái niệm / nguyên tắc | `kb/01_concepts/` | Chung toàn kho, 3 chữ số: `CON-001` |
| `FW` | Framework | `kb/02_frameworks/` | Chung toàn kho: `FW-001`; chunk con `FW-003-01` |
| `PRB` | Vấn đề | `kb/03_problems/` | Chung toàn kho: `PRB-001` |
| `PB` | Playbook | `kb/04_playbook/` | Chung toàn kho: `PB-001` |
| `TOP` | Topic của một khóa | `kb/05_topics/` | Theo khóa: `TOP-<MÃ KHÓA>-<NN>`, ví dụ `TOP-MEGROW-04` |
| `CASE` | Tình huống thực tế | `kb/06_cases/` | Chung toàn kho: `CASE-001` |

**ID là vĩnh viễn.** Không đổi, không tái sử dụng. Chunk bị gộp hoặc loại bỏ thì **giữ file**, đặt `status: deprecated` và `replaced_by: <ID>`.

Mã khóa học (`MEGROW`, …): chữ in hoa, không dấu, không ký tự đặc biệt. Đặt một lần và không bao giờ đổi.

## 3. Ba nhãn nội dung

Mọi đoạn nội dung mang đúng một nhãn:

| Nhãn | Nghĩa |
|---|---|
| `[KHÓA HỌC]` | Có thật trong tài liệu của một khóa học trong `raw/`. Khóa cụ thể xem ở `source`. |
| `[BỔ SUNG]` | Kiến thức bên ngoài khóa học. Ghi nguồn nếu có. |
| `[SUY LUẬN]` | Diễn giải hoặc kết nối do Claude thực hiện. |

Hai nhãn trạng thái dùng kèm:

| Nhãn | Nghĩa |
|---|---|
| `[CẦN XÁC NHẬN]` | Slide thiếu thông tin, không tự điền từ trí nhớ. Có mục tương ứng trong `open_questions.md`. |
| `[KHÓ ĐỌC]` | Slide mờ, OCR lỗi, sơ đồ không đọc được. Ghi nguyên trạng. |

**Không** gắn `[KHÓA HỌC]` cho nội dung không có trong tài liệu. **Không** mặc định khóa học có các framework phổ biến (GROW, ADKAR, RACI…).

## 4. Định dạng nguồn

`[MÃ KHÓA | Topic XX | tên_file | Slide Y]`

Ví dụ: `[MEGROW | Topic 04 | Topic 4 - Practice Performance Conversations - AP Elaine Chew.pdf | Slide 22]`

Một framework xuất hiện ở nhiều topic hoặc nhiều khóa: chỉ có **MỘT** chunk `FW`, liệt kê mọi nguồn trong `source`, ghi rõ mỗi topic bổ sung góc nhìn gì.

## 5. Schema frontmatter

```yaml
---
id: FW-001
type: framework          # concept | principle | framework | problem | playbook | topic | case | tool | exercise
title_vi: Mô hình Lãnh đạo Tình huống
title_en: Situational Leadership
aliases: [SLII, lãnh đạo theo tình huống]
keywords: [giao việc, delegation, mức độ sẵn sàng, readiness]
levels: [TEAM]           # SELF | TEAM | ORG — có thể nhiều giá trị
courses: [MEGROW]
topics: [TOP-MEGROW-04, TOP-MEGROW-09]
problems_addressed: [PRB-003, PRB-007]
related_ids: [FW-004, CON-012]
source: ["MEGROW | Topic 04 | topic04.pdf | Slide 14–18"]
source_type: course      # course | external | inferred | mixed
confidence: high         # high | medium | low
status: verified         # verified | needs_review | deprecated
replaced_by:
last_updated: YYYY-MM-DD
---
```

## 6. Hai trục phân loại

- **Level** (chung cho mọi khóa): `SELF` lãnh đạo bản thân · `TEAM` lãnh đạo đội nhóm · `ORG` lãnh đạo tổ chức và chiến lược. Một chunk có thể có nhiều level.
- **Khóa học và cấu trúc riêng của khóa** (pillar, module, topic): ghi trong `courses`, `topics` của chunk và trong `topic_map.md`.

### Về taxonomy pillar của MEGROW

Ánh xạ topic → pillar của khóa MEGROW là **taxonomy tri thức do người dùng duyệt ngày 2026-11-07**, **không phải cấu trúc pillar chính thức của RMIT đã kiểm chứng** — không slide nào trong `raw/megrow/` ghi pillar. Nhãn: `[SUY LUẬN — người dùng duyệt]`. Chi tiết trong `courses.md`; mục đối chiếu trong `open_questions.md`.

Ràng buộc người dùng đặt ra cho taxonomy này:

1. **Giữ nguyên số topic gốc và mọi tham chiếu nguồn.**
2. **Cho phép quan hệ framework xuyên pillar** — `related_ids` không bị giới hạn trong cùng một pillar.
3. **Không giới hạn truy xuất theo pillar chính.** Pillar chỉ quyết định level *chính* của topic. Một chunk được gán thêm level phụ khi nội dung thực sự thuộc về level đó — ví dụ Topic 13 (Building Trust in Teams) nằm ở P3 nhưng nội dung là TEAM, nên chunk của nó dùng `levels: [ORG, TEAM]`.

## 7. Quy tắc viết chunk

- Một file = một chunk = một khái niệm / framework / vấn đề / playbook / topic / case. Khoảng **150–600 từ**. Dài hơn thì tách chunk chính và chunk con.
- Chunk phải **tự đứng được**: không dùng "như trên", "mô hình này", "phần trước". Luôn nhắc lại tên đầy đủ.
- 1–2 câu đầu là tóm tắt: *đây là gì, dùng khi nào*.
- `keywords` song ngữ, kèm từ đồng nghĩa và cách người dùng hay mô tả vấn đề bằng lời thường.
- Liên kết bằng **ID**, không bằng tiêu đề.
- Thông tin trong bảng hoặc sơ đồ phải có phần diễn giải bằng văn bản đi kèm.
- Heading thống nhất theo template của từng loại (CLAUDE.md §7).
- Ngôn ngữ: tiếng Việt. Thuật ngữ và tên framework giữ tiếng Anh, kèm nghĩa tiếng Việt ở lần xuất hiện đầu tiên trong **mỗi** chunk.
- CASE luôn **ẩn danh**: không tên thật, không thông tin nhận dạng đồng nghiệp.

## 8. Công cụ

```bash
python3 scripts/validate.py     # kiểm tra tính toàn vẹn kho
python3 scripts/export.py       # sinh bản gộp trong export/ để upload lên Claude Project
```

`validate.py` phân biệt **ERROR** (phải sửa trước khi commit) và **WARNING** (ghi nhận, không chặn).

Đọc PDF cần poppler: `brew install poppler` (cung cấp `pdftotext` và `pdftoppm`).

## 9. Trạng thái hiện tại

Kho đang ở giai đoạn **sau inventory MEGROW**: đã lập bản đồ 22 tài liệu / 805 trang, **chưa tạo chunk kiến thức nào**. Bước tiếp theo: lệnh `Xử lý megrow topic X–Y` (tối đa 3 topic mỗi lần).
