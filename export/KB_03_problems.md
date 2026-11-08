# Vấn đề (PRB)

Bản gộp tự động bởi `scripts/export.py`. Mỗi chunk giữ nguyên frontmatter, ngăn cách bằng `=====`. Chunk `deprecated` đã bị loại.

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
topics: [TOP-MEGROW-06, TOP-MEGROW-10]
problems_addressed: []
related_ids: [FW-006, FW-010, CON-003, CON-005, CON-006]
source: ["MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 64–65", "MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 35–37"]
source_type: course
confidence: medium
status: needs_review
replaced_by:
last_updated: 2026-11-08
---

# Thiết kế framework làm việc và giải quyết vấn đề cho team

Mức ưu tiên: **Cao** (vấn đề số 3 trong `problem_index.md`).

> `[SUY LUẬN]` Chunk này mới phủ phần **ra quyết định và quyền sở hữu** từ Topic 06 và 10. Phần **đo lường, nhịp review và hệ thống giao hàng** nằm ở Topic 02, phần **quy trình giải quyết vấn đề** nằm ở Topic 16 — cả hai chưa xử lý. Vì vậy `status: needs_review`.

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

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Vấn đề nằm ở mục tiêu và cách đo chứ không ở quy trình → thuộc vấn đề số 1. `[SUY LUẬN]` Topic 02 phụ trách, chưa xử lý.
- Phụ thuộc chéo nằm ngoài quyền hạn của bạn → cần công cụ về stakeholder. `[SUY LUẬN]` Topic 12 phụ trách, chưa xử lý.

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
topics: [TOP-MEGROW-01, TOP-MEGROW-06, TOP-MEGROW-10]
problems_addressed: []
related_ids: [FW-002, FW-003, FW-004, FW-001, FW-005, CON-001, CON-002]
source: ["MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 4–13, 20–24", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2"]
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

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Bạn đã thử buông nhưng chất lượng tụt rõ rệt → vấn đề là năng lực team, chuyển sang `PRB-005`.
- Nguyên nhân nằm ở nguồn lực hoặc ưu tiên mâu thuẫn từ trên xuống → đó là vấn đề tổ chức, không phải chuyển dịch cá nhân.
- Quá tải kéo dài kèm dấu hiệu kiệt sức → cần can thiệp về khối lượng công việc, không phải thêm framework. `[SUY LUẬN]` Topic 05 có nội dung về burnout, sẽ bổ sung liên kết khi xử lý topic đó.

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
topics: [TOP-MEGROW-01, TOP-MEGROW-06, TOP-MEGROW-10]
problems_addressed: []
related_ids: [FW-001, FW-001-01, FW-001-02, FW-005, FW-006, FW-009, FW-010, CON-002, CON-003, CON-004, CON-005, CON-006]
source: ["MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 15–19", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 59–61, 64–65", "MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 24–36"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Giao việc và phát triển theo năng lực từng người

Mức ưu tiên: **Cao** (vấn đề số 5 trong `problem_index.md`).

## Cách người dùng thường mô tả
"Giao rồi mà vẫn phải làm lại." · "Người giỏi nhất đang gánh hết." · "Không biết giao đến đâu thì vừa với bạn này." · "Senior thì mình để tự do, nhưng collaborator thì phải nói tới đâu?" · "Giao việc rồi mà bạn ấy vẫn hỏi từng bước."

## Triệu chứng quan sát được
- Cùng một mức hướng dẫn được áp cho cả Senior lẫn collaborator.
- Một hoặc hai người nhận hết việc quan trọng, người còn lại nhận việc phụ.
- Việc đã giao vẫn quay lại bàn bạn để quyết.
- Người nhận làm đúng yêu cầu nhưng không bao giờ đề xuất cải tiến.
- `[KHÓA HỌC]` Thách thức 2 và 4 của Topic 06: giao trách nhiệm mà không giao quyền quyết định; người giỏi nhận việc then chốt tới mức quá tải.

## Câu hỏi chẩn đoán
1. Cho **việc cụ thể này**, người này đang ở đâu trên trục năng lực và trục cam kết? (`FW-001`)
2. Tôi có bằng chứng gì cho hai trục đó, hay đang dùng thâm niên thay cho năng lực? (`FW-001-01`)
3. Tôi đã nói rõ cả bốn thành phần — kết quả mong đợi, quyền sở hữu, quyền quyết định, tiêu chí thành công — chưa? (`CON-004`)
4. Ai là chủ sở hữu duy nhất chịu trách nhiệm cho kết quả này? (`CON-003`)
5. Năm thành tố sở hữu tâm lý, người này đang thiếu cái nào? (`FW-009`)
6. Tôi đang tối ưu giao hàng hôm nay bằng cái giá là năng lực ngày mai không? (`CON-004`)

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
| Nhầm giữa "giao việc" và "cho tham gia quyết định" | Họp nhiều mà vẫn không ai sở hữu | `FW-006` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Chẩn đoán ra năng lực đủ nhưng kết quả vẫn hỏng → nguyên nhân ở hệ thống (quy trình, dữ liệu, phụ thuộc chéo), xem `CON-006`.
- Vấn đề là hành vi chứ không phải năng lực → thuộc nhóm hội thoại sửa hành vi. `[SUY LUẬN]` Topic 08 phụ trách nội dung này, sẽ liên kết khi xử lý.
- `[SUY LUẬN]` **Khoảng trống:** MEGROW không có nội dung riêng về giao việc cho cộng tác viên — nhân sự không chính thức, không cùng lộ trình nghề nghiệp. Mọi framework liệt kê trong bảng nguyên nhân gốc rễ đều giả định nhân viên chính thức. Xem `open_questions.md` (OQ-005).

## Chỉ số theo dõi sau xử lý
- Số quyết định phải quay về bạn mỗi tuần (kỳ vọng: giảm).
- Phân bố việc then chốt giữa các thành viên (kỳ vọng: bớt tập trung vào một người).
- Số việc giao kèm đủ bốn thành phần của `CON-004` (kỳ vọng: tiến tới 100%).
- Số đề xuất cải tiến do người nhận việc tự nêu (kỳ vọng: tăng — chỉ dấu của `FW-009`).
- Tỷ lệ việc giao ra phải làm lại (kỳ vọng: giảm).

## Nguồn
- `[MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 15–19]`
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 59–61, 64–65]`
- `[MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 24–36]`

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
topics: [TOP-MEGROW-06]
problems_addressed: []
related_ids: [FW-008, FW-009, FW-007, CON-005]
source: ["MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 33–39, 59, 65"]
source_type: course
confidence: medium
status: needs_review
replaced_by:
last_updated: 2026-11-08
---

# Động lực, gắn kết và giữ người

Mức ưu tiên: **Trung bình** (vấn đề số 7 trong `problem_index.md`).

> `[SUY LUẬN]` Chunk này mới phủ góc nhìn **đòn bẩy xã hội và sở hữu tâm lý** từ Topic 06. Các lý thuyết động lực cá nhân (McClelland, Alderfer ERG) nằm ở Topic 11, chiến lược phát triển cá nhân nằm ở Topic 09 — chưa xử lý. `status: needs_review`.

## Cách người dùng thường mô tả
"Bạn ấy làm đủ việc nhưng mất lửa." · "Team im lặng trong họp." · "Collaborator không gắn bó, hết hợp đồng là đi." · "Không ai đề xuất gì mới nữa."

## Triệu chứng quan sát được
- Làm đúng yêu cầu, không hơn; không còn đề xuất cải tiến.
- Mức tham gia trong thảo luận kỹ thuật giảm.
- Thực hành tốt của một người không lan sang người khác.
- Người giỏi bắt đầu hỏi về cơ hội ở nơi khác.

## Câu hỏi chẩn đoán
1. Trong năm thành tố sở hữu tâm lý, người này đang thiếu cái nào? (`FW-009`)
2. Hành vi tốt ở team có đang được **nhìn thấy** không, hay chỉ mình tôi biết? (`FW-008`)
3. Cái gì đang làm cho hành vi tốt khó xảy ra hơn mức cần thiết? (`FW-008` — Facilitation)
4. Người này có thấy việc mình làm là một phần con người nghề nghiệp của họ không? (`FW-009` — identity)
5. Tôi có đang kiểm soát tới mức thu lại quyền sở hữu vừa trao không? (`CON-005`)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Sở hữu tâm lý chưa hình thành | Thi hành chứ không sở hữu | `FW-009` |
| Đóng góp tốt không được nhìn thấy | Nỗ lực thêm không có hồi đáp | `FW-008` — Recognition |
| Không có chỗ để học và quan sát lẫn nhau | Mỗi người một ốc đảo | `FW-008` — Learning, Cooperation |
| Chuẩn mực nhóm không rõ | "Ở đây mọi người làm thế nào" không ai biết | `FW-008` — Norms |
| Ma sát khiến hành vi tốt khó xảy ra | Thiếu template, môi trường, công cụ | `FW-008` — Facilitation |
| Kiểm soát quá mức làm hỏng self-efficacy | Người nhận mất tự tin quyết định | `CON-005`, `FW-009` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Nguyên nhân là lương thưởng hoặc lộ trình thăng tiến → nằm ngoài phạm vi framework trong MEGROW, cần làm việc với cấp trên và HR.
- Mức gắn kết thấp kèm thiếu an toàn tâm lý → **không** dùng Comparison và Competition của `FW-008`, sẽ làm tệ thêm. `[SUY LUẬN]` Topic 13 phụ trách an toàn tâm lý, chưa xử lý.
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
id: PRB-011
type: problem
title_vi: Dẫn dắt thay đổi
title_en: Leading change
aliases: [dẫn dắt thay đổi, change management, đổi cách làm việc]
keywords: [thay đổi, change, chuyển đổi, transformation, thói quen mới, đổi quy trình, thông báo rồi không ai theo, cách làm mới không dính, dẫn dắt thay đổi]
levels: [ORG, TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-06]
problems_addressed: []
related_ids: [FW-007, FW-008, FW-009, CON-006]
source: ["MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 12–45"]
source_type: course
confidence: medium
status: needs_review
replaced_by:
last_updated: 2026-11-08
---

# Dẫn dắt thay đổi

Mức ưu tiên: **Thấp** (vấn đề số 11 trong `problem_index.md`). CLAUDE.md §2 quy định tạo `PRB` cho mức Thấp khi khóa học có nội dung liên quan — Topic 06 có.

> `[SUY LUẬN]` Chunk này mới phủ góc nhìn **thiết kế thay đổi hành vi** của Topic 06. Góc nhìn **liên minh các bên liên quan** (Kotter) nằm ở Topic 12 và góc nhìn **AI-era change** nằm ở Topic 18 — chưa xử lý. `status: needs_review`.

## Cách người dùng thường mô tả
"Đã thông báo cách làm mới rồi mà không ai theo." · "Được vài tuần rồi đâu lại vào đấy." · "Mọi người gật đầu trong họp nhưng không đổi hành vi."

## Triệu chứng quan sát được
- Thay đổi được công bố một lần rồi không ai nhắc lại.
- Chỉ những người vốn đã đồng tình mới làm theo.
- Hành vi cũ quay lại ngay khi áp lực tăng.
- Không có cách nào đo được hành vi mới đang xảy ra bao nhiêu.

## Câu hỏi chẩn đoán
1. Tôi đang cố đổi **thái độ** hay đang đổi **môi trường**? (`FW-007` — Triangle, Curve)
2. Hành vi này hôm nay đo bằng gì? (`FW-007` — Metric)
3. Team đang ở giai đoạn nào: Self-contained, Social Influencing, Identity Change hay Self-driven? (`FW-007` — Circles)
4. Đòn bẩy xã hội nào đang bỏ trống? (`FW-008`)
5. Nếu cách này hiệu quả quá mức, điều tệ nhất có thể xảy ra là gì? (`FW-007` — Ethics)

## Nguyên nhân gốc rễ và framework tương ứng

| Nguyên nhân gốc rễ | Biểu hiện | Framework |
|---|---|---|
| Chỉ tác động vào thái độ, không thiết kế môi trường | Thông báo xong, không gì đổi | `FW-007` — Triangle, Curve |
| Không đo hành vi hiện tại | Không biết có tiến triển hay không | `FW-007` — Metric |
| Không dùng ảnh hưởng xã hội | Thay đổi phụ thuộc hoàn toàn vào chỉ đạo từ trên | `FW-008` |
| Can thiệp không được điều tiết theo thời gian | Mạnh lúc đầu rồi tắt | `FW-007` — Moderation |
| Không nghĩ trước hệ quả ngoài ý muốn | Phản tác dụng, gây mất lòng tin | `FW-007` — Ethics |
| Người thực thi không thấy mình sở hữu thay đổi | Làm cho có | `FW-009` |
| Thay đổi làm tăng tải nhận thức | Team bỏ qua vì quá tải | `CON-006` |

## Dấu hiệu cần leo thang hoặc can thiệp khác
- Thay đổi cần sự đồng thuận của nhiều phòng ban → cần công cụ liên minh các bên. `[SUY LUẬN]` Topic 12 phụ trách, chưa xử lý.
- Lực cản đến từ việc thay đổi mâu thuẫn với chỉ số mà bộ phận khác đang bị đo → vấn đề tổ chức, không giải được bằng thiết kế hành vi.

## Chỉ số theo dõi sau xử lý
- Chỉ số hành vi đã chọn ở bước Metric (ví dụ: tỷ lệ PR qua review chéo).
- Tỷ lệ người áp dụng, tách theo nhóm chứ không chỉ con số tổng.
- Mức duy trì sau 4 tuần và sau 12 tuần (kỳ vọng: không tụt).
- Số hệ quả ngoài ý muốn đã ghi nhận được từ lưới Ethics.

## Nguồn
- `[MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 12–45]`
