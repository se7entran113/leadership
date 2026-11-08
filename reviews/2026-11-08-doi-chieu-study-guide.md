# Đối chiếu: Leadership Study Guide (Topics 01–19) với kho tri thức

**Nguồn đối chiếu:** `raw/megrow/Leadership_Study_Guide_Topics_01-19_RMIT_Zalo.docx` (82 KB, thêm 2026-11-08)
**Kho tại thời điểm đối chiếu:** 172 chunk, 19/19 topic trong phạm vi, `validate.py` 0 ERROR (HEAD `445bd03`)
**Người thực hiện:** Claude, theo yêu cầu đối chiếu của người dùng
**Trạng thái:** Chờ người dùng duyệt — **chưa sửa chunk nào** trong kho dựa trên báo cáo này

---

## Tóm tắt điều hành

### Bản chất của tài liệu nguồn

File tự khai ngay ở trang đầu (trích nguyên văn):

> *"Ghi chú về độ trung thực nguồn: Tên mô hình, khái niệm và phạm vi được đối chiếu từ slide gốc và chỉ mục khóa học. Nội dung 'Ứng dụng đề xuất', ví dụ và checklist là **diễn giải của trợ lý**; không phải lời giảng nguyên văn hoặc bằng chứng thực nghiệm độc lập."*

Và ở Phụ lục B:

> *"Một số trang (đặc biệt Topic 5–6, 7, 13) có sơ đồ nhiều chữ nằm trong hình; tài liệu này diễn giải sơ đồ ở cấp khái niệm chứ không thay thế bản gốc khi cần đi sâu từng nhãn."*

**Kết luận về vai trò của tài liệu:** đây là **tài liệu thứ cấp do AI hỗ trợ tạo từ cùng bộ slide gốc**, không phải ghi chép lớp hay nguồn độc lập. Nó **không** dùng được làm bằng chứng để gỡ 6 chunk `needs_review` hay đóng các câu hỏi mở (OQ) — kết quả rà soát bên dưới xác nhận điều này: không một OQ nào được giải bởi tài liệu.

Giá trị thật của việc đối chiếu nằm ở ba chỗ: **(1)** một phép thử chéo độc lập — nếu hai diễn giải AI khác nhau cùng đọc sai một slide theo cùng một cách thì đáng ngờ, cùng đọc đúng thì củng cố; **(2)** phát hiện những slide/framework có thật trên deck mà kho đã bỏ sót; **(3)** so sánh cách tổ chức tra cứu (Problem → Framework index) để làm đầu vào cho đợt viết playbook sắp tới.

### Kết quả kiểm ba lỗi đọc hình đã biết (đợt đối chiếu Topic 05/06 trước đó)

| Lỗi đã sửa trong kho | File có nhắc tới không? | Kết luận |
|---|---|---|
| **Circles** (T06): SELF-CONTAINED → SOCIAL PULL → IDENTITY CHANGE → INFLUENCING OTHERS | File không liệt kê nhãn cụ thể, chỉ mô tả chung "thiết kế cơ chế tạo động lực và thay đổi bản sắc từ người nhận task thành owner" | Không xung đột, không corroborate — file né tránh chi tiết đúng chỗ kho từng sai |
| **Moderation** (T06): sơ đồ luồng OTHERS → DYNAMIC DESIGN → AMPLIFY/DECREASE/REVERSE | File viết: *"Xem việc **khuếch đại/giảm/đảo chiều** hành vi và cả kết quả có chủ đích/ngoài dự kiến"* | **Củng cố bản sửa của kho** — "khuếch đại/giảm/đảo chiều" khớp chính xác AMPLIFY/DECREASE/REVERSE, không phải cách đọc sai cũ của kho (which từng ghi "Others · Dynamic · Decrease · Design" như danh sách phẳng) |
| **Slide 35 T05** (biển chỉ dẫn vs lối mòn, không phải thần kinh học) | File không đề cập slide 35 cụ thể | Không xung đột, không corroborate |

**Kết luận:** không phát hiện xung đột ở ba điểm nóng đã biết; một điểm (Moderation) được củng cố độc lập.

### Thống kê phát hiện

| Loại | Số lượng |
|---|---:|
| Conflict (file và KB nói khác nhau, cần trọng tài slide gốc) | 0 |
| KB có, file thiếu hoàn toàn một mảng nội dung | 2 (Topic 11: case Gen Z + Robbins trust; Topic 18: 4 case AI + Luật AI VN) |
| KB có, file thiếu một framework cụ thể (không nêu tên) | 9 |
| File có, KB thiếu | 0 |
| Ý tưởng tham khảo đáng cân nhắc cho playbook | 3 |
| Housekeeping phát hiện ngoài phạm vi đối chiếu | 1 |

**Không tìm thấy conflict nội dung nào.** Đây là kết quả hợp lý: cả hai tài liệu cùng xuất phát từ một bộ slide, và quy trình của kho (đối chiếu từng slide bằng `pdftotext`/`pdftoppm`, hai lượt kiểm lại gần đây) đã lọc hết các điểm dễ sai. Giá trị chính của đợt này là **xác nhận không có gì mới cần sửa**, cộng với một số gợi ý coverage.

---

## Bảng phát hiện

| # | Vị trí trong file | Chunk liên quan | Bằng chứng slide gốc | Mô tả | Phân loại | Đề xuất | Quyết định |
|---|---|---|---|---|---|---|---|
| 1 | Topic 01, mục 3 — chỉ liệt kê 5 framework | `FW-002`, `FW-004` | Slide 4–5 ("Four stages of contribution"), slide 7–8 ("Reference framework · Hill (2007)") — đã xác minh bằng `pdftotext` | File không nhắc tới **Five Myths of the New Manager (Hill 2007)** và **Four Stages of Contribution (Dalton)** như framework card riêng, dù cả hai slide đều tồn tại và có tiêu đề rõ | KB có, file thiếu | Không cần hành động — đây là framework hợp lệ, kho đã có đủ | ☐ |
| 2 | Topic 02, mục 3 — 7 framework, không có tên riêng cho một số mục | `FW-033`, `FW-035`, `FW-041` | — | File gộp "Strategic Management Cycle" và "Three Manager Moves" (Translate/Coordinate/Adjust) và "Team Delivery System" vào các mục chung chung (cascade, execution stack) mà không gọi tên | KB có, file thiếu | Không cần hành động | ☐ |
| 3 | Topic 03, mục 3 — chỉ liệt kê 3 framework | `FW-056`, `FW-058` | Slide 22–25 (The Leak), slide 26 (influence tactics & trust) | File hoàn toàn không nhắc tới **The Leak** (sáu câu quản lý hay nói) và **chiến thuật ảnh hưởng theo đối tượng + ba thành tố niềm tin** — hai mảng nội dung lớn của buổi học | KB có, file thiếu | Không cần hành động | ☐ |
| 4 | Topic 05, mục 3 — chỉ liệt kê 3 framework rất chung | `FW-061`, `FW-062`, `FW-063` | Slide 70 (FranklinCovey Time Matrix), 71 (Eisenhower Matrix), 72 (GTD) — các slide này có chữ rõ, không phải ảnh thuần | File bỏ qua hoàn toàn **Time Matrix, Eisenhower Matrix, GTD** — ba công cụ ưu tiên kinh điển có trên slide rõ ràng, không phải phần ảnh khó đọc | KB có, file thiếu | Không cần hành động | ☐ |
| 5 | Topic 07, mục 3 — 5 framework | `FW-070` | Slide 29–33 (Team Life, enablers/barriers) | File không nhắc **Team Life — Enablers and Barriers** | KB có, file thiếu | Không cần hành động | ☐ |
| 6 | Topic 09, mục 3 — 5 framework | `FW-030` | Slide tương ứng D-R-C route | File không nhắc **lộ trình D–R–C** (Diagnose → Readiness → Coach & Connect) | KB có, file thiếu | Không cần hành động | ☐ |
| 7 | **Topic 11 — toàn bộ phần "Thông điệp cốt lõi" và mục 3** | `CON-027`, `CON-028` | Slide 9 (Cultivating Trust through Behaviour, Robbins:336), slide 14 (Case Study — Generational Leadership Change in Vietnam) — đã xác minh qua `pdftotext` | **File bỏ sót hoàn toàn hai slide có nội dung rõ ràng**: định nghĩa niềm tin theo Robbins và case nghiên cứu Gen Z Việt Nam. Không chỉ thiếu tên framework — toàn bộ chủ đề không được nhắc tới một lần nào | KB có, file thiếu (mảng lớn) | Không cần hành động — kho đã phủ đầy đủ qua `CON-027`, `CON-028` | ☐ |
| 8 | **Topic 16, mục 3** | `FW-053`, `FW-053-01`, `FW-054` | Slide 24–35 (7-Day Test, Four Next Steps, Three-Line Ask) | File gộp các công cụ này vào mục chung "Human-first + AI expansion + prototype", không tách tên **7-Day Test** hay **Three-Line Ask** dù đây là hai công cụ riêng biệt, có slide riêng | KB có, file thiếu | Không cần hành động | ☐ |
| 9 | **Topic 18 — toàn bộ phần "Thông điệp cốt lõi" và mục 3** | `CON-030`, `CON-031` | Slide 9–10 (4 case: Microsoft, Morgan Stanley, Replit, Klarna), slide 13–15 (Voices on AI — Jensen Huang, Sam Altman, Dario Amodei, Bill Gates), slide 30 (Responsible AI, Luật AI VN 134/2025/QH15) | **File bỏ sót hoàn toàn mảng bằng chứng thực tế và mảng quy định pháp lý** — không nhắc một case nào, không nhắc Luật AI Việt Nam dù đây là nội dung cụ thể, có tên luật và ngày hiệu lực rõ ràng trên slide | KB có, file thiếu (mảng lớn) | Không cần hành động — kho đã phủ đầy đủ qua `CON-030`, `CON-031`; đồng thời xác nhận **OQ-020 không được giải bởi file này** | ☐ |
| 10 | Topic 10, mục "Đọc sâu" — "Two-way clarity check" | *(không có chunk tương ứng)* | Slide 12–16 (Blind Drawing debrief) | File đặt tên một "framework" riêng cho bài học rút ra từ Blind Drawing: hỏi lại thay vì chỉ nghe. Nội dung này tồn tại trong `TOP-MEGROW-10` ở dạng tường thuật nhưng không phải một chunk `FW` riêng | Ý tưởng tham khảo | Cân nhắc khi viết playbook cho `PRB-003`/giao việc rõ — không cần tạo chunk mới | ☐ |
| 11 | Phụ lục B | — | — | File tự ghi nhận các slide ảnh-nhiều-chữ tập trung ở **Topic 5–6, 7, 13** — khớp với Topic 5/6 mà kho đã tự phát hiện và sửa hai lỗi (xem commit `a09fedb`, `445bd03`). File **mở rộng danh sách nghi ngờ sang Topic 7 và Topic 13** | Cảnh báo tham khảo | Topic 7 (Johari Window, slide 18) và Topic 13 (TRUST infographic slide 11–12, Trust Equation slide 19, Inclusive Leadership slide 22) **đã được render bằng `pdftoppm` và đọc trực tiếp trong đợt xử lý gốc** — không phải đọc text thuần. Rủi ro thấp hơn Topic 5/6 nhưng có thể đối chiếu lại nếu muốn chắc chắn tuyệt đối | ☐ |
| 12 | *(ngoài phạm vi đối chiếu file — phát hiện phụ)* | `kb/00_index/problem_index.md`, dòng vấn đề 11 | — | Dòng `PRB-011` trong bảng tổng quan vẫn ghi **"✅ một phần (Topic 06, 12)"**, nhưng `PRB-011` đã được nâng lên `status: verified` và mở rộng sang 5 topic (06, 12, 05, 13, 18) ở đợt dọn cờ gần đây (commit `7b7c99c`). Dòng tổng quan này chưa được cập nhật theo | Housekeeping (không liên quan file) | Sửa dòng 11 trong bảng tổng quan của `problem_index.md` thành "✅ đã có (T05, 06, 12, 13, 18)" | ☐ |

---

## Rà soát 11 câu hỏi mở (OQ) còn mở trong kho

| OQ | Chủ đề | File có giải được không? |
|---|---|---|
| OQ-001 | Taxonomy pillar MEGROW chưa đối chiếu tài liệu chương trình chính thức | Không giải, nhưng **corroborate độc lập**: file tự đề xuất cùng cách nhóm 3 pillar theo đúng ranh giới T01–05 / T06–11 / T12–19, tự ghi "ĐỀ XUẤT, KHÔNG PHẢI PILLARS CHÍNH THỨC" — cùng mức độ chắc chắn như kho |
| OQ-002 | Số topic trên slide lệch số trong tên file | Không đề cập |
| OQ-003 | Topic 20 chứa tên thật học viên | N/A — file loại trừ Topic 20 |
| OQ-004 | Case Microsoft thuộc topic nào | Không đề cập case này trong T12 |
| OQ-005 | MEGROW không có nội dung quản lý cộng tác viên | Không đề cập — gap vẫn còn |
| OQ-006 | T10 slide 26 dán nhãn D1/D3/D4 | Không đề cập, file dùng tên S1–S4 chuẩn không qua nhãn lạ |
| OQ-007 | Tên "Vroom–Yetton–Jago" không khớp danh mục nguồn | Không giải — file cũng dùng tên này mà không đối chiếu nguồn |
| OQ-008 | T06: 8 yếu tố không có slide giải thích | **Không giải**, và file tự nhận cùng hạn chế: *"Không suy ra đủ framework chi tiết từ những slide mang nhiều hình; cần đối chiếu slide gốc khi áp dụng sâu"* — corroborate đánh giá của kho |
| OQ-009 | T12 chặng TRUST dựa Edmondson không có slide | Không đề cập |
| OQ-010 | T02 "Case in point" slide 34 không có nội dung | Không đề cập |
| OQ-011 | T05 slide 39 bốn nhãn não không giải thích | Không đề cập — T05 trong file hoàn toàn không nhắc slide này |
| OQ-012 | T03 slide 26 hai nghiên cứu một dòng | Không đề cập — file bỏ qua toàn bộ nội dung này (xem phát hiện #3) |
| OQ-013 | Guiding Arrows không trục | Không đề cập — file bỏ qua toàn bộ FW-063 |
| OQ-014 | T05: 65/78 slide ảnh | Không giải nội dung, nhưng **mở rộng phạm vi cảnh báo** sang T07, T13 (xem phát hiện #11) |
| OQ-015 | T03 Activity 4 Influence Lab không có slide | Không đề cập |
| OQ-016 | T11 slide 21 EI questionnaire không đọc được | Không đề cập nội dung câu hỏi cụ thể |
| OQ-017 | T11 nghiên cứu Gen Z không có nguồn đầy đủ | **Không giải** — file còn không nhắc tới case này (xem phát hiện #7) |
| OQ-018 | T15 Creative Matrix thiếu hàng Division | File mô tả SIT có đủ 5 thao tác nhưng không mô tả chi tiết bảng ma trận có bao nhiêu hàng — không xác nhận cũng không phủ nhận |
| OQ-019 | T15 slide 6–7 Design Thinking không có nội dung | Không đề cập |
| OQ-020 | T18 nội dung Luật AI không rõ | **Không giải** — file hoàn toàn bỏ qua phần Responsible AI (xem phát hiện #9) |

**Tổng kết:** đúng như dự đoán từ bản chất nguồn thứ cấp, **không có OQ nào được giải** bởi tài liệu này. Một OQ (OQ-001) nhận được sự củng cố độc lập; OQ-008 được xác nhận lại; OQ-014 được mở rộng phạm vi nghi ngờ.

---

## So sánh Problem → Framework Index

File có "PHỤ LỤC A · PROBLEM-TO-FRAMEWORK INDEX" với **20 vấn đề cụ thể** (ở mức tình huống, ví dụ: *"Nhân viên không đạt KPI"*, *"Manager là bottleneck"*, *"Team im lặng trong meeting"*), mỗi vấn đề có: dấu hiệu nhận diện, câu hỏi chẩn đoán, gợi ý thực hành theo thứ tự bước, và danh sách framework tham khảo (ghi `(T0X)`).

So với `problem_index.md` của kho — 11 vấn đề ưu tiên ở mức **chủ đề rộng** (ví dụ `PRB-005` "Giao việc và phát triển theo năng lực từng người"), mỗi vấn đề có chunk `PRB` đầy đủ riêng với: cách người dùng mô tả, triệu chứng, câu hỏi chẩn đoán, bảng nguyên nhân gốc rễ ↔ framework, dấu hiệu leo thang, chỉ số theo dõi.

**Nhận xét:** hai cấu trúc phục vụ hai tầng khác nhau, không mâu thuẫn:
- Kho tổ chức theo **11 vấn đề chiến lược** (đúng theo CLAUDE.md §2) — sâu, có nguồn trích dẫn slide, có đường leo thang rõ.
- File tổ chức theo **20 tình huống cụ thể hơn, mức hạt mịn hơn** — gần với văn phong một playbook: "dấu hiệu nhận diện → câu hỏi → gợi ý thực hành theo bước → framework."

**Gợi ý cho đợt viết playbook sắp tới:** cấu trúc 5 cột của file (nhận diện / câu hỏi chẩn đoán / gợi ý thực hành theo bước / framework tham khảo / ghi chú loại nội dung) là một **mẫu trình bày tốt cho `PB`** — gọn hơn nhiều so với template `PB` đầy đủ ở CLAUDE.md §7 nhưng cùng tinh thần "Checklist" + "Kịch bản". Có thể tham khảo văn phong này khi viết 5 playbook cho nhóm ưu tiên Cao, miễn là giữ nguyên yêu cầu bắt buộc của CLAUDE.md §7 (Dùng khi nào / Checklist / Kịch bản / Cách đánh giá hiệu quả / Framework nền tảng).

---

## Phụ lục: Độ phủ đối chiếu theo topic (xác nhận đã rà toàn bộ, không skim)

| Topic | Số framework file liệt kê | Số CON/FW trong KB (không gồm PRB/TOP) | Ghi chú |
|---:|---:|---:|---|
| 01 | 5 | 6 | thiếu FW-002, FW-004 (#1) |
| 02 | 7 | 13 | gộp nhiều mục, thiếu tên riêng FW-033/035/041 (#2) |
| 03 | 3 | 8 | thiếu FW-056, FW-058 (#3) |
| 04 | 4 | 2 | khớp, chi tiết hơn KB ở granularity |
| 05 | 3 | 10 | thiếu FW-061/062/063 (#4) |
| 06 | 4 | 10 | tự nhận hạn chế giống OQ-008 |
| 07 | 5 | 9 | thiếu FW-070 (#5) |
| 08 | 4 | 5 | khớp tốt |
| 09 | 5 | 6 | thiếu FW-030 (#6) |
| 10 | 4 | 4 | khớp tốt, thêm ý tưởng "two-way clarity check" (#10) |
| 11 | 4 | 9 | **thiếu toàn bộ CON-027, CON-028** (#7) |
| 12 | 9 | 8 | khớp rất tốt, đầy đủ nhất trong file |
| 13 | 5 | 7 | khớp tốt |
| 14 | 3 | 2 | khớp |
| 15 | 5 | 5 | khớp hoàn hảo |
| 16 | 6 | 9 | thiếu tên riêng FW-053/053-01/054 (#8) |
| 17 | 6 | 12 | khớp tốt ở các framework chính |
| 18 | 9 | 14 | **thiếu toàn bộ CON-030, CON-031** (#9) |
| 19 | 5 | 6 | khớp tốt |

**Tổng kết độ phủ:** file bao phủ tốt phần lớn framework chính (nhất là Topic 04, 10, 12, 14, 15, 19 — gần như khớp hoàn hảo). Hai khoảng trống đáng kể nhất là **Topic 11** (bỏ sót Robbins trust + case Gen Z) và **Topic 18** (bỏ sót toàn bộ mảng case thực tế + luật AI) — cả hai đều không ảnh hưởng tới kho vì kho đã xử lý đầy đủ, chỉ là thông tin để bạn của người dùng biết nếu muốn hoàn thiện file của họ.

---

## Khuyến nghị tổng thể

1. **Không cần sửa chunk nào trong kho** — không có conflict nội dung, không có thông tin mới để bổ sung.
2. **Housekeeping nhỏ:** sửa dòng 11 trong bảng tổng quan `problem_index.md` cho khớp trạng thái thật của `PRB-011` (phát hiện #12) — việc này độc lập với file, có thể làm ngay hoặc gộp vào đợt "Rà soát tổng thể".
3. **Tùy chọn:** nếu muốn chắc chắn tuyệt đối, có thể chạy thêm một lượt đối chiếu hình ảnh nhanh cho Topic 07 và Topic 13 (phát hiện #11) — nhưng rủi ro thấp vì các sơ đồ chính đã được render và đọc trực tiếp trong đợt xử lý gốc.
4. **Có thể báo lại cho bạn của người dùng** (nếu muốn): 9 framework có trên slide nhưng chưa được đặt tên riêng trong file của họ (các dòng #1–#6, #8 ở bảng phát hiện) — không bắt buộc, chỉ để file của họ đầy đủ hơn nếu họ muốn dùng tiếp.
5. **Sẵn sàng chạy tiếp:** 5 playbook (ưu tiên Cao) + `QUICK_REFERENCE.md`, có tham khảo thêm cấu trúc Problem-to-Framework Index của file này cho phần trình bày.
