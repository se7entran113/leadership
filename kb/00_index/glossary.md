# glossary.md — Thuật ngữ Việt–Anh

Thuật ngữ và tên framework giữ nguyên tiếng Anh, kèm nghĩa tiếng Việt. Mỗi chunk vẫn phải tự giải thích thuật ngữ ở lần xuất hiện đầu tiên (CLAUDE.md §5.3) — glossary này là bảng tra cứu chung, không thay thế việc đó.

**Trạng thái:** thuật ngữ từ Topic 01, 02, 04, 06, 08, 09, 10, 12, 14, 16, 17 và 19 đã được thêm. Các topic còn lại sẽ bổ sung khi xử lý; tên framework ứng viên xem ở `problem_index.md`.

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

### Thực thi vận hành (Topic 02)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Operational execution | Thực thi vận hành | Chuyển mục tiêu thành hành động phối hợp, theo dõi kết quả, sửa kế hoạch khi bằng chứng cho thấy chệch hướng | `CON-014` |
| Translate · Coordinate · Adjust | Dịch · Phối hợp · Điều chỉnh | Ba động tác của người quản lý trong thực thi | `FW-035` |
| Goal / Objective / Output / Outcome / Impact | Mục tiêu rộng / kết quả cụ thể / sản phẩm / thay đổi / giá trị | Năm bậc từ định hướng tới giá trị; ba bậc đầu trong tầm kiểm soát | `CON-015` |
| SMART | Cụ thể – Đo được – Khả thi – Liên quan – Có thời hạn | Mức rõ ràng tối thiểu của một objective | `FW-036` |
| Guardrail | Lằn ranh an toàn | Thứ phải giữ cho khoẻ mạnh trong lúc theo đuổi mục tiêu | `FW-037`, `FW-039` |
| Metric / KPI / Baseline / Target | Chỉ số / chỉ số then chốt / mốc xuất phát / mức cần đạt | Bộ bốn thuật ngữ đo lường tối thiểu | `FW-038` |
| Leading / Lagging indicator | Chỉ số dẫn dắt / chỉ số kết quả | Tín hiệu sớm so với kết quả cuối | `FW-038` |
| Outcome–Driver–Guardrail–Flow | Bốn tầng tín hiệu thực thi | Giá trị có xảy ra · ta có chuyển động · cái gì phải khoẻ · việc đang dồn ở đâu | `FW-039` |
| Initiative / Project / Workstream / Task | Sáng kiến / dự án / luồng công việc / nhiệm vụ | Bốn mức phân rã công việc dưới một objective | `FW-040` |
| Dependency / Critical path | Phụ thuộc / đường găng | Việc chặn việc khác; chuỗi quyết định thời hạn cuối | `FW-040` |
| Responsibility vs Accountability | Trách nhiệm làm vs trách nhiệm giải trình | Nhiều người có thể responsible; chỉ một người accountable | `FW-041` |
| Blocker vs Bottleneck | Vật cản vs nút thắt | Sự kiện chặn một việc vs chỗ hệ thống luôn chậm | `FW-041` |
| Cadence | Nhịp | Tần suất và loại review: daily check, weekly review, milestone gate | `FW-042` |
| Response threshold | Ngưỡng phản ứng | Act now · Act this cycle · Observe and learn | `FW-042` |

### Tư duy chiến lược (Topic 17)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Six disciplines of strategic thinking | Sáu kỷ luật tư duy chiến lược | Pattern recognition · systems analysis · mental agility · structured problem-solving · visioning · political savvy (Watkins, 2024) | `FW-043` |
| Cloud to ground | Từ mây xuống đất | Di chuyển giữa bức tranh lớn và chi tiết — mô tả của Watkins cho mental agility | `FW-043` |
| PESTEL | Chính trị – Kinh tế – Xã hội – Công nghệ – Môi trường – Pháp lý | Sáu loại thay đổi bên ngoài cần quét | `FW-044` |
| So what test | Phép thử "so what" | Mỗi phát hiện phải kết bằng cơ hội hay đe doạ cho team bạn | `FW-044` |
| Five Forces | Năm áp lực cạnh tranh | New entrants · suppliers · buyers · substitutes · rivalry (Porter, 2008) | `FW-045` |
| Willingness to pay (WTP) | Mức sẵn lòng trả | Mức tối đa khách hàng chấp nhận trả; nâng nó là một trong hai cách thắng | `FW-046` |
| Value stick | Thanh giá trị | WTP – Price – Cost – Willingness to sell, chia thành customer delight, firm margin, supplier surplus | `FW-046` |
| Resources vs Capabilities | Nguồn lực vs năng lực | Thứ bạn **có** vs thứ bạn **làm tốt** | `CON-017` |
| Core competence | Năng lực cốt lõi | Vừa quan trọng với khách hàng, vừa làm tốt hơn đối thủ | `CON-017` |
| Outside-in / Inside-out | Nhìn từ ngoài vào / từ trong ra | "Nên cạnh tranh ở đâu" vs "thắng bằng gì" — cần cả hai | `CON-018` |
| VRIN | Có giá trị – Hiếm – Khó sao chép – Khó thay thế | Bốn phép thử lợi thế bền vững (Barney, 1991) | `FW-047` |
| Moat | Hào | Tập nguồn lực VRIN giữ đối thủ ở ngoài; team nới rộng hoặc thu hẹp nó mỗi ngày | `FW-047-01` |
| Line-of-sight test | Phép thử đường ngắm | Mỗi người có nói được việc mình làm đẩy bậc ngay trên nó không | `CON-019` |
| Riskiest assumption | Giả định rủi ro nhất | Giả định mà nếu sai sẽ làm đổi khuyến nghị | `FW-048` |

### Giải quyết vấn đề và gỡ blocker (Topic 16)

| Tiếng Anh | Tiếng Việt | Định nghĩa ngắn | Chunk |
|---|---|---|---|
| Design Thinking | Tư duy thiết kế | Empathize · Define · Ideate · Prototype · Test (mô hình Stanford) | `FW-049` |
| Understand – Create – Deliver | Hiểu – Tạo – Giao | Ba chặng gom năm pha; kết thúc lần lượt ở insight, ideas, reality | `FW-049` |
| Problem-first, not prompt-first | Vấn đề trước, prompt sau | Nguyên tắc 1 khi dùng AI trong giải quyết vấn đề | `FW-049-01` |
| Problem Tree | Cây vấn đề | Nguyên nhân ở rễ, hệ quả ở tán, vấn đề cốt lõi ở thân | `FW-050` |
| Empathy Map | Bản đồ thấu cảm | Hiểu một stakeholder thật trước khi định nghĩa vấn đề | `FW-051` |
| Symptom / Assumption / Possible cause | Triệu chứng / giả định / nguyên nhân có thể | Ba cột tách điều quan sát được khỏi điều ta tin | `FW-052` |
| Problem statement template | Mẫu phát biểu vấn đề | "[Stakeholder] cần… bởi vì… dẫn tới… bằng chứng là…" | `FW-052` |
| How Might We (HMW) | Làm thế nào chúng ta có thể… | Câu hỏi thiết kế: human-centred, focused, open-ended, actionable, chưa phải giải pháp | `CON-020` |
| Prototype | Bản thử | Thử một phiên bản nhỏ trước rồi học — không phải giải pháp cuối cùng | `FW-053` |
| 7-day test | Thử nghiệm 7 ngày | MỘT team · MỘT tuần · MỘT kết quả để kiểm tra | `FW-053-01` |
| Three-line ask | Lời đề nghị ba dòng | "Vấn đề là… · Chúng tôi đã thử… · Chúng tôi cần anh/chị…" trong 45 giây | `FW-054` |

## Thiên kiến và tư duy kiểm toán (Topic 03)

| Thuật ngữ | Tiếng Việt | Nghĩa ngắn | Chunk |
|---|---|---|---|
| System 1 / System 2 | Hệ thống 1 / Hệ thống 2 | Nhanh, tự động, luôn bật / chậm, logic, lười và phải được triệu tập | `CON-021` |
| Expert bias | Thiên kiến chuyên gia | Tin quá mức vào phán đoán chuyên môn ở chỗ nó không áp dụng được | `CON-022` |
| Audit Mindset | Tư duy kiểm toán | Questioning mind · Suspension of judgment · Search for evidence, quay vào chính mình | `FW-055` |
| 5-Step Bias Self-Audit | Tự kiểm thiên kiến 5 bước | PAUSE · EVIDENCE · OPPOSITE · OUTSIDE VIEW · DECIDE & LOG | `FW-055` |
| Overconfidence | Quá tự tin | Mức chắc chắn tự gán cao hơn độ chính xác thật | `CON-024` |
| Framing effect | Hiệu ứng mô tả | Một câu mô tả không đổi dữ kiện vẫn làm dịch chuyển đánh giá | `CON-024` |
| The Leak | Đường rò | Thiên kiến rò vào điều bạn nói, điều bạn không nói, và người bạn chọn để hỏi | `FW-056` |
| Automation bias | Thiên kiến tự động hóa | Văn phong trôi chảy và nhãn độ tin cậy của hệ thống chiêu mộ lòng tin | `FW-057` |
| Data artifact | Hiện vật dữ liệu | Khoảng trống trong dữ liệu bị đọc thành sự kém cỏi (ví dụ: nghỉ thai sản) | `FW-057` |
| Trust = Ability · Benevolence · Integrity | Niềm tin = Năng lực · Thiện ý · Chính trực | Ba thành tố nhân nhau; uy tín do người nghe trao, kiểm theo từng quan hệ | `FW-058` |

## Năng suất cá nhân (Topic 05)

| Thuật ngữ | Tiếng Việt | Nghĩa ngắn | Chunk |
|---|---|---|---|
| Hyper-performance | Hiệu suất vượt trội | Đường đi lên bền, đối lập với nhánh burnout từ cùng một điểm rẽ | `CON-025` |
| Burnout | Kiệt sức | Nhánh đi ngang; thắng ở giai đoạn đầu rồi suy giảm | `CON-025` |
| Neuroplasticity | Tính dẻo thần kinh | Não đổi cấu trúc theo trải nghiệm lặp lại — cơ sở sinh học của thay đổi | `CON-026` |
| Relentless honesty | Trung thực không khoan nhượng | Điều kiện để tích lũy 1% hoạt động: phải đo đúng mình đang ở đâu | `CON-026` |
| Knowledge–Behaviour Gap | Khoảng cách biết – làm | KNOWLEDGE → ACCEPTANCE → INTENTION → BEHAVIOR | `FW-064` |
| Time Matrix Q1–Q4 | Ma trận thời gian Q1–Q4 | Necessity · Effectiveness · Distraction · Waste | `FW-061` |
| Eisenhower Matrix | Ma trận Eisenhower | Do First · Schedule · Delegate · Eliminate | `FW-061` |
| GTD two-minute rule | Quy tắc hai phút | Việc dưới 2 phút thì làm ngay, vì chi phí ghi nhớ lớn hơn chi phí làm | `FW-062` |
| Assisted / Automation / Augmented / Autonomous | Bốn chế độ Người + AI | Mức tự chủ của AI tăng dần, điểm kiểm soát của người lùi dần | `FW-065` |
| Other info (nondigital) | Thông tin phi số hóa | Thứ chỉ đi vào quyết định qua con người vì nó không có trong dữ liệu | `FW-065-01` |

## LEGO® Serious Play® và bản sắc team (Topic 07)

| Thuật ngữ | Tiếng Việt | Nghĩa ngắn | Chunk |
|---|---|---|---|
| LEGO® Serious Play® (LSP®) | — | Phương pháp xây mô hình rồi kể chuyện thay cho phát biểu trực tiếp | `FW-066` |
| 4 NO GO's | Bốn điều không làm | Không đánh giá · không nhận định · không diễn giải · không đi quá mô hình | `FW-066-01` |
| Real Time Identity (RTI) | Bản sắc thời gian thực | Quy trình đưa một nhóm cá nhân thành Real Team | `FW-067` |
| Real Team | Team thật | Hiện thực hóa toàn bộ tiềm năng của team, nhanh và hiệu quả | `FW-067` |
| Core Identity (CI) | Bản sắc cốt lõi | Phẩm chất, giá trị, điểm mạnh định hình cách bạn đóng góp tự nhiên | `FW-068` |
| External Identity (EI) | Bản sắc bên ngoài | Cách người khác nhìn và trải nghiệm bạn trong team | `FW-068` |
| Possible Identity (PI) | Bản sắc tiềm năng | Giá trị bạn có thể mang lại nhưng chưa thể hiện đầy đủ | `FW-068` |
| Johari Window | Cửa sổ Johari | Open · External Perspective · Possible you · Unknown | `FW-069` |
| Self-disclosure / Feedback | Tự bộc lộ / Phản hồi | Hai cơ chế duy nhất làm ô Open mở rộng | `FW-069` |
| Team Life | Đời sống team | Các đặc tính vận hành thật của team, tích cực lẫn tiêu cực | `FW-070` |
| Team Landscape | Bản đồ kết nối team | Quan hệ theo bốn cặp: strong/weak · direct/indirect · supportive/difficult · frequent/limited | `FW-071` |

## Tính cách, giao tiếp và động lực (Topic 11)

| Thuật ngữ | Tiếng Việt | Nghĩa ngắn | Chunk |
|---|---|---|---|
| Driver / Amiable / Analytical / Expressive | Bốn phong cách làm việc | Hướng kết quả · hướng quan hệ · hướng dữ liệu · hướng tầm nhìn | `FW-072` |
| Strong / weak situation | Tình huống mạnh / yếu | Quy tắc rõ thì ai cũng hành xử giống nhau; mơ hồ thì tính cách bộc lộ | `FW-073` |
| Self / Social × Awareness / Management | Bốn địa hạt EI | Nhận ra và làm gì với điều đã nhận ra, ở mình và ở người khác | `FW-075` |
| ERG (Existence · Relatedness · Growth) | Tồn tại · gắn kết · phát triển | Alderfer: thanh trượt hai chiều, không phải bậc thang một chiều | `FW-074` |
| Need for Achievement / Affiliation / Power | Nhu cầu thành tựu / gắn bó / ảnh hưởng | McClelland: ba nhu cầu **có được**, thay đổi theo trải nghiệm | `FW-074` |
| Stretch assignment | Việc thử thách vượt mức | Giao việc vượt vùng an toàn để xây self-efficacy | `FW-076` |
| Convergent / Divergent (Gen Z VN) | Hội tụ / phân kỳ | Điều giống và khác thế hệ trước ở lãnh đạo Gen Z Việt Nam | `CON-028` |

## Niềm tin và an toàn tâm lý (Topic 13)

| Thuật ngữ | Tiếng Việt | Nghĩa ngắn | Chunk |
|---|---|---|---|
| TRUST Framework | Khung TRUST | Transparency · Reliability · Understanding · Safety · Team First | `FW-078` |
| Trust Equation | Phương trình niềm tin | (Credibility + Reliability + Intimacy) ÷ Self-Orientation | `FW-079` |
| Self-Orientation | Mức quy về bản thân | Mẫu số: càng cao càng chia nhỏ mọi thành phần ở tử số | `FW-079` |
| Psychological safety | An toàn tâm lý | Niềm tin rằng môi trường an toàn cho việc chấp nhận rủi ro quan hệ | `FW-080` |
| Comfort / Learning / Apathy / Anxiety Zone | Bốn vùng của Edmondson | An toàn tâm lý × tiêu chuẩn hiệu suất | `FW-080` |
| Six Signature Traits | Sáu phẩm chất lãnh đạo bao trùm | Cognizance · Curiosity · Courage · Cultural intelligence · Commitment · Collaboration | `FW-081` |
| STOP / START / SUSTAIN | Dừng / bắt đầu / duy trì | Bảng cam kết hành vi lãnh đạo cuối buổi | `FW-082` |

## Đổi mới và hành trình stakeholder (Topic 15)

| Thuật ngữ | Tiếng Việt | Nghĩa ngắn | Chunk |
|---|---|---|---|
| Desirability / Feasibility / Viability | Đáng mong muốn / khả thi / bền vững | Ba điều kiện cần cùng lúc để một đổi mới là "useful" | `FW-083` |
| Pain point | Điểm đau | Thời điểm stakeholder gặp bực bội, khó khăn hoặc bất định; đối lập là Gain | `FW-084` |
| Explicit / Latent pain point | Điểm đau hiện / ẩn | Hiện thì hỏi là biết; ẩn thì chỉ lộ khi vẽ lại cả hành trình | `FW-084` |
| Stakeholder Journey Map (SJM) | Bản đồ hành trình stakeholder | Trải nghiệm của một stakeholder qua nhiều team, theo thời gian | `FW-084` |
| Where does value break | Giá trị bị phá vỡ ở đâu | Chậm trễ, lẫn lộn, làm lại — câu hỏi trung tâm của SJM | `FW-084` |
| Systematic Inventive Thinking (SIT) | Tư duy sáng tạo hệ thống | Năm phép biến đổi áp lên thứ đang có để sinh ý tưởng | `FW-085` |
| Attribute Dependency | Phụ thuộc theo thuộc tính | Quy trình thay đổi theo rủi ro, mức khẩn hoặc độ phức tạp | `FW-085` |
| Creative Matrix | Ma trận sáng tạo | Công cụ SIT × điểm giá trị bị phá vỡ, ép sinh ý tưởng cho từng ô | `FW-086` |
| One bottleneck – one improvement – one benefit | Một nút thắt – một cải tiến – một lợi ích | Ràng buộc chốt, buộc bỏ phần lớn ý tưởng vừa sinh | `FW-086` |
