# problem_index.md — Vấn đề → nguyên nhân → framework

Bảng tra cứu chính cho câu hỏi: *"Tôi đang gặp vấn đề này, dùng framework nào?"*

**Trạng thái:** 5 chunk `PRB`, 12 chunk `FW` và 6 chunk `CON` đã tạo (từ Topic 01, 06, 10). Với các vấn đề đã có chunk `PRB`, **chunk đó là nguồn chính** — bảng ở đây chỉ là mục lục. Với các vấn đề còn lại, cột **Framework ứng viên** vẫn là `[SUY LUẬN]` nhận diện từ tiêu đề trang khi lập inventory, **chưa đọc nội dung chi tiết, chưa kiểm chứng**.

| Vấn đề | Mức | Chunk PRB | Trạng thái |
|---:|---|---|---|
| 1 | Cao | — | chờ Topic 02, 17 |
| 2 | Cao | — | chờ Topic 12, 19 |
| 3 | Cao | `PRB-003` | ✅ một phần (Topic 06, 10) |
| 4 | Cao | `PRB-004` | ✅ đã có |
| 5 | Cao | `PRB-005` | ✅ đã có |
| 6 | Trung bình | — | chờ Topic 04, 08, 09 |
| 7 | Trung bình | `PRB-007` | ✅ một phần (Topic 06) |
| 8 | Trung bình | — | chờ Topic 17, 19 |
| 9 | Thấp | — | chờ Topic 13 |
| 10 | Thấp | — | chờ Topic 12, 14 |
| 11 | Thấp | `PRB-011` | ✅ một phần (Topic 06) |

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

### `PRB-003` · 3. Thiết kế framework làm việc và giải quyết vấn đề cho team
*Quy trình, phối hợp, ra quyết định, tiêu chuẩn chất lượng.*
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Team Delivery System · Review rhythm (daily/weekly/milestone gate) · Response thresholds · Monitor the work system, not the person | T2 | _chưa có_ |
| Owner / Responsibility / Accountability / RACI · Decision rights | T2, T6 | `CON-003` (phần T6) |
| AI-augmented Design Thinking (Stanford 5 phases; Understand–Create–Deliver) · Empathy Map · 7-day test | T16 | _chưa có_ |
| Vroom–Yetton–Jago Model (AI / AII / CI / CII / GII) | T10 | `FW-006` |
| Human–AI Decision Rights (4 mức) | T18 | _chưa có_ |
| HAI — phân bổ việc Human / AI / HAI; giao cho AI không giảm trách nhiệm người | T6 | `FW-010` |

### `PRB-004` · 4. Chuyển dịch từ người làm chuyên môn sang người quản lý
*Buông việc kỹ thuật, cân bằng tự làm và dẫn dắt, quản lý thời gian và năng lượng.*
**Level:** SELF

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Dalton, Thompson & Price (1977) Four Stages of Contribution | T1 | `FW-004` |
| Hill (2007) Five Myths · Ba cái bẫy (làm thay, né giao việc, kỳ vọng ngầm) | T1 | `FW-002`, `CON-002` |
| Watkins (2013) First 90 Days · STARS · Break-even point · 12 hành động | T1 | `FW-003` |
| IC → Manager mindset shift | T1, T2, T8 | `CON-001` (phần T1) |
| Expert bias · 5-Step Bias Self-Audit · Audit Mindset | T3 | _chưa có_ |
| Knowledge–Behaviour Gap Model (Knowledge → Acceptance → Intention → Behaviour) | T5, T6 | _chưa có_ |
| FranklinCovey Time Matrix · Eisenhower Matrix · GTD · Human Artificial Intelligence (HAI) | T5 | _chưa có_ |
| Self-awareness & Self-management (Emotional Intelligence) | T8, T11 | _chưa có_ |

### `PRB-005` · 5. Giao việc và phát triển theo năng lực từng người
*Trao quyền cho Senior, hướng dẫn DS, phạm vi rõ cho collaborator.*
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Hersey & Blanchard (1969) Life Cycle Theory / Situational Leadership II | T1, T6, T10 | `FW-001`, `FW-001-02` |
| Skill × Will readiness matrix (Landsberg) — Direct / Coach / Motivate / Delegate | T1 | `FW-001-01` |
| Blake & Mouton (1964) Leadership Grid · Task-oriented vs People-oriented | T10 | `FW-005` |
| Vroom–Yetton–Jago Model — mức tham gia vào quyết định | T10 | `FW-006` |
| Delegate outcomes not tasks · Accountability = clarity + ownership + follow-through · Empower without micromanaging | T6 | `CON-004`, `CON-003`, `CON-005` |
| Theory of Psychological Ownership (5 thành tố) | T6 | `FW-009` |
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

### `PRB-007` · 7. Động lực, gắn kết và giữ người
**Level:** TEAM

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| McClelland — Need for Achievement / Affiliation / Power | T11 | _chưa có_ |
| Alderfer ERG Theory (Existence · Relatedness · Growth) | T11 | _chưa có_ |
| Ba kết nối của Connector Manager: Employee · Team · Organisation | T9 | _chưa có_ |
| Personal Competitive Advantage · EDGE growth strategy | T9 | _chưa có_ |
| Apprenticeship Gap · EEE diagnostic (Environment · Equipping · Experience) | T18 | _chưa có_ |
| Social influence levers (Socium 7) | T6 | `FW-008` |

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
| Psychological safety with accountability | T6 | `CON-005` (một phần) |

### PRB-? · 10. Xung đột trong team hoặc giữa các team
**Level:** TEAM, ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Thomas–Kilmann Conflict Mode Instrument · Conflict Response Planner | T12 | _chưa có_ |
| Ladder of Inference (Argyris) · Seek first to understand (Inquiry) rồi Advocacy | T14 | _chưa có_ |
| Cùng dữ liệu, khác kết luận — chọn lọc dữ liệu khác nhau (case BCPC) | T14 | _chưa có_ |
| Role Play: Mediating Different Working Styles | T11 | _chưa có_ |
| "When they push back": LISTEN → ACKNOWLEDGE → REFOCUS → HOLD | T8 | _chưa có_ |

### `PRB-011` · 11. Dẫn dắt thay đổi
**Level:** ORG

| Framework ứng viên `[SUY LUẬN]` | Topic | ID chunk |
|---|---|---|
| Kotter (2012) Leading Change Through Stakeholder Coalitions (dùng chọn lọc, không phải đủ 8 bước) | T12 | _chưa có_ |
| Transformation Design Framework — 8 yếu tố | T6 | `FW-007` |
| Knowledge–Behaviour Gap Model · Stages of Transformation | T5, T6 | `FW-007` (phần Circles) |
| AI as the Sixth Force · C-FISH / E-MICE / O-LION Leadership OS | T18 | _chưa có_ |
| Case: Microsoft Rebuilding Trust from the Top (Nadella) | T12 + case reading | _chưa có_ |

---

## Khoảng trống đã nhận diện

Chưa phát hiện vấn đề nào trong 11 vấn đề **không có** framework ứng viên nào trong MEGROW. Sẽ xác nhận lại sau khi xử lý hết 20 topic và ghi vào `open_questions.md` nếu có khoảng trống thật.

**Đã xác nhận sau khi xử lý Topic 01, 06, 10:** mọi framework ứng viên liệt kê cho ba topic này đều có thật trong tài liệu — không có mục nào phải gỡ. Phát hiện thêm hai framework không có trong danh sách ứng viên ban đầu: **Human Artificial Intelligence (HAI)** và **Theory of Psychological Ownership**, cả hai từ Topic 06.

Lưu ý riêng cho bối cảnh người dùng: MEGROW không có nội dung chuyên biệt về **quản lý cộng tác viên (collaborator)** — nhân sự không chính thức, mức gắn kết khác nhân viên chính thức. Khả năng cần `[BỔ SUNG]` khi viết `PB` cho vấn đề số 5. Xem `open_questions.md` (OQ-005).
