import matplotlib.pyplot as plt
import numpy as np
import cv2

def compare_images(image1_path, image2_path):
    """
    2つの画像を比較し、差分を表示する関数。

    Args:
        image1_path (str): 1つ目の画像のパス
        image2_path (str): 2つ目の画像のパス
    """

    # 画像を読み込む
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    print(image1.shape)
    print(image2.shape)
    # 差分画像を計算
    diff = cv2.absdiff(image1, image2)

    # グレースケールに変換
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # BGRからRGBに変換
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    # カラーマップを適用するために差分画像を正規化
    norm_diff = gray_diff / np.max(gray_diff)

    # 差分画像に重みをかけて2枚目の画像の色に反映
    diff_img = cv2.addWeighted(gray2, 0.1, gray_diff, 2, 100)

    diff_colored = np.zeros_like(image2_rgb)
    diff_colored[..., 0] = image2_rgb[..., 0] * norm_diff
    diff_colored[..., 1] = image2_rgb[..., 1] * norm_diff
    diff_colored[..., 2] = image2_rgb[..., 2] * norm_diff

    # 結果をMatplotlibで表示
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    # 1枚目の画像を表示
    axes[0, 0].imshow(image1_rgb)
    axes[0, 0].set_title("Image 1")
    axes[0, 0].axis("off")

    # 2枚目の画像を表示
    axes[0, 1].imshow(image2_rgb)
    axes[0, 1].set_title("Image 2")
    axes[0, 1].axis("off")

    # 差分画像（グレースケール）を表示
    axes[1, 0].imshow(diff_img, cmap="gray")
    axes[1, 0].set_title("Difference (Grayscale)")
    axes[1, 0].axis("off")

    # 差分画像（カラー）を表示
    axes[1, 1].imshow(diff_colored)
    axes[1, 1].set_title("Difference (Colored)")
    axes[1, 1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 2つの画像を比較して違いを検出
    image1_path = "image/1.jpg"
    image2_path = "image/2.jpg"
    compare_images(image1_path, image2_path)