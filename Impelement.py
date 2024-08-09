import cv2
import os

folder_path = 'D:\\Football_Analistic_System\\Week_2\\Project\\Project_System\\video'

    
    
    

    
frame_count = 0
saved_count = 0
for filename in os.listdir(folder_path):
    video_path = os.path.join(folder_path, filename)
    cam = cv2.VideoCapture(video_path)
    video_fps = cam.get(cv2.CAP_PROP_FPS)
    total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = int(video_fps // 2)
    while True:
        ret, frame = cam.read()
        if ret:
            if frame_count % interval == 0:
            # Lưu frame
                cv2.imwrite('D:\\Football_Analistic_System\\Week_2\\Project\\Project_System\\image_2\\{}.jpg'.format(saved_count), frame)
                saved_count += 1
            frame_count +=1
        else:
            break
cam.release()
cv2.destroyAllWindows()

