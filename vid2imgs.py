import cv2
vid_path = input("Enter video path: ")
vid = cv2.VideoCapture(vid_path)

i=1
success = 1
while success:
    success, frame = vid.read()
    if success:
        cv2.imwrite('Dataset_images/frame%d.jpg' %i, frame)
        print("Created Frame%d" %i)
        i+=1
print("Transfer of Images Complete")