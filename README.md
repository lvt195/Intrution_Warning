# Intrution_Warning

## Mô tả hệ thống:
Hệ thống sẽ theo dõi 1 vùng, khu vực thông qua camera của thiết bị nếu có đối tượng xâm nhập sẽ gửi cảnh báo cho người dùng thông qua Telegram.

* Ở trường hợp này ta sẽ phát hiện đối tượng là người
* Khi có cảnh báo xâm nhập, hệ thống sẽ chụp ảnh lại và gửi cảnh báo
* Bot chat trên ứng dụng Telegram sẽ gửi hình ảnh của đối tượng, mỗi 1 lần gửi cách nhau 15s 

## Ứng dụng:
- Cảnh báo xâm nhập tại nhà
- Cảnh báo phát hiện người trên đường ray
- Etc...

## Công nghệ, thư viện, ứng dụng sử dụng: 
  - Python
  - Mô hình AI: YOLO
  - Thư viện Open-CV
  - Bot chat trên Telegram
  - Etc...

### YOLO (You Only Look Once) 
YOLO là mô hình phát hiện đối tượng phổ biến được biết đến với tốc độ nhanh và độ chính xác cao. Mô hình này lần đầu tiên được giới thiệu bởi Joseph Redmon và cộng sự vào năm 2016. Kể từ khi ra mắt, phiên bản YOLO nào cũng cho thấy sự cải thiện đáng kể (đặc biệt là về mặt tốc độ) so với các mô hình tốt nhất thời điểm đó.

Chi tiết: https://viblo.asia/p/tim-hieu-ve-yolo-trong-bai-toan-real-time-object-detection-yMnKMdvr57P

### Thư viện Open-cv 
OpenCV (Open Source Computer Vision Library) trong Python là một thư viện mã nguồn mở được sử dụng rộng rãi để xử lý và phân tích hình ảnh, video và dữ liệu thị giác máy tính. Thư viện này cung cấp nhiều công cụ và chức năng để thực hiện các tác vụ như nhận dạng đối tượng, xử lý hình ảnh, phát hiện khuôn mặt, theo dõi đối tượng, và nhiều ứng dụng khác trong lĩnh vực thị giác máy tính.

Ứng dụng của Open-cv:

_**1. Xử lý hình ảnh:**_

- Chuyển đổi, cắt, xoay, và thay đổi kích thước hình ảnh.
- Làm mờ và làm sắc nét hình ảnh.
- Phát hiện biên, đường viền, và đối tượng trong hình ảnh.
- Thực hiện các phép biến đổi hình học như phép co giãn, biến đổi affine, và biến đổi Perspectival.
- Tạo các hiệu ứng hình ảnh như làm sáng, làm tối, và làm nổi bật màu sắc.
_**Nhận dạng đối tượng:**_
- Phát hiện khuôn mặt và mắt.
- Nhận dạng đối tượng trong hình ảnh hoặc video bằng cách sử dụng các thuật toán như Haar Cascades, SIFT, SURF, ORB, và Deep Learning-based models.

_**2. Thị giác máy tính:**_
- Theo dõi đối tượng trong video.
- Phát hiện và theo dõi chuyển động.
- Đo đạc và tính toán các thông số về hình ảnh như khoảng cách, góc độ, và diện tích.

_**3. Xử lý video:**_
- Ghi video và lấy dữ liệu từ video camera.
- Phát hiện và theo dõi đối tượng trong thời gian thực trong video.
- Thực hiện xử lý video như làm mờ video, giảm tiếng ồn, và trích xuất khung hình quan trọng.
  
_**3. Thị giác máy tính trong thời gian thực:**_
- Sử dụng OpenCV với các mô hình Deep Learning để xây dựng các ứng dụng nhận dạng đối tượng trong thời gian thực, như nhận dạng khuôn mặt, xe hơi, người đi bộ, và nhiều đối tượng khác.
  
_**4. Ứng dụng trong robot và tự động hóa:**_
- OpenCV có thể được sử dụng để hỗ trợ việc nhận dạng và theo dõi đối tượng trong các ứng dụng robot và tự động hóa.
- 
_**5. Thực hiện xử lý ảnh y tế:**_
- OpenCV có ứng dụng trong việc xử lý và phân tích hình ảnh y tế như phát hiện và phân loại bệnh lý, xử lý hình ảnh siêu âm và hình ảnh MRI.
  
**=> OpenCV là một thư viện đa năng và được sử dụng rộng rãi trong nhiều lĩnh vực, từ công nghiệp đến nghiên cứu và phát triển ứng dụng sáng tạo.**
