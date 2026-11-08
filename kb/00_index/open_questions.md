# open_questions.md — Câu hỏi mở và mục chờ xác nhận

Mọi mục `[CẦN XÁC NHẬN]`, `[KHÓ ĐỌC]` và mâu thuẫn chờ người dùng quyết định.

**Trạng thái:** 9 mục — 5 từ bước inventory (2026-11-07), 3 từ đợt Topic 01/06/10, 1 từ đợt Topic 12/19/14 (2026-11-08).

| ID | Mức | Tiêu đề | Trạng thái |
|---|---|---|---|
| OQ-001 | Cao | Taxonomy pillar MEGROW chưa đối chiếu tài liệu chương trình chính thức | Đang mở |
| OQ-002 | Trung bình | Số topic trên slide lệch số trong tên file (Topic 3 và Topic 4) | Đang mở |
| OQ-003 | Cao | Topic 20 slide 21–27 chứa tên thật học viên | Đã quyết định — không trích |
| OQ-004 | Thấp | Case reading Microsoft thuộc topic nào | Đã quyết định — Topic 12 |
| OQ-005 | Trung bình | MEGROW không có nội dung về quản lý cộng tác viên | Đang mở |
| OQ-006 | Thấp | Topic 10 slide 26 dán nhãn D1/D3/D4 cho phong cách thay vì mức phát triển | Đang mở |
| OQ-007 | Thấp | Tên mô hình "Vroom–Yetton–Jago" không khớp danh mục nguồn của chính deck | Đang mở |
| OQ-008 | Trung bình | Khung 8 yếu tố của Topic 06 không có slide văn bản giải thích | Đang mở |
| OQ-009 | Thấp | Topic 12 ghi chặng TRUST dựa trên Edmondson nhưng không có slide nào giải thích | Đang mở |

---

## OQ-001 — Taxonomy pillar MEGROW chưa đối chiếu tài liệu chương trình chính thức

**Mức:** Cao · **Ngày mở:** 2026-11-07 · **Trạng thái:** Đang mở

**Vấn đề.** CLAUDE.md §2 nêu me.grow có 20 topic chia theo 3 pillar (P1 Master the Personal Shift → SELF, P2 Develop the Team Talent → TEAM, P3 Navigate the Strategic Landscape → ORG), nhưng **không nói topic nào thuộc pillar nào**.

**Đã kiểm tra.** Quét toàn văn 805 trang của cả 22 tài liệu trong `raw/megrow/` tìm các chuỗi `pillar`, `Master the Personal`, `Develop the Team`, `Navigate the Strategic`. Kết quả: **không trang nào ghi pillar hay tên pillar**. Các lần xuất hiện chữ "pillar" ở Topic 18 slide 9 và Topic 19 slide 16/19/20/22/26/28/30 đều mang nghĩa khác ("four pillars of AI readiness", "pillar" của một lập luận Pyramid Principle). Footer slide chỉ có dạng `RMIT | Zalo me.grow`.

**Quyết định tạm thời (người dùng duyệt 2026-11-07).** Dùng taxonomy do người dùng chỉ định:

| Pillar | Topic | Level chính |
|---|---|---|
| P1 `LEAD_SELF` | 1 – 5 | SELF |
| P2 `LEAD_PEOPLE_AND_TEAMS` | 6 – 11 | TEAM |
| P3 `LEAD_ACROSS_ORGANISATION` | 12 – 20 | ORG |

Người dùng nêu rõ: *"This is a user-approved knowledge taxonomy, not a verified official RMIT pillar structure."* Nhãn trong kho: `[SUY LUẬN — người dùng duyệt]`.

**Cần người dùng.** Nếu sau này có lịch học, slide giới thiệu chương trình, hoặc trang Canvas nào ghi pillar chính thức: cung cấp để đối chiếu. Nếu khác, áp dụng quy tắc mâu thuẫn ở CLAUDE.md §5.2 — giữ cả hai phiên bản, không ghi đè.

**Điểm lệch đáng chú ý nếu đối chiếu.** Tên pillar P2 trong CLAUDE.md là "Develop the Team Talent" và chỉ phủ Topic 6–11 theo taxonomy này; các Topic 13 (Building Trust in Teams) và 14 (Decision Making in Cross-functional Teams) nằm ở P3 dù nội dung rõ ràng ở cấp đội nhóm. Đã xử lý bằng cách gán thêm level phụ `TEAM` cho hai topic này (ràng buộc 3 của người dùng: không giới hạn truy xuất theo pillar chính).

---

## OQ-002 — Số topic trên slide lệch số trong tên file

**Mức:** Trung bình · **Ngày mở:** 2026-11-07 · **Trạng thái:** Đang mở

**Vấn đề.** Hai deck ghi số topic trên trang bìa khác với số trong tên file:

| File | Số trong tên file | Số in trên slide 1 |
|---|---:|---|
| `Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf` | 3 | "Topic 2: Audit Mindset & Biases" |
| `Topic 4 - Practice Performance Conversations - AP Elaine Chew.pdf` | 4 | "Topic 5: Practise Performance Conversation" |

18 deck còn lại hoặc khớp (Topic 1, 2, 7, 8, 9, 17, 18) hoặc không in số topic lên bìa.

**Cập nhật 2026-11-08** (sau khi xử lý Topic 04): nội dung deck Topic 04 nhắc tới *"audited mindset"* ở slide 10 — thuật ngữ lõi của Topic 03 (Audit Mindset & Biases) — và Topic 03 slide 28 kết bằng *"Sáng nay bạn đã kiểm toán phán đoán. Chiều nay bạn thực hành cuộc trò chuyện."* Hai deck vì vậy **diễn ra cùng một ngày, Topic 03 buổi sáng và Topic 04 buổi chiều**. Điều này củng cố thứ tự 3 → 4 theo tên file, và cho thấy số in trên bìa hai deck nhiều khả năng là sót từ bản nháp trước.

**Quyết định tạm thời.** Lấy **số trong tên file** làm chuẩn, vì nó nhất quán cho cả 20 topic và khớp thứ tự chương trình được Topic 17 slide 38 xác nhận (Topic 17 sáng → Topic 18 chiều → Topic 19 tuần 11 sáng → Topic 20 Capstone).

**Cần người dùng.** Xác nhận số topic đúng của hai buổi này theo lịch học thực tế. Nếu tên file sai thì **không đổi tên file trong `raw/`** (CLAUDE.md §12) — chỉ ghi chú lại trong `topic_map.md`.

---

## OQ-003 — Topic 20 slide 21–27 chứa tên thật của học viên

**Mức:** Cao · **Ngày mở:** 2026-11-07 · **Trạng thái:** Đã quyết định

**Vấn đề.** Slide 21–27 của `Topic 20 - Capstone Research & Alignment - AP Burkhard Schrage.pdf` liệt kê danh sách thành viên 7 task force kèm **họ tên thật** của học viên và tên coach.

**Quyết định.** Theo CLAUDE.md §7 (CASE luôn ẩn danh, không ghi thông tin nhận dạng đồng nghiệp) và §12:

- `slide_inventory.md` chỉ ghi tiêu đề trang ("Task force N làm Mandate X, coach là ..."), đã bao gồm tên coach vì đó là giảng viên của chương trình chứ không phải đồng nghiệp của người dùng.
- **Không trích họ tên học viên vào bất kỳ chunk nào.** Khi xử lý Topic 20, các slide này ghi vào `coverage_matrix.md` là "không có nội dung kiến thức — danh sách nhân sự, đã ẩn danh".
- Nội dung kiến thức của Topic 20 nằm ở slide 1–20 và 28 (rubric).

---

## OQ-004 — Case reading Microsoft thuộc topic nào

**Mức:** Thấp · **Ngày mở:** 2026-11-07 · **Trạng thái:** Đã quyết định

**Vấn đề.** File `[Case Reading] Microsoft’s Turnaround – The Satya Nadella Story.pdf` (Bloomberg Businessweek, 6/5/2019, 7 trang) không ghi thuộc topic nào. File case reading còn lại ghi rõ ("of topic 14").

**Bằng chứng.** Chỉ 2 deck nhắc Microsoft/Nadella:
- Topic 12 slide 14: `CASE STUDY · TECH INDUSTRY — Microsoft: Rebuilding Trust from the Top`, nói đúng về Nadella và văn hóa silo năm 2014.
- Topic 18 slide 10 và 15: nhắc Microsoft nhưng về năng suất AI (Microsoft × Accenture) và trích dẫn Bill Gates — không liên quan Nadella turnaround.

**Quyết định (người dùng duyệt 2026-11-07).** Gán là **tài liệu bổ sung của Topic 12**. Nhãn `[SUY LUẬN — người dùng duyệt]`. Ghi trong `topic_map.md` ở dòng phụ của `TOP-MEGROW-12`.

---

## OQ-005 — MEGROW không có nội dung về quản lý cộng tác viên

**Mức:** Trung bình · **Ngày mở:** 2026-11-07 · **Trạng thái:** Đang mở

**Vấn đề.** Team của người dùng gồm cả nhân sự chính thức và **cộng tác viên** (1 Data Science Collaborator, 1 Data Labeling Collaborator) — khác nhau về kinh nghiệm, mức độ gắn kết, phạm vi trách nhiệm và thời gian gắn bó.

Rà soát tiêu đề 805 trang: **không topic nào của MEGROW xử lý riêng tình huống quản lý nhân sự không chính thức.** Các framework về giao việc (Situational Leadership, Skill×Will, Psychological Ownership) và phát triển (EDGE, Development Readiness) đều giả định nhân viên chính thức có lộ trình nghề nghiệp trong tổ chức.

**Hệ quả.** Vấn đề ưu tiên Cao số 5 ("Giao việc và phát triển theo năng lực từng người — phạm vi rõ cho collaborator") sẽ có khoảng trống. Khi viết chunk `PB` cho vấn đề này ở bước "Rà soát tổng thể", phần về cộng tác viên nhiều khả năng phải gắn nhãn `[BỔ SUNG]`.

**Cần người dùng.** Xác nhận có muốn Claude bổ sung kiến thức ngoài khóa học (gắn `[BỔ SUNG]`, ưu tiên ví dụ bối cảnh team Data Science) cho phần này không, hay để trống và ghi rõ là khoảng trống của khóa học.

---

## OQ-006 — Topic 10 slide 26 dán nhãn D1/D3/D4 cho phong cách thay vì mức phát triển

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 26 của Topic 10 ánh xạ ba vòng hoạt động Sequence Challenge lên ma trận và dán nhãn **"D1: Directing"**, **"D3: Supporting"**, **"D4: Delegating"**. Trong Situational Leadership II gốc (Blanchard, Zigarmi & Zigarmi 2013), ký hiệu **D** (Development level) chỉ **mức phát triển của người nhận việc**, còn **S** (Style) mới chỉ **phong cách của người lãnh đạo**. Slide 27 ngay sau đó dùng đúng quy ước S1–S4.

**Đã làm.** Ghi nguyên trạng trong `FW-001` và `FW-001-02`, kèm nhãn `[SUY LUẬN]` nêu khả năng là lỗi nhãn trên slide. **Không tự sửa** theo CLAUDE.md §5.2.

**Cần người dùng.** Xác nhận với giảng viên hoặc tài liệu lớp xem đây là lỗi slide hay là quy ước riêng của buổi học.

---

## OQ-007 — Tên mô hình "Vroom–Yetton–Jago" không khớp danh mục nguồn của chính deck

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 36 của Topic 10 đặt tên mô hình là **"Vroom–Yetton–Jago Model"**, nhưng danh mục tài liệu tham khảo của chính deck (slide 38) chỉ trích:

> Vroom, V. H., & Yetton, P. W. (1973). *Leadership and decision-making*. University of Pittsburgh Press.

Không có Jago. (Bản mở rộng Vroom–Jago là một công trình sau đó, không được trích trong deck.)

**Đã làm.** Giữ tên trên slide làm tên chính của `FW-006`, ghi `[CẦN XÁC NHẬN]` ở mục Nguồn của chunk kèm nguyên văn hai nguồn.

**Cần người dùng.** Không ảnh hưởng tới nội dung năm phong cách AI/AII/CI/CII/GII; chỉ là vấn đề quy ghi nguồn. Xác nhận nếu muốn đổi tên chunk.

---

## OQ-008 — Khung 8 yếu tố của Topic 06 không có slide văn bản giải thích

**Mức:** Trung bình · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** 49/69 slide của Topic 06 là ảnh hoặc từ khóa, không trích được text. Phần giữa buổi — **Transformation Design Framework** 8 yếu tố (slide 12–45) — gồm gần như toàn bộ là slide tiêu đề một từ (`TRIANGLE | 1`, `CURVE | 2`, `METRIC | 3`…) kèm sơ đồ và ảnh ví dụ. **Không có slide nào định nghĩa từng yếu tố bằng văn bản.**

Nội dung đã được đọc bằng thị giác qua `pdftoppm`, nên biết *sơ đồ vẽ gì*, nhưng **nghĩa và cách dùng của từng yếu tố là suy luận** từ nhãn, sơ đồ và các ví dụ xung quanh.

**Đã làm.** Các chunk `FW-007`, `FW-008`, `FW-009`, `TOP-MEGROW-06`, `PRB-007` và `PRB-011` đều để `confidence: medium` và `status: needs_review`; mọi phần diễn giải đều gắn nhãn `[SUY LUẬN]`.

**Cần người dùng.** Nếu anh có ghi chép tại lớp, handout, hoặc link tài liệu của giảng viên (transforms.me) thì gửi để nâng ba chunk này lên `verified`. Nếu không, chúng vẫn dùng được nhưng nên đọc kèm lưu ý.

---

## OQ-009 — Topic 12 ghi chặng TRUST dựa trên Edmondson nhưng không có slide giải thích

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Bảng tổng hợp ở Topic 12 slide 39 ghi chặng **TRUST** dựa trên *"Kouzes & Posner / Edmondson"* với công cụ *"Trust & Safety Check"*. Danh mục nguồn ở slide 41 cũng liệt kê Edmondson, A. C. (2019), *The Fearless Organization*.

Tuy nhiên **không slide nào trong Topic 12 giải thích phần Edmondson** — không có slide về psychological safety, và không có slide nào mô tả công cụ "Trust & Safety Check". Phần Kouzes & Posner thì có đầy đủ (slide 12) cùng case Microsoft (slide 14).

**Đã làm.** `FW-013` ghi nhận nguyên trạng ở mục "Cách kết hợp với framework khác", gắn nhãn `[SUY LUẬN]`. Không tạo chunk cho phần Edmondson vì không có nội dung nguồn.

**Cần người dùng.** Nếu buổi học có handout hoặc worksheet "Trust & Safety Check" không nằm trong file slide thì gửi để bổ sung. Nếu không, nội dung psychological safety sẽ được lấy từ **Topic 13** khi xử lý topic đó, và `FW-013` sẽ được liên kết sang.

---

## OQ-010 — Topic 02 có trang tiêu đề "Case in point" nhưng không có slide nội dung

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 34 của Topic 2 là một trang tiêu đề mục: *"Case in point — IMPROVING NEW-ACCOUNT ACTIVATION"*. Slide 35 ngay sau đó là lời cảm ơn. Không có slide nào trình bày case này.

Các con số ví dụ xuyên suốt deck (onboarding completion 65% → 80%, weekly active use 18% → 35%) gợi ý case được giảng trực tiếp trên bảng hoặc qua handout riêng.

**Đã làm.** Slide 34 ghi `không có nội dung kiến thức` trong `coverage_matrix.md` kèm tham chiếu tới OQ-010. `TOP-MEGROW-02` ghi nhận nguyên trạng với nhãn `[CẦN XÁC NHẬN]`.

**Cần người dùng.** Nếu có ghi chép tại lớp hoặc handout về case "Improving new-account activation" thì gửi để tạo một chunk `CASE` cho Topic 02.

---

## OQ-011 — Topic 05 slide 39: bốn nhãn DECISIVE / INTELLIGENT / RESISTIVE / INSTINCTIVE không có giải thích

**Mức:** Trung bình · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 39 của Topic 5 đặt bốn nhãn **DECISIVE · INTELLIGENT · RESISTIVE · INSTINCTIVE** ở bốn góc một ảnh não, xếp thành dạng ma trận 2×2. Không có slide nào trước hoặc sau giải thích bốn trạng thái này, và hai trục của ma trận không được đặt tên.

**Đã làm.** Ghi nhận trong `CON-021` dưới nhãn `[CẦN XÁC NHẬN]`, **không** tạo chunk `FW` riêng vì chưa đủ cơ sở để mô tả như một framework. Slide 39 ánh xạ tới `CON-021` trong `coverage_matrix.md`.

**Cần người dùng.** Giảng viên có giải thích bốn trạng thái này và hai trục không? Nếu có, đây có thể là một chunk `FW` độc lập.

---

## OQ-012 — Topic 03 slide 26: hai nghiên cứu chỉ được nêu ở mức một dòng

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 26 của Topic 3 nêu kết luận của Yukl & Tracey (1992) và Mayer, Davis & Schoorman (1995) mỗi nghiên cứu đúng một tới hai dòng, không có slide giải thích chi tiết từng chiến thuật gây ảnh hưởng hay từng thành tố của niềm tin.

**Đã làm.** Tạo `FW-058` với `confidence: medium`. Bảng diễn giải ba thành tố Ability–Benevolence–Integrity được gắn nhãn `[SUY LUẬN]`.

**Cần người dùng.** Nếu có ghi chép tại lớp về phần mini-input này thì bổ sung; nếu không, `FW-058` nên giữ nguyên mức tin cậy hiện tại.

---

## OQ-013 — Topic 05 slide 33 "Guiding Arrows": không có trục, không có chú giải

**Mức:** Trung bình · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 33 vẽ năm mũi tên tỏa ra từ một điểm, gắn năm nhãn **LATER · AS ALWAYS · HYPER PERFORMANCE · AS USUAL · OTHER TIME**, phân biệt bằng độ dốc và màu (đỏ / vàng / xanh). Slide không có trục nào được đặt tên và không có một câu chữ nào ngoài năm nhãn.

**Đã làm.** Tạo `FW-063` với `confidence: medium`. Cách đọc độ dốc và màu sắc được ghi rõ là `[SUY LUẬN]` của Claude, dựa trên hình vẽ và mạch slide 29–33.

**Cần người dùng.** Giảng viên giải thích hình này thế nào? Đặc biệt: hai trục là gì, và vì sao mũi tên dốc nhất (LATER) lại là mũi tên xấu nhất?

---

## OQ-014 — Topic 05: 65/78 slide là ảnh hoặc video, gần như không có chữ

**Mức:** Cao · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Topic 5 là deck dài nhất khóa (78 trang) nhưng **chỉ 13 trang có nội dung văn bản thực chất** (slide 2–5 và 73–75). Phần còn lại là ảnh, video (nhiều slide chỉ ghi *SOURCE: YOUTUBE*) và các trang chỉ có một tới hai chữ lớn. Deck **không chứa một slide hướng dẫn hoạt động nhóm nào** — không khung thời gian, không hướng dẫn chia nhóm, không câu hỏi debrief.

Hệ quả: mạch lập luận nối các slide ảnh của `CON-025` (hyper-performance ↔ burnout) và `CON-026` (tích lũy 1%, neuroplasticity, relentless honesty) phần lớn là `[SUY LUẬN]` của Claude dựa trên hình ảnh, nhãn và thứ tự slide, chứ không phải lời giảng được ghi lại.

**Đã làm.** `TOP-MEGROW-05` để `status: needs_review`, `confidence: medium`; `CON-025` và `CON-026` để `confidence: medium` và gắn `[CẦN XÁC NHẬN]` ở mục Nguồn. Toàn bộ 78 trang vẫn được ánh xạ trong `coverage_matrix.md`.

**Cần người dùng.** Đây là topic cần ghi chép tại lớp nhất trong cả khóa. Nếu có note về buổi này — đặc biệt về mảng burnout (slide 7–21) và mảng tự thay đổi (slide 22–28) — thì nội dung sẽ đổi đáng kể.

---

## OQ-015 — Topic 03: "Activity 4 – The Influence Lab" có trong agenda nhưng không có slide

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Agenda ở slide 3 của Topic 3 ghi *"10:55 — Activity 4: The Influence Lab (optional)"*, và kết quả đầu ra số 4 của buổi là *"Adapt one message to two very different audiences"*. Không có slide nội dung nào cho hoạt động này; slide 26 (mini-input về chiến thuật gây ảnh hưởng và niềm tin) là nội dung gần nhất.

**Đã làm.** Ghi nhận trong `TOP-MEGROW-03` mục "Bài tập và hoạt động trong lớp" với nhãn `[CẦN XÁC NHẬN]`. Kiến thức nền của hoạt động nằm ở `FW-058`.

**Cần người dùng.** Hoạt động này có được chạy trong lớp không? Nếu có, kịch bản là gì?

---

## OQ-016 — Topic 11 slide 21: bộ câu hỏi tự đánh giá EI không đọc được

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 21 của Topic 11 có tiêu đề *"Emotional Intelligence – Self-Assessment Questionnaire"* nhưng toàn bộ nội dung là ảnh chụp bảng câu hỏi ở độ phân giải không đọc được từng mục.

**Đã làm.** Ghi nhận trong `FW-075` và `TOP-MEGROW-11` với nhãn `[CẦN XÁC NHẬN]`. Slide 21 vẫn ánh xạ tới `FW-075` trong `coverage_matrix.md`.

**Cần người dùng.** Nếu có bản phát tay hoặc link tới bộ câu hỏi này thì gửi để bổ sung vào `FW-075` như một công cụ tự đánh giá.

---

## OQ-017 — Topic 11 slide 13: nghiên cứu Gen Z Việt Nam không ghi nguồn đầy đủ

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 13 trình bày nghiên cứu *"From Old Bamboo to New Shoots: Leadership Competencies for Vietnam's Generation Z Lotus Leaders"* với cỡ mẫu 100 nam + 100 nữ và bảy phát hiện, nhưng **không ghi tác giả, năm xuất bản hay phương pháp nghiên cứu**.

**Đã làm.** Tạo `CON-028` với `confidence: medium`, ghi rõ giới hạn ở mục Nguồn.

**Cần người dùng.** Nếu giảng viên có nêu nguồn đầy đủ tại lớp thì bổ sung; đây là chunk duy nhất trong kho nói về đặc điểm thế hệ trong bối cảnh Việt Nam nên độ tin cậy của nó đáng được xác nhận.

---

## OQ-018 — Topic 15 slide 19: Creative Matrix thiếu một hàng so với danh sách SIT

**Mức:** Thấp · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 16–17 của Topic 15 liệt kê **năm** công cụ SIT: Task Unification · Subtraction · Division · Multiplication · Attribute Dependency. Nhưng bảng Creative Matrix ở slide 19 chỉ có **bốn hàng** — thiếu **Division**.

**Đã làm.** Giữ nguyên trạng cả hai: `FW-085` liệt kê đủ năm công cụ, `FW-086` mô tả bảng bốn hàng đúng như slide và gắn `[CẦN XÁC NHẬN]`.

**Cần người dùng.** Đây là lỗi soạn slide hay là chủ ý (ví dụ Division ít dùng cho bài toán phối hợp)? Nếu là lỗi, `FW-086` nên ghi bảng năm hàng.

---

## OQ-019 — Topic 15 slide 6–7: hai câu hỏi về Design Thinking không có slide trả lời

**Mức:** Trung bình · **Ngày mở:** 2026-11-08 · **Trạng thái:** Đang mở

**Vấn đề.** Slide 6 hỏi *"What is Design Thinking and why should you care about it?"* và slide 7 hỏi *"How is Design Thinking implemented when tackling business challenges?"* — cả hai chỉ có câu hỏi trên nền đỏ, **không có slide nội dung trả lời**. Agenda cũng không liệt kê Design Thinking như một chặng riêng.

**Đã làm.** Hai slide ánh xạ tới `TOP-MEGROW-15` và được ghi nguyên trạng ở mục Nguồn của chunk đó.

**Cần người dùng.** Phần này được giảng trực tiếp, chiếu video, hay bị bỏ qua? Nếu có nội dung, nó sẽ nối trực tiếp với `FW-049` (Design Thinking có AI hỗ trợ, Topic 16).

---

## Mục `[KHÓ ĐỌC]`

**Không có.** Cả 805 trang đều đọc được: 668 trang trích được text trực tiếp bằng `pdftotext`, 137 trang còn lại (chủ yếu slide dạng ảnh của Topic 5 và Topic 6) đã được **đọc bằng thị giác** qua `pdftoppm` và mô tả trong `slide_inventory.md` với nhãn `[HÌNH]`. Không trang nào mờ, lỗi OCR hay không đọc được.
