# Vấn đề (PRB)

Bản gộp tự động bởi `scripts/export.py`. Mỗi chunk giữ nguyên frontmatter, ngăn cách bằng `=====`. Chunk `deprecated` đã bị loại.

=====

---
id: PRB-001
type: problem
title_vi: Định hướng bài toán cho team
title_en: Setting the problem agenda for the team
aliases: [chọn bài toán, định hướng, ưu tiên, roadmap team, nên làm gì trước]
keywords: [chọn bài toán đáng làm, định hướng cho team, thứ tự ưu tiên, prioritisation, roadmap, không biết nên làm gì trước, team bận mà không ra kết quả, nhiều yêu cầu cùng lúc, đo sai kết quả, mục tiêu mơ hồ, gắn việc của team với chiến lược, nói không với yêu cầu]
levels: [TEAM, ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-02, TOP-MEGROW-17, TOP-MEGROW-16, TOP-MEGROW-15]
problems_addressed: []
related_ids: [FW-033, FW-034, FW-035, FW-036, FW-037, FW-038, FW-039, FW-040, FW-043, FW-044, FW-045, FW-046, FW-047, FW-048, FW-050, FW-052, CON-015, CON-017, CON-018, CON-019, CON-020, FW-083, FW-084, FW-084-01, FW-085, FW-086]
source: ["MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 6–8, 13–19, 21–27, 29", "MEGROW | Topic 17 | Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf | Slide 6–9, 13–16, 19–35", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 13–22"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Định hướng bài toán cho team

Mức ưu tiên: **Cao** (vấn đề số 1): *chọn bài toán đáng làm, xác định hướng đi và thứ tự ưu tiên*.

## Cách người dùng thường mô tả
"Không biết nên cho team làm gì trước." · "Yêu cầu từ nhiều phía, cái nào cũng gấp." · "Team bận cả quý mà cuối quý không có gì để kể." · "Chọn bài toán theo cảm tính." · "Làm xong mô hình mới biết nó không giải quyết vấn đề thật." · "Sếp hỏi việc này đóng góp gì cho công ty mà mình lúng túng."

## Triệu chứng quan sát được
- Danh sách việc dài hơn năng lực, không ai gọi tên đánh đổi.
- Báo cáo dừng ở output ("đã train 4 mô hình"), không tới outcome.
- Mỗi thành viên hiểu ưu tiên quý một kiểu.
- Một bài toán chạy nhiều tháng mà không ai nói được tiêu chí dừng.
- Yêu cầu ad-hoc lặp lại được nhận hết vì không có tiêu chí từ chối.

## Câu hỏi chẩn đoán
1. **Có đường ngắm không?** — `CON-019`.
2. **Đang đo bậc nào: output, outcome hay impact?** — `CON-015`.
3. **Mục tiêu đã qua SMART chưa, và qua rồi có chạm outcome không?** — `FW-036`, `FW-037`.
4. **KPI có chịu được phá thử không?** — `FW-039`.
5. **Đã nhìn ra ngoài chưa: bối cảnh 2–3 năm tới và cấu trúc ngành?** — `FW-044`, `FW-045`.
6. **Thắng bằng gì: năng lực nào của team là VRIN?** — `FW-047`, `CON-017`, `CON-018`.
7. **Vấn đề đã được đóng khung đúng chưa, hay mới là triệu chứng?** — `FW-050`, `FW-052`.

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Framework | Nguồn |
|---|---|---|
| Coi kế hoạch là bất biến, không thấy vòng phản hồi | `FW-033` | T2 |
| Định hướng tổ chức không được dịch xuống tầng team | `FW-034` · `CON-019` | T2, T17 |
| Thiếu từ vựng chung: mỗi người hiểu "mục tiêu", "KPI" một kiểu | `FW-035` | T2 |
| Nhầm hoạt động với tác động; dừng ở output | `CON-015` | T2 |
| Mục tiêu mơ hồ nên đo lường và phối hợp cũng mơ hồ | `FW-036` | T2 |
| SMART nhưng đo sai kết quả, thiếu guardrail | `FW-037` | T2 |
| Chọn sai chỉ số; mọi metric đều bị coi là KPI | `FW-038` · `FW-039` | T2 |
| Không phân rã được mục tiêu thành việc có thứ tự và phụ thuộc | `FW-040` | T2 |
| Không quét môi trường bên ngoài; bị động trước thay đổi | `FW-044`, `FW-044-01` | T17 |
| Không hiểu cấu trúc cạnh tranh của mảng mình phục vụ | `FW-045`, `FW-045-01` | T17 |
| Không có tiêu chí "việc này có tạo giá trị không" | `FW-046` | T17 |
| Không phân biệt lợi thế nhất thời với lợi thế bền vững | `FW-047`, `FW-047-01` · `CON-017` · `CON-018` | T17 |
| Chỉ phân tích, không kết bằng khuyến nghị và đánh đổi | `FW-048` | T17 |
| Năng lực tư duy chiến lược chưa được luyện có chủ đích | `FW-043` | T17 |
| Giải sai bài vì chưa tách triệu chứng khỏi nguyên nhân | `FW-050` · `FW-052` · `CON-020` | T16 |
| Không biết giá trị bị phá vỡ ở đâu trong quy trình liên bộ phận | `FW-084` · `FW-084-01` | T15 |
| Ý tưởng cải tiến chỉ toàn "thêm người, thêm họp" | `FW-085` | T15 |
| Nhiều ý tưởng nhưng không chốt được việc nào để làm | `FW-086` | T15 |
| Chưa sàng ý tưởng qua ba phép thử trước khi xin nguồn lực | `FW-083` | T15 |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Không tầng tổ chức nào phía trên team có định hướng rõ để nối vào: hỏi lên bằng mẫu ba dòng của `FW-054`.
- Ưu tiên bị đổi liên tục bởi một stakeholder có quyền: vấn đề nằm ở `PRB-002`.
- Mục tiêu đã rõ nhưng vẫn không giao được hàng: chuyển sang `PRB-003` và `FW-041`.

## Chỉ số theo dõi sau xử lý
- Tỷ lệ thành viên nói đúng ba ưu tiên của team khi được hỏi ngẫu nhiên (`CON-019`).
- Số mục tiêu quý có đủ baseline, target, deadline và guardrail (`FW-038`).
- Số yêu cầu ad-hoc được từ chối hoặc chuyển thành tự phục vụ.
- Tỷ lệ báo cáo cuối quý nêu được outcome chứ không chỉ output.

## Nguồn
- `[MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 6–8, 13–19, 21–27, 29]`
- `[MEGROW | Topic 17 | Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf | Slide 6–9, 13–16, 19–35]`
- `[MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 13–22]`

=====

---
id: PRB-002
type: problem
title_vi: Làm việc với stakeholder để xây dựng và thống nhất bài toán
title_en: Working with stakeholders to define and agree the problem
aliases: [stakeholder, thuyết phục không có quyền, quản lý kỳ vọng, biết từ chối]
keywords: [stakeholder, thuyết phục khi không có quyền chỉ đạo, chuyển ngôn ngữ business sang bài toán DS, quản lý kỳ vọng, độ bất định, biết từ chối, đề xuất bị bác, bị giao việc không hợp lý, làm việc với bộ phận khác]
levels: [ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-12, TOP-MEGROW-19, TOP-MEGROW-14, TOP-MEGROW-16, TOP-MEGROW-17, TOP-MEGROW-03, TOP-MEGROW-15]
problems_addressed: []
related_ids: [FW-022, FW-011, FW-012, FW-013, FW-014, FW-015, FW-016, FW-017, FW-018, FW-019, FW-020, FW-021, CON-007, CON-008, FW-037, FW-048, FW-051, FW-052, FW-054, FW-058, FW-084, FW-084-01, FW-079, FW-083]
source: ["MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 1–41", "MEGROW | Topic 19 | Topic 19 - Present Business Case - Dr Tony Nguyen.pdf | Slide 1–33", "MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 4–12", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 17–21, 31–33", "MEGROW | Topic 17 | Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf | Slide 33–35"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Làm việc với stakeholder để xây dựng và thống nhất bài toán

Mức ưu tiên: **Cao** (vấn đề số 2).

## Cách người dùng thường mô tả
"Không có quyền chỉ đạo mà vẫn phải làm cho xong." · "Đề xuất bị bác mà không hiểu vì sao." · "Business nói một kiểu, mình hiểu một kiểu." · "Họ kỳ vọng chắc chắn, mà bài toán vốn bất định." · "Không biết từ chối thế nào."

## Triệu chứng quan sát được
- Sáng kiến bị chặn mà không rõ ai đang chặn.
- Người quan trọng nhất biết tới dự án ở phút cuối rồi phản đối.
- Dành hết thời gian cho người nhiệt tình nhưng không có quyền quyết.
- Đề xuất đúng kỹ thuật nhưng bị nghe thành phản đối.

## Câu hỏi chẩn đoán
1. Ai ảnh hưởng tới thành công mà tôi đang **đánh giá thấp**? (`FW-011`)
2. Ai Manage Closely, ai Keep Satisfied? (`FW-012`)
3. Tôi chưa dùng đủ **nguồn quyền lực** nào? (`FW-014`)
4. Điều gì quan trọng với họ, và hai bên tạo giá trị cho nhau thế nào? (`FW-015`)
5. Xung đột lợi ích thật, hay hai tập dữ liệu khác nhau? (`FW-020`)
6. Đề xuất đang **tấn công** hay **bảo vệ** mục tiêu của họ? (`CON-008`)
7. Ai trong nhóm Undecided dịch chuyển được bằng một lời "có" ít rủi ro? (`FW-017`)
8. Đã có phát biểu vấn đề chung chưa? (`FW-052`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Chưa lập bản đồ đầy đủ | Người quan trọng xuất hiện phút cuối | `FW-011` |
| Phân bổ sai sự chú ý | Dồn cho người nhiệt tình, quên người có quyền phủ quyết | `FW-012` |
| Thiếu uy tín để được nghe | Nói đúng nhưng không ai theo | `FW-013` |
| Chỉ dựa vào quyền hạn chính thức | Bế tắc vì "họ không thuộc quyền mình" | `FW-014` |
| Đi xin thay vì trao đổi | Đề nghị một chiều, thiếu vế "tôi đưa gì" | `FW-015` |
| Khác tập dữ liệu, bị tưởng là xung đột | Cãi ở nấc kết luận | `FW-020`, `FW-021` |
| Xung đột thật nhưng phản ứng theo phản xạ | Luôn né, hoặc luôn thỏa hiệp | `FW-016` |
| Đóng khung đề xuất sai | Nghe thành lời phản đối chiến lược | `CON-008` |
| Lập luận lỏng, trụ chồng lấn | Sụp ở phần Q&A | `FW-019` |
| Mở đầu không chạm mối bận tâm người nghe | Mất phòng họp trong ba phút | `FW-018` |
| Vào họp mới thuyết phục | Bị bác bởi phản đối lẽ ra xử lý được trước | `CON-007` |
| Thay đổi cần ủng hộ rộng mà không có liên minh | Duyệt trên giấy, không ai làm | `FW-017` |
| Không hiểu vấn đề từ chỗ stakeholder đứng | Mỗi bên mô tả một kiểu | `FW-051` |
| Không có phát biểu vấn đề chung có bằng chứng | Mỗi cuộc họp lại bắt đầu lại | `FW-052` |
| Cam kết con số khi bài toán còn bất định | Kỳ vọng bị đặt sai | `FW-037` |
| Trình bày phương án mà không khuyến nghị | Bị coi là đẩy quyết định | `FW-048` |
| Xin trợ giúp không rõ cần gì | Lời đề nghị bị trôi | `FW-054` |
| Dùng lập luận đã thuyết phục chính mình cho mọi đối tượng | Hiệu quả với người này, thất bại với người kia | `FW-058` |
| Chưa kiểm nền tảng niềm tin theo từng quan hệ | Lý lẽ đúng nhưng không được tin | `FW-058` |
| Không biết giá trị bị phá vỡ ở đâu trong quy trình chung | Họp nhiều, ai cũng đúng, việc vẫn tắc | `FW-084`, `FW-084-01` |
| Đồng thuận ở bước chốt nhưng hiểu khác nhau khi làm | "Đã thống nhất rồi" mà vẫn làm lại | `FW-084-01`, `FW-020` |
| Thành phần niềm tin cụ thể đang yếu với một stakeholder | Lý lẽ đúng nhưng không ai nghe | `FW-079` |

Diễn giải bảng: nhóm đầu là **quan hệ**; nhóm giữa là **truyền đạt**; năm dòng cuối là **đóng khung bài toán chung**.

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Bất đồng về **quyền quyết định**, không phải nội dung → `CON-003`, `CON-009`.
- Bài toán chưa được định nghĩa rõ chứ không phải thiếu thuyết phục → `PRB-001`.
- Stakeholder liên tục đổi yêu cầu → vấn đề ưu tiên cấp tổ chức.

## Chỉ số theo dõi sau xử lý
- Tỷ lệ bên liên quan xuất hiện muộn giữa chừng (giảm).
- Tỷ lệ đề xuất được duyệt ngay lần trình đầu.
- Số cuộc pre-meet 1:1 trước quyết định lớn (> 0).
- Số phản đối lớn xuất hiện lần đầu **trong** phòng họp (về 0).

## Nguồn
- `[MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 1–41]`
- `[MEGROW | Topic 19 | Topic 19 - Present Business Case - Dr Tony Nguyen.pdf | Slide 1–33]`
- `[MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 4–12]`

=====

---
id: PRB-003
type: problem
title_vi: Thiết kế framework làm việc và giải quyết vấn đề cho team
title_en: Designing the team's way of working and decision process
aliases: [quy trình làm việc, cách ra quyết định của team, chuẩn chất lượng]
keywords: [quy trình, process, phối hợp, coordination, ra quyết định, decision making, tiêu chuẩn chất lượng, nút thắt, bottleneck, team làm việc lộn xộn, ai quyết cái gì, họp nhiều mà không ra quyết định]
levels: [TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-06, TOP-MEGROW-10, TOP-MEGROW-14, TOP-MEGROW-02, TOP-MEGROW-16, TOP-MEGROW-05, TOP-MEGROW-07, TOP-MEGROW-13, TOP-MEGROW-15, TOP-MEGROW-18]
problems_addressed: []
related_ids: [FW-006, FW-010, CON-003, CON-005, CON-006, CON-009, FW-020, FW-021, FW-035, FW-038, FW-039, FW-041, FW-042, CON-016, FW-049, FW-050, FW-051, FW-052, CON-020, FW-053, FW-054, FW-060, FW-061, FW-062, FW-065, FW-065-01, FW-070, FW-071, FW-080, FW-084-01, FW-085, FW-094, FW-089, CON-031, FW-096, FW-088]
source: ["MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 64–65", "MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 35–37", "MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 13", "MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 13, 21–33", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 9–35"]
source_type: course
confidence: medium
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Thiết kế framework làm việc và giải quyết vấn đề cho team

Mức ưu tiên: **Cao** (vấn đề số 3 trong `problem_index.md`).

> `[SUY LUẬN]` Chunk này nay phủ đủ mười topic: **ra quyết định và quyền sở hữu** (Topic 06, 10, 14) · **đo lường, nhịp review và hệ thống giao hàng** (Topic 02) · **quy trình giải quyết vấn đề** (Topic 16) · **phân loại việc và công cụ ưu tiên** (Topic 05) · **đời sống team và bản đồ kết nối** (Topic 07) · **an toàn tâm lý để nêu vấn đề về chính cách làm việc** (Topic 13) · **hành trình stakeholder liên bộ phận** (Topic 15) · **ranh giới quyền cho AI** (Topic 18).

## Cách người dùng thường mô tả
"Mỗi người làm một kiểu." · "Họp nhiều mà không chốt được gì." · "Không rõ ai quyết cái gì." · "Lúc nào cũng bận mà việc quan trọng vẫn trễ." · "Việc gì cũng phải chờ tôi."

## Triệu chứng quan sát được
- Quyết định nhỏ bị đẩy lên bạn; bạn thành nút thắt.
- Nhiều bộ phận cùng tham gia nhưng không ai thấy mình chịu trách nhiệm cuối.
- Mọi thứ đều "gấp", không có thứ tự ưu tiên rõ.
- Team chờ nhau vì phụ thuộc chéo không được quản lý.
- `[KHÓA HỌC]` Topic 06 slide 4: *"Everyone is busy, but important things are still late."*

## Câu hỏi chẩn đoán
1. Quyết định nào team có thể tự ra một cách an toàn mà không cần tôi? (`CON-005`)
2. Với quyết định này, mức tham gia đúng là AI, AII, CI, CII hay GII? (`FW-006`)
3. Ai là chủ sở hữu duy nhất chịu trách nhiệm cho kết quả này? (`CON-003`)
4. Cái gì nên dừng, hoãn, hạ ưu tiên? (`CON-006`)
5. Việc nào nên do người, việc nào do AI, việc nào cả hai? (`FW-010`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Quyền quyết định không được định nghĩa | Mọi thứ escalate lên quản lý | `CON-003`, `CON-005` |
| Không chọn trước mức tham gia cho từng loại quyết định | Họp bàn rồi vẫn không ai chốt; hoặc mời bàn khi đã quyết xong | `FW-006` |
| Không có chủ sở hữu duy nhất cho kết quả | Mỗi bên chứng minh phần mình đã đúng | `CON-003` |
| Tải nhận thức không được thiết kế | Phê duyệt thừa, phụ thuộc chéo, người quá tải | `CON-006` |
| Chưa có quy ước về vai trò của AI | Không rõ ai chịu trách nhiệm cho đầu ra có AI tham gia | `FW-010` |
| Mức tham gia không được nói rõ từ đầu | Người ta tưởng mình cùng quyết rồi thấy không phải | `CON-009` |
| Bất đồng do khác tập dữ liệu, bị tưởng là xung đột quy trình | Cùng một tranh luận lặp lại qua nhiều cuộc họp | `FW-020`, `FW-021` |
| Thiếu hệ thống vận hành: không owner, không nhịp review, không ngưỡng | Đủ người, đủ kế hoạch mà vẫn trễ | `FW-041`, `FW-042` |
| Thiếu từ vựng chung cho thực thi | Mỗi người hiểu "KPI", "owner" một kiểu | `FW-035` |
| Đo thiếu: một KPI, không guardrail, không Flow | Chỉ số đẹp mà thực tế xấu đi | `FW-038`, `FW-039` |
| Giám sát nhắm vào người, không vào hệ thống | Tin xấu báo muộn | `CON-016` |
| Không có quy trình chẩn đoán blocker liên chức năng | Họp tăng, tiến độ không đổi | `FW-049`, `FW-050`, `FW-051` |
| Nhảy vào giải pháp trước khi định nghĩa vấn đề | Làm xong mới biết không trúng gốc | `FW-052`, `CON-020` |
| Không thử nhỏ trước khi triển khai rộng | Áp cho cả team rồi mới biết không chạy | `FW-053`, `FW-053-01` |
| Không ai nói rõ AI được đi tới đâu trong quy trình | Đầu ra AI được tin theo quán tính | `FW-065`, `FW-065-01`, `FW-057` |
| Việc đến không được phân loại trước khi làm | Ai hỏi trước được làm trước | `FW-060`, `FW-061`, `FW-062` |
| Rào cản hợp tác chưa được gọi tên | "Phối hợp chưa tốt" lặp lại qua nhiều quý | `FW-070` |
| Không biết luồng phụ thuộc thật trong team | Tắc ở chỗ không ai dự đoán được | `FW-071` |
| Không ai dám nêu vấn đề về chính cách làm việc | Quy trình hỏng tồn tại nhiều quý | `FW-080`, `PRB-009` |
| Quy trình cứng như nhau cho mọi mức rủi ro | Chặt thì chậm, lỏng thì rủi ro | `FW-085` (Attribute Dependency) |
| Bàn giao giữa các bước không có tiêu chí "xong tốt" | Làm lại nhiều vòng | `FW-084-01`, `CON-004` |
| Không ai viết ra AI được tự chạy tới đâu | Công cụ trượt dần sang mức tự chủ cao hơn mà không ai quyết | `FW-094`, `FW-089` |
| Ranh giới cho AI tồn tại dưới dạng lời dặn, không dưới dạng quyền truy cập | Lệnh bị bỏ qua, hệ quả thật xảy ra | `FW-094`, `CON-030` |
| Không biết công cụ nào được duyệt, dữ liệu nào được dùng | Vi phạm do tiện tay, không do cố ý | `CON-031` |
| Năng lực AI cá nhân không thành năng lực team | Năng suất cá nhân tăng, năng lực tập thể không đổi | `FW-096` (kịch bản 06) |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Vấn đề nằm ở mục tiêu và cách đo chứ không ở quy trình → chuyển sang `PRB-001`, dùng `FW-036`, `FW-037`, `FW-038`.
- Phụ thuộc chéo nằm ngoài quyền hạn của bạn → chuyển sang `PRB-002`, dùng `FW-012`, `FW-015`, `FW-022`.

## Chỉ số theo dõi sau xử lý
- Số quyết định escalate lên bạn mỗi tuần (kỳ vọng: giảm).
- Tỷ lệ quyết định có ghi rõ mức tham gia trước khi họp (kỳ vọng: tăng).
- Số hạng mục công việc không có chủ sở hữu rõ ràng (kỳ vọng: về 0).
- Số bước phê duyệt đã gỡ bỏ.

## Nguồn
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 64–65]`
- `[MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 35–37]`

=====

---
id: PRB-004
type: problem
title_vi: Chuyển dịch từ người làm chuyên môn sang người quản lý
title_en: Moving from individual contributor to manager
aliases: [IC to manager, chuyển sang quản lý, mới lên làm sếp]
keywords: [buông việc kỹ thuật, làm thay nhân viên, cân bằng tự làm và dẫn dắt, quản lý thời gian, quản lý năng lượng, tôi vẫn đang code nhiều quá, không có thời gian cho team, mới lên quản lý]
levels: [SELF]
courses: [MEGROW]
topics: [TOP-MEGROW-01, TOP-MEGROW-06, TOP-MEGROW-10, TOP-MEGROW-08, TOP-MEGROW-02, TOP-MEGROW-03, TOP-MEGROW-05]
problems_addressed: []
related_ids: [FW-002, FW-003, FW-004, FW-001, FW-005, CON-001, CON-002, CON-013, CON-014, CON-016, FW-035, CON-022, CON-023, CON-025, CON-026, FW-055, FW-059, FW-060, FW-061, FW-064]
source: ["MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 4–13, 20–24", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2", "MEGROW | Topic 08 | Topic 8 - Correcting Behaviour Through Coaching - Thao Luong.pdf | Slide 2, 7, 21–27", "MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 9–10, 13, 33", "MEGROW | Topic 03 | Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf | Slide 14, 25, 28", "MEGROW | Topic 05 | Topic 5 - Optimise Personal Productivity - Agnis Stibe.pdf | Slide 2–5, 29–33, 73–75"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Chuyển dịch từ người làm chuyên môn sang người quản lý

Mức ưu tiên: **Cao** (vấn đề số 4 trong `problem_index.md`).

## Cách người dùng thường mô tả
"Tôi vẫn đang tự làm phần khó nhất." · "Giao ra thì chậm hơn tôi tự làm." · "Không có thời gian cho team vì còn deadline của chính mình." · "Lên quản lý rồi mà sao vẫn thấy mình như DS, chỉ thêm họp."

## Triệu chứng quan sát được
- Bạn là người duy nhất hiểu một phần lõi của hệ thống.
- Lịch của bạn kín việc thực thi, 1:1 bị dời thường xuyên.
- Team chờ bạn gỡ những vấn đề kỹ thuật lặp lại.
- Bạn đánh giá một tuần thành công bằng những gì **bạn** đã làm xong.
- `[KHÓA HỌC]` Bối cảnh chung: khoảng **50% quản lý mới được đề bạt không đạt kỳ vọng trong 18 tháng đầu** (Topic 01 slide 9).

## Câu hỏi chẩn đoán
1. Đóng góp lớn nhất của tôi quý này đến từ việc tôi tự làm hay từ việc người khác làm được nhờ tôi? (`FW-004`)
2. Tôi đang tìm sự tuân thủ hay cam kết? (`FW-002`)
3. Tôi đang thừa hưởng loại tình huống nào — Start-up, Turnaround, Accelerated Growth, Realignment hay Sustaining Success? (`FW-003`)
4. Trong ba cái bẫy, cái nào xuất hiện nhiều nhất ở tôi ngay lúc này? (`CON-002`)
5. Tôi nghiêng về trục hành vi nào, và khi áp lực tăng tôi trôi về đâu? (`FW-005`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Thước đo thành công chưa đổi | Vẫn lấy cảm giác hoàn thành từ output cá nhân | `CON-001` |
| Mang theo niềm tin sai về vai trò | Tưởng có quyền là làm được điều mình muốn | `FW-002` |
| Chưa định vị được mình đang ở chặng nào của sự nghiệp | Coi quản lý là phần thưởng cho chuyên môn giỏi | `FW-004` |
| Ba hành vi bẫy: làm thay, né giao việc, kỳ vọng ngầm | Team không trưởng thành, việc giao ra vẫn hỏng | `CON-002` |
| Không có lộ trình cho 90 ngày đầu | Phản ứng theo sự vụ, không có thứ tự | `FW-003` |
| Không biết thiên lệch hành vi của mình | Dùng một phong cách cho mọi người | `FW-005`, `FW-001` |
| Chưa quen giữ cảm xúc của chính mình trong vai trò mới | Phản ứng theo thói quen khi bị áp lực | `CON-013` |
| Vẫn đo giá trị bản thân bằng việc mình tự giải, không bằng việc hệ thống chạy | Tự làm phần khó nhất, team không ai nắm | `CON-014` |
| Giữ cảm giác kiểm soát bằng cách theo dõi từng người | Hỏi tiến độ cá nhân thay vì nhìn trạng thái công việc | `CON-016` |
| Chưa chuyển sang ba động tác Translate – Coordinate – Adjust | Mạnh điều phối, yếu dịch định hướng, bỏ hẳn điều chỉnh | `FW-035` |
| Phán đoán chuyên môn vẫn được dùng để đọc người | *"Nếu cô ấy thực sự cố thì đã xong rồi"* | `CON-022`, `FW-055` |
| Chưa nhận ra phán đoán nay chỉ là đầu vào, câu nói mới là sản phẩm | Nói ra kết luận chưa kiểm, nhân viên tiếp nhận như sự thật | `CON-023`, `FW-056` |
| Không phân biệt việc gấp với việc có tác động cao | Lịch kín, cuối tuần không có việc quan trọng nào tiến lên | `FW-059`, `FW-061` |
| Trở thành nút thắt của mọi quyết định | Cấp trên đòi nhanh, team chờ mình quyết | `FW-059`, `FW-060` |
| Dồn sức thay vì xây hành vi lặp lại | Hiệu suất vọt lên rồi suy giảm; dấu hiệu kiệt sức | `CON-025`, `CON-026`, `FW-064` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Bạn đã thử buông nhưng chất lượng tụt rõ rệt → vấn đề là năng lực team, chuyển sang `PRB-005`.
- Nguyên nhân nằm ở nguồn lực hoặc ưu tiên mâu thuẫn từ trên xuống → đó là vấn đề tổ chức, không phải chuyển dịch cá nhân.
- Quá tải kéo dài kèm dấu hiệu kiệt sức → cần can thiệp về khối lượng công việc, không phải thêm framework. Xem `CON-025` về hai nhánh hyper-performance và burnout, và `FW-059` dòng 10 (*Performance vs. wellbeing*).

## Chỉ số theo dõi sau xử lý
- Số quyết định kỹ thuật phải quay về bạn mỗi tuần (kỳ vọng: giảm).
- Số phần hệ thống chỉ một mình bạn hiểu (kỳ vọng: giảm về 0).
- Tỷ lệ 1:1 diễn ra đúng lịch (kỳ vọng: tăng).
- Số việc bạn đã bàn giao trong 30 ngày qua, kèm tên người nhận.
- `[KHÓA HỌC]` Thời điểm chạm **break-even point** của `FW-003`.

## Nguồn
- `[MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 4–13, 20–24]`
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2]`

=====

---
id: PRB-005
type: problem
title_vi: Giao việc và phát triển theo năng lực từng người
title_en: Delegating and developing according to each person's capability
aliases: [giao việc, phân công, trao quyền cho senior, phạm vi cho collaborator]
keywords: [giao việc, delegation, trao quyền, empower, phát triển nhân viên, mức sẵn sàng, readiness, senior, collaborator, người giỏi quá tải, không dám giao việc, giao rồi vẫn phải làm lại]
levels: [TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-01, TOP-MEGROW-06, TOP-MEGROW-10, TOP-MEGROW-09, TOP-MEGROW-02, TOP-MEGROW-05, TOP-MEGROW-18]
problems_addressed: []
related_ids: [FW-001, FW-001-01, FW-001-02, FW-005, FW-006, FW-009, FW-010, FW-028, FW-029, FW-031, CON-002, CON-003, CON-004, CON-005, CON-006, FW-036, FW-037, FW-041, FW-059, FW-060, FW-062, CON-022, FW-093, FW-096, FW-095]
source: ["MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 15–19", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 59–61, 64–65", "MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 24–36", "MEGROW | Topic 09 | Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf | Slide 31–38", "MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 16–19, 30"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Giao việc và phát triển theo năng lực từng người

Mức ưu tiên: **Cao** (vấn đề số 5 trong `problem_index.md`).

## Cách người dùng thường mô tả
"Giao rồi mà vẫn phải làm lại." · "Người giỏi nhất đang gánh hết." · "Không biết giao đến đâu thì vừa." · "Senior thì để tự do, còn collaborator phải nói tới đâu?" · "Giao rồi mà bạn ấy vẫn hỏi từng bước."

## Triệu chứng quan sát được
- Cùng một mức hướng dẫn được áp cho cả Senior lẫn collaborator.
- Một hoặc hai người nhận hết việc quan trọng, người còn lại nhận việc phụ.
- Việc đã giao vẫn quay lại bàn bạn để quyết.
- Người nhận làm đúng yêu cầu nhưng không bao giờ đề xuất cải tiến.
- `[KHÓA HỌC]` Thách thức 2 và 4 của Topic 06: giao trách nhiệm mà không giao quyền quyết định; người giỏi nhận việc then chốt tới mức quá tải.

## Câu hỏi chẩn đoán
1. Cho **việc cụ thể này**, người này ở đâu trên trục năng lực và cam kết? (`FW-001`)
2. Tôi có bằng chứng gì, hay đang dùng thâm niên thay cho năng lực? (`FW-001-01`)
3. Đã nói rõ bốn thành phần của `CON-004` chưa — kết quả mong đợi, quyền sở hữu, quyền quyết định, tiêu chí thành công?
4. Ai là chủ sở hữu duy nhất chịu trách nhiệm cho kết quả này? (`CON-003`)
5. Năm thành tố sở hữu tâm lý, người này thiếu cái nào? (`FW-009`)
6. Tôi đang tối ưu giao hàng hôm nay bằng cái giá năng lực ngày mai không?

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Không chẩn đoán mức sẵn sàng theo từng việc | Một phong cách cho mọi người | `FW-001`, `FW-001-01` |
| Dùng thâm niên hoặc chức danh thay cho bằng chứng | Senior được giao mọi thứ, collaborator không được giao gì | `FW-001-01` |
| Giao responsibility mà không giao decision rights | Mọi quyết định vẫn quay về bạn | `CON-003` |
| Giao đầu việc thay vì giao kết quả | Người nhận hỏi lại liên tục | `CON-004` |
| Sở hữu tâm lý chưa hình thành | Làm đúng yêu cầu, không chủ động | `FW-009` |
| Theo dõi bằng kiểm soát thay vì bằng checkpoint | Người nhận thấy bị giám sát | `CON-005` |
| Nỗi sợ mất kiểm soát của chính người quản lý | Né giao việc | `CON-002` |
| Nhầm "giao việc" với "cho tham gia quyết định" | Họp nhiều mà vẫn không ai sở hữu | `FW-006` |
| Giao thử thách không tương xứng mức sẵn sàng | Quá tải, hoặc bỏ phí người đã sẵn sàng | `FW-029` |
| Chưa tìm nguyên nhân gốc trước khi quyết cách phát triển | Giao thêm việc trong khi gốc ở Career hoặc Environment | `FW-028` |
| Mục tiêu giao cho từng người mơ hồ; không tách Responsibility khỏi Accountability | Giao xong vẫn phải theo sát, không ai thật sự chịu kết quả | `FW-036`, `FW-037`, `FW-041` |
| Lấy việc lại vì "tự làm nhanh hơn" dưới áp lực deadline | Hiệu quả ngắn hạn, phụ thuộc dài hạn | `FW-059` (dòng 8), `CON-022` |
| Không hỏi "việc này có cần tôi không" trước khi xếp lịch | Quản lý thành nút thắt | `FW-060`, `FW-062` |
| AI đã tự động hóa phần việc tập sự, người mới không còn chỗ học | Ship nhanh nhưng không giải thích được việc mình làm | `FW-093`, `FW-096` |
| Người đã sẵn sàng nhưng vẫn chỉ được giao việc kiểm chứng | Có năng lực mà mất hứng | `FW-093` (Exposure), `FW-029` |
| Chẩn đoán sai điều kiện đang thiếu | Cấp thêm đào tạo cho người đang thiếu cơ hội | `FW-093` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Năng lực đủ nhưng kết quả vẫn hỏng → nguyên nhân ở hệ thống, xem `CON-006` và `CON-012`.
- Vấn đề là hành vi chứ không phải năng lực → `FW-026`, `PRB-006`.
- Nguyên nhân ở hướng nghề nghiệp dài hạn, không ở việc trước mắt → `FW-031`.
- `[SUY LUẬN]` **Khoảng trống:** MEGROW không có nội dung riêng về giao việc cho cộng tác viên; mọi framework trong bảng đều giả định nhân viên chính thức. Xem `open_questions.md` (OQ-005).

## Chỉ số theo dõi sau xử lý
- Số quyết định phải quay về bạn mỗi tuần (giảm).
- Phân bố việc then chốt (bớt tập trung vào một người).
- Số việc giao kèm đủ bốn thành phần của `CON-004` (tiến tới 100%).
- Số đề xuất cải tiến do người nhận việc tự nêu (tăng — chỉ dấu của `FW-009`).
- Tỷ lệ việc giao ra phải làm lại (giảm).

## Nguồn
- `[MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 15–19]`
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 59–61, 64–65]`
- `[MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 24–36]`

=====

---
id: PRB-006
type: problem
title_vi: Feedback, coaching và trao đổi về hiệu suất
title_en: Feedback, coaching and performance conversations
aliases: [góp ý, phản hồi, coaching, trao đổi hiệu suất]
keywords: [góp ý, feedback, coaching, trao đổi hiệu suất, nói chuyện khó, nhân viên làm chưa tốt, hành vi không phù hợp, ngại góp ý, góp ý rồi không đổi, phát triển nhân viên]
levels: [TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-04, TOP-MEGROW-08, TOP-MEGROW-09, TOP-MEGROW-03, TOP-MEGROW-07, TOP-MEGROW-11]
problems_addressed: []
related_ids: [FW-023, FW-024, FW-025, FW-025-01, FW-026, FW-027, FW-028, FW-029, FW-030, FW-031, FW-032, CON-010, CON-011, CON-012, CON-013, FW-055, FW-056, FW-057, FW-069, FW-068-01, CON-022, CON-023, CON-024, FW-072, FW-073, FW-076, FW-077, FW-075, PRB-009, FW-080]
source: ["MEGROW | Topic 04 | Topic 4 - Practice Performance Conversations - AP Elaine Chew.pdf | Slide 5–35", "MEGROW | Topic 08 | Topic 8 - Correcting Behaviour Through Coaching - Thao Luong.pdf | Slide 7–42", "MEGROW | Topic 09 | Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf | Slide 6–51", "MEGROW | Topic 03 | Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf | Slide 4–28", "MEGROW | Topic 07 | Topic 7 - Building Team Capability and Growth - Thao Luong.pdf | Slide 18, 25–28"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Feedback, coaching và trao đổi về hiệu suất

Mức ưu tiên: **Trung bình** (vấn đề số 6).

## Cách người dùng thường mô tả
"Góp ý rồi không thấy đổi gì." · "Ngại nói thẳng, sợ bạn ấy tự ái." · "Không biết mở đầu thế nào." · "Bạn ấy làm đủ việc nhưng mình vẫn lo." · "Coach nhiều mà team vẫn phụ thuộc." · "Không biết giao thêm thử thách tới đâu."

## Triệu chứng quan sát được
- Góp ý chung chung rồi không gì thay đổi.
- Né một cuộc trò chuyện đã nhiều tuần.
- Bạn là người duy nhất đưa phản hồi cho cả team.
- Nhân viên tự chẩn đoán ("chắc em cần học thêm X") và bạn nhận luôn.
- Kế hoạch cải thiện nhắm sai nguyên nhân.

## Câu hỏi chẩn đoán
1. Đây là vấn đề **kết quả công việc** hay **hành vi**? (`FW-024` hay `FW-025`)
2. Nguyên nhân ở Ability, Motivation hay Opportunity? (`FW-023`)
3. Hành vi này chạm bao nhiêu trong năm loại tác động? (`FW-026`)
4. Câu mở đầu có qua được phép thử camera không? (`CON-010`)
5. Tôi đang ở kiểu quản lý nào — kiểu đó có thay thế việc chẩn đoán không? (`FW-027`)
6. Năm lăng kính cho thấy nguyên nhân gốc thật là gì? (`FW-028`)
7. Mức phát triển tương xứng: vai trò hiện tại, stretch, hay luân chuyển? (`FW-029`)
8. Đây có phải vấn đề của hệ thống chứ không phải của con người? (`CON-012`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Chẩn đoán quá nhanh, quy kết thái độ | Kế hoạch cải thiện nhắm sai | `FW-023`, `FW-028` |
| Nguyên nhân thật ở hệ thống, không ở người | Sửa người mãi không hết | `CON-012` |
| Không có cấu trúc cho cuộc trò chuyện | Lan man, không chốt được gì | `FW-024`, `FW-025` |
| Không rõ hành vi nào đáng xử lý | Bỏ qua cái cần nói, soi cái không cần | `FW-026` |
| Câu mở đầu là nhãn dán, không phải quan sát | Người nghe phòng vệ ngay | `CON-010` |
| Cảm xúc của người quản lý rò rỉ vào cuộc trò chuyện | Phản ứng theo thói quen, mất bình tĩnh | `CON-013` |
| Nghe sai cấp độ, hoặc không nghe | Hỏi lấy lệ rồi chuyển sang khuyên | `CON-011` |
| Coach nhiều hơn thay vì coach đúng chỗ | Team phụ thuộc, mất quyền sở hữu | `FW-027`, `FW-032` |
| Tự ôm toàn bộ việc phát triển của team | Bạn thành nút thắt | `FW-032` |
| Giao thử thách không tương xứng | Quá tải hoặc bỏ phí người giỏi | `FW-029` |

| Khuyên trước khi có bằng chứng | Nhận luôn lời tự chẩn đoán của họ | `FW-030` |
| Không chốt cam kết quan sát được | *"Em sẽ cố gắng hơn"* rồi thôi | `FW-025-01` |
| Nguyên nhân ở hướng nghề nghiệp dài hạn | Làm đủ việc nhưng mất lửa | `FW-031` |
| Phán đoán chưa được kiểm trước khi thành cuộc trò chuyện | Kỹ thuật nói chuyện tốt nhưng kết luận sai từ đầu | `FW-055`, `CON-022` |
| Mức tự tin về đánh giá cao hơn độ chính xác thật | Chấm sẵn sàng thăng chức bằng cảm nhận | `CON-024`, `FW-029` |
| Dùng số liệu hoạt động thay cho bằng chứng hiệu suất | Đếm commit, tin nhắn, ticket | `FW-057` |
| Thiên kiến rò vào câu chữ | Nhân viên nghe "tôi không được tin" | `FW-056`, `CON-023` |
| Không có kênh phản hồi ngang hàng | Điểm mù tồn tại vô hạn vì không ai nói | `FW-069`, `FW-068-01` |
| Dùng một cách giao tiếp cho mọi người | Cùng thông điệp, người hiểu người không | `FW-072`, `FW-076` |
| Quy hành vi về tính cách, bỏ qua tình huống và môi trường | "Bạn này thiếu chủ động" khi gốc là tình huống yếu | `FW-073` |
| Không có kịch bản luyện trước cuộc trò chuyện khó | Vào cuộc rồi mới nghĩ cách nói | `FW-077` |

Diễn giải bảng: sáu dòng đầu là lỗi **chẩn đoán và mở đầu**; bảy dòng tiếp là lỗi **cách coach và chốt**; sáu dòng cuối (từ Topic 03 và Topic 07) là lỗi **ở chính phán đoán và ngôn ngữ của người quản lý**, xảy ra trước khi cuộc trò chuyện bắt đầu.

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Hành vi chạm tuân thủ, công bằng, an toàn hoặc đạo đức → xử lý ngay, không coaching (ô POLICY/ETHICS của `FW-026`).
- Nguyên nhân là xung đột giữa hai bộ phận → `PRB-010`.
- Nguyên nhân là lương thưởng hoặc lộ trình thăng tiến → ngoài phạm vi MEGROW, cần làm việc với cấp trên và HR.
- Người đó không dám nói thật → vấn đề an toàn tâm lý, chuyển sang `PRB-009` và `FW-080` trước khi tiếp tục cuộc trò chuyện về hiệu suất.

## Chỉ số theo dõi sau xử lý
- Tỷ lệ cuộc trò chuyện kết thúc bằng cam kết **quan sát được**.
- Số lần chẩn đoán trước khi khuyên, so với số lần khuyên luôn.
- Số nguồn phát triển ngoài bạn mà mỗi thành viên đang dùng (kỳ vọng: tăng).
- Thời gian từ lúc nhận thấy một hành vi tới lúc nói về nó.
- Phân bố mức phát triển theo `FW-029` (kỳ vọng: không ai kẹt ở 5–11 nhiều quý liên tiếp).

## Nguồn
- `[MEGROW | Topic 04 | Topic 4 - Practice Performance Conversations - AP Elaine Chew.pdf | Slide 5–35]`
- `[MEGROW | Topic 08 | Topic 8 - Correcting Behaviour Through Coaching - Thao Luong.pdf | Slide 7–42]`
- `[MEGROW | Topic 09 | Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf | Slide 6–51]`

=====

---
id: PRB-007
type: problem
title_vi: Động lực, gắn kết và giữ người
title_en: Motivation, engagement and retention
aliases: [động lực, gắn kết, giữ chân nhân sự, engagement]
keywords: [động lực, motivation, gắn kết, engagement, giữ người, retention, mất lửa, không chủ động, collaborator không gắn bó, nhân viên giỏi muốn nghỉ, team trầm]
levels: [TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-06, TOP-MEGROW-09, TOP-MEGROW-07, TOP-MEGROW-05, TOP-MEGROW-11, TOP-MEGROW-13]
problems_addressed: []
related_ids: [FW-008, FW-009, FW-007, FW-028, FW-031, FW-032, CON-005, FW-066, FW-067, FW-068, FW-069, FW-070, FW-071, CON-025, FW-074, FW-080, CON-027, CON-029, CON-028]
source: ["MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 33–39, 59, 65", "MEGROW | Topic 09 | Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf | Slide 26–38"]
source_type: course
confidence: medium
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Động lực, gắn kết và giữ người

Mức ưu tiên: **Trung bình** (vấn đề số 7 trong `problem_index.md`).

> `[SUY LUẬN]` Chunk này nay phủ sáu topic: **đòn bẩy xã hội và sở hữu tâm lý** (Topic 06) · **chẩn đoán động lực và phát triển cá nhân** (Topic 09) · **lý thuyết nhu cầu McClelland và ERG** (Topic 11) · **bản sắc và kết nối trong team** (Topic 07) · **hiệu suất bền vững so với kiệt sức** (Topic 05) · **niềm tin và an toàn tâm lý** (Topic 13).

## Cách người dùng thường mô tả
"Bạn ấy làm đủ việc nhưng mất lửa." · "Team im lặng trong họp." · "Collaborator không gắn bó, hết hợp đồng là đi." · "Không ai đề xuất gì mới nữa."

## Triệu chứng quan sát được
- Làm đúng yêu cầu, không hơn; không còn đề xuất cải tiến.
- Mức tham gia trong thảo luận kỹ thuật giảm.
- Thực hành tốt của một người không lan sang người khác.
- Người giỏi bắt đầu hỏi về cơ hội ở nơi khác.

## Câu hỏi chẩn đoán
1. Trong năm thành tố sở hữu tâm lý, người này đang thiếu cái nào? (`FW-009`)
2. Năm lăng kính cho thấy gốc là Motivation hay thật ra là Career? (`FW-028`)
3. Hành vi tốt ở team có đang được **nhìn thấy** không, hay chỉ mình tôi biết? (`FW-008`)
4. Cái gì đang làm cho hành vi tốt khó xảy ra hơn mức cần thiết? (`FW-008` — Facilitation)
5. Người này có thấy việc mình làm là một phần con người nghề nghiệp của họ không? (`FW-009` — identity)
6. Tôi có đang kiểm soát tới mức thu lại quyền sở hữu vừa trao không? (`CON-005`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Sở hữu tâm lý chưa hình thành | Thi hành chứ không sở hữu | `FW-009` |
| Đóng góp tốt không được nhìn thấy | Nỗ lực thêm không có hồi đáp | `FW-008` — Recognition |
| Không có chỗ để học và quan sát lẫn nhau | Mỗi người một ốc đảo | `FW-008` — Learning, Cooperation |
| Chuẩn mực nhóm không rõ | "Ở đây mọi người làm thế nào" không ai biết | `FW-008` — Norms |
| Ma sát khiến hành vi tốt khó xảy ra | Thiếu template, môi trường, công cụ | `FW-008` — Facilitation |
| Kiểm soát quá mức làm hỏng self-efficacy | Người nhận mất tự tin quyết định | `CON-005`, `FW-009` |
| Nguyên nhân thật nằm ở hướng nghề nghiệp, không ở động lực | Làm đủ việc nhưng hết đề xuất mới | `FW-028` (lăng kính Career), `FW-031` |
| Quản lý tự ôm toàn bộ việc phát triển | Nhân viên không có nguồn phát triển nào khác | `FW-032` |
| Team là tập hợp cá nhân, chưa có bản sắc chung | Mỗi người làm tốt phần mình, tổng thể rời rạc | `FW-067` |
| Khoảng cách giữa tự nhận thức và cách đồng đội trải nghiệm | Người giỏi nhưng ảnh hưởng thấp hơn mức đáng có | `FW-068`, `FW-069` |
| Bực bội được chịu đựng thay vì được nói ra | Không ai nêu vấn đề, mọi thứ "vẫn ổn" | `FW-067`, `FW-070` |
| Thành viên ngoại vi chỉ có một mối nối yếu với team | Cộng tác viên không gắn bó dù việc họ làm là đầu vào sống còn | `FW-071` |
| Cường độ cao kéo dài không có cơ chế bền | Mất lửa, hết đề xuất, rồi rời đi | `CON-025` |
| Không biết nhu cầu nền của từng người | Cùng một phần thưởng, người hào hứng người không | `FW-074` |
| Người đang ở đầu Existence của thang ERG | Lời mời phát triển không có sức nặng | `FW-074` |
| Niềm tin bị trừ dần mà không ai nói ra | Làm đủ việc, không còn nêu ý kiến | `CON-027`, `CON-029` |
| Môi trường thiếu an toàn tâm lý | Không ai đề xuất gì mới, không ai nhận sai | `FW-080`, `PRB-009` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Nguyên nhân là lương thưởng hoặc lộ trình thăng tiến → nằm ngoài phạm vi framework trong MEGROW, cần làm việc với cấp trên và HR.
- Mức gắn kết thấp kèm thiếu an toàn tâm lý → **không** dùng Comparison và Competition của `FW-008`, sẽ làm tệ thêm. Xử lý `PRB-009` và `FW-080` trước.
- `[SUY LUẬN]` **Khoảng trống cho cộng tác viên:** đòn bẩy Comparison và Competition giả định người tham gia cùng một hệ quy chiếu nghề nghiệp. Với collaborator, điều này có thể phản tác dụng. Lưới Ethics của `FW-007` là công cụ kiểm tra trước. Xem `open_questions.md` (OQ-005).

## Chỉ số theo dõi sau xử lý
- Số đề xuất cải tiến do thành viên tự nêu mỗi tháng (kỳ vọng: tăng).
- Mức tham gia phát biểu trong họp kỹ thuật.
- Số thực hành tốt được một người khác áp dụng lại.
- Tỷ lệ giữ người theo quý, tách riêng nhân viên chính thức và cộng tác viên.

## Nguồn
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 33–39, 59, 65]`

=====

---
id: PRB-008
type: problem
title_vi: Làm việc với cấp trên và gắn với chiến lược tổ chức
title_en: Managing upward and linking to organisational strategy
aliases: [quản lý ngược lên, managing up, báo cáo cấp trên, xin phê duyệt]
keywords: [làm việc với sếp, managing up, xin phê duyệt, xin nguồn lực, báo cáo lên, gắn với chiến lược, business case, trình bày với ban lãnh đạo, bị cắt ngân sách]
levels: [ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-19, TOP-MEGROW-12, TOP-MEGROW-17, TOP-MEGROW-02, TOP-MEGROW-16]
problems_addressed: []
related_ids: [FW-018, FW-019, FW-019-01, FW-012, FW-015, CON-007, CON-008, FW-033, FW-034, FW-043, FW-044, FW-045, FW-046, FW-047, FW-048, CON-017, CON-018, CON-019, FW-054]
source: ["MEGROW | Topic 19 | Topic 19 - Present Business Case - Dr Tony Nguyen.pdf | Slide 1–33", "MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 17", "MEGROW | Topic 17 | Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf | Slide 6–9, 13–16, 19–35", "MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 6–8", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 31–33"]
source_type: course
confidence: medium
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Làm việc với cấp trên và gắn với chiến lược tổ chức

Mức ưu tiên: **Trung bình** (vấn đề số 8 trong `problem_index.md`).

> `[SUY LUẬN]` Chunk này phủ năm mảng: **trình bày và xin phê duyệt** (Topic 19) · **ảnh hưởng ngược lên** (Topic 12) · **gắn mục tiêu team với chiến lược** (Topic 17: line-of-sight test, PESTEL, options table) · **chuỗi mục tiêu và chỉ số** (Topic 02) · **xin trợ giúp ba dòng** (Topic 16). Toàn bộ topic liên quan đã được xử lý.

## Cách người dùng thường mô tả
"Xin nguồn lực mà không được duyệt." · "Sếp hỏi mấy câu là em đuối." · "Không biết diễn đạt giá trị của việc này cho ban lãnh đạo." · "Mình trình bày kỹ thuật, họ không quan tâm."

## Triệu chứng quan sát được
- Đề xuất bị hoãn vô thời hạn thay vì bị từ chối thẳng.
- Phần hỏi đáp làm sụp cả bài trình bày.
- Sếp nghe xong vẫn không rõ bạn đang xin gì.
- Bạn trình bày quá trình làm, trong khi người nghe cần kết luận.

## Câu hỏi chẩn đoán
1. Ai thực sự phải nói "có", và họ quan tâm điều gì? (`FW-012`)
2. Đề xuất của tôi đang **bảo vệ** hay **tấn công** mục tiêu của họ? (`CON-008`)
3. Tôi đã nói thành lời cái **câu hỏi** mình cần họ trả lời chưa? (`FW-018`)
4. Ba trụ lập luận của tôi có MECE không? Bằng chứng cho từng trụ là gì? (`FW-019`)
5. Nếu họ chỉ đọc tiêu đề slide, câu chuyện có đứng được không? (`FW-019-01`)
6. Ai tôi cần gặp riêng **trước** cuộc họp? (`CON-007`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Mở đầu không chạm vào mối bận tâm của người nghe | Mất sự chú ý trong ba phút đầu | `FW-018` |
| Đóng khung đề xuất như lời phản đối chiến lược | Bị bác dù nội dung đúng | `CON-008` |
| Không nói ra câu hỏi cần quyết | Họ nghe xong không biết phải quyết gì | `FW-018` |
| Lập luận chồng lấn hoặc thiếu mảng | Sụp ở phần hỏi đáp | `FW-019` |
| Trình bày theo thứ tự mình làm, không theo thứ tự họ cần | Dẫn dắt dài, kết luận ở cuối | `FW-019` |
| Tiêu đề slide nêu chủ đề thay vì kết luận | Người lướt slide không nắm được gì | `FW-019-01` |
| Lần đầu người quyết nghe về đề xuất là trong cuộc họp | Bị chặn bởi phản đối lẽ ra xử lý được từ trước | `CON-007` |
| Đi xin thay vì trao đổi hai chiều | Không có vế "tôi mang lại gì cho anh" | `FW-015` |
| Việc của team không nối lên định hướng tổ chức | "Việc này đóng góp gì?" không trả lời được | `FW-034`, `CON-019` |
| Không đọc được bối cảnh ngoài và cấu trúc ngành | Bị động trước thay đổi | `FW-044`, `FW-045` |
| Không nói được lợi thế bằng ngôn ngữ chiến lược | Đề xuất bị coi là "kỹ thuật thuần tuý" | `FW-046`, `FW-047`, `CON-018` |
| Phân tích không kết bằng khuyến nghị | Cấp trên phải quyết thay mình | `FW-048` |
| Tư duy chiến lược chưa được luyện | Chỉ phản ứng việc trước mắt | `FW-043` |
| Leo thang dài dòng | Cấp trên không biết làm gì | `FW-054` |

Diễn giải bảng: bốn dòng đầu là lỗi **đóng khung và cấu trúc**; bốn dòng tiếp là lỗi **chuẩn bị và quan hệ**; sáu dòng cuối (Topic 17, 16, 02) là lỗi **gắn kết chiến lược**.

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Đề xuất bị bác vì **không gắn ưu tiên chiến lược**, không phải vì cách trình bày → `CON-019`.
- Sếp không có quyền quyết việc này → quay lại `FW-012`.
- Vấn đề là khối lượng việc được giao, không phải xin nguồn lực → `CON-006`.

## Chỉ số theo dõi sau xử lý
- Tỷ lệ đề xuất được duyệt ngay lần trình đầu.
- Số phản đối lớn xuất hiện lần đầu trong phòng họp (kỳ vọng: về 0).
- Bộ slide có qua được skim test không (đọc riêng tiêu đề có kể hết câu chuyện).
- Thời gian từ lúc trình tới khi có quyết định (kỳ vọng: giảm).

## Nguồn
- `[MEGROW | Topic 19 | Topic 19 - Present Business Case - Dr Tony Nguyen.pdf | Slide 1–33]`
- `[MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 17]`

=====

---
id: PRB-009
type: problem
title_vi: Văn hóa thử nghiệm và an toàn tâm lý
title_en: A culture of experimentation and psychological safety
aliases: [an toàn tâm lý, psychological safety, văn hóa thử nghiệm, dám sai]
keywords: [không ai dám nói, team im lặng, sợ sai, giấu lỗi, không ai đề xuất ý tưởng, chỉ vài người phát biểu, dám thử, học từ thất bại, nêu rủi ro sớm, bàn riêng sau họp]
levels: [TEAM, ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-13, TOP-MEGROW-07, TOP-MEGROW-16]
problems_addressed: []
related_ids: [FW-080, FW-078, FW-079, FW-081, FW-082, CON-029, CON-027, CON-028, FW-070, FW-053]
source: ["MEGROW | Topic 13 | Topic 13 - Building Trust & Open Communication in Teams - Justin Xavier.pdf | Slide 6–27", "MEGROW | Topic 07 | Topic 7 - Building Team Capability and Growth - Thao Luong.pdf | Slide 10–11, 33", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 28–33"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Văn hóa thử nghiệm và an toàn tâm lý

## Cách người dùng thường mô tả
Ưu tiên **Thấp** theo CLAUDE.md §2. "Hỏi có ai ý kiến gì không thì cả phòng im." · "Họp xong mới có người nhắn riêng nói là không ổn." · "Không ai đề xuất thử cái gì mới." · "Lỗi chỉ lộ ra lúc sát hạn." · "Chỉ Senior với mình nói, mấy bạn còn lại ngồi nghe."

## Triệu chứng quan sát được
- Thảo luận bị một hoặc hai người chi phối; thành viên mới gần như không đóng góp.
- Các lo ngại được bàn **riêng sau họp** thay vì nêu công khai.
- Tin xấu đi chậm: thí nghiệm thất bại, rủi ro kỹ thuật hoặc trượt tiến độ chỉ được báo khi không giấu được nữa.
- Không ai xin giúp đỡ; không ai nói "cách này không chạy, mình nên dừng".
- Nhìn từ ngoài team vẫn bận rộn và không ai phàn nàn — đặc trưng của **Anxiety Zone** (`FW-080`).

## Câu hỏi chẩn đoán
1. Ba tháng qua, đã có ai nêu một rủi ro mà sau đó **không** xảy ra chưa? Nếu chưa, nhiều khả năng không ai dám nêu rủi ro.
2. Lần gần nhất có người phản biện quyết định của tôi trong họp là khi nào?
3. Khi một lỗi lọt lên production, câu hỏi đầu tiên của tôi là *"ai làm"* hay *"quy trình nào lẽ ra phải bắt được"*?
4. Trong ba lần gần nhất tôi xin ý kiến trước khi quyết, tôi hỏi ai? (`FW-081` — Check the Mirror)
5. Team đang ở vùng nào trong bốn vùng của Edmondson, và bằng chứng hành vi nào?
6. Tôi có đang nhầm **trust** (quan hệ đôi một) với **psychological safety** (chuẩn mực nhóm) không?

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Tiêu chuẩn cao nhưng an toàn tâm lý thấp | Team bận rộn, không ai đề xuất gì mới — Anxiety Zone | `FW-080` |
| Hành vi lãnh đạo chưa nhất quán | Nói mời góp ý nhưng phản ứng khi được góp ý | `FW-078`, `CON-027` |
| Một thành phần niềm tin cụ thể đang yếu | Tin chuyên môn nhưng không dám thành thật | `FW-079` |
| Sai lầm bị xử lý như lỗi cá nhân | Không ai báo lỗi sớm | `FW-078` (chữ S), `CON-029` |
| Câu mời phát biểu quá chung chung | *"Có ai ý kiến gì không?"* rồi im lặng | `FW-080`, `FW-082` |
| Luôn hỏi cùng một nhóm nhỏ quen thuộc | Người ngoài nhóm đó ngừng cố gắng góp ý | `FW-081` |
| Chuẩn mực nhóm chưa được đặt ra | Không ai biết nêu rủi ro có được hoan nghênh không | `FW-081`, `FW-066-01` |
| Khoảng cách quyền lực theo văn hóa | Voice Constraints là điểm **hội tụ** qua các thế hệ VN | `CON-028` |
| Rào cản cấu trúc chứ không phải thái độ | KPI xung đột, quyền sở hữu không rõ | `FW-070` |
| Không có cơ chế thử nhỏ, rủi ro thấp | Mọi ý tưởng mới đều là canh bạc lớn | `FW-053`, `FW-053-01` |

Diễn giải bảng: bốn dòng đầu là lỗi **hành vi của người quản lý**; bốn dòng giữa là lỗi **thiết kế chuẩn mực và cấu trúc buổi họp**; hai dòng cuối nằm ngoài tầm hành vi cá nhân — chúng cần đổi KPI, đổi quyền sở hữu, hoặc tạo cơ chế thử nghiệm có chi phí thấp. Thứ tự này cũng là thứ tự nên kiểm: hành vi của chính mình trước, vì đó là thứ đổi được ngay.

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Im lặng xuất hiện ở **mọi** team trong khối, không riêng team bạn → vấn đề ở cấp tổ chức, không ở cấp quản lý trực tiếp.
- Nguyên nhân là KPI xung đột giữa các bộ phận → `FW-070`, và phải đi lên cấp đặt KPI.
- Một cá nhân cụ thể làm người khác không dám nói → đây là vấn đề hành vi cần xử lý riêng bằng `FW-025`, không phải vấn đề văn hóa chung.
- Team vừa trải qua một đợt cắt giảm hoặc một quyết định gây mất niềm tin → không framework nào rút ngắn được thời gian; `CON-027` nhấn niềm tin là quá trình phụ thuộc lịch sử.

## Chỉ số theo dõi sau xử lý
- **Tốc độ tin xấu:** khoảng cách giữa lúc một rủi ro được nhận ra và lúc nó được nói ra trong họp.
- **Độ phủ tiếng nói:** trong một buổi họp, bao nhiêu người phát biểu ít nhất một lần — đếm **ai**, không chỉ đếm **bao nhiêu**.
- Số lần có người nói "mình sai" hoặc "cách này không chạy" mà không bị hệ quả tiêu cực.
- Số thí nghiệm nhỏ được chạy và được dừng sớm (`FW-053`).
- Tỷ lệ lo ngại được nêu trong họp so với nêu riêng sau họp.

## Nguồn
- `[MEGROW | Topic 13 | Topic 13 - Building Trust & Open Communication in Teams - Justin Xavier.pdf | Slide 6–27]` — nguồn chính.
- `[MEGROW | Topic 07 | Topic 7 - Building Team Capability and Growth - Thao Luong.pdf | Slide 10–11, 33]` — bộ luật chơi và rào cản "lack of trust or psychological safety".
- `[MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 28–33]` — thử nghiệm 7 ngày như cơ chế hạ rủi ro của việc thử.

=====

---
id: PRB-010
type: problem
title_vi: Xung đột trong team hoặc giữa các team
title_en: Conflict within or between teams
aliases: [xung đột, bất đồng, mâu thuẫn giữa bộ phận]
keywords: [xung đột, conflict, bất đồng, cãi nhau trong họp, hai bộ phận không thống nhất, căng thẳng, tranh luận không đi tới đâu, mâu thuẫn ưu tiên]
levels: [TEAM, ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-12, TOP-MEGROW-14, TOP-MEGROW-08, TOP-MEGROW-16, TOP-MEGROW-11, TOP-MEGROW-13]
problems_addressed: []
related_ids: [FW-016, FW-020, FW-021, FW-026, CON-009, CON-010, FW-015, FW-051, FW-052, FW-072, FW-076, FW-080, FW-081]
source: ["MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 31–33", "MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 4–13", "MEGROW | Topic 08 | Topic 8 - Correcting Behaviour Through Coaching - Thao Luong.pdf | Slide 8–10, 38", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 17–21"]
source_type: course
confidence: medium
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Xung đột trong team hoặc giữa các team

Mức ưu tiên: **Thấp** (vấn đề số 10 trong `problem_index.md`). CLAUDE.md §2 quy định tạo `PRB` cho mức Thấp khi khóa học có nội dung liên quan — Topic 12 và 14 đều có.

> `[SUY LUẬN]` Chunk này nay phủ sáu topic: **xung đột giữa các bộ phận và trong ra quyết định** (Topic 12, 14, 16) · **xung đột về hành vi cá nhân trong team** (Topic 08) · **khác biệt phong cách làm việc** (Topic 11) · **an toàn tâm lý để dám nêu bất đồng** (Topic 13).

## Cách người dùng thường mô tả
"Hai bên cãi mãi không đi tới đâu." · "Em với bạn ấy không thống nhất được cách tiếp cận." · "Bộ phận kia lúc nào cũng chặn." · "Cả hai đều có lý mà vẫn không ra quyết định."

## Triệu chứng quan sát được
- Cùng một từ được hai bên dùng với hai nghĩa khác nhau.
- Tranh luận lặp lại ở cùng một chỗ qua nhiều cuộc họp.
- Một bên im lặng rút lui thay vì nêu phản đối.
- Quyết định được đưa ra rồi lại bị mở lại.

## Câu hỏi chẩn đoán
1. Hai bên đang ở nấc nào của thang suy luận — đang cãi ở kết luận hay đang so dữ liệu? (`FW-020`)
2. Mỗi bên đang **chọn tập dữ liệu nào**? (`FW-020`)
3. Tôi đã thực sự hỏi về ý định, nguồn lực và tình thế của họ chưa? (`FW-021`)
4. Vấn đề thật sự là gì; cái gì thương lượng được, cái gì không? (`FW-016`)
5. Chế độ ứng xử nào phù hợp với tình huống này, và tôi đang mặc định rơi vào chế độ nào? (`FW-016`)
6. Đây là bất đồng về nội dung hay về **ai được quyền chốt**? (`CON-009`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Hai bên đứng trên hai tập dữ liệu khác nhau | Kết luận đối nghịch, ai cũng thấy mình đúng | `FW-020` |
| Cãi ở nấc kết luận, không ai tụt thang | Tranh luận lặp lại không tiến triển | `FW-020` |
| Advocacy trước Inquiry | Chuẩn bị câu phản bác trong lúc người kia còn nói | `FW-021` |
| Phản ứng theo phản xạ, không chọn chế độ | Luôn né tránh, hoặc luôn thỏa hiệp | `FW-016` |
| Chưa tách được cái thương lượng được và không được | Nhượng bộ ở đúng chỗ không nên nhượng | `FW-016` |
| Mức tham gia vào quyết định không được nói rõ | Người ta tưởng mình cùng quyết rồi thấy không phải | `CON-009`, `FW-006` |
| Không tìm vùng giá trị chung | Cuộc trao đổi thành cuộc mặc cả thắng–thua | `FW-015` |
| Xung đột thật ra là khác góc nhìn chưa được làm lộ | Hai bên tranh luận về giải pháp trước khi thống nhất vấn đề | `FW-051`, `FW-052` |
| Khác biệt phong cách làm việc bị đọc thành khác biệt thái độ | "Người kia khó tính", "người kia hấp tấp" | `FW-072`, `FW-076` |
| Ma sát giao tiếp không được nêu sớm | Để tới khi thành xung đột mới xử lý | `FW-081` (Address Misalignment) |
| Thiếu an toàn tâm lý nên bất đồng chuyển ra sau hậu trường | Đồng ý trong họp, phản đối sau họp | `FW-080` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Xung đột mang tính cá nhân, chạm tới hành vi chứ không tới nội dung công việc → `FW-026` để quyết có xử lý không, rồi `FW-025` và `CON-010`.
- Một bên không dám nêu bất đồng → vấn đề an toàn tâm lý, chuyển sang `PRB-009` và `FW-080`.
- Xung đột bắt nguồn từ việc hai bộ phận bị đo bằng những chỉ số mâu thuẫn nhau → vấn đề thiết kế tổ chức, không giải được bằng kỹ năng hội thoại.

## Chỉ số theo dõi sau xử lý
- Số lần cùng một tranh luận quay lại qua các cuộc họp (kỳ vọng: giảm).
- Tỷ lệ quyết định bị mở lại sau khi đã chốt (kỳ vọng: giảm).
- Trong các cuộc họp liên bộ phận: có ai đặt câu hỏi làm rõ dữ liệu trước khi phản bác không.
- Mức tham gia được nói rõ ngay đầu buổi họp quyết định (kỳ vọng: luôn có).

## Nguồn
- `[MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 31–33]`
- `[MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 4–13]`

=====

---
id: PRB-011
type: problem
title_vi: Dẫn dắt thay đổi
title_en: Leading change
aliases: [dẫn dắt thay đổi, change management, đổi cách làm việc]
keywords: [thay đổi, change, chuyển đổi, transformation, thói quen mới, đổi quy trình, thông báo rồi không ai theo, cách làm mới không dính, dẫn dắt thay đổi]
levels: [ORG, TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-06, TOP-MEGROW-12, TOP-MEGROW-05, TOP-MEGROW-18, TOP-MEGROW-13]
problems_addressed: []
related_ids: [FW-064, FW-007, FW-008, FW-009, FW-017, FW-012, CON-006, FW-090, FW-093, FW-094, CON-030, FW-053, FW-080, CON-028, CON-031]
source: ["MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 12–45", "MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 34–37", "MEGROW | Topic 05 | Topic 5 - Optimise Personal Productivity - Agnis Stibe.pdf | Slide 64–68, 73–74", "MEGROW | Topic 18 | Topic 18 - Leading in the AI-Enabled Organisation - Prof Trung Nguyen.pdf | Slide 9–10, 16, 26–29"]
source_type: course
confidence: medium
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Dẫn dắt thay đổi

Mức ưu tiên: **Thấp** (vấn đề số 11 trong `problem_index.md`). CLAUDE.md §2 quy định tạo `PRB` cho mức Thấp khi khóa học có nội dung liên quan — Topic 06 có.

> `[SUY LUẬN]` Chunk này phủ năm góc nhìn: **cơ chế biết → làm** (Topic 05), **thiết kế thay đổi hành vi** (Topic 06), **liên minh các bên liên quan** (Topic 12), **điều kiện để thay đổi dính** (Topic 13), và **thay đổi do AI mang tới** (Topic 18). `confidence: medium` vì ba framework nền `FW-007`, `FW-008`, `FW-009` đều lấy từ deck Topic 06 gần như không có chữ — xem `open_questions.md` (OQ-008).

## Cách người dùng thường mô tả
"Đã thông báo cách làm mới rồi mà không ai theo." · "Được vài tuần rồi đâu lại vào đấy." · "Mọi người gật đầu trong họp nhưng không đổi hành vi."

## Triệu chứng quan sát được
- Thay đổi được công bố một lần rồi không ai nhắc lại.
- Chỉ những người vốn đã đồng tình mới làm theo.
- Hành vi cũ quay lại ngay khi áp lực tăng.
- Không có cách nào đo được hành vi mới đang xảy ra bao nhiêu.

## Câu hỏi chẩn đoán
1. Khoảng trống nằm ở trạm nào — Knowledge, Acceptance, Intention hay Behavior? (`FW-064`) **Hỏi câu này trước mọi câu khác.**
2. Tôi đang cố đổi **thái độ** hay đang đổi **môi trường**? (`FW-007` — Triangle, Curve)
3. Hành vi này hôm nay đo bằng gì? (`FW-007` — Metric)
4. Team đang ở giai đoạn nào: Self-contained, Social Pull, Identity Change hay Influencing Others? (`FW-007` — Circles)
5. Đòn bẩy xã hội nào đang bỏ trống? (`FW-008`)
6. Ai là Champions, Influencers, Decision Makers, Blockers, Undecided? (`FW-017`)
7. Nếu cách này hiệu quả quá mức, điều tệ nhất có thể xảy ra là gì? (`FW-007` — Ethics)
8. Có ai thấy đủ an toàn để nói rằng thay đổi này đang không chạy không? (`FW-080`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| **Khoảng trống nằm ở ACCEPTANCE, không ở KNOWLEDGE** | Đã giải thích kỹ, ai cũng hiểu, vẫn không ai làm | `FW-064` |
| Khoảng trống nằm giữa INTENTION và BEHAVIOR | Ai cũng định làm, không ai bắt đầu | `FW-064`, `FW-053` |
| Chỉ tác động vào thái độ, không thiết kế môi trường | Thông báo xong, không gì đổi | `FW-007` — Triangle, Curve |
| Không đo hành vi hiện tại | Không biết có tiến triển hay không | `FW-007` — Metric |
| Không dùng ảnh hưởng xã hội | Thay đổi phụ thuộc hoàn toàn vào chỉ đạo từ trên | `FW-008` |
| Can thiệp không được điều tiết theo thời gian | Mạnh lúc đầu rồi tắt | `FW-007` — Moderation |
| Không nghĩ trước hệ quả ngoài ý muốn | Phản tác dụng, gây mất lòng tin | `FW-007` — Ethics |
| Người thực thi không thấy mình sở hữu thay đổi | Làm cho có | `FW-009` |
| Thay đổi làm tăng tải nhận thức | Team bỏ qua vì quá tải | `CON-006` |
| Không có liên minh đủ ảnh hưởng ngoài team | Duyệt trên giấy, không bộ phận nào làm | `FW-017` |
| Dồn sức thuyết phục Blockers, bỏ quên nhóm Undecided | Tốn công vào nhóm khó chuyển nhất | `FW-017` |
| Không ai dám nói thay đổi này đang không chạy | Làm cho có, vấn đề lộ ra quá muộn | `FW-080`, `PRB-009` |
| Thay đổi do AI mang tới nhưng chỉ triển khai công cụ, không thiết kế lại công việc | Năng suất cá nhân tăng, kết quả tổ chức không đổi | `FW-090`, `CON-030` |
| AI tự động hóa mất thao trường đào tạo mà không ai thiết kế lại lộ trình phát triển | Người mới ship nhanh nhưng không lớn lên | `FW-093` |
| Quyền cho AI trượt dần thay vì được quyết | Hệ thống chạy ở mức tự chủ không ai cho phép | `FW-094`, `CON-030` |
| Áp một nhịp thay đổi cho nhóm có rào cản văn hóa về việc lên tiếng | Im lặng bị đọc là đồng thuận | `CON-028` |

Diễn giải bảng: hai dòng đầu là **chẩn đoán gốc** và phải chạy trước — `FW-064` chỉ ra khoảng trống nằm ở trạm nào, vì can thiệp sai trạm thì mọi nỗ lực sau đó đều trượt. Chín dòng giữa là **thiết kế thay đổi** ở cấp hành vi và liên minh. Năm dòng cuối là các dạng thất bại **đặc thù của thay đổi do AI mang tới**: chúng khác ở chỗ thay đổi đến từ bên ngoài chứ không do bạn khởi xướng, nên việc của bạn là thiết kế lại cách làm việc quanh nó chứ không phải thuyết phục ai.

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Thay đổi cần đồng thuận nhiều phòng ban → dùng `FW-017` Stakeholder Coalition Map và toàn bộ chuỗi `FW-022`.
- Lực cản đến từ việc thay đổi mâu thuẫn với chỉ số mà bộ phận khác đang bị đo → vấn đề tổ chức, không giải được bằng thiết kế hành vi.
- Thay đổi đến từ quy định pháp lý chứ không từ lựa chọn nội bộ → `CON-031`; phạm vi của bạn là phân loại ca sử dụng và leo thang, không phải thuyết phục.
- Không ai phản đối nhưng cũng không ai làm, và team chưa từng nêu một rủi ro nào → vấn đề thật là `PRB-009`, xử lý an toàn tâm lý trước.

## Chỉ số theo dõi sau xử lý
- Chỉ số hành vi đã chọn ở bước Metric (ví dụ: tỷ lệ PR qua review chéo).
- Tỷ lệ người áp dụng, tách theo nhóm chứ không chỉ con số tổng.
- Mức duy trì sau 4 tuần và sau 12 tuần (kỳ vọng: không tụt).
- Số hệ quả ngoài ý muốn đã ghi nhận được từ lưới Ethics.
- `[SUY LUẬN]` Với thay đổi liên quan tới AI: tỷ lệ đầu việc đã được gán một mức quyền rõ ràng theo `FW-094`, và số lần có người nêu rằng cách làm mới đang không hiệu quả.

## Nguồn
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 12–45]`
- `[MEGROW | Topic 05 | Topic 5 - Optimise Personal Productivity - Agnis Stibe.pdf | Slide 64–68, 73–74]` — Knowledge–Behaviour Gap.
- `[MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 34–37]`
- `[MEGROW | Topic 18 | Topic 18 - Leading in the AI-Enabled Organisation - Prof Trung Nguyen.pdf | Slide 9–10, 16, 26–29]`
