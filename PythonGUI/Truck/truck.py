from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import os, sys
import mainWindow



# this is the main window
class Truck(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Truck, self).__init__(parent)
        self.setupUi(self)
        self.light = 2 # 0 is red, 1 is yellow, 2 is green, 3 is green-left
        self.changeLight(2)
        self.move = 0 # 0 is nothing, 1 is forward, 2 is left, 3 is right, 4 is stop
        # listen for the buttons
        self.redButton.clicked.connect(self.handleRedButton)
        self.yellowButton.clicked.connect(self.handleYellowButton)
        self.greenButton.clicked.connect(self.handleGreenButton)
        self.leftGreenButton.clicked.connect(self.handleLeftGreenButton)
        self.fowardButton.clicked.connect(self.handleFowardButton)
        self.leftButton.clicked.connect(self.handleLeftButton)
        self.rightButton.clicked.connect(self.handleRightButton)
        self.stopButton.clicked.connect(self.handleStopButton)
        self.output("Semi Truck is fueled and ready!")


    # handle if the red button is clicked
    def handleRedButton(self):
        self.changeLight(0)

    # handle if the yellow button is clicked
    def handleYellowButton(self):
        self.changeLight(1)

    # handle if the green button is clicked
    def handleGreenButton(self):
        self.changeLight(2)

    # handle if the left green button is clicked
    def handleLeftGreenButton(self):
        self.changeLight(3)

    # handle if the forward button is clicked
    def handleFowardButton(self):
        if (self.move == 1):
            self.output("ERROR:  The truck is already moving forward!")
            self.resetLight()
            return
        elif (self.light == 0):
            self.output("ERROR:  You can't go through a red light!")
            self.resetLight()
            return
        elif (self.light == 1):
            self.output("Phew!  Squeezed through that one!")
        elif (self.light == 2):
            self.output("Went foward through the green light.")
        elif (self.light == 3):
            self.output("ERROR:  You can't go forward through a left-turn green light!")
            self.resetLight()
            return
        self.move = 1
        self.resetLight()

    # handle if the left button is clicked
    def handleLeftButton(self):
        if (self.move == 4):
            self.output("ERROR:  The truck is jack-knifed.  Can only move forward.")
            self.resetLight()
            return
        elif (self.light == 0):
            self.output("ERROR:  You can't turn left on a red light!")
            self.resetLight()
            return
        elif (self.light == 1):
            self.output("ERROR:  You can't turn left on a yellow light!")
            self.resetLight()
            return
        elif (self.light == 2):
            self.output("ERROR:  You can't turn left on a green light!")
            self.resetLight()
            return
        elif (self.light == 3):
            self.output("You turned left on the left-turn green light.")
        self.move = 2
        self.resetLight()

    # handle if the right button is clicked
    def handleRightButton(self):
        if (self.move == 4):
            self.output("ERROR:  The truck is jack-knifed.  Can only move forward.")
            self.resetLight()
            return
        elif (self.light == 0):
            self.output("You turn right after looking for oncoming traffic.")
        elif (self.light == 1):
            self.output("Phew!  Squeezed through that one!")
        elif (self.light == 2):
            self.output("You turned right on the green light.")
        elif (self.light == 3):
            self.output("ERROR:  You can't turn right on a left-turn green light!")
            self.resetLight()
            return
        self.move = 3
        self.resetLight()

    # handle if the stop button is clicked
    def handleStopButton(self):
        if (self.move == 4):
            self.output("ERROR:  The truck is already jack-knifed.  Can only move forward.")
            self.resetLight()
            return
        self.output("The truck has been jack-knifed.  You can only go forward.")
        self.move = 4
        self.resetLight()

    # output to the list
    def output(self, string):
        self.outputList.addItem(string)

    # function to streamline changing the light
    def changeLight(self, number):
        self.light = number
        if (number == 0):
            self.redLabel.setText("Red")
            self.yellowLabel.setText("")
            self.greenLabel.setText("")
            self.leftGreenLabel.setText("")
        elif (number == 1):
            self.redLabel.setText("")
            self.yellowLabel.setText("Yellow")
            self.greenLabel.setText("")
            self.leftGreenLabel.setText("")
        elif (number == 2):
            self.redLabel.setText("")
            self.yellowLabel.setText("")
            self.greenLabel.setText("Green")
            self.leftGreenLabel.setText("")
        elif (number == 3):
            self.redLabel.setText("")
            self.yellowLabel.setText("")
            self.greenLabel.setText("")
            self.leftGreenLabel.setText("<---Green")

     # reset the light to green
    def resetLight(self):
        self.changeLight(2)

# this is the main driver for the GUI and client
def main():
    # make the app
    app = QApplication(sys.argv)
    # make the main window form
    form = Truck()
    # show the main window
    form.show()
    # exit the program after it's done (closes or runs to end)
    exit(app.exec())

# if the script is run directly, run the main function
if __name__=='__main__':
    main()