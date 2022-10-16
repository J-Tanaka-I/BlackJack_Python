
class deck:
    __deck = [
        ["1" , "S", ""]
      , ["2" , "S", ""]
      , ["3" , "S", ""]
      , ["4" , "S", ""]
      , ["5" , "S", ""]
      , ["6" , "S", ""]
      , ["7" , "S", ""]
      , ["8" , "S", ""]
      , ["9" , "S", ""]
      , ["10", "S", ""]
      , ["11", "S", ""]
      , ["12", "S", ""]
      , ["13", "S", ""]
      , ["1" , "C", ""]
      , ["2" , "C", ""]
      , ["3" , "C", ""]
      , ["4" , "C", ""]
      , ["5" , "C", ""]
      , ["6" , "C", ""]
      , ["7" , "C", ""]
      , ["8" , "C", ""]
      , ["9" , "C", ""]
      , ["10", "C", ""]
      , ["11", "C", ""]
      , ["12", "C", ""]
      , ["13", "C", ""]
    ]

    def ClearDeck(self):
        for i in range(0, len(self.__deck) + 4):
            self.__deck[i][2] = ""
    def PrintCard(self):
        print(self.__deck[1][2])        

ideck = deck()
ideck.PrintCard()
#print(ideck.__deck[1][2])

#ideck.__deck[1][2] = "ddd"
#ideck.ClearDeck
#print(ideck.__deck[1][2])




import random

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
         , [11, 1, 0]
         , [12, 1, 0]
         , [13, 1, 0]]
#    def ClearDeck():
#deck = [[__Rank[i] for i in range(13), __Suit[0]]]
#print(deck)

#print(random.randint(0, 13))
#print(random.sample(__Rank, 13))
#Player = __deck[random.sample(__Rank, 13)]
#print(random.sample(__deck, 13))

def GetCard() :
    SelectedCard = random.sample(__deck, 1)
    SelectedRank = SelectedCard[0][0]
    print(SelectedRank)
#    SelectedSuit = SelectedCard[1]
#    __deck[SelectedRank] = [SelectedRank, SelectedSuit, 1]
    return SelectedCard[0]

print(GetCard())













from ast import Is
import random
import sys
from tkinter import messagebox
import tkinter


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
#    def ClearDeck():
#deck = [[__Rank[i] for i in range(13), __Suit[0]]]
#print(deck)


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
frm = tkinter.Tk()
frm.geometry('600x400')
frm.title('BLACKJACK')
frm.mainloop()

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
    exit()


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