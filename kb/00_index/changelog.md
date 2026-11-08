# changelog.md — Lịch sử cập nhật kho

Mới nhất ở trên cùng.

---

## 2026-11-08 — Dọn cờ `needs_review` lỗi thời và vá liên kết sót ở PRB-011

**Lệnh:** "hiện tại làm 1 và 2 luôn" — xử lý trước hai việc đã nêu, chưa chạy "Rà soát tổng thể".

### Phát hiện: `PRB-011` thiếu liên kết thật
Ba chunk **khai báo** phục vụ `PRB-011` qua `problems_addressed` nhưng `PRB-011` **không trỏ ngược lại chunk nào**: `FW-064`, `FW-090`, `CON-030`. Đáng kể nhất là **`FW-064` Khoảng cách Biết–Làm** — đây chính là framework trung tâm cho triệu chứng mà `PRB-011` mô tả ngay ở dòng đầu (*"thông báo rồi không ai theo"*), nhưng chưa từng được nối.

Nguyên nhân: đợt Topic 18 có cập nhật `PRB-003` và `PRB-005` nhưng **bỏ sót `PRB-011`**, dù chính ghi chú của `PRB-011` ghi rõ đang chờ Topic 18.

**Đã sửa `PRB-011`:** thêm `FW-064` làm hai dòng nguyên nhân **đầu bảng** và một câu hỏi chẩn đoán đứng trước mọi câu khác (khoảng trống nằm ở trạm nào — Knowledge, Acceptance, Intention hay Behavior); thêm năm dòng nguyên nhân đặc thù cho thay đổi do AI mang tới (`FW-090`, `FW-093`, `FW-094`, `CON-030`, `CON-028`) và một dòng về an toàn tâm lý (`FW-080`); mở rộng `topics` từ 2 lên 5, `related_ids` từ 6 lên 15, `source` từ 2 lên 4 nguồn.

### Dọn cờ `needs_review` lỗi thời (5 chunk)
Năm chunk `PRB` bị gắn `needs_review` vì **topic cần thiết chưa xử lý** tại thời điểm viết. Toàn bộ topic đó nay đã xong và nội dung đã được bổ sung qua các đợt sau, nhưng cờ và ghi chú chưa được cập nhật.

| Chunk | Ghi chú gốc chờ | Xử lý |
|---|---|---|
| `PRB-003` | Topic 02, 16 | → `verified`; ghi chú viết lại, nay phủ 10 topic |
| `PRB-007` | Topic 11 | → `verified`; nay phủ 6 topic |
| `PRB-008` | — (ghi chú đã mô tả đủ) | → `verified`; bổ sung Topic 02, 16 vào ghi chú |
| `PRB-010` | Topic 08, 13 | → `verified`; nay phủ 6 topic |
| `PRB-011` | Topic 18 | → `verified` sau khi vá liên kết ở trên |

`confidence` giữ nguyên `medium` ở những chunk dựa vào `FW-007`/`FW-008`/`FW-009` — đó là trục khác, phản ánh chất lượng nguồn chứ không phản ánh độ hoàn chỉnh.

### Dọn 7 ghi chú chéo lỗi thời khác
Quét toàn kho tìm các cụm "chưa xử lý", "sẽ liên kết khi xử lý topic đó", "chờ Topic": `CON-016` (chờ `PRB-009` — nay đã có) · `PRB-006` (chờ Topic 13) · `TOP-MEGROW-01` (expert bias → `CON-022`, `FW-055`) · `TOP-MEGROW-06` (psychological safety → `FW-080`) · `TOP-MEGROW-08` (gộp nguồn EI → `CON-013`, `FW-075`) · `TOP-MEGROW-09` (VRIFA ↔ VRIN → `FW-047`) · `TOP-MEGROW-14` (case BCPC ↔ an toàn tâm lý → `FW-080`). Mỗi chỗ thay lời hứa bằng liên kết thật và bổ sung `related_ids`.

### Còn lại 6 chunk `needs_review` — **không dọn được**
`FW-007` · `FW-008` · `FW-009` · `TOP-MEGROW-06` (Topic 06: 49/69 slide là ảnh, OQ-008) · `TOP-MEGROW-05` (Topic 05: 65/78 slide là ảnh/video, OQ-014) · `FW-031` (Topic 09: slide ghi nguồn *"through experience and knowledge from different models"*, không có tài liệu gốc để đối chiếu).

Đây là **thiếu nguồn thật**, không phải cờ lỗi thời. Chỉ gỡ được bằng ghi chép tại lớp của người dùng cho Topic 05 và 06. Nếu không có, `needs_review` là nhãn trung thực và nên giữ.

### Kết quả
`scripts/validate.py`: **0 ERROR**. Không còn ghi chú "chưa xử lý" nào trong kho ngoài hai tài liệu Capstone để riêng.

---

## 2026-11-08 — MEGROW Topic 18: thêm 13 chunk (tổng 172) — ✅ **độ phủ 100% trong phạm vi**

**Lệnh:** "ừ làm topic 18 luôn" (đợt 7, đợt cuối của giai đoạn chunk hóa).

### Cột mốc
**Toàn bộ 19 topic trong phạm vi đã được xử lý — 777/777 trang, độ phủ 100%.** Hai tài liệu Capstone (Topic 20 và Lumo Case, 49 trang) để riêng theo quyết định của người dùng.

### Chunk mới (13)
**Part I — bối cảnh cạnh tranh (4):** `FW-087` AI là áp lực thứ sáu · `FW-088` bốn trụ sẵn sàng về AI · `FW-089` thang Generative → Agentic → AGI · `CON-030` bằng chứng về AI (bốn case + số liệu McKinsey + Voices on AI).

**Part II — Leadership OS (3):** `FW-090` BE → LEAD → MASTER · `FW-091` C-FISH · `FW-092` O-LION.

**Part III — điều kiện phát triển (3):** `FW-093` EEE và Khoảng trống Tập sự · `FW-094` bốn mức quyền quyết định người–AI · `CON-031` AI có trách nhiệm là trách nhiệm địa phương.

**Part IV — hành động (2):** `FW-095` T-GROW · `FW-096` bảy kịch bản lãnh đạo AI tại Zalo.

**Topic (1):** `TOP-MEGROW-18`.

### Gộp nguồn, không tạo chunk trùng
- **`FW-013` nhận E-MICE.** Topic 18 ghi rõ *"Adapted from Kouzes and Posner (2023)"* — E-MICE là **cùng framework, sắp xếp lại thành từ viết tắt**. Thêm mục "Các phiên bản và góc nhìn khác" vào `FW-013` với bảng năm chữ và mười cam kết, thay vì tạo chunk mới (CLAUDE.md §5.3).
- **`FW-045` gỡ ghi chú chờ.** Ghi chú "Topic 18 sẽ bổ sung AI như áp lực thứ sáu" mở từ đợt 4 nay trỏ sang `FW-087`.
- **`FW-010` nhận nguồn Topic 18.** Câu *"delegation can increase, accountability does not decrease"* xuất hiện ở cả Topic 06 (Stibe) và Topic 18 (Trung Nguyen, dưới tiêu đề "Delegation ≠ Abdication") — hai giảng viên, cùng một nguyên tắc.
- **`FW-065` nối sang `FW-094` và `FW-089`:** kho nay có **ba cách cắt** cùng chủ đề phân vai người–AI — theo kiểu hợp tác (`FW-065`), theo năng lực công nghệ (`FW-089`), theo quyền quyết định (`FW-094`). Phần "Phân biệt" của cả ba đã ghi rõ dùng cái nào khi nào.
- `PRB-003`, `PRB-005`: thêm nguyên nhân gốc rễ từ Topic 18.

### Index
- `coverage_matrix.md`: thêm 44 dòng slide cho Topic 18 (33 ánh xạ, 11 không có nội dung). **Độ phủ 777/777 (100%)**.
- `catalog.md` sinh lại — **172 chunk**; bộ đếm ID sang `CON-032` / `FW-097`.
- `topic_map.md`, `problem_index.md`, `glossary.md` (thêm 13 thuật ngữ), `open_questions.md` (**OQ-020** — Luật AI VN được nêu tên nhưng không có nội dung điều khoản).

### Ghi chú kỹ thuật
- Topic 18 gần như toàn văn bản: chỉ 3/44 slide là ảnh, không cần đọc bằng thị giác. Không có trang `[KHÓ ĐỌC]`.
- `scripts/validate.py`: **0 ERROR**.
- **Độ dài:** 10/13 chunk ≤1000 từ. Ba chunk vượt — `FW-093` (1115), `FW-096` (1249), `FW-013` (1122 sau khi nhận thêm E-MICE) — phần vượt đều là bảng nhiều dòng và trích dẫn nguyên văn, thuộc diện CLAUDE.md §5.1 không được lược bỏ. `FW-096` là bảng bảy kịch bản nên dài là bản chất của chunk.

### Bước tiếp theo
Giai đoạn chunk hóa đã xong. Việc còn lại là lệnh **"Rà soát tổng thể"** (CLAUDE.md §9): tìm chunk chồng chéo, hoàn thiện `problem_index.md`, viết các chunk `PB` (hiện **0**), và viết `QUICK_REFERENCE.md`.

---

## 2026-11-08 — Đăng ký tài liệu Capstone mới (Lumo Case), để riêng

**Phát hiện.** `validate.py` báo có tài liệu mới chưa xử lý: `raw/megrow/me.grow(2026)_Capstone Lumo Case_Mandate C.pdf` (21 trang, sửa 2026-11-06).

**Phân loại — người dùng xác nhận.** Đây là **nội dung case của Capstone Project**, sẽ được người dùng review sau. Xếp cùng nhóm với Topic 20: **để riêng, ngoài phạm vi chunk hóa**.

Nội dung case (đọc ở mức tiêu đề trang): Lumo — một nền tảng nhắn tin/dịch vụ tại Việt Nam; người học đóng vai lãnh đạo một mảng sản phẩm, nhận mandate từ Chau để ra mắt **Mira business**. Tài liệu gồm bối cảnh, bốn áp lực cho 2027, mô tả vai trò và thước đo, yêu cầu bài nộp, timeline, và các Exhibit 1–6 (chung) cùng C1–C7 (riêng cho Mandate C).

**Hệ quả.**
- `topic_map.md`: thêm một dòng dưới Topic 20 với trạng thái `để riêng`; tổng tài liệu **22 → 23**, tổng trang **805 → 826**. Phần để riêng nay là **49 trang** (Topic 20: 28 + Lumo Case: 21).
- **Phạm vi kho không đổi: 777 trang.** Độ phủ vẫn **733 / 777 (94.3%)**.
- `slide_inventory.md`: thêm mục `CAPSTONE` liệt kê 21 trang ở mức tiêu đề, kèm ghi chú để riêng — để hồ sơ đầy đủ nếu sau này người dùng muốn đưa vào kho.
- Không tạo chunk nào; không đụng `coverage_matrix.md`.

---

## 2026-11-08 — MEGROW Topic 11, 13, 15: thêm 23 chunk (tổng 159), độ phủ 94.3%

**Lệnh:** "tiếp" (đợt 6). Ba topic chưa xử lý còn lại sau khi Topic 20 được đưa ra ngoài phạm vi.

### Chunk mới (23)

**Topic 11 — Customised Approach for Individuals (8):** `FW-072` bốn phong cách làm việc · `FW-073` các yếu tố định hình hành vi · `FW-074` McClelland và ERG · `FW-075` bốn địa hạt EI · `FW-076` năm chiến lược và bốn kỹ thuật · `FW-077` ba kịch bản đóng vai · `CON-027` niềm tin qua hành vi nhất quán · `CON-028` lãnh đạo Gen Z Việt Nam.

**Topic 13 — Building Trust & Open Communication (7):** `FW-078` khung TRUST · `FW-079` Trust Equation · `FW-080` an toàn tâm lý và bốn vùng Edmondson · `FW-081` sáu phẩm chất lãnh đạo bao trùm · `FW-082` case The Silent Team và bảng STOP/START/CONTINUE · `CON-029` niềm tin là yếu tố thúc đẩy hiệu quả · **`PRB-009`**.

**Topic 15 — From Stakeholder Insight to Market Impact (5):** `FW-083` Desirability–Feasibility–Viability · `FW-084` + `FW-084-01` pain point và bản đồ hành trình stakeholder · `FW-085` năm công cụ SIT · `FW-086` Creative Matrix.

**Topic (3):** `TOP-MEGROW-11`, `TOP-MEGROW-13`, `TOP-MEGROW-15`.

### Cột mốc: cả 11 vấn đề ưu tiên đã có chunk
`PRB-009` (văn hóa thử nghiệm và an toàn tâm lý) là vấn đề cuối cùng trong 11 vấn đề ưu tiên ở CLAUDE.md §2 chưa có chunk. Topic 13 cung cấp nguồn chính; Topic 07 và Topic 16 bổ sung. **Bảng đặt chỗ `PRB` trong `catalog.md` nay đã đầy đủ.**

### Chunk đã cập nhật
- `CON-013`: gỡ ghi chú "Topic 11 sẽ gộp nguồn khi xử lý topic đó", nối sang `FW-075`, thêm nguồn Topic 11.
- `PRB-001`, `PRB-002`, `PRB-003`, `PRB-006`, `PRB-007`, `PRB-010`: thêm nguyên nhân gốc rễ, `topics`, `related_ids` từ ba topic mới.

### Quyết định đáng ghi
- **`CON-027` gộp hai nguồn** (Topic 11 slide 8 — Robbins; Topic 13 slide 6) vì cả hai nói cùng một điều: niềm tin là kết quả tích lũy của hành vi, không đến từ chức vụ. Chunk này đối chiếu **ba mô hình niềm tin** của khóa học — Robbins (5 chiều), Maister (`FW-079`), Mayer et al. (`FW-058`) — và chỉ ra điểm khác biệt thật nằm ở Self-Orientation.
- **`FW-074` gộp hai lý thuyết nhu cầu** (McClelland và Alderfer) vì deck trình bày chúng trên hai slide liên tiếp và agenda gọi ERG là lý thuyết đầu mục.
- **Tách `FW-084-01`** (ví dụ hành trình AGREE→DELIVER) khỏi `FW-084` tại đường nối tự nhiên: ví dụ có nguồn riêng (slide 13) và một bài học độc lập.
- **Không tạo chunk `CASE`** cho "The Silent Team" — loại `CASE` dành cho tình huống thật của người dùng (CLAUDE.md §7); case giảng dạy nằm trong `FW-082`.

### Index
- `coverage_matrix.md`: thêm ánh xạ từng trang cho **96 slide** (Topic 11: 45, Topic 13: 30, Topic 15: 21). Độ phủ **733 / 777 trang trong phạm vi (94.3%)**, 18/19 topic.
- `catalog.md` sinh lại; bộ đếm ID sang `CON-030` / `FW-087`; bảng đặt chỗ `PRB` đánh dấu đủ 11/11.
- `topic_map.md`, `problem_index.md`, `glossary.md` (thêm 3 nhóm, 23 thuật ngữ), `open_questions.md` (**OQ-016 … OQ-019**).

### Ghi chú kỹ thuật
- Bảy slide dạng sơ đồ đọc bằng thị giác qua `pdftoppm`: Topic 13 slide 11, 12, 16, 18, 19, 22; Topic 11 slide 20; Topic 15 slide 7. Không có trang `[KHÓ ĐỌC]`.
- `scripts/validate.py`: **0 ERROR**.
- **Độ dài chunk:** theo quyết định của người dùng (xem mục dưới), chuẩn là **≤1000 từ** cho chunk mới, không sửa lại chunk cũ. 20/23 chunk đợt này đạt; ba chunk vượt nhẹ — `FW-080` (1017), `FW-081` (1067), `FW-082` (1085) — vì phần vượt là bảng và trích dẫn nguyên văn thuộc diện §5.1 không được lược bỏ.

### Quyết định của người dùng trong đợt này
- **Ngôn ngữ kho giữ nguyên:** thân chunk tiếng Việt, thuật ngữ + tên framework + trích dẫn giữ tiếng Anh. Đo được: toàn kho 1.0 MB, phần song ngữ chỉ chiếm 1.6–4.4%; tiếng Việt tốn ~1.6× byte so với tiếng Anh nhưng token không phải ràng buộc đang có.
- **Chuẩn độ dài chunk là 1000, không chuẩn hóa ngược chunk cũ.** 63 chunk `FW` của bốn đợt đầu có trung vị 746 từ và trần đúng 799 — dấu vết của việc bị tỉa theo ngưỡng 800 cũ, ngưỡng mà chính dự án đã kết luận là quá chật khi nới lên 1000 ở commit `9f788d4`. Ép chunk mới xuống cho khớp là đi lùi; viết lại 63 chunk cũ thì tốn tương đương làm lại bốn đợt. Chọn: lấy 1000 làm chuẩn, để chunk cũ dãn ra tự nhiên khi topic sau bổ sung nguồn cho chúng.

---

## 2026-11-08 — Topic 20 (Capstone) để riêng, ngoài phạm vi kho

**Quyết định của người dùng.** Topic 20 — *Capstone Research & Alignment* (AP Burkhard Schrage, 28 trang) — **không chunk hóa vào kho**. Người dùng sẽ tự review deck này để làm slide Capstone riêng.

**Hệ quả.**
- `topic_map.md`: trạng thái Topic 20 đổi từ `chưa xử lý` sang `để riêng`, kèm ghi chú để các đợt sau bỏ qua.
- Mẫu số tiến độ đổi từ 20 sang **19 topic trong phạm vi**, và từ 805 sang **777 trang**. Độ phủ hiện tại tính lại: **637 / 777 (82.0%)**.
- File vẫn giữ trong `topic_map.md` và `slide_inventory.md` để `validate.py` không báo "có tài liệu mới chưa xử lý"; không cần ánh xạ trang trong `coverage_matrix.md` vì trạng thái không phải `đã xử lý`.
- Có thể đảo ngược: nếu sau này muốn đưa nội dung Capstone vào kho thì xử lý như một đợt bình thường.

**Còn lại trong phạm vi: 4 topic** — 11, 13, 15, 18.

---

## 2026-11-08 — MEGROW Topic 03, 05, 07: thêm 31 chunk (tổng 136)

**Lệnh:** "xử lý tiếp các topic tiếp theo" (đợt 5 của chỉ thị "cứ lần lượt làm hết topic và commit theo đợt").

Ba topic chưa xử lý có số thứ tự nhỏ nhất. Không cùng chủ đề như các đợt trước — chọn theo thứ tự còn lại.

### Chunk mới (31)

**Topic 03 — Audit Mindset & Biases (9):** `CON-021` System 1 / System 2 · `CON-022` expert bias · `CON-023` phán đoán từ sản phẩm thành đầu vào · `CON-024` quá tự tin và hiệu ứng mô tả · `FW-055` Audit Mindset và tự kiểm 5 bước · `FW-055-01` Bias Audit Card · `FW-056` The Leak · `FW-057` Audit the Algorithm · `FW-058` chiến thuật ảnh hưởng và ba thành tố niềm tin.

**Topic 05 — Optimise Personal Productivity (10):** `FW-059` mười thách thức năng suất · `FW-060` bộ phân loại bốn quyết định · `FW-061` Time Matrix và Eisenhower · `FW-062` GTD · `FW-063` Guiding Arrows · `FW-064` Knowledge–Behaviour Gap · `FW-065` bốn chế độ Người + AI · `FW-065-01` mô hình Colson · `CON-025` hyper-performance và burnout · `CON-026` tích lũy 1% và neuroplasticity.

**Topic 07 — Building Team Capability & Growth (9):** `FW-066` phương pháp LSP® · `FW-066-01` Ground Rules và 4 NO GO's · `FW-067` Real Time Identity cho team · `FW-067-01` RTI for YOU · `FW-068` ba lớp CI/EI/PI · `FW-068-01` hoạt động External Identity · `FW-069` Johari Window · `FW-070` Team Life enablers và barriers · `FW-071` The Team Landscape.

**Topic (3):** `TOP-MEGROW-03` · `TOP-MEGROW-05` · `TOP-MEGROW-07`.

### Chunk đã cập nhật
- `PRB-004`: thêm 6 dòng nguyên nhân gốc rễ từ Topic 03 và 05; gỡ ghi chú "Topic 05 sẽ bổ sung liên kết khi xử lý".
- `PRB-006`: thêm 6 dòng từ Topic 03 và 07 — nhóm lỗi **ở chính phán đoán và ngôn ngữ của quản lý**, xảy ra trước khi cuộc trò chuyện bắt đầu.
- `PRB-003`, `PRB-007`, `PRB-002`, `PRB-005`: thêm nguyên nhân, `topics`, `related_ids` tương ứng.

### Quyết định đáng ghi
- **`CON-021` gộp hai nguồn** (Topic 03 slide 12–13 và Topic 05 slide 36–53): cùng mô hình Kahneman, hai hướng khai thác khác nhau — một bên về phán đoán, một bên về tri giác.
- **`FW-061` gộp hai ma trận** FranklinCovey Time Matrix và Eisenhower Matrix vào một chunk, vì chúng cùng hai trục và được dạy liên tiếp; giữ cả hai tên trong `aliases` để không mất đường truy xuất.
- **`FW-065` tách khỏi `FW-010`**: `FW-010` (Topic 06) trả lời *việc nào cho Human/AI/HAI*; `FW-065` (Topic 05) phân giải mức HAI thành bốn chế độ. Cùng giảng viên AP Agnis Stibe.
- **Bốn chunk con được tách sau khi viết xong bản đầy đủ**, tại các đường nối tự nhiên: `FW-065-01` (mô hình Colson, nguồn riêng slide 62) · `FW-066-01` (bộ luật chơi, dùng độc lập được) · `FW-067-01` (bài tập về nhà) · `FW-068-01` (Activity 2, có bộ ràng buộc riêng).
- **`TOP-MEGROW-05` để `needs_review` và `confidence: medium`** — 65/78 slide là ảnh hoặc video gần như không có chữ; xem OQ-014.
- **Không tạo chunk cho slide 39 của Topic 05** (bốn nhãn DECISIVE/INTELLIGENT/RESISTIVE/INSTINCTIVE) vì không có slide nào giải thích — ghi vào `CON-021` với `[CẦN XÁC NHẬN]` và mở OQ-011.

### Index đã cập nhật
- `coverage_matrix.md`: thêm ánh xạ từng trang cho **151 slide** (Topic 03: 30, Topic 05: 78, Topic 07: 43). Độ phủ **637 / 805 trang (79.1%)**, 15/20 topic.
- `catalog.md` sinh lại bằng `scripts/gen_catalog.py`; sửa bộ đếm ID (`CON-027`, `FW-072`) và bảng đặt chỗ `PRB` vốn đã lỗi thời từ đợt 1.
- `topic_map.md`, `problem_index.md`, `glossary.md` (thêm 3 nhóm, 31 thuật ngữ), `open_questions.md` (**OQ-011 … OQ-015**).

### Ghi chú kỹ thuật
- Chín slide dạng sơ đồ đọc bằng thị giác qua `pdftoppm`: Topic 05 slide 18, 30–33, 39, 55, 62, 67, 68, 70–72; Topic 07 slide 18. Không có trang `[KHÓ ĐỌC]`.
- `scripts/validate.py`: **0 ERROR**. Còn **14 WARNING về độ dài** — xem mục dưới.
- **Độ dài chunk lệch so với các đợt trước.** Đo được: 63 chunk `FW` của bốn đợt đầu có trung vị **746 từ**, tối đa **799**; 25 chunk `FW` đợt này có trung vị **1093**. Phần chênh tập trung ở mục "Các bước áp dụng" (182 → 355 từ trung vị), tức phần bảng và diễn giải bảng. Đã tách bốn chunk con và tỉa phần diễn giải dài nhất; 14 chunk vẫn ở mức 1015–1168 từ. Chưa tỉa tiếp vì phần còn lại là bảng, trích dẫn nguyên văn và ví dụ — thuộc diện CLAUDE.md §5.1 không được lược bỏ. **Cần người dùng quyết định** có chạy một đợt chuẩn hóa độ dài cho toàn kho hay không.

---
## 2026-11-08 — MEGROW Topic 02, 16, 17: thêm 38 chunk (tổng 105)

**Lệnh:** "Xử lý megrow topic 2, 16, 17" (đợt 4 của chỉ thị "cứ lần lượt làm hết topic và commit theo đợt").

### Chunk mới (38)
- **Khái niệm (7):** `CON-014` thực thi là hệ thống · `CON-015` chuỗi Goal → Impact · `CON-016` giám sát hệ thống không giám sát người · `CON-017` nguồn lực vs năng lực · `CON-018` outside-in / inside-out · `CON-019` line-of-sight test · `CON-020` How Might We.
- **Framework Topic 02 (10):** `FW-033` Strategic Management Cycle · `FW-034` Strategy Cascade · `FW-035` Three Manager Moves · `FW-036` SMART và giới hạn · `FW-037` mẫu outcome–evidence–guardrail · `FW-038` metric/KPI/baseline/target · `FW-039` signal stack + phá thử KPI · `FW-040` OKR và phân rã công việc · `FW-041` Team Delivery System · `FW-042` nhịp review và ngưỡng phản ứng.
- **Framework Topic 17 (9):** `FW-043` sáu kỷ luật Watkins · `FW-044` + `FW-044-01` PESTEL và hoạt động quét · `FW-045` + `FW-045-01` Five Forces và bằng chứng về vai trò của ngành · `FW-046` value stick · `FW-047` + `FW-047-01` VRIN và moat · `FW-048` reframe → giả định → khuyến nghị.
- **Framework Topic 16 (8):** `FW-049` + `FW-049-01` AI-augmented Design Thinking · `FW-050` Problem Tree · `FW-051` Empathy Map · `FW-052` Problem Statement Template · `FW-053` + `FW-053-01` thử nghiệm 7 ngày · `FW-054` bốn đường đi và lời đề nghị ba dòng.
- **Vấn đề (1):** `PRB-001` Định hướng bài toán cho team — vấn đề ưu tiên **Cao** số 1, trước đó chưa có chunk.
- **Topic (3):** `TOP-MEGROW-02`, `TOP-MEGROW-16`, `TOP-MEGROW-17`.

### Chunk đã cập nhật
- `PRB-002`, `PRB-003`, `PRB-004`, `PRB-005`, `PRB-008`, `PRB-010`: bổ sung `topics`, `related_ids`, `source` và các dòng nguyên nhân gốc rễ mới từ Topic 02, 16, 17.
- `PRB-008`: gỡ ghi chú "Topic 17 chưa xử lý", nối sang `CON-019`.
- `PRB-005`: gỡ ghi chú "Topic 08 sẽ liên kết khi xử lý", nối sang `FW-026`/`PRB-006`.

### Index
- `coverage_matrix.md`: thêm ánh xạ từng trang cho 111 slide (Topic 02: 35, Topic 16: 37, Topic 17: 39). Độ phủ **486 / 805 trang (60,4%)**, 12/20 topic.
- `topic_map.md`, `problem_index.md`, `glossary.md` (ba bảng thuật ngữ mới), `catalog.md` (sinh lại bằng `scripts/gen_catalog.py`).
- `open_questions.md`: mở **OQ-010** — Topic 02 slide 34 là trang tiêu đề "Case in point — Improving new-account activation" nhưng không có slide nội dung.

### Ghi chú kỹ thuật
- Ba slide dạng ảnh (Topic 02 slide 4, 34, 35; Topic 16 slide 10–11) đọc bằng thị giác qua `pdftoppm`. Không có trang `[KHÓ ĐỌC]`.
- Năm chunk con được tách ra để giữ dưới ngưỡng 800 từ: `FW-044-01`, `FW-045-01`, `FW-047-01`, `FW-049-01`, `FW-053-01`.
- `scripts/validate.py`: **0 ERROR, 0 WARNING**.

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
