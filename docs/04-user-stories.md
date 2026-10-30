# 04 — User Stories (INVEST) & Acceptance Criteria

> Trạng thái thiết kế: **TARGET V1**
>
> Mỗi user story tương ứng với một use case cùng số (USxx ↔ UCxx). Các yêu cầu chung (xác thực, phân quyền, validate, audit, xử lý lỗi) là **ràng buộc chấp nhận**, không tách thành tính năng riêng.

## 1. Tiêu chí INVEST áp dụng

| Tiêu chí | Cách áp dụng trong ReLoop |
|---|---|
| **Independent** | Mỗi story tạo ra một kết quả demo được; chỉ phụ thuộc story khác khi thật sự cần (ghi ở cột *Phụ thuộc*). |
| **Negotiable** | Bố cục UI và cách cài đặt có thể đổi, miễn giữ nguyên mục tiêu, quy tắc nghiệp vụ và quyền. |
| **Valuable** | Mỗi story nêu rõ lợi ích cho một vai trò và gắn với painpoint P1–P6. |
| **Estimable** | Đầu vào, đầu ra, vai trò, quy tắc (BRxx) và ngoại lệ đều được ghi rõ. |
| **Small** | Mỗi story là một năng lực, làm xong trong ≤ 3 ngày/người, chia được thành task API / DB / UI / test. |
| **Testable** | Mỗi story có acceptance criteria quan sát được (mục 4). |

## 2. Product Backlog

Ưu tiên theo MoSCoW. Kế hoạch 5 tuần: **Tuần 1** làm tài liệu & dựng khung, **Sprint 1–4** tương ứng tuần 2–5.

| ID | User story | Giá trị (painpoint) | Ưu tiên | Sprint | Phụ thuộc |
|---|---|---|---|---|---|
| US01 | Là người dùng đang hoạt động, tôi muốn **đăng nhập** để truy cập đúng khu vực theo vai trò. | Truy cập an toàn | Must | S1 | Tài khoản seed |
| US02 | Là người dùng đã đăng nhập, tôi muốn **đăng xuất** để phiên làm việc trên thiết bị này kết thúc. | An toàn phiên | Must | S1 | US01 |
| US03 | Là người dùng quên mật khẩu, tôi muốn **nhận link đặt lại mật khẩu qua email** để tự lấy lại quyền truy cập. | Tự phục vụ | Could | S4 | US01 |
| US04 | Là nhân viên hoặc người gửi được mời, tôi muốn **kích hoạt tài khoản bằng link mời** và tự đặt mật khẩu. | Onboarding nhanh | Must | S2 | US08, US31 |
| US05 | Là người dùng, tôi muốn **cập nhật hồ sơ và đổi mật khẩu** mà không đổi được vai trò của mình. | Tự phục vụ | Should | S4 | US01 |
| US06 | Là người dùng, tôi muốn xem **dashboard theo phạm vi vai trò** để nắm nhanh tình hình. | Tổng quan (P3, P5) | Should | S4 | US22, US24 |
| US07 | Là chủ shop hoặc nhân viên, tôi muốn **tạo và tra cứu người ký gửi**; chỉ chủ shop được sửa, vô hiệu hóa và đặt chính sách chia riêng. | Quản lý chủ sở hữu hàng (P4) | Must | S1 | US01 |
| US08 | Là chủ shop hoặc nhân viên, tôi muốn **gửi link mời** để người gửi dùng cổng riêng. | Minh bạch (P5) | Must | S2 | US07 |
| US09 | Là chủ shop hoặc nhân viên, tôi muốn **tạo phiếu nhận hàng theo lô** với ảnh, thông tin, giá niêm yết, giá sàn cho từng món. | Số hóa nhận hàng (P1) | Must | S1 | US07, US32 |
| US10 | Là nhân viên, tôi muốn **AI nhận diện ảnh và tự điền** danh mục, thương hiệu, size, màu, tình trạng, mô tả để không phải gõ tay. | Nhận hàng nhanh (P1) | Must | S3 | US09 |
| US11 | Là chủ shop, tôi muốn **AI gợi ý giá kèm lý do** dựa trên hàng tương tự đã bán của shop để định giá có căn cứ. | Định giá đúng (P2) | Must | S3 | US09, US22 |
| US12 | Là người gửi, tôi muốn **xem và xác nhận (hoặc yêu cầu sửa) phiếu nhận hàng** trước khi hàng lên kệ; chủ shop có thể xác nhận tại quầy. | Đồng thuận giá (P6) | Must | S2 | US04, US09 |
| US13 | Là nhân viên, tôi muốn **in tem QR** cho các món đã xác nhận để dán lên hàng và quét khi bán. | Bán nhanh, không nhầm | Should | S2 | US12 |
| US14 | Là chủ shop hoặc nhân viên, tôi muốn **tìm và lọc kho hàng** theo trạng thái, danh mục, người gửi, tuổi tồn. | Kiểm soát tồn (P3) | Must | S1 | US09 |
| US15 | Là chủ shop, tôi muốn **điều chỉnh giá món đang bán** trong khoảng từ giá sàn trở lên, có ghi lịch sử giá. | Linh hoạt giá | Should | S2 | US14 |
| US16 | Là chủ shop, tôi muốn hệ thống **tự giảm giá theo lịch** (BR03) và không bao giờ xuống dưới giá sàn. | Giảm tồn kho (P3, P6) | Must | S3 | US14, US32 |
| US17 | Là chủ shop, tôi muốn **gửi yêu cầu giảm dưới giá sàn** kèm lý do cho người gửi. | Đồng thuận (P6) | Should | S3 | US14 |
| US18 | Là người gửi, tôi muốn **đồng ý hoặc từ chối yêu cầu giảm giá** trên cổng. | Kiểm soát hàng của mình (P6) | Should | S3 | US17, US04 |
| US19 | Là chủ shop hoặc nhân viên, tôi muốn **danh sách hàng sắp/đã hết hạn** và ghi nhận *trả lại* hoặc *thanh lý* theo BR07. | Kho không ứ đọng (P3) | Must | S3 | US14 |
| US20 | Là chủ shop, tôi muốn **báo thất lạc/hư hỏng** để hệ thống ghi nhận bồi thường theo BR12. | Trách nhiệm rõ ràng | Could | S4 | US14 |
| US21 | Là nhân viên, tôi muốn **AI viết caption đăng bán** từ thông tin món hàng để đăng Facebook/Instagram nhanh. | Tiết kiệm thời gian | Could | S4 | US14 |
| US22 | Là nhân viên, tôi muốn **bán hàng bằng cách quét mã**; hệ thống tự ghi phần chia tạm giữ cho từng người gửi. | Bán & ghi nhận tự động (P4) | Must | S2 | US14 |
| US23 | Là nhân viên, tôi muốn **xử lý đổi trả trong thời hạn**; ngoài thời hạn chỉ chủ shop làm được. | Đúng chính sách (BR08) | Should | S3 | US22 |
| US24 | Là người gửi, tôi muốn **xem số dư (tạm giữ / khả dụng) và lịch sử giao dịch**; chủ shop xem được của mọi người gửi. | Minh bạch tiền (P4, P5) | Must | S2 | US22 |
| US25 | Là người gửi, tôi muốn **yêu cầu rút tiền** từ số dư khả dụng. | Nhận tiền chủ động | Must | S3 | US24, US28 |
| US26 | Là chủ shop, tôi muốn **duyệt yêu cầu rút tiền bằng mã VietQR sinh sẵn** rồi đánh dấu đã chuyển. | Chi trả nhanh, không nhầm STK (P4) | Must | S3 | US25 |
| US27 | Là chủ shop hoặc người gửi, tôi muốn **xuất sao kê theo kỳ (PDF)**. | Đối soát nhanh (P4) | Should | S4 | US24 |
| US28 | Là chủ shop, tôi muốn hệ thống **tự chuyển tiền tạm giữ sang khả dụng** sau thời hạn đổi trả (BR05). | Đối soát tự động (P4) | Must | S3 | US22 |
| US29 | Là người gửi, tôi muốn **xem danh sách hàng của mình** với trạng thái, giá hiện tại, số ngày còn lại. | Hết phải nhắn hỏi (P5) | Must | S2 | US04, US12 |
| US30 | Là chủ shop, tôi muốn **báo cáo doanh thu, hoa hồng, tuổi tồn, công nợ** và xuất Excel. | Ra quyết định | Should | S4 | US22, US24 |
| US31 | Là chủ shop, tôi muốn **tạo, vô hiệu hóa tài khoản nhân viên**. | Kiểm soát truy cập | Must | S1 | US01 |
| US32 | Là chủ shop, tôi muốn **cấu hình tỷ lệ chia, thời hạn, lịch giảm giá, thời hạn đổi trả và danh mục**. | Chính sách nhất quán | Must | S1 | US01 |
| US33 | Là chủ shop, tôi muốn **xem nhật ký các thao tác quan trọng** (giá, tiền, quyền). | Truy vết (BR10) | Should | S4 | US01 |
| US34 | Là người dùng, tôi muốn **nhận thông báo in-app** khi có việc cần làm hoặc thay đổi liên quan đến tôi. | Phản hồi kịp thời | Should | S3 | US01 |

**Tổng kết:** 20 Must · 11 Should · 3 Could. Nếu thiếu thời gian, cắt nhóm Could (US03, US20, US21) trước.

## 3. Đánh giá INVEST từng story

`PASS` nghĩa là thiết kế đã đủ thông tin để lập kế hoạch và nghiệm thu; không có nghĩa là đã cài đặt.

| Story | I | N | V | E | S | T | Ghi chú |
|---|---|---|---|---|---|---|---|
| US01 | PASS | PASS | PASS | PASS | PASS | PASS | JWT access token 60 phút, không refresh token ở V1 |
| US02 | PASS | PASS | PASS | PASS | PASS | PASS | Client xóa token; không có blacklist |
| US03 | PASS | PASS | PASS | PASS | PASS | PASS | Token đặt lại dùng một lần, hết hạn sau 30 phút |
| US04 | PASS | PASS | PASS | PASS | PASS | PASS | Link mời hết hạn sau 7 ngày, dùng một lần |
| US05 | PASS | PASS | PASS | PASS | PASS | PASS | Chỉ sửa tên, SĐT, avatar; đổi mật khẩu cần mật khẩu cũ |
| US06 | PASS | PASS | PASS | PASS | PASS | PASS | Ba biến thể dashboard theo vai trò, KPI định nghĩa ở AC |
| US07 | PASS | PASS | PASS | PASS | PASS | PASS | STK bị che phía server với STAFF |
| US08 | PASS | PASS | PASS | PASS | PASS | PASS | Link mời hiển thị để sao chép, không phụ thuộc email |
| US09 | PASS | PASS | PASS | PASS | PASS | PASS | Tối đa 50 món/phiếu, 4 ảnh/món, mỗi ảnh ≤ 5 MB |
| US10 | PASS | PASS | PASS | PASS | PASS | PASS | Schema JSON cố định; timeout 15 giây; phương án dự phòng là nhập tay |
| US11 | PASS | PASS | PASS | PASS | PASS | PASS | Tối đa 20 món tương tự làm ngữ cảnh; trả về khoảng giá + lý do |
| US12 | PASS | PASS | PASS | PASS | PASS | PASS | Xác nhận theo cả phiếu; yêu cầu sửa bắt buộc kèm ghi chú |
| US13 | PASS | PASS | PASS | PASS | PASS | PASS | Tem 40×30 mm: QR, mã món, giá, size |
| US14 | PASS | PASS | PASS | PASS | PASS | PASS | Phân trang 20 dòng/trang, các bộ lọc ghi rõ |
| US15 | PASS | PASS | PASS | PASS | PASS | PASS | Giá mới phải ≥ giá sàn, nếu không thì chuyển sang US17 |
| US16 | PASS | PASS | PASS | PASS | PASS | PASS | Job chạy 00:30 hằng ngày, idempotent |
| US17 | PASS | PASS | PASS | PASS | PASS | PASS | Mỗi món có tối đa một yêu cầu `PENDING` |
| US18 | PASS | PASS | PASS | PASS | PASS | PASS | Tự hết hạn sau 3 ngày (BR04) |
| US19 | PASS | PASS | PASS | PASS | PASS | PASS | Mốc 7 / 14 ngày theo BR07 |
| US20 | PASS | PASS | PASS | PASS | PASS | PASS | Bồi thường = giá sàn × tỷ lệ chia |
| US21 | PASS | PASS | PASS | PASS | PASS | PASS | Caption ≤ 600 ký tự, có hashtag; sửa được trước khi sao chép |
| US22 | PASS | PASS | PASS | PASS | PASS | PASS | Khóa lạc quan chống bán trùng |
| US23 | PASS | PASS | PASS | PASS | PASS | PASS | Đảo bút toán tạm giữ theo BR08 |
| US24 | PASS | PASS | PASS | PASS | PASS | PASS | Số dư = tổng bút toán sổ cái, không lưu cộng dồn tay |
| US25 | PASS | PASS | PASS | PASS | PASS | PASS | Tối thiểu 100.000đ; chỉ một yêu cầu `PENDING` mỗi lúc |
| US26 | PASS | PASS | PASS | PASS | PASS | PASS | VietQR theo chuẩn NAPAS; xác nhận đã chuyển bằng tay |
| US27 | PASS | PASS | PASS | PASS | PASS | PASS | Kỳ = tháng; PDF gồm đầu kỳ, phát sinh, cuối kỳ |
| US28 | PASS | PASS | PASS | PASS | PASS | PASS | Job hằng ngày, idempotent |
| US29 | PASS | PASS | PASS | PASS | PASS | PASS | Chỉ dữ liệu của chính người gửi |
| US30 | PASS | PASS | PASS | PASS | PASS | PASS | Bộ lọc theo khoảng ngày; Excel dùng cùng bộ lọc |
| US31 | PASS | PASS | PASS | PASS | PASS | PASS | Không xóa cứng, chỉ vô hiệu hóa |
| US32 | PASS | PASS | PASS | PASS | PASS | PASS | Thay đổi chỉ áp dụng cho phiếu tạo sau đó |
| US33 | PASS | PASS | PASS | PASS | PASS | PASS | Chỉ đọc, lọc theo người dùng, hành động, ngày |
| US34 | PASS | PASS | PASS | PASS | PASS | PASS | Danh sách sự kiện kích hoạt thông báo ghi ở AC |

## 4. Acceptance Criteria

### Nhóm M1 — Xác thực

**AC-US01 Đăng nhập**
```gherkin
Scenario: Đăng nhập thành công theo vai trò
  Given tài khoản "staff01" đang hoạt động với vai trò STAFF
  When người dùng nhập đúng email và mật khẩu
  Then hệ thống trả access token và chuyển đến Back-office Dashboard

Scenario: Người gửi đăng nhập
  Given tài khoản có vai trò CONSIGNOR
  When đăng nhập thành công
  Then hệ thống chuyển đến Consignor Portal, không thấy menu Back-office

Scenario: Sai thông tin hoặc tài khoản bị vô hiệu hóa
  When nhập sai mật khẩu hoặc tài khoản bị vô hiệu hóa
  Then hiển thị "Email hoặc mật khẩu không đúng" (không tiết lộ lý do cụ thể)
  And khóa đăng nhập 15 phút sau 5 lần sai liên tiếp
```

- **AC-US02:** Bấm Đăng xuất → token bị xóa ở client → chuyển về trang Đăng nhập; bấm Back không vào lại được trang cần đăng nhập.
- **AC-US03:** Nhập email → luôn hiển thị cùng một thông báo dù email có tồn tại hay không; link đặt lại dùng một lần, hết hạn sau 30 phút; mật khẩu mới ≥ 8 ký tự, có chữ và số.
- **AC-US04:** Mở link mời hợp lệ → đặt mật khẩu → tài khoản kích hoạt với đúng vai trò. Link đã dùng hoặc quá 7 ngày → báo "Link không còn hiệu lực".
- **AC-US05:** Sửa được tên, SĐT, avatar; không có trường vai trò; đổi mật khẩu cần đúng mật khẩu hiện tại.

### Nhóm M2 — Người ký gửi

- **AC-US06:**
  - OWNER thấy doanh thu, hoa hồng shop, số món bán, số món tồn theo tuổi, tổng công nợ người gửi, 5 giao dịch gần nhất.
  - STAFF thấy số đơn và doanh thu ca của mình, món sắp hết hạn.
  - CONSIGNOR thấy số món đang bán / đã bán, số dư tạm giữ / khả dụng, việc cần làm (phiếu chờ xác nhận, yêu cầu giảm giá).
- **AC-US07:** Bắt buộc có họ tên và SĐT (duy nhất). STAFF tạo và xem được, nhưng response không chứa STK ngân hàng; STAFF gọi API sửa → `403`. Người gửi bị vô hiệu hóa không chọn được khi tạo phiếu mới.
- **AC-US08:** Tạo link mời cho người gửi chưa có tài khoản → hiển thị link và nút sao chép; mỗi người gửi chỉ có một link còn hiệu lực tại một thời điểm.

### Nhóm M3 — Nhận hàng

**AC-US09 Tạo phiếu nhận hàng**
```gherkin
Scenario: Tạo phiếu với nhiều món
  Given người gửi "Nguyễn A" đang hoạt động
  When nhân viên tạo phiếu, thêm 3 món, mỗi món có ít nhất 1 ảnh, danh mục, giá niêm yết, giá sàn
  Then phiếu được lưu ở trạng thái DRAFT với 3 món DRAFT
  And phiếu ghi lại chính sách chia đang áp dụng tại thời điểm tạo

Scenario: Giá sàn không hợp lệ
  When nhập giá sàn lớn hơn giá niêm yết
  Then hiển thị lỗi "Giá sàn phải nhỏ hơn hoặc bằng giá niêm yết" và không lưu
```

**AC-US10 AI nhận diện ảnh**
```gherkin
Scenario: AI điền thông tin thành công
  Given món hàng đã có ít nhất 1 ảnh
  When nhân viên bấm "AI nhận diện"
  Then trong ≤ 15 giây form được điền danh mục, thương hiệu, size, màu, tình trạng, mô tả
  And các trường do AI điền có nhãn "AI" cho đến khi người dùng sửa hoặc xác nhận
  And hệ thống lưu lại bản đề xuất gốc của AI để đối chiếu

Scenario: AI lỗi hoặc quá thời gian
  When dịch vụ AI lỗi hoặc quá 15 giây
  Then hiển thị "Không nhận diện được, vui lòng nhập tay"
  And form vẫn nhập tay và lưu bình thường
```

**AC-US11 AI gợi ý giá**
```gherkin
Scenario: Gợi ý giá có dữ liệu tham chiếu
  Given shop đã bán ít nhất 3 món cùng danh mục
  When chủ shop bấm "Gợi ý giá"
  Then hiển thị khoảng giá (thấp – cao), giá đề xuất, giá sàn đề xuất và lý do
  And liệt kê các món tham chiếu đã dùng (tên, giá bán, số ngày bán được)

Scenario: Thiếu dữ liệu
  Given shop có ít hơn 3 món tương tự đã bán
  Then gợi ý vẫn hiển thị nhưng kèm nhãn "Độ tin cậy thấp"
```

- **AC-US12:**
  - Người gửi thấy phiếu `PENDING_CONFIRM` của mình, với ảnh, thông tin, giá niêm yết, giá sàn, tỷ lệ chia, thời hạn.
  - **Xác nhận** → tất cả món chuyển sang `ACTIVE` và bắt đầu tính thời hạn.
  - **Yêu cầu sửa** → bắt buộc ghi chú, phiếu quay về `DRAFT` và nhân viên được thông báo.
  - OWNER "Xác nhận tại quầy" → kết quả tương tự, audit ghi rõ người xác nhận.
- **AC-US13:** Chọn một hoặc nhiều món `ACTIVE` → tạo trang in tem 40×30 mm (QR chứa mã món, kèm giá hiện tại và size); món chưa `ACTIVE` không in được.

### Nhóm M4 — Kho hàng

- **AC-US14:** Lọc theo trạng thái, danh mục, người gửi, khoảng giá, tuổi tồn (0–30 / 31–60 / > 60 ngày); tìm theo mã món hoặc tên; 20 dòng/trang; món sắp hết hạn (≤ 7 ngày) được tô màu cảnh báo.
- **AC-US15:** OWNER đặt giá mới ≥ giá sàn → áp dụng ngay và ghi vào lịch sử giá (giá cũ, giá mới, người sửa, thời điểm). Giá mới < giá sàn → hệ thống chuyển sang tạo yêu cầu (US17).

**AC-US16 Giảm giá tự động**
```gherkin
Scenario: Giảm giá ngày 30
  Given món niêm yết 500.000đ, giá sàn 300.000đ, ACTIVE được 30 ngày
  When job giảm giá chạy
  Then giá hiện tại = 400.000đ và lịch sử giá ghi người sửa là "SYSTEM"
  And người gửi nhận thông báo

Scenario: Không xuống dưới giá sàn
  Given món niêm yết 500.000đ, giá sàn 420.000đ, ACTIVE được 30 ngày
  When job giảm giá chạy
  Then giá hiện tại = 420.000đ (giá sàn), không phải 400.000đ

Scenario: Job chạy lại trong cùng ngày
  When job chạy hai lần trong cùng ngày
  Then mức giảm chỉ được áp dụng một lần
```

> Ghi chú công thức: `giá mới = max(làm_tròn_1000(giá_niêm_yết × (1 − %giảm)), giá_sàn)`.

- **AC-US17:** Chỉ cho phép với món `ACTIVE`; lý do bắt buộc; mỗi món có tối đa một yêu cầu `PENDING`; người gửi nhận thông báo.
- **AC-US18:** **Đồng ý** → giá bán và giá sàn mới được áp dụng, ghi lịch sử. **Từ chối** → giá giữ nguyên, có thể chọn "Tôi sẽ đến lấy lại". Quá 3 ngày → `EXPIRED`. Không xử lý được yêu cầu của người gửi khác (`403`).
- **AC-US19:** Danh sách "Sắp hết hạn (≤ 7 ngày)" và "Đã hết hạn"; người gửi được thông báo ở mốc 7 ngày và ngày hết hạn. Ghi nhận "Đã trả lại" → `RETURNED`. Sau 14 ngày, nút "Thanh lý / quyên góp" mới được bật → `DISPOSED`.
- **AC-US20:** Báo thất lạc → `LOST`, tạo bút toán bồi thường = giá sàn × tỷ lệ chia (khả dụng ngay). Báo hư hỏng → `DAMAGED`, không bồi thường nếu hàng hư sẵn (bắt buộc ghi chú).
- **AC-US21:** Sinh caption tiếng Việt ≤ 600 ký tự gồm tên, tình trạng, size, giá và 3–5 hashtag; sửa được; có nút sao chép; AI lỗi → hiển thị thông báo, không chặn thao tác khác.

### Nhóm M5 — Bán hàng

**AC-US22 Bán hàng POS**
```gherkin
Scenario: Bán thành công 2 món của 2 người gửi khác nhau
  Given món A (người gửi X, 400.000đ) và món B (người gửi Y, 150.000đ) đang ACTIVE
  When nhân viên quét 2 mã, chọn "Tiền mặt" và xác nhận
  Then đơn hàng tổng 550.000đ được tạo, A và B chuyển sang SOLD
  And X có bút toán tạm giữ 240.000đ (60%), Y có bút toán tạm giữ 75.000đ (50%)

Scenario: Quét món không bán được
  When quét món ở trạng thái khác ACTIVE
  Then hiển thị "Món này đang ở trạng thái <tên trạng thái>" và không thêm vào giỏ

Scenario: Hai quầy bán trùng một món
  When hai giao dịch cùng chứa món A được xác nhận gần như đồng thời
  Then chỉ một giao dịch thành công, giao dịch còn lại báo "Món đã được bán"
```

- **AC-US23:** Trong thời hạn tạm giữ: STAFF và OWNER làm được → bút toán tạm giữ bị đảo, món về `ACTIVE` hoặc `DAMAGED`, hoàn tiền ghi theo phương thức. Ngoài thời hạn: chỉ OWNER, và phải nhập lý do.

### Nhóm M6 — Đối soát & Chi trả

- **AC-US24:** Hiển thị số dư **tạm giữ**, **khả dụng**, **đã rút**; lịch sử bút toán (ngày, loại, món, số tiền, số dư sau); số dư luôn bằng tổng bút toán. OWNER chọn được từng người gửi.
- **AC-US25:** Số tiền ≥ 100.000đ và ≤ số dư khả dụng; chỉ một yêu cầu `PENDING`; khi tạo yêu cầu, số tiền bị trừ tạm khỏi khả dụng; người gửi phải có thông tin ngân hàng.

**AC-US26 Duyệt & chi trả**
```gherkin
Scenario: Chi trả thành công
  Given yêu cầu rút 500.000đ của người gửi X đang PENDING
  When chủ shop mở yêu cầu
  Then hiển thị mã VietQR với đúng STK, số tiền 500.000đ, nội dung "RELOOP <mã yêu cầu>"
  When chủ shop bấm "Đã chuyển"
  Then yêu cầu chuyển sang PAID, ghi bút toán chi trả, X nhận thông báo, audit ghi người duyệt

Scenario: Từ chối
  When chủ shop từ chối kèm lý do
  Then yêu cầu chuyển sang REJECTED và 500.000đ được hoàn vào số dư khả dụng của X
```

- **AC-US27:** Chọn tháng → PDF gồm thông tin shop, người gửi, số dư đầu kỳ, danh sách bút toán, số dư cuối kỳ; người gửi chỉ xuất được sao kê của mình.
- **AC-US28:** Job hằng ngày chuyển các bút toán tạm giữ quá 7 ngày sang khả dụng, món chuyển sang `SETTLED`; chạy lại không cộng trùng; người gửi được thông báo.

### Nhóm M7–M9 — Cổng người gửi, Báo cáo, Quản trị

- **AC-US29:** Người gửi thấy danh sách hàng của mình với ảnh, trạng thái, giá hiện tại, số ngày còn lại; lọc theo trạng thái; gọi API với `consignor_id` khác → `403`.
- **AC-US30:** Báo cáo theo khoảng ngày gồm doanh thu, hoa hồng shop, số món bán, thời gian bán trung bình, tồn theo tuổi, công nợ theo người gửi, top danh mục; xuất Excel đúng bộ lọc đang chọn.
- **AC-US31:** Tạo nhân viên → sinh link mời (US04); vô hiệu hóa → phiên hiện tại bị từ chối ở request kế tiếp; không xóa cứng.
- **AC-US32:**
  - Các bậc tỷ lệ chia không chồng lấn, mỗi bậc từ 0–100%.
  - Lịch giảm giá: các mốc ngày tăng dần, % giảm tăng dần.
  - Thay đổi chính sách không làm đổi các phiếu đã tạo trước đó.
  - Danh mục có thể bật/tắt, không xóa nếu đã có món.
- **AC-US33:** Ghi audit cho: đăng nhập thất bại, đổi giá, xác nhận phiếu, bán hàng, đổi trả, chi trả, đổi chính sách, quản lý tài khoản. Mỗi bản ghi gồm thời điểm, người thực hiện, hành động, đối tượng, giá trị trước/sau. Chỉ đọc.
- **AC-US34:** Thông báo in-app khi: phiếu chờ xác nhận, phiếu bị yêu cầu sửa, món được giảm giá, yêu cầu giảm giá mới, món sắp/đã hết hạn, món đã bán, tiền chuyển sang khả dụng, yêu cầu rút được duyệt/từ chối. Có badge số chưa đọc, đánh dấu đã đọc.

## 5. Ràng buộc chấp nhận chung

- Chỉ tồn tại 3 vai trò người dùng: `OWNER`, `STAFF`, `CONSIGNOR`.
- Backend (không phải frontend) thực thi RBAC và quyền sở hữu dữ liệu của `CONSIGNOR`.
- Tiền lưu dạng số nguyên VND; mọi thay đổi tiền đi qua **sổ cái bút toán** (không sửa số dư trực tiếp).
- Kết quả AI luôn cần người xác nhận (BR09); hệ thống vẫn chạy đầy đủ khi tắt AI.
- Các job của `SYSTEM` phải idempotent.
- Lỗi API trả theo định dạng `ProblemDetails` (sẽ định nghĩa trong OpenAPI).
- Ảnh tải lên được kiểm tra loại file (JPEG/PNG/WebP) và kích thước phía server.

---

**Liên quan:** [Use cases](03-use-cases.md) · [Phạm vi & quy tắc](02-scope.md) · [Information architecture](05-information-architecture.md)
