from Cards import *
class User:
    count = 0
    click = 0
    sum = 0
    userNum = 0;
    name = "default"
    def __init__(self, name):
        self.name = name
   
    @staticmethod
    def user1_sum(_int):
       User.sum = User.sum + Cards.get_user1card(_int)
       User.click = User.click + 1

    @staticmethod
    def user2_sum(_int):
       User.sum = User.sum + Cards.get_user2card(_int)
       User.click = User.click + 1
    
    @staticmethod
    def user3_sum(_int):
       User.sum = User.sum + Cards.get_user3card(_int)
       User.click = User.click + 1
   
    @staticmethod
    def get_clicks():
       return User.click
    