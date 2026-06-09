import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,QHBoxLayout
  
)
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Username Generator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        hbox = QHBoxLayout()

        layout = QVBoxLayout()
        title_label = QLabel("Enter a premade username if you have one:")
        explanatory_sentence = QLabel("This app is for generating usernames and checking to see if theyve been created already or not.")

        
        self.name_input = QLineEdit(placeholderText="Type premade username here: ")
        # TODO: add a push button to greet user
        submit_button = QPushButton("greet me!")
        submit_button.clicked.connect(self.get_input)
        # TODO: add a label to greet user
        submit_button_job = QPushButton("username")
        submit_button_job.clicked.connect(self.job_input, self.name_data)

        
       


        self.instructions = "Enter your name and click the button, then, enter your job in the box to the right."
        self.output_label = QLabel(self.instructions)
        self.job_inputs = QLineEdit(placeholderText="Enter your first name")
        self.name_datas = QLineEdit(placeholderText= "Type your job here...")
       
        
        layout.addWidget(explanatory_sentence)
        layout.addWidget(title_label)
        layout.addWidget(self.name_input)
        layout.addWidget(submit_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.name_datas) 
        layout.addWidget(self.job_inputs)
        layout.addWidget(submit_button_job)
        
        
        layout.addStretch()
    
#setsize - .setsize -for changing the size to make the boxes small 
        widget = QWidget()
        widget.setLayout(layout)
        widget.setLayout(hbox)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


    def get_input(self):
        output = "Hello, "
        name = self.name_input.text()
        if not name:
            output = "friend" + "Give a real name next time, you didn't this time!" 
            output += "your name is empty!"
        else:
            output = f"You've entered: {name} as your username." 
        self.output_label.setText(output)

    def name_data(self):
        output = "Hello, "
        name_d = self.name_datas.text()
        if not name_d:
           output = f"g"
           output  += "n"
        else:
            output = f"your username is, {name_d}"
        self.output_label.setText(output)
    
    def job_input(self):
        output = "Hello, "
        job = self.job_inputs.text() 
        if not job:
           output = f"No username was entered."
        else:
            output = f"you entered, {job} as your job."
        self.output_label.setText(output)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
