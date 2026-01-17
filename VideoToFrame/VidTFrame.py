import cv2 as cv
from tqdm import tqdm
import time


#c:\Users\dell\Downloads\BadApple.mp4

print("Welcome to Video to Frame Capture")

videoPath = input("Enter Video path: ")

while True:
    try:
        vid = cv.VideoCapture(f"{videoPath}")
        break
    except:
        continue

if not vid.isOpened:
    print("Error opening video")

running = True
saved_id = 0
N = 30

totalframes = int(vid.get(cv.CAP_PROP_FRAME_COUNT))


for frame_id in tqdm(range(totalframes)):
    rel, frame = vid.read()

    if rel == False:
        break

    if frame_id % N == 0:
        cv.imwrite(f"VideoToFrame/frames/frame_{saved_id:05d}.jpg", frame)
        saved_id += 1
        
    


vid.release()
cv.destroyAllWindows()

