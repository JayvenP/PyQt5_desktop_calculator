# Import libraries
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # Set Window Title
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = [] # Create a list for first set of numbers 
        self.fin_nums = [] # Create list for final set of numbers
        
        self.show()
        
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        # Labeling buttons and fields
        self.results_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('=', clicked = self.func_result)
        btn_clear = qtw.QPushButton('CE', clicked = self.clear_calc)
        btn_0 = qtw.QPushButton('0', clicked = lambda: self.num_press('0'))
        btn_1 = qtw.QPushButton('1', clicked = lambda: self.num_press('1'))
        btn_2 = qtw.QPushButton('2', clicked = lambda: self.num_press('2'))
        btn_3 = qtw.QPushButton('3', clicked = lambda: self.num_press('3'))
        btn_4 = qtw.QPushButton('4', clicked = lambda: self.num_press('4'))
        btn_5 = qtw.QPushButton('5', clicked = lambda: self.num_press('5'))
        btn_6 = qtw.QPushButton('6', clicked = lambda: self.num_press('6'))
        btn_7 = qtw.QPushButton('7', clicked = lambda: self.num_press('7'))
        btn_8 = qtw.QPushButton('8', clicked = lambda: self.num_press('8'))
        btn_9 = qtw.QPushButton('9', clicked = lambda: self.num_press('9'))
        btn_plus = qtw.QPushButton('+', clicked = lambda: self.func_press('+'))
        btn_mins = qtw.QPushButton('-', clicked = lambda: self.func_press('-'))
        btn_mult = qtw.QPushButton('*', clicked = lambda: self.func_press('*'))
        btn_divd = qtw.QPushButton('/', clicked = lambda: self.func_press('/'))
        
        # Adding buttons into grid layout
        # Example: addWidget(variable,row,column,row_size,column_size)
        container.layout().addWidget(self.results_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,3)
        container.layout().addWidget(btn_clear,2,3)
        container.layout().addWidget(btn_plus,3,3)
        container.layout().addWidget(btn_mins,4,3)
        container.layout().addWidget(btn_7,1,0)
        container.layout().addWidget(btn_8,1,1)
        container.layout().addWidget(btn_9,1,2)
        container.layout().addWidget(btn_4,2,0)
        container.layout().addWidget(btn_5,2,1)
        container.layout().addWidget(btn_6,2,2)
        container.layout().addWidget(btn_1,3,0)
        container.layout().addWidget(btn_2,3,1)
        container.layout().addWidget(btn_3,3,2)
        container.layout().addWidget(btn_0,4,0)
        container.layout().addWidget(btn_mult,4,1)
        container.layout().addWidget(btn_divd,4,2)
        
        # Putting widgets back into MainWindow when self.keypad() is called
        self.layout().addWidget(container)
        
    def num_press(self, key_number):
        self.temp_nums.append(key_number) # Append number pressed to 'temp_nums' list
        temp_string = ''.join(self.temp_nums) # Create a temporary string to store numbers pressed
        if self.fin_nums: # If something exists in 'fin_nums' list then print it out as a string
            self.results_field.setText(''.join(self.fin_nums) + temp_string)
        else: # If nothing exists in 'fin_nums' list then just print out what is in temp_string to the 'results_field'
            self.results_field.setText(temp_string)
            
    def func_press(self, operator): 
        temp_string = ''.join(self.temp_nums) # Append 'temp_nums' (numbers) that was previously pressed to local temp_string
        self.fin_nums.append(temp_string) # Append 'temp_string to 'fin_nums' list
        self.fin_nums.append(operator) # Append operator pressed to 'temp_nums' list
        self.temp_nums = [] # Clear the 'temp_nums' list
        self.results_field.setText(''.join(self.fin_nums)) # Set the results_field to what is in the 'fin_nums' list as a string
        
    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums) # Takes in all elements from 'fin_nums' and 'temp_nums' list
        result_string = eval(fin_string) # Using python built in function eval() to convert string to an equation
        fin_string += '=' # Add equal sign to evaluate the equation, for visual cosmetic only*
        fin_string += str(result_string) # Append in the result as a string to the 'result_string'
        self.results_field.setText(fin_string) # Set the results_field to what is in the 'fin_string' list as a string
        
    def clear_calc(self):
        self.results_field.clear() # Clears the results_field
        self.temp_nums = [] # Sets the 'temp_nums' as an empty list
        self.fin_nums = [] # Sets the 'fin_nums' as an empty list
        
app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
