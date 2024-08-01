import cv2

    
cam = cv2.VideoCapture('D:\\Football_Analistic_System\\Week_2\\Project\\Project_System\\image\\Test.mp4')
    
    
    # Lấy thông tin về số frame và FPS của video
video_fps = cam.get(cv2.CAP_PROP_FPS)
total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Tính khoảng thời gian giữa các frame cần lưu
interval = int(video_fps // 2)
    
frame_count = 0
saved_count = 0
    
while True:
    ret, frame = cam.read()
    if ret:
        if frame_count % interval == 0:
        # Lưu frame
            cv2.imwrite('D:\\Football_Analistic_System\\Week_2\\Project\\Project_System\\image\\{}.jpg'.format(saved_count), frame)
            saved_count += 1
        frame_count +=1
    else:
        break
cam.release()
cv2.destroyAllWindows()

