# courses.md — Danh mục khóa học

Mỗi khóa học có một mã cố định (chữ in hoa, không dấu). Mã đặt một lần và **không bao giờ đổi**.

| Mã khóa | Tên khóa | Đơn vị tổ chức | Thời gian | Thư mục `raw/` | Cấu trúc | Số tài liệu | Số trang | Trạng thái |
|---|---|---|---|---|---|---:|---:|---|
| `MEGROW` | me.grow (2026) L2 Leadership Development Program | The Business School, RMIT University Vietnam — phối hợp với Zalo | 2026 (Capstone trình bày 20/11/2026) | `raw/megrow/` | 20 topic / 3 pillar | 22 | 805 | Đã inventory, chưa xử lý chunk |

---

## MEGROW — me.grow (2026) L2 Leadership Development Program

**Đối tượng:** leader cấp L2.2 và L2.3 tại Zalo, đang chuyển sang phạm vi lãnh đạo rộng hơn.

**Hình thức:** workshop tương tác, peer learning, áp dụng vào công việc, Capstone Project theo nhóm (task force ~8 người).

**Thư mục gốc:** `raw/megrow/` — 20 file slide theo topic + 2 file case reading.

**Địa điểm:** RMIT University Vietnam, Saigon South Campus.

### Ánh xạ pillar → level

> ⚠️ **Taxonomy do người dùng duyệt, không phải cấu trúc RMIT chính thức đã kiểm chứng.**
> Nhãn: `[SUY LUẬN — người dùng duyệt 2026-11-07]`.
> Lý do: đã quét toàn bộ 805 trang của 22 tài liệu, **không trang nào ghi pillar** hay tên pillar ("Master the Personal Shift", "Develop the Team Talent", "Navigate the Strategic Landscape"). Footer slide chỉ có dạng `RMIT | Zalo me.grow`. CLAUDE.md §4 cấm đoán, nên ánh xạ dưới đây lấy từ chỉ định trực tiếp của người dùng. Xem mục đối chiếu trong `open_questions.md` (OQ-001).

| Pillar | Tên pillar (người dùng đặt) | Topic | Level chính |
|---|---|---|---|
| P1 | `LEAD_SELF` | 1 – 5 | `SELF` |
| P2 | `LEAD_PEOPLE_AND_TEAMS` | 6 – 11 | `TEAM` |
| P3 | `LEAD_ACROSS_ORGANISATION` | 12 – 20 | `ORG` |

### Ràng buộc kèm theo taxonomy (người dùng chỉ định)

1. **Giữ nguyên số topic gốc và mọi tham chiếu nguồn.** Topic giữ đúng số trong tên file; `source` luôn trỏ về file và số trang thật.
2. **Cho phép quan hệ framework xuyên pillar.** `related_ids` của một chunk không bị giới hạn trong cùng pillar — ví dụ Situational Leadership xuất hiện ở cả Topic 1 (P1), Topic 6 (P2) và Topic 10 (P2) và phải liên kết chéo tự do.
3. **Không giới hạn truy xuất theo pillar chính.** Pillar chỉ quyết định level *chính* của topic. Chunk được gán thêm level phụ khi nội dung thực sự thuộc về level đó.

Ví dụ áp dụng ràng buộc 3:

| Topic | Pillar → level chính | Level phụ nên thêm | Lý do |
|---|---|---|---|
| Topic 12 Stakeholder Influence | ORG | — | Đúng level |
| Topic 13 Building Trust in Teams | ORG | `TEAM` | Nội dung hoàn toàn về đội nhóm (TRUST Framework, Psychological Safety) |
| Topic 14 Decision Making in Cross-functional Teams | ORG | `TEAM` | Ladder of Inference, group dynamics áp dụng trong team |
| Topic 18 Leading in the AI-Enabled Organisation | ORG | `TEAM`, `SELF` | EEE diagnostic dùng ở cấp team; C-FISH là phẩm chất cá nhân |
| Topic 4 Practice Performance Conversations | SELF | `TEAM` | AMO và SAIL là hội thoại với nhân viên |
| Topic 2 Driving Operational Execution | SELF | `TEAM`, `ORG` | Chuỗi Corporate → Business → Functional → Operational chạm cả ba level |

### Giảng viên

| Giảng viên | Topic phụ trách |
|---|---|
| AP Burkhard Schrage | 1, 17, 20 |
| Dr Phuong (Emmy) Hoang | 2 |
| Dr Thu Nguyen | 3 |
| AP Elaine Chew | 4 |
| AP Agnis Stibe | 5, 6 |
| Dr Thao Luong | 7, 8 |
| Dr Quyen Dang | 9 |
| Dr Tony Nguyen | 10, 19 |
| Dr Gavin Nicholson | 11 |
| Prof Seng Kiat Kok | 12 |
| Dr Justin Xavier Batinadan | 13 |
| Dr Phuong Nguyen | 14, 15 |
| Dr Thuan Nguyen & Dr Bidyut Hazarika | 16 |
| Prof Trung Nguyen | 18 |

### Capstone

Topic 20 vừa là một topic được đánh số, vừa là **phiên định hướng Capstone** (6/11/2026). Vì vậy nó nhận `TOP-MEGROW-20` **và** nhãn `CAPSTONE`.

- Case giả định: **Lumo**, nền tảng Việt Nam, đang thử nghiệm agent AI thường trực **Mira**. Lumo được dựng gần với thế giới Zalo để học viên nói thẳng.
- 7 task force, 3 mandate (A: agent cá nhân hay doanh nghiệp trước; B: go-to-market agent cá nhân; C: go-to-market agent doanh nghiệp).
- 4 vai trong mỗi task force: Product & Market Development Lead, Engineering Lead, Data and AI Lead, Trust & Safety Lead.
- Trình bày 20/11/2026, 15 phút + 5 phút hỏi đáp. Rubric 5 tiêu chí × 20 điểm.

> ⚠️ Slide 21–27 của Topic 20 chứa **tên thật của học viên** trong danh sách task force. Theo CLAUDE.md §7 (CASE luôn ẩn danh) và §12, **không trích tên thật vào bất kỳ chunk nào**. Xem `open_questions.md` (OQ-003).
