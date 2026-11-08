# KB_00_index — Chỉ mục kho tri thức Leadership

=====



=====

Bản gộp tự động bởi `scripts/export.py`. Không sửa trực tiếp file này; sửa các file nguồn trong `kb/00_index/` rồi chạy lại export.

=====

<!-- nguồn: kb/00_index/README.md -->

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

=====

<!-- nguồn: kb/00_index/courses.md -->

# courses.md — Danh mục khóa học

Mỗi khóa học có một mã cố định (chữ in hoa, không dấu). Mã đặt một lần và **không bao giờ đổi**.

| Mã khóa | Tên khóa | Đơn vị tổ chức | Thời gian | Thư mục `raw/` | Cấu trúc | Số tài liệu | Số trang | Trạng thái |
|---|---|---|---|---|---|---:|---:|---|
| `MEGROW` | me.grow (2026) L2 Leadership Development Program | The Business School, RMIT University Vietnam — phối hợp với Zalo | 2026 (Capstone trình bày 20/11/2026) | `raw/megrow/` | 20 topic / 3 pillar | 22 | 805 | Đã inventory, chưa xử lý chunk |

---

## MEGROW — me.grow (2026) L2 Leadership Development Program

**Đối tượng:** leader cấp L2.2 và L2.3 tại Zalo, đang chuyển sang phạm vi lãnh đạo rộng hơn.

**Hình thức:** workshop tương tác, peer learning, áp dụng vào công việc, Capstone Project theo nhóm (task force ~8 người).

**Thư mục gốc:** `raw/megrow/` — 20 file slide theo topic + 2 file case reading.

**Địa điểm:** RMIT University Vietnam, Saigon South Campus.

### Ánh xạ pillar → level

> ⚠️ **Taxonomy do người dùng duyệt, không phải cấu trúc RMIT chính thức đã kiểm chứng.**
> Nhãn: `[SUY LUẬN — người dùng duyệt 2026-11-07]`.
> Lý do: đã quét toàn bộ 805 trang của 22 tài liệu, **không trang nào ghi pillar** hay tên pillar ("Master the Personal Shift", "Develop the Team Talent", "Navigate the Strategic Landscape"). Footer slide chỉ có dạng `RMIT | Zalo me.grow`. CLAUDE.md §4 cấm đoán, nên ánh xạ dưới đây lấy từ chỉ định trực tiếp của người dùng. Xem mục đối chiếu trong `open_questions.md` (OQ-001).

| Pillar | Tên pillar (người dùng đặt) | Topic | Level chính |
|---|---|---|---|
| P1 | `LEAD_SELF` | 1 – 5 | `SELF` |
| P2 | `LEAD_PEOPLE_AND_TEAMS` | 6 – 11 | `TEAM` |
| P3 | `LEAD_ACROSS_ORGANISATION` | 12 – 20 | `ORG` |

### Ràng buộc kèm theo taxonomy (người dùng chỉ định)

1. **Giữ nguyên số topic gốc và mọi tham chiếu nguồn.** Topic giữ đúng số trong tên file; `source` luôn trỏ về file và số trang thật.
2. **Cho phép quan hệ framework xuyên pillar.** `related_ids` của một chunk không bị giới hạn trong cùng pillar — ví dụ Situational Leadership xuất hiện ở cả Topic 1 (P1), Topic 6 (P2) và Topic 10 (P2) và phải liên kết chéo tự do.
3. **Không giới hạn truy xuất theo pillar chính.** Pillar chỉ quyết định level *chính* của topic. Chunk được gán thêm level phụ khi nội dung thực sự thuộc về level đó.

Ví dụ áp dụng ràng buộc 3:

| Topic | Pillar → level chính | Level phụ nên thêm | Lý do |
|---|---|---|---|
| Topic 12 Stakeholder Influence | ORG | — | Đúng level |
| Topic 13 Building Trust in Teams | ORG | `TEAM` | Nội dung hoàn toàn về đội nhóm (TRUST Framework, Psychological Safety) |
| Topic 14 Decision Making in Cross-functional Teams | ORG | `TEAM` | Ladder of Inference, group dynamics áp dụng trong team |
| Topic 18 Leading in the AI-Enabled Organisation | ORG | `TEAM`, `SELF` | EEE diagnostic dùng ở cấp team; C-FISH là phẩm chất cá nhân |
| Topic 4 Practice Performance Conversations | SELF | `TEAM` | AMO và SAIL là hội thoại với nhân viên |
| Topic 2 Driving Operational Execution | SELF | `TEAM`, `ORG` | Chuỗi Corporate → Business → Functional → Operational chạm cả ba level |

### Giảng viên

| Giảng viên | Topic phụ trách |
|---|---|
| AP Burkhard Schrage | 1, 17, 20 |
| Dr Phuong (Emmy) Hoang | 2 |
| Dr Thu Nguyen | 3 |
| AP Elaine Chew | 4 |
| AP Agnis Stibe | 5, 6 |
| Dr Thao Luong | 7, 8 |
| Dr Quyen Dang | 9 |
| Dr Tony Nguyen | 10, 19 |
| Dr Gavin Nicholson | 11 |
| Prof Seng Kiat Kok | 12 |
| Dr Justin Xavier Batinadan | 13 |
| Dr Phuong Nguyen | 14, 15 |
| Dr Thuan Nguyen & Dr Bidyut Hazarika | 16 |
| Prof Trung Nguyen | 18 |

### Capstone

Topic 20 vừa là một topic được đánh số, vừa là **phiên định hướng Capstone** (6/11/2026). Vì vậy nó nhận `TOP-MEGROW-20` **và** nhãn `CAPSTONE`.

- Case giả định: **Lumo**, nền tảng Việt Nam, đang thử nghiệm agent AI thường trực **Mira**. Lumo được dựng gần với thế giới Zalo để học viên nói thẳng.
- 7 task force, 3 mandate (A: agent cá nhân hay doanh nghiệp trước; B: go-to-market agent cá nhân; C: go-to-market agent doanh nghiệp).
- 4 vai trong mỗi task force: Product & Market Development Lead, Engineering Lead, Data and AI Lead, Trust & Safety Lead.
- Trình bày 20/11/2026, 15 phút + 5 phút hỏi đáp. Rubric 5 tiêu chí × 20 điểm.

> ⚠️ Slide 21–27 của Topic 20 chứa **tên thật của học viên** trong danh sách task force. Theo CLAUDE.md §7 (CASE luôn ẩn danh) và §12, **không trích tên thật vào bất kỳ chunk nào**. Xem `open_questions.md` (OQ-003).

=====

<!-- nguồn: kb/00_index/topic_map.md -->

# topic_map.md — Bản đồ topic ↔ tài liệu

Mọi file trong `raw/` phải xuất hiện đúng một lần ở bảng dưới.

**Trạng thái:** `chưa xử lý` → `đang xử lý` → `đã xử lý`.

**Tiến độ MEGROW: 9 / 20 topic đã xử lý** (Topic 01, 04, 06, 08, 09, 10, 12, 14, 19) — 375 / 805 trang, độ phủ 46.6%.

---

## MEGROW — me.grow (2026) L2 Leadership Development Program

Pillar lấy từ taxonomy người dùng duyệt (xem `courses.md`), nhãn `[SUY LUẬN — người dùng duyệt]`.
Cột **Level** ghi level chính (từ pillar) trước, level phụ sau dấu `+` khi nội dung thực sự thuộc về level đó.

### P1 `LEAD_SELF` — Topic 1–5 (level chính SELF)

| ID | Topic | Tên topic | Giảng viên | Level | File | Trang | Trạng thái | Ngày thêm |
|---|---:|---|---|---|---|---:|---|---|
| `TOP-MEGROW-01` | 1 | Navigating the Leadership Transition | AP Burkhard Schrage | SELF + TEAM | `Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf` | 25 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-02` | 2 | Driving Operational Execution | Dr Phuong (Emmy) Hoang | SELF + TEAM, ORG | `Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf` | 35 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-03` | 3 | Audit Mindset & Biases | Dr Thu Nguyen | SELF | `Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf` | 30 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-04` | 4 | Practice Performance Conversations (AMO Framework) | AP Elaine Chew | SELF + TEAM | `Topic 4 - Practice Performance Conversations - AP Elaine Chew.pdf` | 46 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-05` | 5 | Optimise Personal Productivity | AP Agnis Stibe | SELF | `Topic 5 - Optimise Personal Productivity - Agnis Stibe.pdf` | 78 | chưa xử lý | 2026-11-07 |

### P2 `LEAD_PEOPLE_AND_TEAMS` — Topic 6–11 (level chính TEAM)

| ID | Topic | Tên topic | Giảng viên | Level | File | Trang | Trạng thái | Ngày thêm |
|---|---:|---|---|---|---|---:|---|---|
| `TOP-MEGROW-06` | 6 | Delegation & Accountability in Fast-Paced Teams | AP Agnis Stibe | TEAM + SELF | `Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf` | 69 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-07` | 7 | Building Team Capability & Growth (LEGO® Serious Play®) | Dr Thao Luong | TEAM | `Topic 7 - Building Team Capability and Growth - Thao Luong.pdf` | 43 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-08` | 8 | Correcting Behaviour Through Coaching | Dr Thao Luong | TEAM + SELF | `Topic 8 - Correcting Behaviour Through Coaching - Thao Luong.pdf` | 44 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-09` | 9 | Coaching for High Performance | Dr Quyen Dang | TEAM | `Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf` | 54 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-10` | 10 | Adapt Your Leadership Style | Dr Tony Nguyen | TEAM | `Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf` | 38 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-11` | 11 | Customised Approach for Individuals | Dr Gavin Nicholson | TEAM + SELF | `Topic 11 - Customise Approach for Individuals - Gavin Nicholson-1.pdf` | 45 | chưa xử lý | 2026-11-07 |

### P3 `LEAD_ACROSS_ORGANISATION` — Topic 12–20 (level chính ORG)

| ID | Topic | Tên topic | Giảng viên | Level | File | Trang | Trạng thái | Ngày thêm |
|---|---:|---|---|---|---|---:|---|---|
| `TOP-MEGROW-12` | 12 | Stakeholder Influence & Leadership in Technology | Prof Seng Kiat Kok | ORG | `Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf` | 41 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-12` | 12 | ↳ *Case reading bổ sung:* Microsoft's Turnaround – The Satya Nadella Story | Bloomberg Businessweek, 6/5/2019 | ORG | `[Case Reading] Microsoft’s Turnaround – The Satya Nadella Story.pdf` | 7 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-13` | 13 | Building Trust & Open Communication in Teams | Dr Justin Xavier Batinadan | ORG + TEAM | `Topic 13 - Building Trust & Open Communication in Teams - Justin Xavier.pdf` | 30 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-14` | 14 | Decision Making in Cross-functional Teams | Dr Phuong Nguyen | ORG + TEAM | `Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf` | 14 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-14` | 14 | ↳ *Case reading bổ sung:* The BCPC Internet Strategy Team: An Exercise | Amy C. Edmondson, HBS 604-035 | ORG + TEAM | `[Case Reading] of topic 14 .pdf` | 4 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-15` | 15 | From Stakeholder Insight to Market Impact | Dr Phuong Nguyen | ORG | `Topic 15 - From Stakeholder Insight to Market Impact - Dr Phuong Nguyen.pdf` | 21 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-16` | 16 | Solve Tech & Organisational Blockers | Dr Thuan Nguyen & Dr Bidyut Hazarika | ORG + TEAM | `Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf` | 37 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-17` | 17 | Apply Strategic Thinking | AP Burkhard Schrage | ORG | `Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf` | 39 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-18` | 18 | Leading in the AI-Enabled Organisation | Prof Trung Nguyen | ORG + TEAM, SELF | `Topic 18 - Leading in the AI-Enabled Organisation - Prof Trung Nguyen.pdf` | 44 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-19` | 19 | Presenting Business Cases (SCQA, Pyramid Principle, Stakeholder Mapping) | Dr Tony Nguyen | ORG | `Topic 19 - Present Business Case - Dr Tony Nguyen.pdf` | 33 | **đã xử lý** | 2026-11-07 |
| `TOP-MEGROW-20` | 20 | Capstone Research & Alignment `CAPSTONE` | AP Burkhard Schrage | ORG | `Topic 20 - Capstone Research & Alignment - AP Burkhard Schrage.pdf` | 28 | chưa xử lý | 2026-11-07 |

**Tổng: 22 tài liệu / 805 trang / 20 topic.**

---

## Ghi chú

- **Số topic lấy theo tên file**, không theo số in trên slide. Deck của Topic 3 ghi "Topic 2" ở trang bìa và deck của Topic 4 ghi "Topic 5" — xem `open_questions.md` (OQ-002).
- `TOP-MEGROW-20` vừa là topic, vừa mang nhãn `CAPSTONE` (phiên định hướng Capstone Project ngày 6/11/2026).
- Hai file `[Case Reading]` là **tài liệu bổ sung** cho topic tương ứng, không nhận số topic riêng. Việc gán case Microsoft cho Topic 12 là suy luận của Claude đã được người dùng duyệt — xem `open_questions.md` (OQ-004).
- Không tài liệu nào trong `raw/megrow/` thuộc loại `PROGRAM` (lịch học, giới thiệu chương trình) — chưa có file nào như vậy.

=====

<!-- nguồn: kb/00_index/catalog.md -->

# catalog.md — Danh mục mọi chunk trong kho

Mọi chunk phải xuất hiện ở đây. Chunk `deprecated` vẫn liệt kê nhưng ghi rõ trạng thái.

**Trạng thái kho: 67 chunk.** Đã xử lý 3/20 topic MEGROW (Topic 01, 06, 10).

| Loại | Số lượng |
|---|---:|
| `CON` Khái niệm & nguyên tắc | 13 |
| `FW` Framework | 36 |
| `PRB` Vấn đề | 9 |
| `PB` Playbook | 0 |
| `TOP` Topic | 9 |
| `CASE` Tình huống thực tế | 0 |
| **Tổng** | **67** |

---

## Khái niệm & nguyên tắc (CON)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| `CON-001` | Chuyển dịch tư duy từ chuyên môn sang quản lý (The IC-to-Manager Mindset Shift) | concept | SELF | MEGROW | Thành công đổi từ kết quả cá nhân sang kết quả của đội; công việc đã đổi nên bạn phải đổi theo |
| `CON-002` | Ba cái bẫy của quản lý mới (The Three Traps of the New Manager) | concept | SELF, TEAM | MEGROW | Làm thay, né giao việc, và để kỳ vọng ngầm — ba hành vi khiến ~50% quản lý mới dưới kỳ vọng |
| `CON-003` | Responsibility, accountability và decision rights (Responsibility, Accountability and Decision Rights) | concept | TEAM | MEGROW | Tách ba khái niệm hay bị trộn; accountability = clarity + ownership + follow-through |
| `CON-004` | Giao kết quả, không giao đầu việc (Delegate outcomes, not just tasks) | concept | TEAM | MEGROW | Giao việc đủ phải nói rõ bốn thứ: kết quả mong đợi, quyền sở hữu, quyền quyết định, tiêu chí thành công |
| `CON-005` | Có tầm nhìn mà không kiểm soát (Visibility without control) | concept | TEAM | MEGROW | Ranh giới và checkpoint thỏa thuận trước giữ được quyền tự chủ; hỏi cập nhật liên tục thì không |
| `CON-006` | Tải nhận thức của quản lý và của team (Cognitive load of the manager and the team) | concept | TEAM, SELF | MEGROW | Gỡ nút thắt thay vì thúc mạnh hơn; thiết kế sự rõ ràng ở vai trò, ưu tiên, kênh, luồng việc, quyền quyết |
| `CON-007` | Pre-wiring — thắng quyết định trước cuộc họp (Pre-wiring) | concept | ORG | MEGROW | Giành đồng thuận trước cuộc họp: Map → Pre-meet → Adapt → Present; khuyến nghị không đổi, chỉ trọng tâm đổi |
| `CON-008` | Đừng tranh cãi với mục tiêu của họ (Don't argue against their goal) | concept | ORG | MEGROW | Đừng tranh cãi với mục tiêu của người quyết — chỉ ra ý tưởng của bạn bảo vệ mục tiêu đó thế nào |
| `CON-009` | Mời góp ý và vẫn giữ quyền chốt (Invite input and still reserve the call) | concept | TEAM, ORG | MEGROW | Mời góp ý và giữ quyền chốt không loại trừ nhau; mấu chốt là nói rõ mức tham gia ngay từ đầu |
| `CON-010` | Quan sát thay vì phán xét — phép thử camera (Observation not judgement - the camera test) | concept | TEAM | MEGROW | Phép thử camera: câu mở đầu phải mô tả hành vi quan sát được, không dán nhãn lên con người |
| `CON-011` | Ba cấp độ lắng nghe (Three levels of listening) | concept | TEAM, SELF | MEGROW | Ba cấp độ nghe — sự kiện, cảm xúc, trực giác; câu hỏi mở giúp người kia tự tạo nhận thức |
| `CON-012` | Vấn đề của tổ chức khoác áo vấn đề của nhân viên (Organisational problems disguised as employee problems) | concept | TEAM, ORG | MEGROW | Vấn đề tổ chức thường ngụy trang thành vấn đề nhân viên: quy trình kém, thiếu nguồn lực, ưu tiên không rõ |
| `CON-013` | Tự nhận thức và tự quản lý cảm xúc (Self-awareness and self-management) | concept | SELF, TEAM | MEGROW | Tự nhận thức giúp nhận ra mình đang cảm thấy gì; tự quản lý quyết định làm gì với điều đó |

## Framework (FW)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| `FW-001` | Lãnh đạo theo tình huống (Situational Leadership) | framework | TEAM | MEGROW | Điều chỉnh mức chỉ đạo và hỗ trợ theo mức sẵn sàng của từng người cho từng việc — S1 đến S4 |
| `FW-002` | Năm ngộ nhận của quản lý mới (Five Myths of the New Manager) | framework | SELF | MEGROW | Hill (2007): quyền hạn → phụ thuộc lẫn nhau, kiểm soát → cam kết, quản từng người → dẫn cả đội |
| `FW-003` | 90 ngày đầu và chẩn đoán STARS (The First 90 Days & STARS) | framework | SELF, TEAM | MEGROW | Chẩn đoán tình huống thừa hưởng rồi chạy 12 hành động theo ba chặng 30/60/90 để sớm chạm break-even |
| `FW-004` | Bốn giai đoạn đóng góp trong sự nghiệp (Four Stages of Contribution) | framework | SELF | MEGROW | Dalton et al. (1977): lên quản lý là chuyển từ đóng góp độc lập sang đóng góp qua người khác |
| `FW-005` | Lưới Lãnh đạo và hai nhóm hành vi (The Leadership Grid & the two behaviour dimensions) | framework | TEAM, SELF | MEGROW | Blake & Mouton: định vị xu hướng tự nhiên trên hai trục Task-Oriented và People-Oriented |
| `FW-006` | Năm phong cách ra quyết định Vroom–Yetton–Jago (Vroom-Yetton-Jago Decision Styles) | framework | TEAM | MEGROW | AI · AII · CI · CII · GII — chọn mức tham gia của nhân viên theo loại quyết định |
| `FW-007` | Khung Thiết kế Chuyển đổi (8 yếu tố) (Transformation Design Framework) `needs_review` | framework | TEAM, ORG | MEGROW | Stibe: Triangle · Curve · Metric · Circles · Architecture · Socium · Moderation · Ethics |
| `FW-008` | Bảy đòn bẩy ảnh hưởng xã hội (Socium - Seven Social Influence Levers) `needs_review` | framework | TEAM | MEGROW | Comparison · Competition · Recognition · Cooperation · Learning · Norms · Facilitation |
| `FW-009` | Lý thuyết Sở hữu Tâm lý (Theory of Psychological Ownership) `needs_review` | framework | TEAM | MEGROW | Năm thành tố biến "được giao" thành "thấy mình sở hữu": identity, accountability, self-efficacy, belongingness, responsibility |
| `FW-010` | Phân bổ việc giữa người và AI (HAI) (Human Artificial Intelligence (HAI) task allocation) | framework | TEAM, SELF | MEGROW | Đặt đúng loại trí tuệ vào đúng việc: Human, AI hay HAI — giao thêm cho AI không giảm trách nhiệm người |
| `FW-011` | Lý thuyết Các bên liên quan (Stakeholder Theory) | framework | ORG | MEGROW | Freeman (1984): đổi câu hỏi từ "ai báo cáo cho tôi" sang "ai tác động tới kết quả và ai bị tác động" |
| `FW-012` | Ma trận Quyền lực – Mức quan tâm (The Power-Interest Matrix) | framework | ORG | MEGROW | Mendelow (1991): bốn ô Manage Closely · Keep Satisfied · Keep Informed · Monitor để dồn đúng sự chú ý |
| `FW-013` | Năm thực hành lãnh đạo Kouzes & Posner (The Leadership Challenge - Five Practices) | framework | ORG, TEAM | MEGROW | Kouzes & Posner: năm thực hành — Model the Way, Inspire, Challenge, Enable, Encourage; kèm case Nadella |
| `FW-014` | Sáu nguồn quyền lực xã hội (Sources of Social Power) | framework | ORG | MEGROW | French & Raven: sáu nguồn quyền lực và công cụ Power Audit cho người không có quyền chỉ đạo |
| `FW-015` | Gây ảnh hưởng khi không có quyền chỉ đạo (Influence Without Authority (the Exchange)) | framework | ORG | MEGROW | Cohen & Bradford: đổi "làm sao để họ ủng hộ tôi" thành "giá trị chung nằm ở đâu"; Influence Map và Planner |
| `FW-016` | Năm chế độ ứng xử với xung đột Thomas–Kilmann (Thomas-Kilmann Conflict Mode Instrument) | framework | ORG, TEAM | MEGROW | Thomas–Kilmann: năm chế độ trên trục assertiveness × cooperativeness, kèm Conflict Response Planner |
| `FW-017` | Dẫn dắt thay đổi qua liên minh các bên (Leading Change Through Stakeholder Coalitions) | framework | ORG | MEGROW | Kotter dùng chọn lọc: xây liên minh dẫn dắt và dịch chuyển nhóm Undecided bằng lời "có" ít rủi ro |
| `FW-018` | Cấu trúc mở đầu SCQA (SCQA) | framework | ORG | MEGROW | Situation → Complication → Question → Answer: mở đầu bằng điều người nghe đã đồng ý |
| `FW-019` | Nguyên lý Kim tự tháp và MECE (The Pyramid Principle & MECE) | framework | ORG | MEGROW | Câu trả lời ở đỉnh, 3–4 trụ MECE ở giữa, bằng chứng ở đáy; reasons so với chain |
| `FW-020` | Thang Suy luận (The Ladder of Inference) | framework | ORG, TEAM | MEGROW | Argyris: năm nấc từ dữ liệu tới kết luận; kết luận đối nghịch thường do chọn tập dữ liệu khác nhau |
| `FW-021` | Hỏi trước, trình bày sau (Inquiry before Advocacy) | framework | ORG, TEAM | MEGROW | Seek first to understand: hỏi về intentions, resources, situation của họ trước khi trình bày của mình |
| `FW-022` | Chuỗi sáu chặng làm việc với stakeholder (MAP - PRIORITISE - TRUST - INFLUENCE - ALIGN - ACT) | framework | ORG | MEGROW | Khung tổng hợp Topic 12: MAP → PRIORITISE → TRUST → INFLUENCE → ALIGN → ACT, mỗi chặng một công cụ |
| `FW-023` | Khung chẩn đoán AMO (The AMO Framework) | framework | TEAM, SELF | MEGROW | Ability · Motivation · Opportunity — chẩn đoán vì sao hiệu suất đi xuống, đừng vội quy kết thái độ |
| `FW-024` | Quy trình hội thoại SAIL (SAIL - the underperformance conversation) | framework | TEAM | MEGROW | State the gap → Ask → Identify root causes (AMO) → Launch actions; kết bằng thỏa thuận phục hồi hiệu suất |
| `FW-025` | Bốn bước sửa hành vi (NOTICE - CONVERSE - COACH - HOLD ACCOUNTABLE) | framework | TEAM, SELF | MEGROW | Bốn bước sửa hành vi; clarity + curiosity + follow-through |
| `FW-026` | Phép thử Năm Tác động (The 5-Impact Test) | framework | TEAM | MEGROW | Năm loại tác động — Performance, People, Culture, Trust, Policy/Ethics — quyết định có nên lên tiếng không |
| `FW-027` | Bốn kiểu quản lý khi coaching (The Four Manager Types) | framework | TEAM, SELF | MEGROW | Teacher · Always-On · Cheerleader · Connector, kèm ba huyền thoại giữ Always-On luôn bật |
| `FW-028` | Chẩn đoán nguyên nhân gốc theo năm lăng kính (Root-cause diagnosis - five lenses) | framework | TEAM | MEGROW | Knowledge · Skills · Motivation · Career · Environment — tìm nguyên nhân, không tìm triệu chứng |
| `FW-029` | Thang đo Mức sẵn sàng phát triển (Employee Development Readiness Assessment) | framework | TEAM | MEGROW | Năm phát biểu chấm 1–5: 5–11 vai trò hiện tại · 12–18 stretch · 19–25 luân chuyển hoặc thăng chức |
| `FW-030` | Lộ trình D–R–C (The D-R-C route) | framework | TEAM | MEGROW | Diagnose → Readiness → Coach & Connect; bảo vệ khỏi việc khuyên quá sớm |
| `FW-031` | EDGE và Lợi thế cạnh tranh cá nhân (EDGE and Personal Competitive Advantage) `needs_review` | framework | SELF, TEAM | MEGROW | Explore → Decode → Generate & test (VRIFA) → Execute, ra một thí nghiệm tăng trưởng 90 ngày |
| `FW-032` | Connector Manager (The Connector Manager) | framework | TEAM | MEGROW | Hiểu người, coach có chọn lọc, kết nối có chủ đích; năm phẩm chất và ba kết nối Person → Team → Organization |
| `FW-001-01` | Ma trận Kỹ năng × Ý chí (Skill × Will Matrix) | framework | TEAM | MEGROW | Bản thao tác của FW-001: đo Skill và Will bằng bằng chứng, ra Direct/Coach/Motivate/Delegate |
| `FW-001-02` | Ba biến thể Situational Leadership trong MEGROW (Situational Leadership — the three MEGROW variants) | framework | TEAM | MEGROW | Đối chiếu tên gọi giữa Topic 01, 06, 10 để không tưởng là ba framework khác nhau |
| `FW-019-01` | Action title và phép thử lướt (Action titles and the skim test) | framework | ORG | MEGROW | Tiêu đề slide nêu kết luận chứ không nêu chủ đề; skim test kiểm tra kim tự tháp có đứng vững không |
| `FW-025-01` | Ma trận Hỗ trợ × Trách nhiệm (The Support x Accountability matrix) | framework | TEAM | MEGROW | Ma trận hỗ trợ × trách nhiệm: tránh ba ô Avoidance, Supportive-but-unclear, Command/compliance |

## Vấn đề (PRB)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| `PRB-002` | Làm việc với stakeholder để xây dựng và thống nhất bài toán (Working with stakeholders to define and agree the problem) | problem | ORG | MEGROW | Ưu tiên **Cao**. Thuyết phục khi không có quyền chỉ đạo, chuyển ngôn ngữ business, quản lý kỳ vọng, biết từ chối |
| `PRB-003` | Thiết kế framework làm việc và giải quyết vấn đề cho team (Designing the team's way of working and decision process) `needs_review` | problem | TEAM | MEGROW | Ưu tiên **Cao**. Quyền quyết định không rõ, quản lý thành nút thắt, bận mà việc quan trọng vẫn trễ |
| `PRB-004` | Chuyển dịch từ người làm chuyên môn sang người quản lý (Moving from individual contributor to manager) | problem | SELF | MEGROW | Ưu tiên **Cao**. Vẫn tự làm phần khó nhất, không có thời gian cho team, thước đo thành công chưa đổi |
| `PRB-005` | Giao việc và phát triển theo năng lực từng người (Delegating and developing according to each person's capability) | problem | TEAM | MEGROW | Ưu tiên **Cao**. Giao rồi vẫn phải làm lại, người giỏi gánh hết, không biết giao đến đâu thì vừa |
| `PRB-006` | Feedback, coaching và trao đổi về hiệu suất (Feedback, coaching and performance conversations) | problem | TEAM | MEGROW | Ưu tiên **Trung bình**. Góp ý rồi không đổi, ngại nói thẳng, coach nhiều mà team vẫn phụ thuộc |
| `PRB-007` | Động lực, gắn kết và giữ người (Motivation, engagement and retention) `needs_review` | problem | TEAM | MEGROW | Ưu tiên **Trung bình**. Làm đủ việc nhưng mất lửa, không ai đề xuất gì mới, collaborator không gắn bó |
| `PRB-008` | Làm việc với cấp trên và gắn với chiến lược tổ chức (Managing upward and linking to organisational strategy) `needs_review` | problem | ORG | MEGROW | Ưu tiên **Trung bình**. Xin nguồn lực không được duyệt, sụp ở phần hỏi đáp, sếp nghe xong không rõ xin gì |
| `PRB-010` | Xung đột trong team hoặc giữa các team (Conflict within or between teams) `needs_review` | problem | TEAM, ORG | MEGROW | Ưu tiên **Thấp**. Hai bên cãi mãi không đi tới đâu, cùng một tranh luận lặp lại qua nhiều cuộc họp |
| `PRB-011` | Dẫn dắt thay đổi (Leading change) `needs_review` | problem | ORG, TEAM | MEGROW | Ưu tiên **Thấp**. Thông báo cách làm mới rồi không ai theo; được vài tuần rồi đâu lại vào đấy |

## Playbook (PB)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có — viết ở bước "Rà soát tổng thể" sau khi xử lý xong các topic)_ | | | | | |

## Topic (TOP)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| `TOP-MEGROW-01` | Điều hướng bước chuyển sang vai trò lãnh đạo (Navigating the Leadership Transition) | topic | SELF, TEAM | MEGROW | Buổi mở đầu chương trình: tư duy chuyển vai, ba cái bẫy, giao việc theo mức sẵn sàng, kế hoạch 90 ngày |
| `TOP-MEGROW-04` | Thực hành hội thoại về hiệu suất với khung AMO (Practise Performance Conversations with the AMO Framework) | topic | SELF, TEAM | MEGROW | Từ đánh giá quá khứ sang quản trị hiệu suất bền vững; AMO chẩn đoán, SAIL dẫn cuộc trò chuyện |
| `TOP-MEGROW-06` | Giao việc và trách nhiệm trong team tốc độ cao (Delegation & Accountability in Fast-Paced Teams) `needs_review` | topic | TEAM, SELF | MEGROW | Mười thách thức giao việc và trách nhiệm; khung Transformation Design 8 yếu tố; HAI và tải nhận thức |
| `TOP-MEGROW-08` | Sửa hành vi thông qua coaching (Correcting Behaviour Through Coaching) | topic | TEAM, SELF | MEGROW | Bốn bước sửa hành vi, kèm mảng lớn về trí tuệ cảm xúc và lắng nghe chèn giữa bước CONVERSE |
| `TOP-MEGROW-09` | Coaching để đạt hiệu suất cao (Coaching for High Performance) | topic | TEAM | MEGROW | Coach nhiều hơn không làm nhân viên giỏi hơn; Connector Manager và lộ trình D–R–C |
| `TOP-MEGROW-10` | Điều chỉnh phong cách lãnh đạo (Adapt Your Leadership Style) | topic | TEAM | MEGROW | Bốn hoạt động trải nghiệm để tự rút ra Situational Leadership và mức tham gia vào quyết định |
| `TOP-MEGROW-12` | Ảnh hưởng tới các bên liên quan và lãnh đạo trong công nghệ (Stakeholder Influence & Leadership in Technology) | topic | ORG | MEGROW | Bảy lý thuyết ghép thành chuỗi sáu chặng MAP→ACT, đầu ra là chiến lược stakeholder 90 ngày |
| `TOP-MEGROW-14` | Ra quyết định trong nhóm liên chức năng (Decision Making in Cross-functional Teams) | topic | ORG, TEAM | MEGROW | Một bài tập đóng vai BCPC; vì sao các nhóm cùng dữ liệu lại ra quyết định khác nhau |
| `TOP-MEGROW-19` | Trình bày business case để được duyệt (Presenting Business Cases - Getting Buy-in) | topic | ORG | MEGROW | Ba công cụ cho ba câu hỏi của người quyết: SCQA, Pyramid Principle, Stakeholder Mapping |

## Tình huống thực tế (CASE)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có — tạo bằng lệnh "Thêm case")_ | | | | | |
---

## Bộ đếm ID tiếp theo

| Tiền tố | ID tiếp theo | Ghi chú |
|---|---|---|
| `CON` | `CON-007` | |
| `FW` | `FW-011` | |
| `PRB` | `PRB-012` | Xem mục đặt chỗ dưới đây |
| `PB` | `PB-001` | |
| `CASE` | `CASE-001` | |

### ID `PRB` đã đặt chỗ

`PRB-001` … `PRB-011` được **đặt chỗ sẵn** cho đúng 11 vấn đề ưu tiên theo thứ tự ở CLAUDE.md §2 và `problem_index.md`. Năm chunk đã tạo nằm đúng vị trí số của chúng; sáu ID còn lại sẽ được dùng khi topic tương ứng được xử lý — **không tái sử dụng cho mục đích khác**.

| ID | Vấn đề | Mức | Trạng thái |
|---|---|---|---|
| `PRB-001` | Định hướng bài toán cho team | Cao | chưa tạo — chờ Topic 02, 17 |
| `PRB-002` | Làm việc với stakeholder để xây dựng và thống nhất bài toán | Cao | chưa tạo — chờ Topic 12, 19 |
| `PRB-003` | Thiết kế framework làm việc và giải quyết vấn đề cho team | Cao | ✅ đã tạo (`needs_review`) |
| `PRB-004` | Chuyển dịch từ chuyên môn sang quản lý | Cao | ✅ đã tạo |
| `PRB-005` | Giao việc và phát triển theo năng lực từng người | Cao | ✅ đã tạo |
| `PRB-006` | Feedback, coaching và trao đổi về hiệu suất | Trung bình | chưa tạo — chờ Topic 04, 08, 09 |
| `PRB-007` | Động lực, gắn kết và giữ người | Trung bình | ✅ đã tạo (`needs_review`) |
| `PRB-008` | Làm việc với cấp trên và gắn với chiến lược tổ chức | Trung bình | chưa tạo — chờ Topic 17, 19 |
| `PRB-009` | Văn hóa thử nghiệm và an toàn tâm lý | Thấp | chưa tạo — chờ Topic 13 |
| `PRB-010` | Xung đột trong team hoặc giữa các team | Thấp | chưa tạo — chờ Topic 12, 14 |
| `PRB-011` | Dẫn dắt thay đổi | Thấp | ✅ đã tạo (`needs_review`) |

=====

<!-- nguồn: kb/00_index/problem_index.md -->

# problem_index.md — Vấn đề → nguyên nhân → framework

Bảng tra cứu chính cho câu hỏi: *"Tôi đang gặp vấn đề này, dùng framework nào?"*

**Trạng thái:** 9 chunk `PRB`, 36 chunk `FW` và 13 chunk `CON` đã tạo (từ Topic 01, 04, 06, 08, 09, 10, 12, 14, 19). Với các vấn đề đã có chunk `PRB`, **chunk đó là nguồn chính** — bảng ở đây chỉ là mục lục. Với các vấn đề còn lại, cột **Framework ứng viên** vẫn là `[SUY LUẬN]` nhận diện từ tiêu đề trang khi lập inventory, **chưa đọc nội dung chi tiết, chưa kiểm chứng**.

| Vấn đề | Mức | Chunk PRB | Trạng thái |
|---:|---|---|---|
| 1 | Cao | — | chờ Topic 02, 17 |
| 2 | Cao | `PRB-002` | ✅ đã có |
| 3 | Cao | `PRB-003` | ✅ một phần (Topic 06, 10, 14) |
| 4 | Cao | `PRB-004` | ✅ đã có |
| 5 | Cao | `PRB-005` | ✅ đã có (T01, 06, 09, 10) |
| 6 | Trung bình | `PRB-006` | ✅ đã có |
| 7 | Trung bình | `PRB-007` | ✅ một phần (Topic 06, 09) |
| 8 | Trung bình | `PRB-008` | ✅ một phần (Topic 19, 12) |
| 9 | Thấp | — | chờ Topic 13 |
| 10 | Thấp | `PRB-010` | ✅ một phần (Topic 08, 12, 14) |
| 11 | Thấp | `PRB-011` | ✅ một phần (Topic 06, 12) |

Danh sách 11 vấn đề lấy từ CLAUDE.md §2 (người dùng nêu 1–3; 4–11 suy ra từ vai trò).

Bối cảnh người học: Associate Data Science Manager tại Zalo (L2), quản lý trực tiếp 6 người — 1 Senior DS, 3 DS, 1 DS Collaborator, 1 Data Labeling Collaborator.

---

## Mức ưu tiên CAO

Yêu cầu: mỗi vấn đề có chunk `PRB` riêng **và** ít nhất một chunk `PB` (checklist, kịch bản) khi rà soát tổng thể; liên kết tới mọi framework liên quan từ mọi topic.

### PRB-? · 1. Định hướng bài toán cho team — chọn bài toán đáng làm, xác định hướng đi và thứ tự ưu tiên
**Level:** TEAM, ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Strategic Management Cycle (Research & Analysis → Strategy Formulation → Translation & Planning → Execution → Evaluation & Adaptation) | T2 | _chưa có_ |
| Cascade Corporate → Business → Functional → Operational strategy | T2 | _chưa có_ |
| SMART + mẫu mục tiêu theo outcome/evidence/guardrail; phân biệt Output–Outcome–Impact | T2 | _chưa có_ |
| Stress-test KPI (4 câu hỏi phá KPI) · Balanced execution signal stack | T2 | _chưa có_ |
| PESTEL · Porter Five Forces · VRIN / Resource-Based View · Options table · Line-of-sight test | T17 | _chưa có_ |
| Stakeholder Journey Map · Systematic Inventive Thinking (SIT) · Creative Matrix | T15 | _chưa có_ |
| Problem Tree Analysis · Problem Statement Template · "How Might We" reframe | T16 | _chưa có_ |
| FranklinCovey Time Matrix · Eisenhower Matrix · GTD | T5 | _chưa có_ |

### `PRB-002` · 2. Làm việc với stakeholder để xây dựng và thống nhất bài toán
*Thuyết phục khi không có quyền chỉ đạo, chuyển ngôn ngữ business sang bài toán DS, quản lý kỳ vọng về độ bất định, biết từ chối.*
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Freeman (1984) Stakeholder Theory · Stakeholder Ecosystem Map | T12 | `FW-011` |
| Mendelow (1991) Power–Interest Matrix | T12, T19 | `FW-012` |
| French & Raven (1959) Sources of Social Power · Power Audit | T12 | `FW-014` |
| Cohen & Bradford (2017) Influence Without Authority · Influence Map · Conversation Planner | T12 | `FW-015` |
| Kotter (2012) Stakeholder Coalitions · Coalition Map | T12 | `FW-017` |
| Kouzes & Posner (2023) The Leadership Challenge — 5 thực hành | T12, T18 | `FW-013` |
| Chuỗi sáu chặng MAP → PRIORITISE → TRUST → INFLUENCE → ALIGN → ACT | T12 | `FW-022` |
| SCQA | T19 | `FW-018` |
| Pyramid Principle · MECE | T19 | `FW-019` |
| Action titles · skim test | T19 | `FW-019-01` |
| Pre-wiring | T19 | `CON-007` |
| Đừng tranh cãi với mục tiêu của họ | T19 | `CON-008` |
| Power–Interest Grid (bản của T19) | T19 | `FW-012` |
| Yukl & Tracey (1992) influence tactics · Mayer, Davis & Schoorman (1995) trust = ability·benevolence·integrity | T3 | _chưa có_ |
| Ladder of Inference (Argyris) | T14 | `FW-020` |
| Advocacy ↔ Inquiry | T14 | `FW-021` |

### `PRB-003` · 3. Thiết kế framework làm việc và giải quyết vấn đề cho team
*Quy trình, phối hợp, ra quyết định, tiêu chuẩn chất lượng.*
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Team Delivery System · Review rhythm (daily/weekly/milestone gate) · Response thresholds · Monitor the work system, not the person | T2 | _chưa có_ |
| Owner / Responsibility / Accountability / RACI · Decision rights | T2, T6 | `CON-003` (phần T6) |
| AI-augmented Design Thinking (Stanford 5 phases; Understand–Create–Deliver) · Empathy Map · 7-day test | T16 | _chưa có_ |
| Vroom–Yetton–Jago Model (AI / AII / CI / CII / GII) | T10 | `FW-006` |
| Human–AI Decision Rights (4 mức) | T18 | _chưa có_ |
| HAI — phân bổ việc Human / AI / HAI; giao cho AI không giảm trách nhiệm người | T6 | `FW-010` |

### `PRB-004` · 4. Chuyển dịch từ người làm chuyên môn sang người quản lý
*Buông việc kỹ thuật, cân bằng tự làm và dẫn dắt, quản lý thời gian và năng lượng.*
**Level:** SELF

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Dalton, Thompson & Price (1977) Four Stages of Contribution | T1 | `FW-004` |
| Hill (2007) Five Myths · Ba cái bẫy (làm thay, né giao việc, kỳ vọng ngầm) | T1 | `FW-002`, `CON-002` |
| Watkins (2013) First 90 Days · STARS · Break-even point · 12 hành động | T1 | `FW-003` |
| IC → Manager mindset shift | T1, T2, T8 | `CON-001` (phần T1) |
| Expert bias · 5-Step Bias Self-Audit · Audit Mindset | T3 | _chưa có_ |
| Tự nhận thức và tự quản lý cảm xúc | T8 | `CON-013` |
| Knowledge–Behaviour Gap Model (Knowledge → Acceptance → Intention → Behaviour) | T5, T6 | _chưa có_ |
| FranklinCovey Time Matrix · Eisenhower Matrix · GTD · Human Artificial Intelligence (HAI) | T5 | _chưa có_ |
| Self-awareness & Self-management (Emotional Intelligence) | T8, T11 | `CON-013` (phần T8) |

### `PRB-005` · 5. Giao việc và phát triển theo năng lực từng người
*Trao quyền cho Senior, hướng dẫn DS, phạm vi rõ cho collaborator.*
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Hersey & Blanchard (1969) Life Cycle Theory / Situational Leadership II | T1, T6, T10 | `FW-001`, `FW-001-02` |
| Skill × Will readiness matrix (Landsberg) — Direct / Coach / Motivate / Delegate | T1 | `FW-001-01` |
| Blake & Mouton (1964) Leadership Grid · Task-oriented vs People-oriented | T10 | `FW-005` |
| Vroom–Yetton–Jago Model — mức tham gia vào quyết định | T10 | `FW-006` |
| Delegate outcomes not tasks · Accountability = clarity + ownership + follow-through · Empower without micromanaging | T6 | `CON-004`, `CON-003`, `CON-005` |
| Theory of Psychological Ownership (5 thành tố) | T6 | `FW-009` |
| Chẩn đoán 5 nguyên nhân gốc (Knowledge · Skills · Motivation · Career · Environment) | T9 | `FW-028` |
| Employee Development Readiness Assessment | T9 | `FW-029` |
| EDGE · Personal Competitive Advantage · VRIFA | T9 | `FW-031` |

---

## Mức ưu tiên TRUNG BÌNH

Yêu cầu: có chunk `PRB` riêng, liên kết đầy đủ.

### `PRB-006` · 6. Feedback, coaching và trao đổi về hiệu suất
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| AMO Framework (Ability · Motivation · Opportunity) | T4 | `FW-023` |
| SAIL (State the gap · Ask · Identify root causes · Launch actions) | T4 | `FW-024` |
| Vấn đề tổ chức khoác áo vấn đề nhân viên | T4 | `CON-012` |
| NOTICE → CONVERSE → COACH → HOLD ACCOUNTABLE | T8 | `FW-025` |
| 5-Impact Test (phỏng theo SBI của CCL) | T8 | `FW-026` |
| Ba cấp độ lắng nghe (factual · emotional · intuitive) | T8 | `CON-011` |
| Observation vs judgement · camera test | T8 | `CON-010` |
| Tự nhận thức và tự quản lý cảm xúc | T8 | `CON-013` |
| Ma trận Support × Accountability | T8 | `FW-025-01` |
| Bốn kiểu quản lý và ba huyền thoại của Always-On | T9 | `FW-027` |
| Connector Manager — 5 phẩm chất, 3 kết nối | T9 | `FW-032` |
| Lộ trình D–R–C (Diagnose → Readiness → Coach & Connect) | T9 | `FW-030` |
| T-GROW coaching model | T18 | _chưa có_ |

### `PRB-007` · 7. Động lực, gắn kết và giữ người
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| McClelland — Need for Achievement / Affiliation / Power | T11 | _chưa có_ |
| Alderfer ERG Theory (Existence · Relatedness · Growth) | T11 | _chưa có_ |
| Ba kết nối của Connector Manager: Employee · Team · Organisation | T9 | `FW-032` |
| Personal Competitive Advantage · EDGE growth strategy | T9 | `FW-031` |
| Apprenticeship Gap · EEE diagnostic (Environment · Equipping · Experience) | T18 | _chưa có_ |
| Social influence levers (Socium 7) | T6 | `FW-008` |

### `PRB-008` · 8. Làm việc với cấp trên và gắn với chiến lược tổ chức
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Line-of-sight test (VNG mission → Zalo direction → department goals → team goals) | T17 | _chưa có_ |
| SCQA · Pyramid Principle · Action titles · Pre-wiring | T19 | `FW-018`, `FW-019`, `FW-019-01`, `CON-007` |
| Reframe → Surface assumptions → Compare & recommend · Options table | T17 | _chưa có_ |
| (đã gộp ở dòng trên) | | |
| Influencing upwards (Cohen & Bradford exchange) | T12 | `FW-015` |
| "Năm cuộc trò chuyện rõ ràng với sếp" trong First 90 Days | T1 | _chưa có_ |

---

## Mức ưu tiên THẤP

Yêu cầu: tạo `PRB` khi khóa học có nội dung liên quan. **Cả ba vấn đề dưới đây đều có nội dung trong MEGROW**, nên sẽ có chunk `PRB`.

### PRB-? · 9. Văn hóa thử nghiệm và an toàn tâm lý
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Psychological Safety (Edmondson) · Ma trận Comfort / Learning / Apathy / Anxiety Zone · Phân biệt Trust vs Psychological Safety | T13 | _chưa có_ |
| TRUST Framework (Transparency · Reliability · Understanding · Safety · Team First) | T13 | _chưa có_ |
| Trust Equation (Maister): (Credibility + Reliability + Intimacy) ÷ Self-Orientation | T13 | _chưa có_ |
| 6 Signature Traits of an Inclusive Leader (Bourke/Deloitte) | T13 | _chưa có_ |
| Kouzes & Posner (2023) The Leadership Challenge — 5 practices | T12, T18 | `FW-013` |
| Psychological safety with accountability | T6 | `CON-005` (một phần) |

### `PRB-010` · 10. Xung đột trong team hoặc giữa các team
**Level:** TEAM, ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Thomas–Kilmann Conflict Mode Instrument · Conflict Response Planner | T12 | `FW-016` |
| Ladder of Inference (Argyris) | T14 | `FW-020` |
| Seek first to understand (Inquiry) rồi Advocacy | T14 | `FW-021` |
| Cùng dữ liệu, khác kết luận — chọn lọc dữ liệu khác nhau (case BCPC) | T14 | `FW-020` |
| Role Play: Mediating Different Working Styles | T11 | _chưa có_ |
| Mời góp ý và vẫn giữ quyền chốt (thế lưỡng nan giả) | T14 | `CON-009` |
| "When they push back": LISTEN → ACKNOWLEDGE → REFOCUS → HOLD | T8 | _chưa có_ |

### `PRB-011` · 11. Dẫn dắt thay đổi
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Kotter (2012) Leading Change Through Stakeholder Coalitions (dùng chọn lọc) | T12 | `FW-017` |
| Transformation Design Framework — 8 yếu tố | T6 | `FW-007` |
| Knowledge–Behaviour Gap Model · Stages of Transformation | T5, T6 | `FW-007` (phần Circles) |
| AI as the Sixth Force · C-FISH / E-MICE / O-LION Leadership OS | T18 | _chưa có_ |
| Case: Microsoft Rebuilding Trust from the Top (Nadella) | T12 + case reading | `FW-013` |

---

## Khoảng trống đã nhận diện

Chưa phát hiện vấn đề nào trong 11 vấn đề **không có** framework ứng viên nào trong MEGROW. Sẽ xác nhận lại sau khi xử lý hết 20 topic và ghi vào `open_questions.md` nếu có khoảng trống thật.

**Đã xác nhận sau khi xử lý 9 topic:** mọi framework ứng viên liệt kê cho các topic này đều có thật trong tài liệu — không mục nào phải gỡ. Phát hiện thêm sáu framework không có trong danh sách ứng viên ban đầu: **HAI** và **Theory of Psychological Ownership** (Topic 06), **chuỗi sáu chặng MAP→ACT** (Topic 12), **Action titles và skim test** (Topic 19), **Connector Manager** và **lộ trình D–R–C** (Topic 09).

Lưu ý riêng cho bối cảnh người dùng: MEGROW không có nội dung chuyên biệt về **quản lý cộng tác viên (collaborator)** — nhân sự không chính thức, mức gắn kết khác nhân viên chính thức. Khả năng cần `[BỔ SUNG]` khi viết `PB` cho vấn đề số 5. Xem `open_questions.md` (OQ-005).

=====

<!-- nguồn: kb/00_index/glossary.md -->

# glossary.md — Thuật ngữ Việt–Anh

Thuật ngữ và tên framework giữ nguyên tiếng Anh, kèm nghĩa tiếng Việt. Mỗi chunk vẫn phải tự giải thích thuật ngữ ở lần xuất hiện đầu tiên (CLAUDE.md §5.3) — glossary này là bảng tra cứu chung, không thay thế việc đó.

**Trạng thái:** thuật ngữ từ Topic 01, 04, 06, 08, 09, 10, 12, 14 và 19 đã được thêm. Các topic còn lại sẽ bổ sung khi xử lý; tên framework ứng viên xem ở `problem_index.md`.

## Thuật ngữ vận hành kho tri thức

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn |
|---|---|---|
| Chunk | Mẩu tri thức | Một file Markdown chứa đúng một khái niệm / framework / vấn đề / playbook / topic / case, khoảng 150–600 từ, tự đứng được |
| Level | Cấp độ lãnh đạo | Trục phân loại chung mọi khóa: `SELF` (bản thân) · `TEAM` (đội nhóm) · `ORG` (tổ chức, chiến lược) |
| Pillar | Trụ cột | Cách chia nhóm topic riêng của từng khóa học. Với MEGROW là P1/P2/P3, ánh xạ sang level trong `courses.md` |
| Provenance | Truy xuất nguồn | Ghi rõ nội dung đến từ đâu, theo định dạng `[MÃ KHÓA / Topic XX / tên_file / Slide Y]` |
| Coverage | Độ phủ | Tỷ lệ trang slide đã được ánh xạ tới ít nhất một chunk hoặc được ghi "không có nội dung kiến thức" |
| RAG | Retrieval-Augmented Generation | Kỹ thuật cho agent truy xuất từng chunk liên quan thay vì đọc cả kho |
| Deprecated | Đã loại bỏ | Chunk không còn dùng nhưng vẫn giữ file, có `replaced_by` trỏ sang chunk thay thế |
| Capstone | Dự án tổng kết | Dự án nhóm cuối chương trình MEGROW (Topic 20, case Lumo/Mira) |
| Task force | Nhóm dự án | Nhóm ~8 học viên me.grow làm chung một mandate Capstone |

## Thuật ngữ chuyên môn từ khóa học

### Giao việc và mức sẵn sàng (Topic 01, 06, 10)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Situational Leadership (SLII) | Lãnh đạo theo tình huống | Điều chỉnh mức chỉ đạo và hỗ trợ theo mức sẵn sàng của từng người cho từng việc | `FW-001` |
| Readiness | Mức sẵn sàng | Mức độ một người đã sẵn sàng cho **một việc cụ thể** — theo việc, không phải nhãn vĩnh viễn | `FW-001` |
| Competence | Năng lực | Trục "họ *làm được* việc này không" | `FW-001` |
| Commitment | Cam kết | Trục "họ *muốn* và đủ tự tin nhận không" | `FW-001` |
| Skill / Will | Kỹ năng / Ý chí | Hai trục của bản thao tác Skill × Will Matrix | `FW-001-01` |
| Directing · Coaching · Supporting · Delegating (S1–S4) | Chỉ đạo · Kèm cặp · Hỗ trợ · Trao quyền | Bốn phong cách của SLII | `FW-001` |
| Direct · Coach · Motivate · Delegate | Chỉ đạo · Kèm cặp · Khơi động lực · Trao quyền | Bốn phong cách bản Topic 01 — "Motivate" thay cho "Supporting" | `FW-001-02` |
| Delegate outcomes, not just tasks | Giao kết quả, không giao đầu việc | Giao đủ phải nói rõ kết quả mong đợi, quyền sở hữu, quyền quyết định, tiêu chí thành công | `CON-004` |

### Trách nhiệm và quyền quyết định (Topic 06, 10)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Responsibility | Trách nhiệm thực thi | Ai phải *làm* công việc | `CON-003` |
| Accountability | Trách nhiệm giải trình | Ai *trả lời* về kết quả cuối cùng — nên quy về một người | `CON-003` |
| Decision rights | Quyền quyết định | Ai được quyết cái gì, trong phạm vi nào | `CON-003` |
| Single accountable owner | Chủ sở hữu duy nhất chịu trách nhiệm | Một người duy nhất trả lời cho một kết quả | `CON-003` |
| Psychological ownership | Sở hữu tâm lý | Cảm giác "đây là việc của tôi", gồm 5 thành tố | `FW-009` |
| Micromanagement vs visibility | Quản lý vi mô và tầm nhìn | Nhìn thấy trạng thái công việc mà không kiểm soát cách làm | `CON-005` |
| Cognitive load | Tải nhận thức | Tổng lượng thông tin, quyết định và chuyển ngữ cảnh một người phải xử lý | `CON-006` |
| Bottleneck | Nút thắt cổ chai | Điểm mà công việc dồn lại, thường là chính người quản lý | `CON-006` |
| AI · AII · CI · CII · GII | Năm phong cách ra quyết định | Từ tự quyết tới nhóm quyết (A=autocratic, C=consultative, G=group) | `FW-006` |

### Bước chuyển sang vai trò quản lý (Topic 01)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Individual Contributor (IC) | Cá nhân đóng góp | Người tạo ra kết quả bằng công việc của chính mình | `CON-001` |
| First-Line Manager | Quản lý trực tiếp | Cấp quản lý đầu tiên, quản lý người làm chứ không quản lý quản lý | `CON-001` |
| Break-even point | Điểm hòa vốn | Thời điểm bạn đã đóng góp cho tổ chức bằng đúng cái bạn đã tiêu của nó | `FW-003` |
| STARS | Năm loại tình huống thừa hưởng | Start-up · Turnaround · Accelerated Growth · Realignment · Sustaining Success | `FW-003` |
| Expertise trap | Cái bẫy chuyên môn | Tự làm thay vì xây năng lực để việc chạy mà không cần mình | `CON-002` |
| Compliance vs commitment | Tuân thủ và cam kết | Làm theo vì phải, so với làm theo vì muốn | `FW-002` |
| Four Stages of Contribution | Bốn giai đoạn đóng góp | Phụ thuộc → độc lập → qua người khác → chiến lược | `FW-004` |
| Task-Oriented / People-Oriented | Hướng công việc / Hướng con người | Hai nhóm hành vi lãnh đạo từ nghiên cứu Michigan và Ohio State | `FW-005` |

### Thay đổi hành vi và AI (Topic 06)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| HAI — Human Artificial Intelligence | Trí tuệ người kết hợp AI | Đặt đúng loại trí tuệ vào đúng việc: Human, AI hay cả hai | `FW-010` |
| Transformation Design Framework | Khung Thiết kế Chuyển đổi | 8 yếu tố thiết kế thay đổi hành vi bền vững | `FW-007` |
| Socium | Đòn bẩy ảnh hưởng xã hội | 7 đòn bẩy: Comparison, Competition, Recognition, Cooperation, Learning, Norms, Facilitation | `FW-008` |
| Knowledge–Behaviour Gap | Khoảng cách giữa biết và làm | Biết điều gì quan trọng không đủ; năng suất đến từ việc làm điều đó đều đặn | `FW-007` |

### Stakeholder và ảnh hưởng (Topic 12, 19)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Stakeholder | Bên liên quan | Bất kỳ ai có thể ảnh hưởng tới, hoặc bị ảnh hưởng bởi, tổ chức hay sáng kiến | `FW-011` |
| Stakeholder Ecosystem Map | Bản đồ hệ sinh thái các bên | Hình dung mọi bên có lợi ích liên quan, vượt ngoài sơ đồ tổ chức | `FW-011` |
| Power–Interest Matrix | Ma trận quyền lực – mức quan tâm | Bốn ô: Manage Closely · Keep Satisfied · Keep Informed · Monitor | `FW-012` |
| Power | Quyền lực | Tiềm năng tác động tới hành vi và làm xong việc qua người khác; **tự nó trung tính** | `FW-014` |
| Legitimate / Reward / Coercive power | Quyền lực chính danh / thưởng / cưỡng chế | Ba nguồn gắn với **vị trí** trong tổ chức | `FW-014` |
| Expert / Referent / Informational power | Quyền lực chuyên môn / quy chiếu / thông tin | Ba nguồn gắn với **con người bạn** — phần tự xây được | `FW-014` |
| Power Audit | Kiểm kê quyền lực | Ba câu: họ có quyền lực gì, tôi có gì, tôi xây thêm được gì | `FW-014` |
| Influence | Ảnh hưởng | Năng lực trở thành lực tác động lên hành động, hành vi hoặc quan điểm người khác | `FW-015` |
| Influence Without Authority | Gây ảnh hưởng không có quyền chỉ đạo | Đổi "làm sao để họ ủng hộ tôi" thành "giá trị chung nằm ở đâu" | `FW-015` |
| Executive Influence Map | Bản đồ ảnh hưởng | Chuỗi 5 câu: họ coi trọng gì → sợ gì → cần gì ở tôi → tôi cần gì → trò chuyện gì tiếp | `FW-015` |
| Champions / Influencers / Decision Makers / Blockers / Undecided | Năm nhóm lập trường | Phân loại các bên theo thái độ với thay đổi | `FW-017` |
| Guiding Coalition | Liên minh dẫn dắt | Nhóm các bên có ảnh hưởng đủ sức dịch chuyển tổ chức | `FW-017` |
| Pre-wiring | Vận động trước họp | Giành đồng thuận trước cuộc họp quyết định, không phải trong nó | `CON-007` |

### Xung đột và ra quyết định nhóm (Topic 12, 14)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Assertiveness / Cooperativeness | Mức quyết đoán / mức hợp tác | Hai trục của Thomas–Kilmann | `FW-016` |
| Avoiding · Competing · Compromising · Accommodating · Collaborating | Né tránh · cạnh tranh · thỏa hiệp · nhường nhịn · hợp tác | Năm chế độ ứng xử với xung đột | `FW-016` |
| Ladder of Inference | Thang suy luận | Năm nấc từ kho dữ liệu sẵn có lên tới kết luận | `FW-020` |
| Conclusion Rung | Nấc kết luận | Nơi quá nhiều cuộc trò chuyện ở công sở diễn ra | `FW-020` |
| Pool of Available Data | Kho dữ liệu sẵn có | Toàn bộ dữ liệu, chung cho mọi người; mỗi người chỉ chọn một phần | `FW-020` |
| Advocacy / Inquiry | Trình bày / hỏi để hiểu | Hỏi trước, trình bày sau — "seek first to understand" | `FW-021` |
| False dichotomy | Thế lưỡng nan giả | Tưởng phải chọn giữa độc đoán và đồng thuận; thực ra làm được cả hai | `CON-009` |

### Trình bày business case (Topic 19)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| SCQA | Tình huống – Biến cố – Câu hỏi – Câu trả lời | Cấu trúc mở đầu biến đề xuất thành câu chuyện người nghe đi theo được | `FW-018` |
| Governing thought | Luận điểm chủ đạo | Khuyến nghị gói trong một câu, đặt ở đỉnh kim tự tháp | `FW-019` |
| MECE | Không chồng lấn, không bỏ sót | Mutually Exclusive, Collectively Exhaustive | `FW-019` |
| Reasons / Chain | Lý do / chuỗi | "và thêm nữa" cho các trụ; "do đó" bên trong một trụ | `FW-019` |
| Action title | Tiêu đề nêu kết luận | Tiêu đề slide nêu kết luận, không nêu chủ đề | `FW-019-01` |
| Skim test | Phép thử lướt | Đọc riêng tiêu đề các slide; nếu kể được trọn câu chuyện thì lập luận đứng vững | `FW-019-01` |

### Hội thoại về hiệu suất và hành vi (Topic 04, 08)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| AMO | Năng lực – Động lực – Cơ hội | Ba nhánh chẩn đoán vì sao hiệu suất đi xuống | `FW-023` |
| Sustainable performance management | Quản trị hiệu suất bền vững | Đảm bảo nhân viên làm tốt lâu dài mà không kiệt sức, mất gắn kết, hổng năng lực hay gặp rào cản tổ chức | `TOP-MEGROW-04` |
| SAIL | Nêu – Hỏi – Xác định – Khởi động | State the gap · Ask and understand · Identify root causes · Launch improvement actions | `FW-024` |
| Performance recovery agreement | Thỏa thuận phục hồi hiệu suất | Chốt kỳ vọng, hỗ trợ, thời hạn và mốc theo dõi | `FW-024` |
| Camera test | Phép thử camera | Camera có ghi lại được đúng điều bạn đang mô tả không? Nếu không, đó là nhãn dán | `CON-010` |
| 5-Impact Test | Phép thử năm tác động | Performance · People · Culture · Trust · Policy/Ethics | `FW-026` |
| SBI | Situation–Behavior–Impact | Khung phản hồi của Center for Creative Leadership, nền của 5-Impact Test | `FW-026` |
| Intention ≠ impact | Ý định khác tác động | Ghi nhận ý định rồi chuyển trọng tâm sang tác động, không tranh cãi "có cố ý hay không" | `FW-025` |
| Factual / emotional / intuitive listening | Nghe sự kiện / cảm xúc / trực giác | Ba cấp độ lắng nghe, mỗi cấp cho một mục đích | `CON-011` |
| Self-awareness / Self-management | Tự nhận thức / tự quản lý | Nhận ra mình đang cảm thấy gì; quyết định làm gì với điều đó | `CON-013` |

### Coaching và phát triển con người (Topic 09)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Teacher / Always-On / Cheerleader / Connector | Bốn kiểu quản lý khi coaching | Bốn cách tiếp cận coaching, mỗi kiểu tạo trải nghiệm phát triển khác nhau | `FW-027` |
| Connector Manager | Quản lý kiểu kết nối | Hiểu người, coach có chọn lọc, kết nối tới nguồn khác — *phát triển là một mạng lưới* | `FW-032` |
| Judicious generosity | Hào phóng có kỷ luật | Chia sẻ công trạng, thông tin, quyền tiếp cận — nhưng **kết nối chứ không giải cứu** | `FW-032` |
| KSMCE | Năm lăng kính chẩn đoán | Knowledge · Skills · Motivation · Career · Environment | `FW-028` |
| Development readiness | Mức sẵn sàng phát triển | Thang 5 mục, 5–25 điểm, quyết định quy mô bước phát triển kế tiếp | `FW-029` |
| Right-size the stretch | Vừa đủ thử thách | Phát triển nên thử thách, không làm quá tải hay bỏ phí | `FW-029` |
| D–R–C | Chẩn đoán – Sẵn sàng – Coach & Kết nối | Lộ trình ba chặng bảo vệ khỏi việc khuyên quá sớm | `FW-030` |
| EDGE | Explore – Decode – Generate – Execute | Bốn chặng biến phản tư thành chiến lược tăng trưởng cá nhân | `FW-031` |
| VRIFA | Năm phép thử lợi thế cá nhân | Valuable · Rare · Inimitable · Future-relevant · Authentic | `FW-031` |
| Professional signature | Dấu ấn nghề nghiệp | *"Khi người ta cần ______, tôi muốn họ nghĩ tới tôi."* | `FW-031` |
