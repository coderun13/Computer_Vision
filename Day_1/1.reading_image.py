import cv2

#  Reading Image
# image = cv2.imread("resources/lena.png")

# print(image)
# print(image.shape) #(512(w), 512(h), 3(channel))

# cv2.imshow("Output", image)
# cv2.waitKey(0)
#  cv2.destroyAllWindows()


#  Reading Video

# cap = cv2.VideoCapture("resources/elon.mp4")

# while True:
#     success, image = cap.read()
#     print(image.shape)
#     cv2.imshow("Video", image)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Reading webcam

cap = cv2.VideoCapture(0)

cap.set(3, 640) #width
cap.set(4, 480) #height

while True:
    success, image = cap.read()
    print(image.shape)
    cv2.imshow("Webcam", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    