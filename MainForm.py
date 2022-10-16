from cgi import test
import tkinter as tk
import main
import DefConst as C

def StartGame():
    GameResult = main.mainMethod
 #   PlayerLabel(text = GameResult)

#メインフォーム作成
frm = tk.Tk()
frm.geometry('600x400')
frm.title('BLACKJACK')


#ボタン配置
StartButton = tk.Button(frm, text = 'ゲーム開始', command = main.mainMethod).place(x = 260, y = 300)


#ラベル配置
PlayerLabel = tk.Label(text = 'プレイヤー : ', foreground = 'black', background = 'silver', width = 30, height = 2, anchor = tk.W).place(x = 200, y = 200)
DealerLabel = tk.Label(text = 'ディーラー : ', foreground = 'black', background = 'silver', width = 30, height = 2, anchor = tk.W).place(x = 200, y = 100)


frm.mainloop()

