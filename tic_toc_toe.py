import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np
# import drowX 
import detection

def get_image():
    print("start get image")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not cap.isOpened():
        print("カメラを開けません")
        exit()
    if ret:
        print("end get image")
    else:
        print("フレームをキャプチャできませんでした")
        exit()
    # cap.release()
    # 画像のトリミング
    frame = frame[0 : 480, 80 : 560]
    return frame
    
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")

def is_valid_move(board, row, col):
    return board[row][col] == " "

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def is_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

# def get_move():
#     while True:
#         try:
#             row, col = map(int, input("Enter row and column (0-2 for each): ").split())
#             if 0 <= row <= 2 and 0 <= col <= 2:
#                 return row, col
#             else:
#                 print("Invalid input. Please enter numbers between 0 and 2.")
#         except ValueError:
#             print("Invalid input. Please enter two numbers separated by a space.")

def switch_player(player):
    return "O" if player == "X" else "X"

def find_drow_position(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return row, col

def main():
    # 画像の読み込み
    # image_old = cv2.imread('image/1.jpg')
    # image_old = image_old[0 : 480, 80 : 560]
    image_old = get_image()
    # ボードの初期化
    board = initialize_board()
    # playerの選択
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "O":
            # 人が手書きするのを待つ
            wait = input("if drow circle, press the button")
            # image_new = cv2.imread("image/2.jpg")
            # image_new = image_new[0 : 480, 80 : 560]
            image_new = get_image()
            image_diff = detection.compare_images(image_old, image_new)
            row, col = detection.detect_circle_and_update_board(image_diff)
            image_old = image_new
        if current_player == "X":
            row, col = find_drow_position(board)
            print("drowX")
            # drowX.a(row, col)
        if make_move(board, row, col, current_player):
            if is_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = switch_player(current_player)
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    main()