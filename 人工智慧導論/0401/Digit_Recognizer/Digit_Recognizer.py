import cv2
import numpy as np
from keras.models import load_model

# 載入模型
CNN_model = load_model("C:\\Users\\drlin\\Program\\Project_Python\\人工智慧導論\\0401\\Digit_Recognizer\\cnn_model.h5")

# 定義畫布大小
img = np.zeros(shape=(256, 256), dtype=np.uint8)

# 初始值
drawing = False
(ix, iy) = (-1, -1)

# 定義事件
def mouse_down_event(event, x, y, flags, param):
    global ix, iy, drawing, img, model

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = cv2.line(img, (ix, iy), (x, y), (255, 255, 255), 8) #cv2.line(image, start_point, end_point, rgb_color, thickness)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        ret = cv2.waitKey(0)

        if ret == ord('c'):
            inputs = cv2.resize(img, (28, 28))
            inputs = inputs.reshape(1, 28, 28, 1)
            inputs = inputs.astype(np.float32)
            #inputs = inputs / 255.0

            outputs = CNN_model(inputs)
            outputs = np.argmax(outputs, axis=1)
            outputs = outputs.item()
            print(f"Predict answer: {outputs}")

            img = np.zeros((256, 256), dtype=np.uint8)
            cv2.imshow("Image", img)
    cv2.imshow("Image", img)
    
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", mouse_down_event)

ret = cv2.waitKey(0)
cv2.destroyAllWindows()