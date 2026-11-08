# Playbook (PB)

Bản gộp tự động bởi `scripts/export.py`. Mỗi chunk giữ nguyên frontmatter, ngăn cách bằng `=====`. Chunk `deprecated` đã bị loại.

=====

---
id: PB-001
type: playbook
title_vi: Chốt ưu tiên của team cho một quý
title_en: Setting the Team's Priorities for a Quarter
aliases: [lập kế hoạch quý, chốt ưu tiên, quarterly planning, chọn bài toán]
keywords: [đầu quý làm gì, chọn bài toán nào, quá nhiều yêu cầu, không biết ưu tiên, OKR quý, từ chối việc, team bận mà không có kết quả, kế hoạch quý]
levels: [TEAM, ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-02, TOP-MEGROW-17, TOP-MEGROW-15, TOP-MEGROW-16]
problems_addressed: [PRB-001]
related_ids: [PRB-001, CON-019, FW-034, FW-044, FW-047, FW-084, FW-052, FW-037, FW-038, FW-039, FW-048, FW-054]
source: ["MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 6–33", "MEGROW | Topic 17 | Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf | Slide 8–35", "MEGROW | Topic 15 | Topic 15 - From Stakeholder Insight to Market Impact - Dr Phuong Nguyen.pdf | Slide 8–20", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 19–22"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Chốt ưu tiên của team cho một quý

## Dùng khi nào
Hai tuần trước khi quý mới bắt đầu; khi danh sách yêu cầu đã dài hơn năng lực của team; khi cấp trên hỏi "quý này team em làm gì" mà bạn chưa có câu trả lời một dòng. Playbook này chạy trong khoảng **3–4 giờ làm việc chia làm hai buổi** — một buổi chuẩn bị một mình, một buổi với team.

## Checklist

**Buổi 1 — chuẩn bị một mình (90 phút)**

1. **Dựng đường ngắm.** Viết ra chuỗi: mục tiêu VNG → định hướng Zalo → mục tiêu khối → mục tiêu team → quyết định tuần này. Chỗ nào bạn không điền được là chỗ bạn chưa biết. Đi hỏi trước khi làm tiếp. (`CON-019`, `FW-034`)
2. **Quét ngoài 20 phút.** Ghi **ba** thay đổi bên ngoài có thể ảnh hưởng mảng của bạn trong 2–3 năm tới, mỗi cái kèm một dòng "so what cho team tôi". Ba, không nhiều hơn. (`FW-044`)
3. **Liệt kê bài toán ứng viên.** Gom mọi thứ đang được kỳ vọng: từ cấp trên, từ stakeholder, từ chính team, từ nợ kỹ thuật. Chưa sàng, chỉ gom.
4. **Sàng vòng một bằng hai câu hỏi.** Với mỗi bài toán: *việc này nới rộng hay thu hẹp hào của team?* (`FW-047`) và *nó nằm ở chỗ giá trị đang bị phá vỡ, hay chỗ dễ nhìn thấy nhất?* (`FW-084`). Bỏ những cái trượt cả hai.
5. **Đóng khung 3–5 bài toán còn lại.** Mỗi cái viết theo mẫu: *"[Ai] cần [gì], bởi vì [lý do], dẫn tới [hệ quả], bằng chứng là [số liệu]."* Nếu không điền được ô bằng chứng thì đó là **giả định**, không phải bài toán — đánh dấu để kiểm trước. (`FW-052`)

**Buổi 2 — với team (90 phút)**

6. **Trình bày đường ngắm trước, bài toán sau.** Đừng mở đầu bằng danh sách việc.
7. **Với mỗi bài toán, viết objective.** Dùng mẫu outcome khi đã biết đường đi, mẫu learning khi còn bất định — **đừng cam kết một con số cho việc chưa ai làm bao giờ**. (`FW-037`)
8. **Chọn chỉ số rồi phá thử nó.** Mỗi objective: một outcome, một driver (tín hiệu sớm), một guardrail (thứ không được xấu đi). Rồi hỏi bốn câu phá thử: ai có thể gaming nó? nó có đổi quyết định nào không? dữ liệu ai sở hữu? nếu chỉ số này đẹp mà kết quả vẫn tệ thì sao? (`FW-038`, `FW-039`)
9. **Chốt cái KHÔNG làm — bước quan trọng nhất.** Viết ra danh sách "quý này team không làm" và nói rõ lý do. Một kế hoạch không có danh sách này chưa phải là ưu tiên, chỉ là mong muốn.
10. **Gán chủ sở hữu và nhịp review.** Mỗi objective một người accountable, một mốc giữa quý.

## Kịch bản / câu hỏi mẫu

**Khi hỏi lên để điền đường ngắm:**
> *"Em đang lập kế hoạch quý cho team. Em hiểu ưu tiên của khối quý này là X — em hiểu đúng chưa? Và trong X thì phần nào anh muốn team em chịu trách nhiệm?"*

**Khi từ chối một yêu cầu:**
> *"Việc này mình làm được. Nhưng nhận nó thì [bài toán Y] lùi ba tuần. Anh muốn ưu tiên cái nào?"*
Không nói "không", nói **đánh đổi**. (`FW-048`)

**Khi team đề xuất một bài toán nghe hay nhưng chưa có bằng chứng:**
> *"Mình đang giả định gì ở đây? Nếu giả định đó sai thì cả hướng này sai. Có cách nào kiểm nó trong một tuần không?"* (`FW-053`)

**Khi không tầng nào phía trên có định hướng rõ để nối vào** — hỏi bằng mẫu ba dòng, 45 giây: *"Vấn đề là… · Tụi em đã thử… · Tụi em cần anh…"* (`FW-054`)

## Cách đánh giá hiệu quả
- Hỏi ngẫu nhiên ba người trong team ba ưu tiên của quý — bao nhiêu người trả lời giống nhau? (`CON-019`)
- Số objective có đủ **baseline, target, deadline và guardrail**: mục tiêu là 100%.
- Tồn tại một **danh sách việc không làm** được viết ra và truyền đạt: có hay không.
- Cuối quý, báo cáo nêu được **outcome** hay chỉ liệt kê output? (`CON-015`)
- Số yêu cầu ad-hoc bị từ chối hoặc chuyển thành tự phục vụ (kỳ vọng: tăng so với quý trước).

## Framework nền tảng
`CON-019` đường ngắm · `FW-034` thang chuyển dịch chiến lược · `FW-044` PESTEL · `FW-047` VRIN và hào · `FW-084` bản đồ hành trình stakeholder · `FW-052` mẫu phát biểu vấn đề · `FW-037` mẫu objective · `FW-038` + `FW-039` chỉ số và phá thử KPI · `FW-048` khuyến nghị kèm đánh đổi · `FW-054` lời đề nghị ba dòng · `FW-053` thử nghiệm 7 ngày.

Chẩn đoán đầy đủ khi playbook này không đủ: `PRB-001`.

## Nguồn
- `[MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 6–33]`
- `[MEGROW | Topic 17 | Topic 17 - Apply Strategic Thinking - AP Burkhard Schrage.pdf | Slide 8–35]`
- `[MEGROW | Topic 15 | Topic 15 - From Stakeholder Insight to Market Impact - Dr Phuong Nguyen.pdf | Slide 8–20]`
- `[MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 19–22]`
- `[SUY LUẬN]` Trình tự mười bước và các câu nói mẫu là tổng hợp của Claude từ các framework trên; bản thân trình tự này không có trong một slide nào.

=====

---
id: PB-002
type: playbook
title_vi: Đưa một đề xuất qua được người không thuộc quyền mình
title_en: Getting a Proposal Through Stakeholders You Don't Manage
aliases: [xin duyệt đề xuất, thuyết phục stakeholder, pre-wiring, business case]
keywords: [đề xuất bị bác, xin nguồn lực, thuyết phục không có quyền, họp duyệt, sếp không duyệt, bị chặn, trình bày đề xuất, pre-meet, liên bộ phận]
levels: [ORG]
courses: [MEGROW]
topics: [TOP-MEGROW-12, TOP-MEGROW-19, TOP-MEGROW-03, TOP-MEGROW-14]
problems_addressed: [PRB-002, PRB-008]
related_ids: [PRB-002, FW-011, FW-012, FW-079, FW-058, FW-015, FW-021, CON-007, CON-008, FW-018, FW-019, FW-019-01, FW-054, FW-048]
source: ["MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 7–39", "MEGROW | Topic 19 | Topic 19 - Present Business Case - Dr Tony Nguyen.pdf | Slide 10–26", "MEGROW | Topic 03 | Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf | Slide 26", "MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 11"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Đưa một đề xuất qua được người không thuộc quyền mình

## Dùng khi nào
Bạn cần nguồn lực, dữ liệu, quyền truy cập hoặc một quyết định từ người **không báo cáo cho bạn**; hoặc một đề xuất vừa bị bác và bạn chưa rõ vì sao. Chạy **trước** khi mở PowerPoint — phần lớn công việc nằm ở ngoài phòng họp.

## Checklist

**Giai đoạn 1 — lập bản đồ (45 phút, một mình)**

1. **Liệt kê rộng hơn sơ đồ tổ chức.** Ai tác động tới kết quả, ai bị kết quả tác động? Gồm cả người có quyền **phủ quyết** mà không có quyền duyệt (Legal, Security, một senior có ảnh hưởng). (`FW-011`)
2. **Xếp bốn ô Quyền lực × Mức quan tâm.** Manage Closely · Keep Satisfied · Keep Informed · Monitor. Kiểm lại: bạn đang dành thời gian cho ô nào? Lỗi phổ biến là dồn hết cho người nhiệt tình nhưng không có quyền quyết. (`FW-012`)
3. **Với mỗi người ô "Manage Closely", chấm bốn thành phần niềm tin** từ **góc nhìn của họ**: họ tin chuyên môn mình không (Credibility) · họ cậy được vào mình không (Reliability) · họ dám nói thật với mình không (Intimacy) · họ nghĩ mình đang phục vụ ai (Self-Orientation). **Nếu mẫu số cao, xử lý nó trước — cải thiện ba thành phần kia khi mẫu số còn cao gần như vô ích.** (`FW-079`)

**Giai đoạn 2 — pre-wiring (một tuần trước buổi duyệt)**

4. **Gặp riêng từng người ô Manage Closely.** Mục tiêu của buổi này **không phải thuyết phục** mà là hiểu. Hỏi trước, trình bày sau. (`FW-021`, `CON-007`)
5. **Tìm vế trao đổi.** Không đi xin — tìm chỗ lợi ích giao nhau: họ cần gì mà mình có? (`FW-015`)
6. **Điều chỉnh cách trình bày theo hướng quan hệ.** Lên trên, ngang, xuống dưới cần ba cách khác nhau; và lập luận thuyết phục được bạn chưa chắc thuyết phục được họ. (`FW-058`)
7. **Xử lý mọi phản đối lớn ở đây.** Mục tiêu: **không phản đối lớn nào xuất hiện lần đầu trong phòng họp.**

**Giai đoạn 3 — dựng bài (2 giờ)**

8. **Viết SCQA bốn dòng trước khi mở slide.** Situation (điều họ đã đồng ý) → Complication (điều đe dọa mục tiêu **của họ**) → Question → Answer (đề xuất cụ thể: phạm vi, chi phí, thời gian). (`FW-018`)
9. **Dựng kim tự tháp.** Khuyến nghị ở đỉnh, 3–4 trụ MECE ở giữa, bằng chứng ở đáy. (`FW-019`)
10. **Viết action title cho mỗi slide, rồi chạy phép thử lướt** — đọc riêng các tiêu đề theo thứ tự, chúng có kể được toàn bộ logic không? (`FW-019-01`)
11. **Kết bằng một lời đề nghị cụ thể**, không phải "mong anh chị cho ý kiến".

## Kịch bản / câu hỏi mẫu

**Mở một buổi pre-meet:**
> *"Em đang chuẩn bị đề xuất về X và muốn nghe anh trước khi chốt. Mục tiêu quý này của team anh là gì, và anh lo nhất điều gì nếu mình làm X?"*

**Khi đề xuất của bạn đụng mục tiêu của họ** — đừng tranh cãi với mục tiêu đó, chỉ ra cách đề xuất **bảo vệ** nó: (`CON-008`)
> *"Em hiểu anh cần giữ SLA dưới 200ms. Đề xuất này đặt guardrail đúng ở ngưỡng đó — nếu vượt, pipeline tự rollback."*

**Khi mẫu số Self-Orientation đang cao:**
> *"Việc này em đề xuất vì nó gỡ điểm nghẽn của team anh, không phải vì nó đẹp trong báo cáo của em."*

**Khi hai bên cùng nói "chi phí quá cao" mà ý khác nhau** — tụt xuống nấc dữ liệu: *"Anh đang nhìn con số nào khi nói vậy? Em đang nhìn cái này — mình xem chênh ở đâu."* (`FW-020`)

**Khi cần trợ giúp mà chỉ có 45 giây** — mẫu ba dòng: *"Vấn đề là… · Tụi em đã thử… · Tụi em cần anh…"* (`FW-054`)

## Cách đánh giá hiệu quả
- **Số phản đối lớn xuất hiện lần đầu trong phòng họp: mục tiêu bằng 0.** Đây là chỉ số quan trọng nhất của playbook này.
- Tỷ lệ đề xuất được duyệt ngay lần trình đầu.
- Số buổi pre-meet 1:1 trước mỗi quyết định lớn: phải lớn hơn 0.
- Số lần một người quan trọng xuất hiện ở phút chót rồi chặn (kỳ vọng: giảm về 0).
- Sau buổi họp, người duyệt có nhắc lại được **đúng một câu** bạn muốn họ nhớ không?

## Framework nền tảng
`FW-011` Stakeholder Theory · `FW-012` ma trận Quyền lực–Mức quan tâm · `FW-079` Trust Equation · `FW-058` chiến thuật theo đối tượng · `FW-015` trao đổi giá trị · `FW-021` hỏi trước trình bày sau · `CON-007` pre-wiring · `CON-008` đừng tranh cãi với mục tiêu của họ · `FW-018` SCQA · `FW-019` + `FW-019-01` kim tự tháp và action title · `FW-020` thang suy luận · `FW-054` lời đề nghị ba dòng · `FW-048` khuyến nghị kèm đánh đổi.

Chẩn đoán đầy đủ: `PRB-002`. Khi đối tượng là cấp trên trực tiếp: `PRB-008`.

## Nguồn
- `[MEGROW | Topic 12 | Topic 12 - Stakeholder Influence & Leadership in Technology - Prof Seng Kiat Kok.pdf | Slide 7–39]`
- `[MEGROW | Topic 19 | Topic 19 - Present Business Case - Dr Tony Nguyen.pdf | Slide 10–26]`
- `[MEGROW | Topic 03 | Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf | Slide 26]`
- `[MEGROW | Topic 14 | Topic 14 - Decision Making in Cross-functional Team - Phuong Nguyen.pdf | Slide 11]`
- `[SUY LUẬN]` Trình tự ba giai đoạn và các câu nói mẫu là tổng hợp của Claude; không có slide nào trình bày chuỗi này.

=====

---
id: PB-003
type: playbook
title_vi: Thiết kế lại cách team làm việc và ra quyết định
title_en: Redesigning How the Team Works and Decides
aliases: [cách làm việc của team, decision rights, quy trình team, way of working]
keywords: [quản lý thành nút thắt, mọi việc phải qua mình, ai quyết cái gì, quy trình không rõ, họp nhiều không ra quyết định, bàn giao hỏng, nhịp review, quyền quyết định, AI được làm gì]
levels: [TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-02, TOP-MEGROW-06, TOP-MEGROW-15, TOP-MEGROW-18, TOP-MEGROW-16]
problems_addressed: [PRB-003]
related_ids: [PRB-003, CON-003, FW-006, FW-041, FW-042, CON-016, FW-084, FW-085, FW-094, FW-010, FW-053, CON-005, FW-070]
source: ["MEGROW | Topic 02 | Topic 2 - Driving Operational Execution - Dr Emmy Hoang.pdf | Slide 30–33", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 3–5, 64–65", "MEGROW | Topic 15 | Topic 15 - From Stakeholder Insight to Market Impact - Dr Phuong Nguyen.pdf | Slide 10–20", "MEGROW | Topic 18 | Topic 18 - Leading in the AI-Enabled Organisation - Prof Trung Nguyen.pdf | Slide 29–30", "MEGROW | Topic 16 | Topic 16 - Solve Tech and Org Blockers - Thuan Nguyen & Bidyut Hazarika.pdf | Slide 24–30"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Thiết kế lại cách team làm việc và ra quyết định

## Dùng khi nào
Khi bạn là điểm duyệt của gần như mọi việc; khi team họp nhiều mà ít quyết định được chốt; khi cùng một loại trục trặc lặp lại ở khâu bàn giao. Đừng chạy playbook này giữa lúc có sự cố — chạy nó ở một tuần bình thường.

## Checklist

**Bước 1 — Nhìn thấy luồng việc thật (90 phút, với team)**
1. **Vẽ hành trình của một loại công việc** từ lúc nhận yêu cầu tới lúc kết quả được dùng. Chọn **một** loại, không gộp. Ghi các giai đoạn · ai tham gia · chỗ nào chậm, lẫn lộn, làm lại. (`FW-084`)
2. **Đánh dấu 2–3 chỗ giá trị bị phá vỡ.** Chú ý: giai đoạn *cảm thấy ổn nhất* (thường là lúc "đã thống nhất") hay là chỗ gieo mầm cho đứt gãy ở sau. (`FW-084-01`)
3. **Liệt kê rào cản bằng danh sách có sẵn** thay vì hỏi chung chung: ưu tiên xung đột · quyền sở hữu không rõ · thông tin đến chậm · thiếu niềm tin · theo đuổi yếu. (`FW-070`)

**Bước 2 — Chốt quyền quyết định (60 phút)**
4. **Liệt kê các loại quyết định lặp lại** trong tháng vừa rồi. Với mỗi loại, trả lời ba câu tách biệt: ai **làm** (responsible) · ai **chịu kết quả** (accountable, đúng một người) · ai được **quyết** (decision right). Ba thứ này hay bị trộn. (`CON-003`)
5. **Với mỗi loại, chọn mức tham gia** — tự quyết · hỏi một người · hỏi nhóm · nhóm cùng quyết. Chọn theo *loại quyết định*, không theo thói quen. (`FW-006`)
6. **Đẩy xuống những quyết định rủi ro thấp và đảo ngược được.** Phép thử: *nếu quyết sai, bao lâu thì biết, và sửa có tốn không?* Rẻ và nhanh biết thì không cần qua bạn.
7. **Nếu có AI trong luồng, gán một trong bốn mức quyền** cho từng đầu việc: AI Assists · AI Recommends · AI Acts with Approval · AI Acts Within Boundaries. Với mức 3 và 4, **viết ra** ranh giới và tên người sở hữu việc leo thang — ranh giới chỉ nằm trong đầu thì không phải ranh giới. (`FW-094`, `FW-010`)

**Bước 3 — Đặt nhịp và ngưỡng (30 phút)**
8. **Ba nhịp, ba mục đích:** check ngắn hằng ngày gỡ vướng · review tuần nhìn outcome–driver–guardrail · milestone gate quyết định tiếp hay dừng. (`FW-042`)
9. **Đặt ngưỡng phản ứng trước**: cái gì xử lý ngay, cái gì xử lý trong chu kỳ này, cái gì chỉ quan sát.
10. **Kiểm nguyên tắc giám sát:** dashboard đang nhìn vào *trạng thái công việc và phụ thuộc* hay vào *từng người làm được bao nhiêu*? (`CON-016`, `CON-005`)

**Bước 4 — Thử trước khi áp rộng**
11. **Chọn đúng một thay đổi, chạy 7 ngày, đo một chỉ số.** Đừng đổi cả quy trình trong một lần. (`FW-053`)
12. Nếu phản xạ của team là "thêm một bước kiểm", hỏi ngược: **bỏ được phê duyệt/cuộc họp/bàn giao nào?** (`FW-085` — Subtraction)

## Kịch bản / câu hỏi mẫu

**Mở buổi vẽ hành trình:**
> *"Mình không bàn ai sai ở đâu. Mình vẽ lại đường đi của một yêu cầu từ lúc nhận tới lúc xong, rồi tìm chỗ nó bị kẹt."*

**Khi chuyển một quyết định xuống:**
> *"Từ giờ loại quyết định này em tự chốt. Ranh giới là [X]. Vượt ranh giới đó thì nói với anh trước. Anh không cần biết từng lần."*

**Khi team đẩy ngược quyết định lên:**
> *"Em nghĩ phương án nào đúng, và vì sao? Nếu em chốt luôn thì rủi ro lớn nhất là gì?"* — hỏi trước khi trả lời.

**Khi đặt ranh giới cho một công cụ AI:**
> *"Nó được chạy tự động với ca dưới ngưỡng [X]. Trên ngưỡng đó phải có người duyệt. Người trực tuần nào sở hữu việc leo thang."*

**Giữ tầm nhìn mà không kiểm soát** — thay câu hỏi tiến độ hằng ngày bằng thỏa thuận: *"Dashboard tự cập nhật, mình gặp giữa tuần, em báo sớm khi lệch quá hai ngày hoặc chất lượng dữ liệu tụt dưới ngưỡng."* (`CON-005`)

## Cách đánh giá hiệu quả
- **Số quyết định quay lại bạn mỗi tuần** (kỳ vọng giảm rõ rệt) — chỉ số chính.
- Số loại quyết định có người accountable được viết ra: mục tiêu 100%.
- Thời gian từ lúc một rủi ro được nhận ra tới lúc nó được nói trong review.
- Số vòng làm lại ở khâu bàn giao đã đánh dấu ở bước 2.
- Với luồng có AI: tỷ lệ đầu việc đã gán mức quyền rõ và có tên người leo thang.

## Framework nền tảng
`CON-003` responsibility/accountability/decision rights · `FW-006` năm mức tham gia · `FW-041` hệ thống giao hàng · `FW-042` nhịp review và ngưỡng · `CON-016` giám sát hệ thống · `CON-005` tầm nhìn không kiểm soát · `FW-084` + `FW-084-01` bản đồ hành trình · `FW-070` enablers/barriers · `FW-085` SIT · `FW-094` bốn mức quyền AI · `FW-010` HAI · `FW-053` thử nghiệm 7 ngày.

Chẩn đoán đầy đủ: `PRB-003`. Nếu team không dám nêu vấn đề về chính cách làm việc: `PRB-009` trước.

## Nguồn
- `[MEGROW | Topic 02 | … Dr Emmy Hoang.pdf | Slide 30–33]` · `[MEGROW | Topic 06 | … Agnis Stibe-2.pdf | Slide 3–5, 64–65]` · `[MEGROW | Topic 15 | … Dr Phuong Nguyen.pdf | Slide 10–20]` · `[MEGROW | Topic 18 | … Prof Trung Nguyen.pdf | Slide 29–30]` · `[MEGROW | Topic 16 | … Thuan Nguyen & Bidyut Hazarika.pdf | Slide 24–30]` — tên file đầy đủ ở `source` trong frontmatter.
- `[SUY LUẬN]` Trình tự bốn bước là tổng hợp của Claude từ các framework trên.

=====

---
id: PB-004
type: playbook
title_vi: Rút khỏi việc kỹ thuật mà không để chất lượng tụt
title_en: Stepping Back from Hands-On Work Without Losing Quality
aliases: [buông việc kỹ thuật, 90 ngày đầu, IC to manager, chuyển vai]
keywords: [mới lên quản lý, vẫn code nhiều quá, tự làm nhanh hơn, không có thời gian cho team, sợ chất lượng tụt, buông việc, 90 ngày đầu, quản lý thời gian, mất kiểm soát]
levels: [SELF, TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-01, TOP-MEGROW-05, TOP-MEGROW-03, TOP-MEGROW-06]
problems_addressed: [PRB-004]
related_ids: [PRB-004, CON-001, CON-002, FW-003, FW-001-01, CON-004, FW-059, FW-060, FW-061, CON-022, FW-055, CON-023, FW-064, CON-025]
source: ["MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 6–23", "MEGROW | Topic 05 | Topic 5 - Optimise Personal Productivity - Agnis Stibe.pdf | Slide 2–5, 70–75", "MEGROW | Topic 03 | Topic 3 - Audit Mindset & Biases - Dr Thu Nguyen - Updated.pdf | Slide 14, 17, 25", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Rút khỏi việc kỹ thuật mà không để chất lượng tụt

## Dùng khi nào
Bạn vẫn là người sửa phần khó nhất và duyệt mọi thứ; lịch kín nhưng không có thời gian cho team; bạn biết nên buông nhưng sợ chất lượng tụt. Playbook này chạy theo **nhịp 30/60/90 ngày**, không làm trong một tuần.

## Checklist

**Tuần 0 — chẩn đoán (60 phút, một mình)**
1. **Đọc bối cảnh mình đang thừa hưởng** bằng STARS: khởi tạo, xoay chuyển, tăng trưởng nhanh, tái định vị, hay duy trì thành công? Mỗi bối cảnh cho một tốc độ buông khác nhau. (`FW-003`)
2. **Gọi tên cái bẫy của mình.** Ba cái: làm thay cho nhanh · né giao việc vì sợ mất kiểm soát · để kỳ vọng ở dạng ngầm. Chọn cái đúng nhất với mình trong tháng vừa rồi. (`CON-002`)
3. **Ghi lại một tuần thật.** Mỗi khối thời gian rơi vào ô nào trong bốn ô Khẩn cấp × Quan trọng. Nếu Q1+Q3 chiếm phần lớn, bạn đang sống trong việc của người khác. (`FW-061`)

**Ngày 1–30 — lọc và giữ nguyên chất lượng**
4. **Liệt kê việc bạn đang ôm.** Với mỗi việc, hỏi bốn câu: *việc này có cần tôi không · có cần một người khác không · AI làm được không · có nên làm không?* (`FW-060`)
5. **Chọn hai việc để chuyển đi trước.** Tiêu chí: rủi ro thấp, đảo ngược được, và có người đủ sẵn sàng.
6. **Với mỗi việc chuyển đi, đo Skill và Will cho đúng việc đó** — không đo con người nói chung, không dùng thâm niên thay bằng chứng. Ra một trong bốn: Direct · Coach · Motivate · Delegate. (`FW-001-01`)
7. **Giao đủ bốn thứ**, nếu không nó sẽ quay lại: kết quả mong đợi · ai sở hữu · quyết định nào họ được tự chốt · "xong tốt" nghĩa là gì. (`CON-004`)
8. **Thay chất lượng-bằng-tự-làm bằng chất lượng-bằng-tiêu chuẩn.** Viết ra định nghĩa "done well" cho loại việc đó. Đây là bước thực sự bảo vệ chất lượng — không phải việc bạn tự làm.

**Ngày 31–60 — bảo vệ thời gian và kiểm phán đoán**
9. **Khóa một khối Q2 cố định hằng tuần** và không nhận họp vào đó. Q2 là thứ làm Q1 của quý sau nhỏ lại. (`FW-061`)
10. **Chạy tự kiểm khi định nhảy vào sửa.** PAUSE (tôi đang gấp à?) → EVIDENCE → OPPOSITE (60 giây cãi lại chính mình) → OUTSIDE VIEW → DECIDE & LOG. (`FW-055`)
11. **Để ý thiên kiến chuyên gia.** Ba câu báo động: *"Nếu cô ấy thực sự cố thì đã xong rồi" · "Để anh làm cho nhanh" · "Không cần hỏi, nhìn là biết chất lượng không đạt."* (`CON-022`)

**Ngày 61–90 — chuyển thước đo**
12. **Đổi cách bạn tự chấm tuần của mình**: từ "tôi đã xử lý bao nhiêu việc" sang "team đã tự quyết được bao nhiêu việc". (`CON-001`)
13. **Rà lại hai việc đã chuyển ở bước 5.** Chất lượng có tụt thật không, hay chỉ *khác cách làm của bạn*? Phân biệt hai thứ này là phần khó nhất.
14. **Chọn hai việc tiếp theo** và lặp lại từ bước 6.

## Kịch bản / câu hỏi mẫu

**Thay vì "Để anh làm cho nhanh":**
> *"Em chạy thử hướng của em, 30 phút nữa mình xem cùng — anh chỉ hai chỗ rủi ro nhất."*

**Khi giao việc và muốn nó không quay lại:**
> *"Kết quả cần đạt là [X]. Em sở hữu việc này. Em tự quyết [A, B]; [C] thì nói với anh trước. 'Xong tốt' nghĩa là [tiêu chí]. Mình gặp lại [mốc]."*

**Khi bạn muốn nhảy vào sửa:** hỏi mình trước — *"Nếu tôi không động vào, kết quả tệ hơn bao nhiêu, và cái giá của việc tôi làm thay là gì tính tới quý sau?"*

**Khi bảo vệ khối Q2:**
> *"Sáng thứ Ba 9–11h mình không nhận họp. Có việc gấp thì nhắn, mình xử lý sau 11h."*

**Khi cấp trên hỏi vì sao bạn ít code hơn:**
> *"Em chuyển trọng tâm sang [định hướng/coaching/gỡ phụ thuộc]. Chỉ số em muốn anh nhìn là [outcome của team], không phải số commit của em."*

## Cách đánh giá hiệu quả
- **Số quyết định team tự chốt mỗi tuần** (tăng) và **số việc quay lại bạn sau khi giao** (giảm) — hai chỉ số chính.
- Tỷ lệ thời gian ở Q2 trong tuần (tăng), Q1+Q3 (giảm). Đo lại sau 30 và 90 ngày. (`FW-061`)
- Số loại việc có định nghĩa "done well" được viết ra.
- Bạn đã ghi được bao nhiêu "giả định yếu" trong nhật ký quyết định? (`FW-055` bước 5)
- Cảnh báo ngược: nếu sau 90 ngày bạn vẫn là người duy nhất xử lý được phần khó, vấn đề có thể là năng lực team — chuyển sang `PRB-005`.

## Framework nền tảng
`CON-001` chuyển dịch IC→quản lý · `CON-002` ba cái bẫy · `FW-003` 90 ngày và STARS · `FW-001-01` Skill × Will · `CON-004` giao đủ bốn thứ · `FW-059` mười thách thức · `FW-060` bốn quyết định · `FW-061` ma trận khẩn cấp–quan trọng · `CON-022` thiên kiến chuyên gia · `FW-055` tự kiểm 5 bước · `CON-023` · `FW-064` · `CON-025`.

Chẩn đoán đầy đủ: `PRB-004`.

## Nguồn
- `[MEGROW | Topic 01 | … AP Burkhard Schrage.pdf | Slide 6–23]` · `[MEGROW | Topic 05 | … Agnis Stibe.pdf | Slide 2–5, 70–75]` · `[MEGROW | Topic 03 | … Dr Thu Nguyen - Updated.pdf | Slide 14, 17, 25]` · `[MEGROW | Topic 06 | … Agnis Stibe-2.pdf | Slide 2–5]` — tên file đầy đủ ở `source` trong frontmatter.
- `[SUY LUẬN]` Nhịp 30/60/90 và trình tự 14 bước là tổng hợp của Claude; `FW-003` cung cấp khung thời gian, phần còn lại ghép từ các topic khác.

=====

---
id: PB-005
type: playbook
title_vi: Giao một việc lớn cho đúng người
title_en: Handing Over a Significant Piece of Work
aliases: [giao việc, delegate, trao quyền, giao dự án, stretch assignment]
keywords: [giao việc cho ai, giao rồi vẫn phải làm lại, trao quyền cho senior, giao việc cho người mới, stretch assignment, phát triển nhân viên, giao việc cho cộng tác viên, người giỏi gánh hết]
levels: [TEAM]
courses: [MEGROW]
topics: [TOP-MEGROW-01, TOP-MEGROW-06, TOP-MEGROW-09, TOP-MEGROW-10, TOP-MEGROW-18]
problems_addressed: [PRB-005]
related_ids: [PRB-005, FW-001, FW-001-01, CON-004, CON-003, CON-005, FW-009, FW-028, FW-029, FW-030, FW-093, FW-032, FW-074, FW-025-01]
source: ["MEGROW | Topic 01 | Topic 1 - Navigating the Leadership Transition - AP Burkhard Schrage.pdf | Slide 15–18", "MEGROW | Topic 06 | Topic 6 - Delegation & Accountability in Fast-Paced Teams - Agnis Stibe-2.pdf | Slide 2–5, 59, 64–65", "MEGROW | Topic 09 | Topic 9 - Coaching for High Performance - Final (without key answer) - Quyen Dang.pdf | Slide 31–36", "MEGROW | Topic 10 | Topic 10 - Adapt Your Leadership Style -  Tony Nguyen.pdf | Slide 24–27", "MEGROW | Topic 18 | Topic 18 - Leading in the AI-Enabled Organisation - Prof Trung Nguyen.pdf | Slide 27–28"]
source_type: course
confidence: high
status: verified
replaced_by:
last_updated: 2026-11-08
---

# Giao một việc lớn cho đúng người

## Dùng khi nào
Có một việc đáng kể cần chuyển đi: một dự án, một mảng sở hữu, một quyết định lặp lại. Dùng cả khi bạn đã giao rồi mà việc cứ quay lại, hoặc khi người giỏi nhất đang gánh hết còn người khác không lớn lên. Chuẩn bị mất **30 phút**, cuộc trò chuyện giao việc **30–45 phút**.

## Checklist

**Trước cuộc trò chuyện (30 phút)**

1. **Viết ra kết quả, không viết đầu việc.** Một câu: *"Sau [thời hạn], [điều gì] khác đi."* Nếu bạn chỉ viết được danh sách task thì bạn chưa biết mình muốn gì.
2. **Chọn người bằng Skill × Will cho đúng việc này**, không theo thâm niên và không theo "ai đang rảnh". Đo Skill bằng bằng chứng (họ đã làm việc tương tự chưa), đo Will bằng câu hỏi (họ có muốn không, rào cản là gì). (`FW-001-01`)
3. **Chọn mức dẫn dắt tương ứng**: Skill thấp–Will thấp → Direct · thấp–cao → Coach · cao–thấp → Motivate · cao–cao → Delegate. Mức này áp cho **việc này**, không phải cho con người đó mãi mãi. (`FW-001`)
4. **Nếu giao để phát triển, chấm mức sẵn sàng trước.** Năm mục, mỗi mục 1–5: 5–11 → trong vai trò hiện tại · 12–18 → stretch có giới hạn · 19–25 → cân nhắc luân chuyển. **Chấm sau khi trò chuyện, ghi bằng chứng cho từng mức điểm.** (`FW-029`)
5. **Kiểm điều kiện trước khi trách người.** Họ có thấy an toàn để hỏi và sai không (Environment) · có đủ công cụ và kiến thức không (Equipping) · đã từng tiếp xúc bối cảnh thật chưa (Exposure). Thiếu cái nào cho triệu chứng riêng cái đó. (`FW-093`)

**Trong cuộc trò chuyện (30–45 phút)**

6. **Nói đủ bốn thứ.** Thiếu một trong bốn là lý do việc quay lại: (`CON-004`)
   - **Kết quả mong đợi** — không phải danh sách việc
   - **Ai sở hữu** — đúng một người accountable (`CON-003`)
   - **Quyền quyết định** — họ tự chốt được gì, cái gì phải hỏi
   - **"Xong tốt" nghĩa là gì** — tiêu chí quan sát được
7. **Thỏa thuận checkpoint trước, thay vì hỏi tiến độ sau.** Ranh giới và mốc được chốt tại đây thì bạn có tầm nhìn mà không cần kiểm soát. (`CON-005`)
8. **Để họ nói lại bằng lời của họ.** Đây là bước kiểm sự rõ ràng duy nhất đáng tin — *"bạn không rõ ràng như bạn tưởng"*.
9. **Hỏi họ cần gì từ bạn**, và nói rõ bạn sẽ **không** làm gì.

**Sau khi giao**

10. **Giữ checkpoint đã hẹn, không thêm.** Mỗi lần hỏi ngoài lịch là một lần quyền sở hữu dịch ngược về bạn.
11. **Khi họ hỏi bạn một quyết định thuộc quyền họ**, hỏi ngược trước khi trả lời.
12. **Nếu việc quay lại**, chẩn đoán bằng năm lăng kính — Knowledge · Skills · Motivation · Career · Environment — thay vì cho rằng thiếu nỗ lực. (`FW-028`)
13. **Nếu bạn không phải chuyên gia đúng mảng họ cần**, kết nối thay vì tự dạy. (`FW-032`)

## Kịch bản / câu hỏi mẫu

**Câu giao việc đầy đủ:**
> *"Kết quả cần đạt là [X] trước [mốc]. Em sở hữu việc này. Em tự quyết [A, B]; với [C] thì nói với anh trước khi làm. 'Xong tốt' nghĩa là [tiêu chí quan sát được]. Mình gặp lại ngày [mốc] — ngoài mốc đó anh không hỏi tiến độ."*

**Kiểm sự rõ ràng (bước 8):**
> *"Em nói lại giúp anh: em hiểu kết quả cần đạt là gì, và em sẽ bắt đầu từ đâu?"*

**Đo Will mà không hỏi suông:**
> *"Việc này em thấy thế nào? Có phần nào em thấy khó hoặc không chắc không?"*

**Khi họ đẩy quyết định ngược lên:**
> *"Em nghĩ phương án nào đúng, vì sao? Nếu em chốt luôn thì rủi ro lớn nhất là gì?"*

**Với cộng tác viên — phạm vi chặt hơn:** `[BỔ SUNG]` *"Phần này là của em từ [A] tới [B]. Ngoài phạm vi đó em chuyển lại, không tự nhận thêm."* MEGROW không có nội dung riêng cho cộng tác viên (OQ-005) — ranh giới rõ quan trọng hơn tự chủ rộng.

**Khi chất lượng khác cách làm của bạn:** hỏi *"kết quả có đạt tiêu chí đã thỏa thuận không?"* — không hỏi *"sao không làm theo cách của anh?"*

## Cách đánh giá hiệu quả
- **Số lần việc quay lại sau khi đã giao** — chỉ số chính, kỳ vọng giảm về gần 0.
- Số câu xin duyệt chi tiết trong hai tuần đầu (giảm dần, không mất ngay).
- Người nhận nói lại được kết quả mong đợi bằng lời của họ không — kiểm tại bước 8.
- Sau một quý: số việc họ tự chốt mà trước đây phải hỏi bạn.
- Việc giao để phát triển: họ làm được việc **cùng loại nhưng khó hơn** ở lần sau không?

## Framework nền tảng
`FW-001` + `FW-001-01` Situational Leadership và Skill × Will · `CON-004` giao kết quả · `CON-003` quyền quyết định · `CON-005` tầm nhìn không kiểm soát · `FW-009` sở hữu tâm lý · `FW-028` năm lăng kính · `FW-029` thang sẵn sàng · `FW-030` D–R–C · `FW-093` EEE · `FW-032` · `FW-074` · `FW-025-01`.

Chẩn đoán đầy đủ: `PRB-005`.

## Nguồn
- `[MEGROW | Topic 01 | … AP Burkhard Schrage.pdf | Slide 15–18]` · `[MEGROW | Topic 06 | … Agnis Stibe-2.pdf | Slide 2–5, 59, 64–65]` · `[MEGROW | Topic 09 | … Quyen Dang.pdf | Slide 31–36]` · `[MEGROW | Topic 10 | … Tony Nguyen.pdf | Slide 24–27]` · `[MEGROW | Topic 18 | … Prof Trung Nguyen.pdf | Slide 27–28]` — tên file đầy đủ ở `source`.
- `[SUY LUẬN]` Trình tự 13 bước là tổng hợp của Claude từ các framework trên.
