from ultralytics import YOLO

model  = YOLO("D:\\Football_Analistic_System\\Week_2\\Project\\Project_System\\models\\best.pt")

results = model.predict("D:\\Football_Analistic_System\\Week_2\\Project\\Project_System\\video\\Test.mp4",save=True)
print(results[0])
print("========================")
for box in results[0].boxes:
    print(box)