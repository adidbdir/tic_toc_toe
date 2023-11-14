import cv2
import numpy as np

# カメラから画像取得
def get_image_from_camera():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'));
    ret, frame = cap.read()
    
    return frame

def recognize_circle1(image):
    # 画像をグレースケールにする
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Canny法
    binary = cv2.Canny(gray, 100, 200)
    res_close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, np.ones((5, 5), dtype=binary.dtype))
    contours, _ = cv2.findContours(res_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # 輪郭線の長さを計算
        arclen = cv2.arcLength(cnt, True)
        if arclen < 1000:    
            # 輪郭線の近似
            approx = cv2.approxPolyDP(cnt, 0.01 * arclen, True)
            # 何角形かを見てみる
            if len(approx) > 10 :
                # 輪郭線の描画
                print(len(approx))
                cv2.drawContours(image, [approx], -1, (255, 0, 0), 3, cv2.LINE_AA)
                position = np.asarray(approx).reshape((-1, 2)).max(axis=0).astype('int32')
                px, py = position
                # cv2.circle(image, (px, py), 5, color=(255, 0, 0), thickness=2)
    cv2.imwrite("image/output/contours.jpg", image)
    return contours

def recognize_circle(image):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=100, param2=60, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))

    for circle in circles[0, :]:
        # 円周を描画する
        cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 165, 255), 5)
        # 中心点を描画する
        cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 3)

    cv2.imwrite("sample_after.png", img)

    return circles

def update_cell(cell, circle):
    if circle:
        cell
    return cell

def tic_toc_toe():
    return
def check_win():
    win = [
        [1,2,3], [4,5,6], [7,8,9],
        [1,4,7], [2,5,8], [3,6,9],
        [1,5,9], [3,5,7]
    ]
if __name__ == "__main__":
    # init
    cell = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    position =[
        [x, y], [x, y], [x,y],
        [x, y], [x, y], [x,y],
        [x, y], [x, y], [x,y]
        ]

    # すべて埋まるか3つ並んだら終了
    while true:
        img = get_image_from_camera()
        # 認識
        circle = recognize_circle(img)
        # cell更新
        cell = update_cell(cell, circle)
        # 描く位置考える
        write_position = tic_toc_toe(cell)
        # 位置を基に描く
        
    # get image from camera
    # image_old = get_image_from_camera()
    # image_new = get_image_from_camera()
    # cv2.imwrite("image/new.jpg", image_new)
    # print("new")

    # img = get_image_def(image_old, image_new)
    # print(img)

    # 丸の認識
    # 画像をグレースケールにする
    img = cv2.imread("image/new.jpg")
    circles = recognize_circle1(img)
    # print(circle)

    # 丸の位置を更新
    cell = update_cell():
