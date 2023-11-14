import cv2
import numpy as np

def recognize_circle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=100, param2=60, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))

    for circle in circles[0, :]:
        # 円周を描画する
        cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 165, 255), 5)
        # 中心点を描画する
        cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 3)

    cv2.imwrite("new.png", img)

    return circles

if __name__ == "__main__":
    flag = 0
    if flag == 0:
        img = cv2.imread("1.jpg")
    else:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        img = frame
    img2 = img[0 : 480, 80 : 560] # top : bottom, left, right
    cv2.imwrite("img.jpg", img2)
    # recognize_circle(img2)

# cv2.imwrite("image/a.jpg", img2)

# import time
# # カメラのキャプチャを開始
# x = time.time()
# cap = cv2.VideoCapture(0)  # 0はデフォルトのカメラを指します

# # カメラが正常にオープンしているか確認
# if not cap.isOpened():
#     print("カメラを開けません")
#     exit()

# # カメラからフレームをキャプチャ
# ret, frame = cap.read()
# y = time.time()
# print(y-x)
# print(frame.shape)
# # フレームのキャプチャに成功したか確認
# if not ret:
#     print("フレームをキャプチャできませんでした")
#     exit()

# # キャプチャした画像を表示
# cv2.imwrite("image/image.jpg", frame)
# cv2.imshow('Captured Image', frame)

# # 何かキーが押されるまで待機
# cv2.waitKey(0)

# # すべてのウィンドウを閉じる
# cv2.destroyAllWindows()

# # カメラのキャプチャを解放
# cap.release()