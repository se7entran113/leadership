# open_questions.md — Câu hỏi mở và mục chờ xác nhận

Mọi mục `[CẦN XÁC NHẬN]`, `[KHÓ ĐỌC]` và mâu thuẫn chờ người dùng quyết định.

**Trạng thái:** 5 mục mở sau khi lập inventory MEGROW (2026-11-07).

| ID | Mức | Tiêu đề | Trạng thái |
|---|---|---|---|
| OQ-001 | Cao | Taxonomy pillar MEGROW chưa đối chiếu tài liệu chương trình chính thức | Đang mở |
| OQ-002 | Trung bình | Số topic trên slide lệch số trong tên file (Topic 3 và Topic 4) | Đang mở |
| OQ-003 | Cao | Topic 20 slide 21–27 chứa tên thật học viên | Đã quyết định — không trích |
| OQ-004 | Thấp | Case reading Microsoft thuộc topic nào | Đã quyết định — Topic 12 |
| OQ-005 | Trung bình | MEGROW không có nội dung về quản lý cộng tác viên | Đang mở |

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

## Mục `[KHÓ ĐỌC]`

**Không có.** Cả 805 trang đều đọc được: 668 trang trích được text trực tiếp bằng `pdftotext`, 137 trang còn lại (chủ yếu slide dạng ảnh của Topic 5 và Topic 6) đã được **đọc bằng thị giác** qua `pdftoppm` và mô tả trong `slide_inventory.md` với nhãn `[HÌNH]`. Không trang nào mờ, lỗi OCR hay không đọc được.
