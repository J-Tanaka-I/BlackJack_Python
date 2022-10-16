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