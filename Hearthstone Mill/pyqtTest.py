import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


#Much help from https://pythonspot.com/pyqt5/
 
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
 
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
 
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
 
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Next Draw:"), QLineEdit())
        layout.addRow(QLabel("Last Draw:"), QLineEdit())
        layout.addRow(QLabel("Total Dmg:"), QTextEdit(
        self.formGroupBox.setLayout(layout)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())