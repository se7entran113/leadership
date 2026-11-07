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

---

## MEGROW — me.grow (2026) L2 Leadership Development Program

Pillar lấy từ taxonomy người dùng duyệt (xem `courses.md`), nhãn `[SUY LUẬN — người dùng duyệt]`.
Cột **Level** ghi level chính (từ pillar) trước, level phụ sau dấu `+` khi nội dung thực sự thuộc về level đó.

### P1 `LEAD_SELF` — Topic 1–5 (level chính SELF)

| ID | Topic | Tên topic | Giảng viên | Level | File | Trang | Trạng thái | Ngày thêm |
|---|---:|---|---|---|---|---:|---|---|
| `TOP-MEGROW-01` | 1 | Navigating the Leadership Transition | AP Burkhard Schrage | SELF + TEAM | `Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf` | 25 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-02` | 2 | Driving Operational Execution | Dr Phuong (Emmy) Hoang | SELF + TEAM, ORG | `Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf` | 35 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-03` | 3 | Audit Mindset & Biases | Dr Thu Nguyen | SELF | `Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf` | 30 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-04` | 4 | Practice Performance Conversations (AMO Framework) | AP Elaine Chew | SELF + TEAM | `Topic 4 - Practice Performance Conversations - AP Elaine Chew.pdf` | 46 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-05` | 5 | Optimise Personal Productivity | AP Agnis Stibe | SELF | `Topic 5 - Optimise Personal Productivity - Agnis Stibe.pdf` | 78 | chưa xử lý | 2026-11-07 |

### P2 `LEAD_PEOPLE_AND_TEAMS` — Topic 6–11 (level chính TEAM)

| ID | Topic | Tên topic | Giảng viên | Level | File | Trang | Trạng thái | Ngày thêm |
|---|---:|---|---|---|---|---:|---|---|
| `TOP-MEGROW-06` | 6 | Delegation & Accountability in Fast-Paced Teams | AP Agnis Stibe | TEAM + SELF | `Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf` | 69 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-07` | 7 | Building Team Capability & Growth (LEGO® Serious Play®) | Dr Thao Luong | TEAM | `Topic 7 - Building Team Capability and Growth - Thao Luong.pdf` | 43 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-08` | 8 | Correcting Behaviour Through Coaching | Dr Thao Luong | TEAM + SELF | `Topic 8 - Correcting Behaviour Through Coaching - Thao Luong.pdf` | 44 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-09` | 9 | Coaching for High Performance | Dr Quyen Dang | TEAM | `Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf` | 54 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-10` | 10 | Adapt Your Leadership Style | Dr Tony Nguyen | TEAM | `Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf` | 38 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-11` | 11 | Customised Approach for Individuals | Dr Gavin Nicholson | TEAM + SELF | `Topic 11 - Customise Approach for Individuals - Gavin Nicholson-1.pdf` | 45 | chưa xử lý | 2026-11-07 |

### P3 `LEAD_ACROSS_ORGANISATION` — Topic 12–20 (level chính ORG)

| ID | Topic | Tên topic | Giảng viên | Level | File | Trang | Trạng thái | Ngày thêm |
|---|---:|---|---|---|---|---:|---|---|
| `TOP-MEGROW-12` | 12 | Stakeholder Influence & Leadership in Technology | Prof Seng Kiat Kok | ORG | `Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf` | 41 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-12` | 12 | ↳ *Case reading bổ sung:* Microsoft's Turnaround – The Satya Nadella Story | Bloomberg Businessweek, 6/5/2019 | ORG | `[Case Reading] Microsoft’s Turnaround – The Satya Nadella Story.pdf` | 7 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-13` | 13 | Building Trust & Open Communication in Teams | Dr Justin Xavier Batinadan | ORG + TEAM | `Topic 13 - Building Trust & Open Communication in Teams - Justin Xavier.pdf` | 30 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-14` | 14 | Decision Making in Cross-functional Teams | Dr Phuong Nguyen | ORG + TEAM | `Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf` | 14 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-14` | 14 | ↳ *Case reading bổ sung:* The BCPC Internet Strategy Team: An Exercise | Amy C. Edmondson, HBS 604-035 | ORG + TEAM | `[Case Reading] of topic 14 .pdf` | 4 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-15` | 15 | From Stakeholder Insight to Market Impact | Dr Phuong Nguyen | ORG | `Topic 15 - From Stakeholder Insight to Market Impact - Dr Phuong Nguyen.pdf` | 21 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-16` | 16 | Solve Tech & Organisational Blockers | Dr Thuan Nguyen & Dr Bidyut Hazarika | ORG + TEAM | `Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf` | 37 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-17` | 17 | Apply Strategic Thinking | AP Burkhard Schrage | ORG | `Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf` | 39 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-18` | 18 | Leading in the AI-Enabled Organisation | Prof Trung Nguyen | ORG + TEAM, SELF | `Topic 18 - Leading in the AI-Enabled Organisation - Prof Trung Nguyen.pdf` | 44 | chưa xử lý | 2026-11-07 |
| `TOP-MEGROW-19` | 19 | Presenting Business Cases (SCQA, Pyramid Principle, Stakeholder Mapping) | Dr Tony Nguyen | ORG | `Topic 19 - Present Business Case - Dr Tony Nguyen.pdf` | 33 | chưa xử lý | 2026-11-07 |
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

Mọi chunk (trừ chunk `deprecated`, vẫn liệt kê nhưng ghi rõ trạng thái) phải xuất hiện ở đây.

**Trạng thái kho: 0 chunk.** Inventory MEGROW đã xong (22 tài liệu / 805 trang), chưa tạo chunk kiến thức nào. Theo CLAUDE.md §9, lệnh "Lập inventory" dừng lại trước bước tạo chunk.

Bước tiếp theo: `Xử lý megrow topic 1–3` (tối đa 3 topic mỗi lần).

---

## Khái niệm & nguyên tắc (CON)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có)_ | | | | | |

## Framework (FW)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có)_ | | | | | |

## Vấn đề (PRB)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có)_ | | | | | |

## Playbook (PB)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có)_ | | | | | |

## Topic (TOP)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có — 20 topic MEGROW đã đăng ký trong `topic_map.md`, chunk sẽ tạo khi xử lý)_ | | | | | |

## Tình huống thực tế (CASE)

| ID | Tiêu đề | Loại | Level | Khóa | Tóm tắt 1 dòng |
|---|---|---|---|---|---|
| _(chưa có)_ | | | | | |

---

## Bộ đếm ID tiếp theo

| Tiền tố | ID tiếp theo |
|---|---|
| `CON` | `CON-001` |
| `FW` | `FW-001` |
| `PRB` | `PRB-001` |
| `PB` | `PB-001` |
| `CASE` | `CASE-001` |

=====

<!-- nguồn: kb/00_index/problem_index.md -->

# problem_index.md — Vấn đề → nguyên nhân → framework

Bảng tra cứu chính cho câu hỏi: *"Tôi đang gặp vấn đề này, dùng framework nào?"*

**Trạng thái:** chưa có chunk `PRB` hoặc `FW` nào trong kho. Cột **Framework ứng viên** dưới đây là `[SUY LUẬN]` — nhận diện từ tiêu đề trang khi lập inventory MEGROW, **chưa đọc nội dung chi tiết, chưa kiểm chứng**. Cột **ID** sẽ được điền khi chạy lệnh `Xử lý megrow topic X–Y`.

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

### PRB-? · 2. Làm việc với stakeholder để xây dựng và thống nhất bài toán
*Thuyết phục khi không có quyền chỉ đạo, chuyển ngôn ngữ business sang bài toán DS, quản lý kỳ vọng về độ bất định, biết từ chối.*
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Freeman (1984) Stakeholder Theory · Mendelow (1991) Power–Interest Matrix · Stakeholder Ecosystem Map | T12 | _chưa có_ |
| French & Raven (1959) Sources of Social Power · Power Audit | T12 | _chưa có_ |
| Cohen & Bradford (2017) Influence Without Authority · Executive Influence Map · Influence Conversation Planner | T12 | _chưa có_ |
| Kotter (2012) Stakeholder Coalitions · Stakeholder Coalition Map | T12 | _chưa có_ |
| SCQA · Pyramid Principle · MECE · Action titles · Pre-wiring | T19 | _chưa có_ |
| Power–Interest Grid (bản của T19) | T19 | _chưa có_ |
| Yukl & Tracey (1992) influence tactics · Mayer, Davis & Schoorman (1995) trust = ability·benevolence·integrity | T3 | _chưa có_ |
| Ladder of Inference (Argyris) · Advocacy ↔ Inquiry | T14 | _chưa có_ |

### PRB-? · 3. Thiết kế framework làm việc và giải quyết vấn đề cho team
*Quy trình, phối hợp, ra quyết định, tiêu chuẩn chất lượng.*
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Team Delivery System · Review rhythm (daily/weekly/milestone gate) · Response thresholds · Monitor the work system, not the person | T2 | _chưa có_ |
| Owner / Responsibility / Accountability / RACI · Decision rights | T2, T6 | _chưa có_ |
| AI-augmented Design Thinking (Stanford 5 phases; Understand–Create–Deliver) · Empathy Map · 7-day test | T16 | _chưa có_ |
| Vroom–Yetton–Jago Model (AI / AII / CI / CII / GII) | T10 | _chưa có_ |
| Human–AI Decision Rights (4 mức: AI Assists → AI Recommends → AI Acts with Approval → AI Acts Within Boundaries) | T18 | _chưa có_ |

### PRB-? · 4. Chuyển dịch từ người làm chuyên môn sang người quản lý
*Buông việc kỹ thuật, cân bằng tự làm và dẫn dắt, quản lý thời gian và năng lượng.*
**Level:** SELF

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Dalton, Thompson & Price (1977) Four Stages of Contribution | T1 | _chưa có_ |
| Hill (2007) Five Myths of the New Manager · Ba cái bẫy (làm thay, né giao việc, kỳ vọng ngầm) | T1 | _chưa có_ |
| Watkins (2013) First 90 Days · STARS diagnostic · Break-even point · 12 hành động 30/60/90 | T1 | _chưa có_ |
| IC → Manager mindset shift | T1, T2, T8 | _chưa có_ |
| Expert bias · 5-Step Bias Self-Audit · Audit Mindset | T3 | _chưa có_ |
| Knowledge–Behaviour Gap Model (Knowledge → Acceptance → Intention → Behaviour) | T5, T6 | _chưa có_ |
| FranklinCovey Time Matrix · Eisenhower Matrix · GTD · Human Artificial Intelligence (HAI) | T5 | _chưa có_ |
| Self-awareness & Self-management (Emotional Intelligence) | T8, T11 | _chưa có_ |

### PRB-? · 5. Giao việc và phát triển theo năng lực từng người
*Trao quyền cho Senior, hướng dẫn DS, phạm vi rõ cho collaborator.*
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Hersey & Blanchard (1969) Life Cycle Theory / Situational Leadership II — S1 Directing · S2 Coaching · S3 Supporting · S4 Delegating | T1, T6, T10 | _chưa có_ |
| Skill × Will readiness matrix (Landsberg, *The Tao of Coaching*) — Direct / Coach / Motivate / Delegate | T1 | _chưa có_ |
| Blake & Mouton (1964) Leadership Grid · Task-oriented vs People-oriented behaviours | T10 | _chưa có_ |
| Vroom–Yetton–Jago Model — mức tham gia của nhân viên vào quyết định | T10 | _chưa có_ |
| Delegate outcomes not tasks · Accountability = clarity + ownership + follow-through · Empower without micromanaging | T6 | _chưa có_ |
| Theory of Psychological Ownership (identity · accountability · self-efficacy · belongingness · responsibility) | T6 | _chưa có_ |
| Employee Development Readiness Assessment · Chẩn đoán 5 nguyên nhân gốc (Knowledge · Skills · Motivation · Career · Environment) | T9 | _chưa có_ |
| EDGE (Explore · Decode · Generate · Execute) · Personal Competitive Advantage | T9 | _chưa có_ |

---

## Mức ưu tiên TRUNG BÌNH

Yêu cầu: có chunk `PRB` riêng, liên kết đầy đủ.

### PRB-? · 6. Feedback, coaching và trao đổi về hiệu suất
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| AMO Framework (Ability · Motivation · Opportunity) | T4 | _chưa có_ |
| SAIL (State the gap · Ask and understand · Identify root causes · Launch improvement actions) | T4 | _chưa có_ |
| NOTICE → CONVERSE → COACH → HOLD ACCOUNTABLE | T8 | _chưa có_ |
| 5-Impact Test (phỏng theo SBI của CCL) — quyết định có nên xử lý hành vi hay không | T8 | _chưa có_ |
| Ba cấp độ lắng nghe (factual · emotional · ...) · Observation vs judgement · Intention ≠ impact | T8 | _chưa có_ |
| Ma trận Support × Accountability | T8 | _chưa có_ |
| Bốn kiểu quản lý: Teacher · Always-On · Cheerleader · Connector · Ba huyền thoại của Always-On | T9 | _chưa có_ |
| Lộ trình D–R–C (Diagnose → Readiness → Coach & Connect) | T9 | _chưa có_ |
| T-GROW coaching model (Topic · Goal · Reality · Options · Will) | T18 | _chưa có_ |

### PRB-? · 7. Động lực, gắn kết và giữ người
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| McClelland — Need for Achievement / Affiliation / Power | T11 | _chưa có_ |
| Alderfer ERG Theory (Existence · Relatedness · Growth) | T11 | _chưa có_ |
| Ba kết nối của Connector Manager: Employee · Team · Organisation | T9 | _chưa có_ |
| Personal Competitive Advantage · EDGE growth strategy | T9 | _chưa có_ |
| Apprenticeship Gap · EEE diagnostic (Environment · Equipping · Experience) | T18 | _chưa có_ |
| Social influence levers: Comparison · Competition · Recognition · Cooperation · Learning · Norms · Facilitation | T6 | _chưa có_ |

### PRB-? · 8. Làm việc với cấp trên và gắn với chiến lược tổ chức
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Line-of-sight test (VNG mission → Zalo direction → department goals → team goals) | T17 | _chưa có_ |
| Reframe → Surface assumptions → Compare & recommend · Options table | T17 | _chưa có_ |
| SCQA · Pyramid Principle · Pre-wiring · Action titles | T19 | _chưa có_ |
| Influencing upwards (Cohen & Bradford exchange) | T12 | _chưa có_ |
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
| Kouzes & Posner (2023) The Leadership Challenge — 5 practices | T12, T18 | _chưa có_ |
| Psychological safety with accountability | T6 | _chưa có_ |

### PRB-? · 10. Xung đột trong team hoặc giữa các team
**Level:** TEAM, ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Thomas–Kilmann Conflict Mode Instrument · Conflict Response Planner | T12 | _chưa có_ |
| Ladder of Inference (Argyris) · Seek first to understand (Inquiry) rồi Advocacy | T14 | _chưa có_ |
| Cùng dữ liệu, khác kết luận — chọn lọc dữ liệu khác nhau (case BCPC) | T14 | _chưa có_ |
| Role Play: Mediating Different Working Styles | T11 | _chưa có_ |
| "When they push back": LISTEN → ACKNOWLEDGE → REFOCUS → HOLD | T8 | _chưa có_ |

### PRB-? · 11. Dẫn dắt thay đổi
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Kotter (2012) Leading Change Through Stakeholder Coalitions (dùng chọn lọc, không phải đủ 8 bước) | T12 | _chưa có_ |
| Transformation Design Framework của Agnis Stibe — 8 yếu tố: Triangle · Curve · Metric · Circles · Architecture · Socium · Moderation · Ethics | T6 | _chưa có_ |
| Knowledge–Behaviour Gap Model · Stages of Transformation (Self-contained → Social Influencing → Identity Change → Self-driven) | T5, T6 | _chưa có_ |
| AI as the Sixth Force · C-FISH / E-MICE / O-LION Leadership OS | T18 | _chưa có_ |
| Case: Microsoft Rebuilding Trust from the Top (Nadella) | T12 + case reading | _chưa có_ |

---

## Khoảng trống đã nhận diện

Chưa phát hiện vấn đề nào trong 11 vấn đề **không có** framework ứng viên nào trong MEGROW. Sẽ xác nhận lại sau khi xử lý hết 20 topic và ghi vào `open_questions.md` nếu có khoảng trống thật.

Lưu ý riêng cho bối cảnh người dùng: MEGROW không có nội dung chuyên biệt về **quản lý cộng tác viên (collaborator)** — nhân sự không chính thức, mức gắn kết khác nhân viên chính thức. Khả năng cần `[BỔ SUNG]` khi viết `PB` cho vấn đề số 5. Xem `open_questions.md` (OQ-005).

=====

<!-- nguồn: kb/00_index/glossary.md -->

# glossary.md — Thuật ngữ Việt–Anh

Thuật ngữ và tên framework giữ nguyên tiếng Anh, kèm nghĩa tiếng Việt. Mỗi chunk vẫn phải tự giải thích thuật ngữ ở lần xuất hiện đầu tiên (CLAUDE.md §5.3) — glossary này là bảng tra cứu chung, không thay thế việc đó.

**Trạng thái:** mới chỉ có thuật ngữ vận hành của kho. Thuật ngữ chuyên môn của MEGROW sẽ được thêm khi chạy lệnh `Xử lý megrow topic X–Y`; tên framework ứng viên đã nhận diện xem ở `problem_index.md`.

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

_(chưa có — sẽ thêm khi xử lý từng topic)_
