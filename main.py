# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import re

# class mainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
     
        # add title to window
        self.setWindowTitle("Linear Algebra")

        # setting window size
        self.setFixedSize(800,400)

        # call style window methods
        self.style_Mwindow()
  

        # displying window
        self.show()

    # style of window
    def style_Mwindow(self):

        # add label To clarify what the program is
        self.Label = QLabel("<b>Solving Systems of Linear Equations using Gaussian Elimination</b>",self)
        self.Label.move(150,10)
        self.Label.resize(600,40)
        self.Label.setStyleSheet("font-size:15px")

        # add area to enter equations as input
        self.input_area = QTextEdit(self)
        self.input_area.move(15,50)
        self.input_area.resize(380,250)
        self.input_area.setStyleSheet("font-size:15px")
        self.input_area.setPlaceholderText("Enter equations Like 1x(+,-) 2x(+,-)...nx = constant.")

        # add area to show Solving Equations
        self.output_area = QTextEdit(self)
        self.output_area.move(405,50)
        self.output_area.resize(385,250)
        self.output_area.setStyleSheet("font-size:15px")
        self.output_area.setPlaceholderText("when you click Gaussian Elimination button will see output here")

        # add Gaussian Elimination button
        self.button_Gaussian_Elimination = QPushButton("Apply Gaussian Elimination method",self)
        self.button_Gaussian_Elimination.move(260,340)
        self.button_Gaussian_Elimination.resize(280,32)
        self.button_Gaussian_Elimination.setStyleSheet("border-radius:8px;font-size:15px;bacKground:#344D67;color:white;")
        self.button_Gaussian_Elimination.clicked.connect(self.Prepare_matrix)

    # Prepare matrix to apply Gaussian Elimination function
    def Prepare_matrix(self):
        # empty list to assign equations value
        matrix = []
        # git each unique row 
        filter_Equations = [i for i in self.input_area.toPlainText().split("\n")]

        for num in range(len(filter_Equations)):
            filter_Equations[num] = filter_Equations[num].replace(" ","")
            filter_Equations[num] = filter_Equations[num].replace("x","")

        # filter input to git coefficients of variables
        for j in range(len(filter_Equations)):
            matrix+=[[int(num) for num in re.findall(r'-?\d+', filter_Equations[j])]]
    
        # Show output in output area
        self.output_area.setPlainText(self.handle_output(self.Gaussian_Elimination(matrix)))

    # function to handle output
    def handle_output(self,array):
        # creat empty string to assign final output
        array_ass_string = ""
        for key,value in array.items():
            array_ass_string+= f"{key} = {str(value)}" + "{}".format("\n")

        return array_ass_string # final output send to output area
       
    # function of Gaussian Elimination
    def Gaussian_Elimination(self,Matrix):
        # find number of row in matrix
        size = len(Matrix)
        # list of zeros to handle output
        soul_Equation = [0] * size
        for i in range(size):
            if Matrix[i][i] == 0.0:
                if i < size :
                    Matrix[i][i+1] = Matrix[i+1][i] # swap tow row if not last row
                else:
                    Matrix[i][i-1] = Matrix[i-1][i] # swap tow row if last row

            for j in range(i+1,size):
                ratio = Matrix[j][i]/Matrix[i][i]

                for k in range(size+1):
                    Matrix[j][k] = Matrix[j][k] - ratio * Matrix[i][k]

        soul_Equation[size-1] = Matrix[size-1][size]/Matrix[size-1][size-1]
        for i in range(size-2,-1,-1):
            soul_Equation[i] = Matrix[i][size]
            
            for j in range(i+1,size):
                soul_Equation[i] = soul_Equation[i] - Matrix[i][j]*soul_Equation[j]
            soul_Equation[i] = soul_Equation[i]/Matrix[i][i]

        soul_equation = {f"X{index+1}":value for index,value in enumerate(soul_Equation)}
        return soul_equation


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = MainWindow()


# start the app
sys.exit(App.exec_())