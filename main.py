from ast import Is
from cgitb import text
import random
import sys
from tkinter import messagebox
#import MainForm 

#class Deck:
__Rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
__Suit = [ [1, 'Spade']
         , [2, 'Heart']
         , [3, 'Club']    
         , [4, 'Diamond']]
          
__deck = [ [1 , 1, 0]
         , [2 , 1, 0]
         , [3 , 1, 0]
         , [4 , 1, 0]
         , [5 , 1, 0]
         , [6 , 1, 0]
         , [7 , 1, 0]
         , [8 , 1, 0]
         , [9 , 1, 0]
         , [10, 1, 0]
         , [10, 1, 0]
         , [10, 1, 0]
         , [10, 1, 0]]

def ClearDeck():
    for i in range(0, 13): 
        __deck[i][2] = 0



def GetCard() :
    SelectedCard = random.sample(__deck, 1)
    
    IsUsed = True
    
    while IsUsed == True:
        #使用済みのカードの場合
        if SelectedCard[0][2] == 1: 
            IsUsed = True      
            SelectedCard = random.sample(__deck, 1)
        else:
            IsUsed = False  
            SelectedCard[0][2] = 1
            break
    return SelectedCard[0]

def Deal() :
    DealtCardValue = GetCard()[0] + GetCard()[0]
    return DealtCardValue

def AddCard():
    AddCardValue = GetCard()[0]
    return AddCardValue

def CheckBurst(pValue):
    if pValue > 21 :
        messagebox.showinfo("終了", "バーストしました") 
        return True
    else :
        return False      


#---------------------------------------------------------------------------
# メイン
#---------------------------------------------------------------------------
def mainMethod():
    ClearDeck()
    ISPlayerBurst = False
    ISDealerBurst = False
    
    PlayerCard = Deal()
    
    ISHit = messagebox.askyesno("Hitしますか？", "手札:" + str(PlayerCard))
    if ISHit == True:
        PlayerCard += AddCard()
        messagebox.showinfo("終了", "手札:" + str(PlayerCard))
        if CheckBurst(PlayerCard): 
            ISPlayerBurst = True
    else:
        messagebox.showinfo("終了", "手札:" + str(PlayerCard))
    
    #プレイヤーがバーストしたら終了
    if ISPlayerBurst:
        messagebox.showinfo("結果", "プレイヤーバースト")
        return 'CCCC'
    
    
    DealerCard = Deal()
    messagebox.showinfo("ディーラー", "手札:" + str(DealerCard))
    
    if DealerCard < 17:
        while DealerCard < 17:
            messagebox.showinfo("ディーラー", "ヒット" )
            DealerCard += AddCard()
            messagebox.showinfo("ディーラー", "手札:" + str(DealerCard))
            if CheckBurst(DealerCard) :
                ISDealerBurst = True 
                break 
    else:
        messagebox.showinfo("ディーラー", "手札:" + str(DealerCard))
    
    
    #結果表示
    if ISPlayerBurst:
        messagebox.showinfo("結果", "プレイヤーバースト")
    elif ISDealerBurst:
        messagebox.showinfo("結果", "ディーラーバースト")
    else :
        if PlayerCard > DealerCard :
            messagebox.showinfo("結果", "プレーヤー勝利:" + str(PlayerCard) + " 対 " + str(DealerCard))
        else:
            messagebox.showinfo("結果", "ディーラー勝利:" + str(PlayerCard) + " 対 " + str(DealerCard))

    return 'CCCC'