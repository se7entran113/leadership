# glossary.md — Thuật ngữ Việt–Anh

Thuật ngữ và tên framework giữ nguyên tiếng Anh, kèm nghĩa tiếng Việt. Mỗi chunk vẫn phải tự giải thích thuật ngữ ở lần xuất hiện đầu tiên (CLAUDE.md §5.3) — glossary này là bảng tra cứu chung, không thay thế việc đó.

**Trạng thái:** thuật ngữ từ Topic 01, 06 và 10 đã được thêm. Các topic còn lại sẽ bổ sung khi xử lý; tên framework ứng viên xem ở `problem_index.md`.

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
