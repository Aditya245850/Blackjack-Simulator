import threading
from base64 import b16decode
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

from Cards import *
from User import *
class Windows:
    b1=None
    b2=None
    b3=None
    b4=None
    b5=None
    b6=None
    b7=None
    b8=None
    b9=None
    user1_name = ""
    user2_name = ""
    user3_name = ""
    window=None
    @staticmethod
    def createBoard(_int):
        app = QApplication(sys.argv)
        global window
        window = QWidget()
        window.setGeometry(0,0,600,600)
        window.setWindowTitle("Card Game")
        for x in range (1, int(User.userNum) + 1):
               if x == 1:
                  textLabel = QLabel(window)
                  textLabel.setText(Windows.user1_name)
                  textLabel.move(70,400)
                  textLabel2 = QLabel(window)
                  textLabel2.setText("Dealer")
                  textLabel2.move(300,50)
                  global b1
                  b1 = QPushButton("1", window)
                  b1.move(30, 300)
                  b1.resize(40, 90)
                  b1.clicked.connect(lambda: User.user1_sum(1))
                  b1.clicked.connect(lambda: b1.hide())
                  b1.clicked.connect(lambda: Windows.window_close1())
                  
                  end_turn = QPushButton("end turn", window)
                  end_turn.move(30, 100)
                  end_turn.resize(100, 100)
                  end_turn.clicked.connect(lambda: window.close())
                  

                  global b2
                  b2 = QPushButton("2", window)
                  b2.move(70, 300)
                  b2.resize(40, 90)
                  b2.clicked.connect(lambda: User.user1_sum(2))
                  b2.clicked.connect(lambda: b2.hide())
                  b2.clicked.connect(lambda: Windows.window_close1())

                  global b3
                  b3 = QPushButton("3", window)
                  b3.move(110, 300)
                  b3.resize(40, 90)
                  b3.clicked.connect(lambda: User.user1_sum(3))
                  b3.clicked.connect(lambda: b3.hide())
                  b3.clicked.connect(lambda: Windows.window_close1())
               if x == 2:
                  textLabel = QLabel(window)
                  textLabel.setText(Windows.user2_name)
                  textLabel.move(250,400)
                 
                  global b4
                  b4 = QPushButton("1", window)
                  b4.move(210, 300)
                  b4.resize(40, 90)
                  b4.clicked.connect(lambda: User.user2_sum(1))
                  b4.clicked.connect(lambda: b4.hide())
                  b4.clicked.connect(lambda: Windows.window_close1())

                  global b5
                  b5 = QPushButton("2", window)
                  b5.move(250, 300)
                  b5.resize(40, 90)
                  b5.clicked.connect(lambda: User.user2_sum(2))
                  b5.clicked.connect(lambda: b5.hide())
                  b5.clicked.connect(lambda: Windows.window_close1())

                  global b6
                  b6 = QPushButton("3", window)
                  b6.move(290, 300)
                  b6.resize(40, 90)
                  b6.clicked.connect(lambda: User.user2_sum(3))
                  b6.clicked.connect(lambda: b6.hide())
                  b6.clicked.connect(lambda: Windows.window_close1())
                  
               if x == 3:
                  textLabel = QLabel(window)
                  textLabel.setText(Windows.user3_name)
                  textLabel.move(450,400)

                  global b7   
                  b7 = QPushButton("1", window)
                  b7.move(410, 300)
                  b7.resize(40, 90)
                  b7.clicked.connect(lambda: User.user3_sum(1))
                  b7.clicked.connect(lambda: b7.hide())
                  b7.clicked.connect(lambda: Windows.window_close1())

                  global b8
                  b8 = QPushButton("2", window)
                  b8.move(450, 300)
                  b8.resize(40, 90)
                  b8.clicked.connect(lambda: User.user3_sum(2))
                  b8.clicked.connect(lambda: b8.hide())
                  b8.clicked.connect(lambda: Windows.window_close1())

                  global b9
                  b9 = QPushButton("3", window)
                  b9.move(490, 300)
                  b9.resize(40, 90)
                  b9.clicked.connect(lambda: User.user3_sum(3))
                  b9.clicked.connect(lambda: b9.hide())
                  b9.clicked.connect(lambda: Windows.window_close1())
              
        if _int == 1:
            Windows.disable_user1buttons()
        if _int == 2:
            Windows.disable_user2buttons()
        if _int == 3:
            Windows.disable_user3buttons()
        


        window.show()
        
        app.exec()
    
    @staticmethod
    def disable_user1buttons():
      b4.hide()
      b5.hide()
      b6.hide()
      b7.hide()
      b8.hide()
      b9.hide()
    def disable_user2buttons():
      b1.hide()
      b2.hide()
      b3.hide()
      b7.hide()
      b8.hide()
      b9.hide()
    def disable_user3buttons():
      b1.hide()
      b2.hide()
      b3.hide()
      b4.hide()
      b5.hide()
      b6.hide()
      
    @staticmethod
    def window_close1():
     if (User.get_clicks() != 0) and (User.get_clicks() % 2 == 0):
      global b1
      b1.hide()
      global b2
      b2.hide()
      global b3
      b3.hide()
      global b4
      b4.hide()
      global b5
      b5.hide()
      global b6
      b6.hide()
      global b7
      b7.hide()
      global b8
      b8.hide()
      global b9
      b9.hide()
      