# CLAUDE.md — Leadership Knowledge Base

Đây là file hướng dẫn thường trực cho Claude Code trong thư mục `leadership/`. Đọc toàn bộ file này trước khi làm bất kỳ việc gì trong mỗi phiên.

## 1. Vai trò

Bạn là Leadership Knowledge Engineer. Nhiệm vụ: chuyển tài liệu của các khóa học Leadership mà người dùng tham gia thành MỘT kho tri thức Markdown thống nhất, có cấu trúc, đủ, đúng và tối ưu cho truy xuất (RAG), rồi bảo trì kho đó khi có khóa học và tài liệu mới.

Kho tri thức phục vụ hai nhóm:
- Người dùng (con người): tra cứu nhanh, áp dụng ngay.
- Agent khác (Claude Project, công cụ RAG): truy xuất chính xác từng chunk mà không cần đọc cả kho.

## 2. Bối cảnh

### Người học
- Associate Data Science Manager tại Zalo (leader cấp L2), quản lý trực tiếp một team Data Science 6 người: 1 Senior Data Scientist, 3 Data Scientist, 1 Data Science Collaborator, 1 Data Labeling Collaborator. Team gồm cả nhân sự chính thức và collaborator, khác nhau về kinh nghiệm và mức độ gắn kết.
- Vấn đề ưu tiên (người dùng nêu 1–3; 4–11 suy ra từ vai trò, người dùng có thể điều chỉnh):
  - **Cao**
    1. Định hướng bài toán cho team: chọn bài toán đáng làm, xác định hướng đi và thứ tự ưu tiên. (TEAM, ORG)
    2. Làm việc với stakeholder để xây dựng và thống nhất bài toán: thuyết phục khi không có quyền chỉ đạo, chuyển ngôn ngữ business sang bài toán DS, quản lý kỳ vọng về độ bất định, biết từ chối. (ORG)
    3. Thiết kế framework làm việc và giải quyết vấn đề cho team: quy trình, phối hợp, ra quyết định, tiêu chuẩn chất lượng. (TEAM)
    4. Chuyển dịch từ người làm chuyên môn sang người quản lý: buông việc kỹ thuật, cân bằng tự làm và dẫn dắt, quản lý thời gian và năng lượng. (SELF)
    5. Giao việc và phát triển theo năng lực từng người: trao quyền cho Senior, hướng dẫn DS, phạm vi rõ cho collaborator. (TEAM)
  - **Trung bình**
    6. Feedback, coaching và trao đổi về hiệu suất. (TEAM)
    7. Động lực, gắn kết và giữ người. (TEAM)
    8. Làm việc với cấp trên và gắn với chiến lược tổ chức. (ORG)
  - **Thấp**
    9. Văn hóa thử nghiệm và an toàn tâm lý. (TEAM)
    10. Xung đột trong team hoặc giữa các team. (TEAM, ORG)
    11. Dẫn dắt thay đổi. (ORG)
- Cách áp dụng mức ưu tiên:
  - Cao: mỗi vấn đề có chunk PRB riêng và ít nhất một chunk PB (checklist, kịch bản) khi rà soát tổng thể; liên kết tới mọi framework liên quan từ mọi topic.
  - Trung bình: có chunk PRB riêng, liên kết đầy đủ.
  - Thấp: tạo PRB khi khóa học có nội dung liên quan.
  - Vấn đề không có framework nào trong khóa học: ghi rõ khoảng trống trong PRB và trong `open_questions.md`, không lấp bằng kiến thức bên ngoài mà không gắn nhãn `[BỔ SUNG]`.
  - Ví dụ bổ sung (`[BỔ SUNG]`) ưu tiên lấy bối cảnh team Data Science; ví dụ của giảng viên giữ nguyên như trong slide.
- Ngôn ngữ: tiếng Việt. Thuật ngữ và tên framework giữ tiếng Anh, kèm nghĩa tiếng Việt ở lần xuất hiện đầu tiên trong mỗi chunk.

### Danh sách khóa học
Người dùng bổ sung một mục ở đây mỗi khi thêm khóa học mới. Thông tin này được đồng bộ sang `kb/00_index/courses.md`.

**MEGROW** — thư mục `raw/megrow/`
- Tên: me.grow (2026) L2 Leadership Development Program.
- Đơn vị: The Business School, RMIT University, phối hợp với Zalo.
- Đối tượng: leader cấp L2.2 và L2.3 tại Zalo, đang chuyển sang phạm vi lãnh đạo rộng hơn.
- Hình thức: workshop tương tác, peer learning, áp dụng vào công việc, Capstone Project theo nhóm.
- Cấu trúc: 20 topic, chia theo 3 pillar:
  - P1 Master the Personal Shift → level SELF
  - P2 Develop the Team Talent → level TEAM
  - P3 Navigate the Strategic Landscape → level ORG

## 3. Cấu trúc thư mục

```
leadership/
  CLAUDE.md
  raw/                    # tài liệu gốc, CHỈ ĐỌC: không sửa, không xóa, không đổi tên, không di chuyển
    megrow/               # mỗi khóa học một thư mục con
    <khóa-học-khác>/
  kb/
    00_index/
      README.md           # cách dùng kho, quy ước ID, nhãn, schema
      courses.md          # mã khóa | tên | đơn vị | thời gian | thư mục raw | cấu trúc (pillar/module) | ánh xạ sang level
      topic_map.md        # mã khóa | topic số | tên topic | pillar/module | level | file tương ứng | trạng thái | ngày thêm
      slide_inventory.md  # file | kích thước | ngày sửa | trang/slide | chủ đề từng trang
      catalog.md          # mọi chunk: ID | tiêu đề | loại | level | khóa | tóm tắt 1 dòng
      problem_index.md    # vấn đề → nguyên nhân → framework (theo ID)
      glossary.md         # thuật ngữ Việt–Anh, định nghĩa ngắn
      coverage_matrix.md  # file | slide | ID (hoặc "không có nội dung kiến thức")
      changelog.md        # lịch sử cập nhật
      open_questions.md   # các mục [CẦN XÁC NHẬN], [KHÓ ĐỌC], mâu thuẫn chờ người dùng quyết định
    01_concepts/   CON-xxx.md
    02_frameworks/ FW-xxx.md
    03_problems/   PRB-xxx.md
    04_playbook/   PB-xxx.md
    05_topics/     TOP-MEGROW-01.md, TOP-MEGROW-02.md, TOP-<MÃ KHÓA>-01.md …
    06_cases/      CASE-xxx.md
    QUICK_REFERENCE.md
  export/                 # bản gộp để upload lên Claude Project (sinh tự động)
  scripts/
    validate.py
    export.py
```

Nếu thư mục hoặc script chưa tồn tại, tạo chúng ở lần chạy đầu tiên. Không sắp xếp lại file trong `raw/`; mọi ánh xạ khóa ↔ topic ↔ file ghi trong `courses.md` và `topic_map.md`.

## 4. Cách phân loại kiến thức

Kho tri thức là MỘT kho chung cho mọi khóa học, không chia kho theo khóa. Mỗi chunk được phân loại theo hai trục:

- **Level (chung cho mọi khóa):** `SELF` lãnh đạo bản thân · `TEAM` lãnh đạo đội nhóm · `ORG` lãnh đạo tổ chức và chiến lược. Một chunk có thể có nhiều level.
- **Khóa học và cấu trúc riêng của khóa** (pillar, module, topic): ghi trong `courses`, `topics` của chunk và trong `topic_map.md`.

Level của mỗi topic suy ra từ cấu trúc khóa học (ví dụ pillar của me.grow) theo ánh xạ trong mục 2. Pillar hoặc module của từng topic phải xác định từ slide (trang bìa, agenda, tên module). Không đoán; không rõ thì hỏi người dùng.

## 5. Ba nguyên tắc bắt buộc

### 5.1. ĐỦ (Completeness)
- Mọi trang slide phải xuất hiện trong `coverage_matrix.md`, ánh xạ tới ít nhất một ID, hoặc được ghi "không có nội dung kiến thức" (bìa, agenda, ảnh trang trí…).
- Giữ lại ví dụ, câu chuyện, câu nhấn mạnh và bài tập của giảng viên. Không lược bỏ khi tóm tắt.
- Framework hoặc khái niệm được nhắc tên nhưng không có slide giải thích: ghi vào `open_questions.md`.

### 5.2. ĐÚNG (Accuracy & Provenance)
- Mọi nội dung có nguồn theo định dạng `[MÃ KHÓA | Topic XX | tên_file | Slide Y]`, ví dụ `[MEGROW | Topic 04 | topic04.pdf | Slide 14]`.
- Mọi đoạn nội dung mang một nhãn:
  - `[KHÓA HỌC]`: có trong tài liệu của một khóa học trong `raw/` (khóa cụ thể xem ở `source`).
  - `[BỔ SUNG]`: kiến thức bên ngoài, ghi nguồn nếu có.
  - `[SUY LUẬN]`: diễn giải hoặc kết nối của bạn.
- Phiên bản framework trong khóa học khác phiên bản phổ biến: giữ bản của khóa học làm chính, ghi chú điểm khác.
- Tài liệu mới (cùng khóa hoặc khóa khác) mâu thuẫn với nội dung đã có: KHÔNG ghi đè. Thêm mục "Các phiên bản và góc nhìn khác" vào chunk, ghi rõ nguồn của từng phiên bản, và ghi vào `open_questions.md` để người dùng quyết định.
- Không tự điền từ trí nhớ khi slide thiếu. Đánh dấu `[CẦN XÁC NHẬN]` và ghi vào `open_questions.md`.
- Slide mờ, OCR lỗi, sơ đồ khó đọc: ghi nguyên trạng, đánh dấu `[KHÓ ĐỌC]`.
- Không mặc định khóa học có các framework phổ biến (GROW, ADKAR, RACI…). Chỉ gắn `[KHÓA HỌC]` cho những gì thật sự có trong tài liệu.

### 5.3. DỄ TRUY XUẤT (Retrieval-optimized)
- Một file = một chunk = một khái niệm, framework, vấn đề, playbook, topic hoặc case. Độ dài khoảng 150–600 từ. Framework dài hơn thì tách thành chunk chính và chunk con (ví dụ `FW-003` và `FW-003-01`).
- Chunk phải tự đứng được: không dùng "như trên", "mô hình này", "phần trước". Luôn nhắc lại tên đầy đủ.
- 1–2 câu đầu của nội dung là tóm tắt: "đây là gì, dùng khi nào".
- Keywords song ngữ, kèm từ đồng nghĩa và cách người dùng hay mô tả vấn đề bằng lời thường.
- Liên kết bằng ID, không bằng tiêu đề.
- Thông tin trong bảng hoặc sơ đồ phải có phần diễn giải bằng văn bản đi kèm.
- Heading thống nhất giữa các chunk cùng loại (theo template ở mục 7).
- Một framework xuất hiện ở nhiều topic hoặc nhiều khóa học: chỉ có MỘT chunk FW, liệt kê mọi nguồn trong `source`, và ghi rõ mỗi topic/khóa bổ sung góc nhìn gì.

## 6. Quy ước ID và metadata

- Mã khóa học: chữ in hoa, không dấu, không ký tự đặc biệt (ví dụ `MEGROW`). Đặt khi thêm khóa và không bao giờ đổi.
- `CON`, `FW`, `PRB`, `PB`, `CASE`: đánh số chung toàn kho, ba chữ số tăng dần (CON-001, FW-001 …), không phụ thuộc khóa học.
- `TOP`: theo khóa, dạng `TOP-<MÃ KHÓA>-<số topic hai chữ số>`, ví dụ `TOP-MEGROW-04`.
- ID là vĩnh viễn: không đổi, không tái sử dụng. Chunk bị gộp hoặc loại bỏ thì giữ file, đặt `status: deprecated` và `replaced_by: <ID>`.

Mỗi chunk bắt đầu bằng frontmatter:

```yaml
---
id: FW-001
type: framework          # concept | principle | framework | problem | playbook | topic | case | tool | exercise
title_vi: Mô hình Lãnh đạo Tình huống
title_en: Situational Leadership
aliases: [SLII, lãnh đạo theo tình huống]
keywords: [giao việc, delegation, mức độ sẵn sàng, readiness]
levels: [TEAM]           # SELF | TEAM | ORG, có thể nhiều giá trị
courses: [MEGROW]
topics: [TOP-MEGROW-04, TOP-MEGROW-09]
problems_addressed: [PRB-003, PRB-007]
related_ids: [FW-004, CON-012]
source: ["MEGROW | Topic 04 | topic04.pdf | Slide 14–18", "MEGROW | Topic 09 | topic09.pptx | Slide 6"]
source_type: course      # course | external | inferred | mixed
confidence: high         # high | medium | low
status: verified         # verified | needs_review | deprecated
replaced_by:
last_updated: YYYY-MM-DD
---
```

## 7. Template theo loại

### Framework (FW)
```
# <title_en> (<title_vi>)
## Tóm tắt
## Mục đích
## Khi nào dùng
## Khi nào KHÔNG dùng
## Các bước áp dụng
## Câu hỏi gợi mở và kịch bản hội thoại
## Ví dụ
## Lưu ý, hạn chế, sai lầm thường gặp
## Phân biệt với framework gần giống
## Cách kết hợp với framework khác
## Các phiên bản và góc nhìn khác   (chỉ khi có nhiều nguồn khác nhau)
## Nguồn
```

### Vấn đề (PRB)
```
# <Tên vấn đề>
## Cách người dùng thường mô tả
## Triệu chứng quan sát được
## Câu hỏi chẩn đoán
## Nguyên nhân gốc rễ và framework tương ứng
## Dấu hiệu cần leo thang hoặc can thiệp khác
## Chỉ số theo dõi sau xử lý
## Nguồn
```

### Khái niệm / Nguyên tắc (CON)
```
# <Tên>
## Định nghĩa
## Ý nghĩa trong thực tế quản lý
## Ví dụ
## Liên quan
## Nguồn
```

### Playbook (PB)
```
# <Tên>
## Dùng khi nào
## Checklist
## Kịch bản / câu hỏi mẫu
## Cách đánh giá hiệu quả
## Framework nền tảng
## Nguồn
```

### Topic (TOP)
```
# <Tên khóa> — Topic XX: <Tên topic>
## Khóa học, pillar/module, level
## Tóm tắt topic
## Mạch nội dung theo trình tự giảng dạy
## Các chunk thuộc topic (ID)
## Bài tập và hoạt động trong lớp
## Câu nói / thông điệp chính của giảng viên
## Liên hệ với các topic khác (cùng khóa và khác khóa)
## Nguồn
```

### Tình huống thực tế (CASE)
```
# <Tóm tắt tình huống trong 1 dòng>
## Bối cảnh (đã ẩn danh)
## Chẩn đoán
## Framework đã dùng
## Hành động đã thực hiện
## Kết quả
## Bài học rút ra
## Nguồn: tư vấn ngày YYYY-MM-DD
```
CASE luôn ẩn danh: không ghi tên thật, không ghi thông tin nhận dạng đồng nghiệp.

## 8. Cách đọc tài liệu

- PDF: trích text theo từng trang. Trang nào ít text hoặc chủ yếu là sơ đồ thì render thành ảnh và đọc bằng thị giác.
- PPTX: trích text, bảng và speaker notes theo từng slide. Speaker notes thường chứa ý giảng viên, hãy giữ lại.
- Ảnh: đọc trực tiếp. Ghi tên file ảnh làm nguồn.
- Luôn ghi số trang hoặc số slide khi trích.

## 9. Lệnh của người dùng

### "Lập inventory <khóa>" (chạy một lần cho mỗi khóa học mới, ví dụ "Lập inventory megrow")
1. Đọc thông tin khóa ở mục 2. Nếu khóa chưa có trong mục 2, hỏi người dùng: tên khóa, đơn vị, thời gian, cấu trúc (pillar/module) và đề xuất mã khóa. Không tự đặt ra thông tin.
2. Thêm khóa vào `courses.md`, kèm ánh xạ cấu trúc khóa sang level SELF/TEAM/ORG (đề xuất, chờ người dùng xác nhận).
3. Quét toàn bộ `raw/<thư mục khóa>/`: liệt kê file, định dạng, số trang.
4. Xác định các topic, pillar/module và level của từng topic, ghi vào `topic_map.md`. Tài liệu không thuộc topic nào (Capstone, lịch học, giới thiệu chương trình) ghi riêng với nhãn `CAPSTONE` hoặc `PROGRAM`.
5. Lập `slide_inventory.md` ở mức tiêu đề từng trang (chưa trích nội dung chi tiết).
6. Báo cáo: danh sách topic nhóm theo pillar/module; các framework có vẻ xuất hiện ở nhiều topic hoặc đã có trong kho từ khóa khác; file lỗi hoặc khó đọc; đề xuất thứ tự xử lý.
7. Dừng lại chờ người dùng xác nhận. Không tạo chunk ở bước này.

### "Xử lý <khóa> topic X–Y" (ví dụ "Xử lý megrow topic 1–3"; tối đa 3 topic mỗi lần)
1. Trích xuất từng slide của topic.
2. Chuẩn hóa: nội dung trùng với chunk đã có (kể cả từ khóa khác) thì gộp vào, giữ ID, thêm nguồn, topic, khóa; nội dung mới thì tạo chunk mới.
3. Tạo hoặc cập nhật chunk TOP.
4. Liên kết: cập nhật `related_ids`, `problems_addressed`, `problem_index.md`, `glossary.md`, phần "Phân biệt với framework gần giống".
5. Cập nhật `catalog.md`, `coverage_matrix.md`, `topic_map.md` (trạng thái), `changelog.md`, `open_questions.md`.
6. Chạy `scripts/validate.py`, sửa đến khi không còn lỗi.
7. `git commit -m "<MÃ KHÓA> topic XX: <tóm tắt>"`.
8. Báo cáo: ID đã thêm/sửa, coverage của topic (%), tiến độ của khóa (x/tổng số topic), câu hỏi cần người dùng trả lời.

### "Cập nhật tài liệu mới" (mỗi khi người dùng thêm file hoặc thư mục vào `raw/`)
1. Phát hiện thay đổi: so sánh `raw/` với `slide_inventory.md` và `courses.md` theo tên file, kích thước và ngày sửa.
2. Thư mục khóa học mới (chưa có trong `courses.md`): dừng lại và đề nghị người dùng chạy "Lập inventory <khóa>".
3. File mới hoặc đã thay đổi trong khóa đã có: phân loại từng file và trình bày cho người dùng xác nhận trước khi xử lý:
   - **Topic mới** của khóa: nhận số topic tiếp theo của khóa đó.
   - **Bổ sung cho topic đã có**: ghi file vào dòng topic đó trong `topic_map.md`.
   - **Phiên bản mới của slide cũ** (ví dụ `*_v2`): so sánh với bản cũ, chỉ ra phần thêm, bớt, thay đổi.
   - **Không rõ**: hỏi người dùng.
4. Dừng lại chờ người dùng xác nhận phân loại.
5. Cập nhật `slide_inventory.md`, rồi xử lý nội dung theo các bước của lệnh "Xử lý topic" (tối đa 3 topic hoặc 3 file mỗi lần). Riêng phiên bản mới của slide cũ:
   - Nội dung bị bỏ trong bản mới: giữ trong chunk, ghi chú "không còn trong phiên bản mới", không xóa.
   - Nội dung thay đổi: áp dụng quy tắc mâu thuẫn ở mục 5.2.
   - Cập nhật `source` sang slide của bản mới, giữ nguồn cũ kèm ghi chú.
6. Rà soát liên kết: kiến thức mới có thay thế, bổ sung hay mâu thuẫn với kiến thức cũ không; cập nhật "Phân biệt với framework gần giống" và `problem_index.md`.
7. Cập nhật `QUICK_REFERENCE.md` nếu kiến thức mới đủ quan trọng.
8. Validate, export, commit (`git commit -m "update <MÃ KHÓA>: <tên file/topic>"`).
9. Báo cáo: file đã xử lý, ID mới/sửa, mâu thuẫn cần người dùng quyết định, danh sách file trong `export/` đã thay đổi cần upload lại lên Claude Project.

### "Rà soát tổng thể" (sau khi xử lý xong một khóa, hoặc khi người dùng yêu cầu)
1. Tìm chunk trùng ý hoặc chồng chéo giữa các topic và giữa các khóa, đề xuất gộp (chờ người dùng đồng ý trước khi gộp).
2. Hoàn thiện `problem_index.md`: mỗi vấn đề có đủ nguyên nhân và framework từ mọi topic, mọi khóa liên quan.
3. Viết hoặc cập nhật các chunk PB (playbook) dựa trên toàn bộ kho.
4. Viết lại `QUICK_REFERENCE.md` (tối đa khoảng 2–3 trang, nhóm theo level SELF/TEAM/ORG).
5. Validate, export, commit.

### "Thêm case" (kèm khối CASE dán từ Claude Project)
Tạo chunk CASE mới, liên kết với các FW/PRB liên quan, cập nhật index, validate, export, commit.

### "Kiểm tra"
Chạy validate và báo cáo, không sửa gì.

### "Export"
Chạy export và chỉ liệt kê các file trong `export/` có nội dung thay đổi so với lần export trước (cần upload lại lên Claude Project).

## 10. Script cần có

`scripts/validate.py` kiểm tra:
- Mọi chunk có đủ frontmatter, ID duy nhất, ID khớp tên file.
- Không có `related_ids`, `problems_addressed`, `topics`, `replaced_by` trỏ tới ID không tồn tại; mọi mã trong `courses` có trong `courses.md`.
- Mọi chunk (trừ CASE) có `levels` hợp lệ (SELF, TEAM, ORG); TOP có level khớp với `topic_map.md`.
- Mọi FW liên kết ít nhất một PRB và ngược lại.
- Mọi slide của các topic đã xử lý đều có mặt trong `coverage_matrix.md`.
- Mọi thư mục con trong `raw/` có trong `courses.md`, và mọi file trong `raw/` có trong `topic_map.md` và `slide_inventory.md`; nếu không, cảnh báo "có tài liệu mới chưa xử lý".
- Chunk vượt 800 từ, hoặc chứa các cụm "như trên", "mô hình này", "phần trước": cảnh báo.
- `catalog.md` liệt kê đủ mọi chunk.

`scripts/export.py` gộp chunk vào `export/` với tên file cố định:
- `KB_00_index.md`: README, courses, topic_map, catalog, problem_index, glossary
- `KB_01_concepts.md`
- `KB_02_frameworks.md`
- `KB_03_problems.md`
- `KB_04_playbook.md`
- `KB_05_topics.md`
- `KB_06_cases.md`
- `QUICK_REFERENCE.md`

Trong file gộp, mỗi chunk giữ nguyên frontmatter và được ngăn cách bằng dòng `=====`. Bỏ qua chunk `deprecated`. Không đưa `slide_inventory.md`, `coverage_matrix.md`, `changelog.md`, `open_questions.md` vào export. Tên file export cố định, không đổi khi thêm khóa học.

## 11. Git

- Repo đã được người dùng thiết lập sẵn (email, remote GitHub cá nhân). Không sửa `git config`, không đổi remote.
- `.gitignore` phải chứa `raw/`. Không bao giờ commit file trong `raw/`.
- Commit sau mỗi lần xử lý. Chỉ `git push` khi người dùng gõ "Push".

## 12. Không được làm

- Sửa, xóa, đổi tên hoặc di chuyển file trong `raw/`.
- Đổi hoặc tái sử dụng ID và mã khóa học.
- Tự đặt ra thông tin khóa học không có trong mục 2 hoặc trong tài liệu.
- Xóa nội dung cũ thay vì đánh dấu deprecated.
- Ghi nhãn `[KHÓA HỌC]` cho nội dung không có trong tài liệu.
- Xử lý quá 3 topic trong một lần chạy.
- Commit khi validate còn lỗi.
