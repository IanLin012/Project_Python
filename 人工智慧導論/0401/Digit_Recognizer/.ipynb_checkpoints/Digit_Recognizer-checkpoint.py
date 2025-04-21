{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ef6ff83-a39d-46bd-af10-66bc6860e5e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "from keras.models import load_model\n",
    "\n",
    "# 載入模型\n",
    "CNN_model = load_model(cnn_model.h5)\n",
    "\n",
    "# 定義畫布大小\n",
    "img = np.zeros(shape=(256, 256), dtype=np.uint8)\n",
    "\n",
    "# 初始值\n",
    "drawing = False\n",
    "(ix, iy) = (-1, -1)\n",
    "\n",
    "# 定義事件\n",
    "def mouse_down_event(event, x, y, flags, param):\n",
    "    global ix, iy, drawing, img, model\n",
    "\n",
    "    if event == cv2.EVENT_LBUTTONDOWN:\n",
    "        drawing = True\n",
    "        (ix, iy) = x, y\n",
    "\n",
    "    elif event == cv2.EVENT_MOUSEMOVE:\n",
    "        if drawing == True:\n",
    "            img = cv2.line(img, (ix, iy), (x, y), (255, 255, 255), 8) #cv2.line(image, start_point, end_point, rgb_color, thickness)\n",
    "            ix, iy = x, y\n",
    "\n",
    "    elif event == cv2.EVENT_LBUTTONUP:\n",
    "        drawing = False\n",
    "\n",
    "        ret = cv2.waitKey(0)\n",
    "\n",
    "        if ret == ord('c'):\n",
    "            inputs = cv2.resize(img, (28, 28))\n",
    "            inputs = cv2.reshape(1, 28, 28, 1)\n",
    "            inputs = inputs.astype(np.float32)\n",
    "            #inputs = inputs / 255.0\n",
    "\n",
    "            outputs = CNN_model(inputs)\n",
    "            outputs = np.argmax(outputs, axis=1)\n",
    "            outputs = output.item()\n",
    "            print(f\"Predict answer: {outputs}\")\n",
    "\n",
    "            cv2.imshow(\"Image\", img)\n",
    "    cv2.imshow(\"Image\", img)\n",
    "    \n",
    "cv2.imshow(\"Image\", img)\n",
    "cv2.setMouseCallback(\"Image\", mouse_down_event)\n",
    "\n",
    "ret = cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
