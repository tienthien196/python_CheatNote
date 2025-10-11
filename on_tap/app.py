import NGLxAPIClient
# Thông tin từ request bạn cung cấp
client = NGLxAPIClient(
    user_id="691faf92-92de-45f0-b84d-ae8dad27ed53",
    content_id="d32ef972-fdba-4551-aebb-dc3f18f260e5",
    registration_id="6ff24efb-834d-416c-9da3-fceee914d88d",
    session_cookie="_unity_session=a629be948ae4f6351e864ffed27c93a0"
)

# 1. Lấy bookmark
bookmark = client.get_bookmark()
print("Bookmark:", bookmark)

# 2. Lưu bookmark mới
client.save_bookmark({"page": 10, "time": 123.45})

# 3. Lấy suspend_data
suspend = client.get_suspend_data()
print("Suspend data:", suspend)

# 4. Lưu trạng thái tạm
client.save_suspend_data({
    "currentSlide": "quiz_3",
    "answers": {"q1": "A"},
    "visited": [1,2,3]
})

# 5. Gửi sự kiện "started"
client.send_started()

# 6. Gửi hoàn thành với điểm
client.send_completed(success=True, score=0.85)