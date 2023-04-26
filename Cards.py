import random
from User import *
class Cards:
    user1_deck = [0,0,0]
    user2_deck = [0,0,0]
    user3_deck = [0,0,0]
    def create_decks():
        Cards.user1_deck = random.sample(range(1, 100), 3)
        Cards.user2_deck = random.sample(range(1, 100), 3)
        Cards.user3_deck = random.sample(range(1, 100), 3)
    
    
    @staticmethod
    def get_user1card(_int):
        return Cards.user1_deck[_int - 1]

    def get_user2card(_int):
        return Cards.user2_deck[_int - 1]
    
    def get_user3card(_int):
        return Cards.user3_deck[_int - 1]
