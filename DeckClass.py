suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
import random
class Deck():
  
  def __init_(self):
    
    self.all_cards = []
    
    for suit in suits:
      for rank in ranks:
        #create the Card  Object
        created_card = Card(suit, rank)
        self.all_cards.append(created_card)
       
   def shuffle(self):
    
    random.shuffle(self.all_cards)
    
   def deal_one(self):
    return self.all_cards.pop()
