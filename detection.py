import cv2
import numpy as np

# 画像から丸を検出する
def detect_circle_and_update_board(image):
    # 画像をグレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ノイズを減らすためにぼかしを適用
    gray = cv2.medianBlur(gray, 5)
    # Hough変換を使用して円を検出
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)
    # for circle in circles[0, :]:
    #     # 円周を描画する
    #     cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 165, 255), 5)
    #     # 中心点を描画する
    #     cv2.circle(image, (circle[0], circle[1]), 2, (0, 0, 255), 3)
    # cv2.imwrite("sample_after.png", image)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # 円の中心座標を取得
            center = (i[0], i[1])
            print(f"center:{center}")
            # ここで、centerを使用してボードのどのセルが選ばれたかを決定します
            # これは、画像の座標とボードのセルの座標をマッピングするロジックが必要です
            # 例えば、画像の解像度とボードのサイズに基づいて変換を行います
            # 以下はその変換を行うダミーのコードです
            row, col = convert_to_board_coordinates(center)

            return row, col

    else:
        print("circle is not find")

# 画像の座標をボードのセルの座標に変換する関数
def convert_to_board_coordinates(center):
    # 画像の解像度とボードのサイズに基づいて、centerからrowとcolを計算します
    # これは単純な例で、実際の変換ロジックは画像のサイズとボードのレイアウトに依存します
    image_size = (480, 480)
    cell_size = image_size[0] // 3  # 画像サイズを3で割ったものが各セルのサイズ
    print(cell_size)
    row = center[1] // cell_size
    col = center[0] // cell_size
    print(row, col)
    return row, col

def compare_images(image_old, image_new):
    """
    2つの画像を比較し、差分を表示する関数。

    Args:
        image_old (str): 1つ目の画像のパス
        image_new (str): 2つ目の画像のパス
    """
    diff = cv2.absdiff(image_old, image_new)
    cv2.imwrite("image/diff.jpg", diff)
    return diff