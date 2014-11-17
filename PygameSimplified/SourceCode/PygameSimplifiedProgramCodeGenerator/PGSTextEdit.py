import sys,os
from code import InteractiveInterpreter
from PyQt4 import QtCore, QtGui, Qsci
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
from PyQt4.Qsci import *
from PyQt4.QtGui import QApplication
from PyQt4.Qsci import QsciScintilla


#window for the text editor
class PGSTextEditor(QMainWindow):
    def __init__(self, parent=None):
        super(PGSTextEditor, self).__init__(parent)

        #call FromWigit class, so that the wdigets can be drawn on the main window        
        self.form_widget = FromWidget(self) 
        self.setCentralWidget(self.form_widget)
        self.setGeometry(300,100,600,680)
        self.setWindowTitle('Pygame Simplified IDE')

        #create a save action        
        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)

        #create a open action       
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.openaFile)

        #create menubacr        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveAction)
        fileMenu.addAction(openFile)

        #add the Pygame Simplified logo to IDE
        pic = QtGui.QLabel(self)
        pic.setGeometry(10, 10, 400, 100)
        pic.setPixmap(QtGui.QPixmap("images/pgs.png"))

        #set the background colour        
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255,255, 255))
        self.setPalette(p)

    #save file dialogue      
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.form_widget.text()
        f.write(filedata)
        f.close()
    #open file dialogue     
    def openaFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        f = open(fname, 'r')
        with f:        
            data = f.read()
            self.form_widget.text.setText(data) 

#widget for the text editor       
class FromWidget(QWidget):

    def __init__(self, parent):
        super(FromWidget, self).__init__(parent)
        
        #add the text editor to the widget.        
        self.text = QsciScintilla(self)
        self.text.setGeometry(10,100,500,500)
        
        #set the code to be read to Python code        
        self.lexer = QsciLexerPython()

        ## Create an API for us to populate with our autocomplete terms
        self.generate_code = Qsci.QsciAPIs(self.lexer)
        
        ## Add autocompletion strings
        self.generate_code.add("set_image")
        self.generate_code.add("draw_actor")

        # Compile the api for use in the lexer
        self.generate_code.prepare()

        #sets the program code in the text editor to the generated code        
        self.open_generated_code()

        #set the lext         
        self.text.setLexer(self.lexer)

        #Set the length of the string before the editor tries to autocomplete
        self.text.setAutoCompletionThreshold(1)
        
        #Tell the editor we are using a QsciAPI for the autocompletion
        self.text.setAutoCompletionSource(QsciScintilla.AcsAPIs)

        #set the background and foreground colour of the margin        
        self.text.setMarginsBackgroundColor(QColor(34,139,34))
        self.text.setMarginsForegroundColor(QColor(0,0,0))
        
        #set the line numbers from 1        
        self.text.setMarginLineNumbers(1,True) 
        self.text.setAutoIndent(True)
        self.text.setIndentationsUseTabs(False)
       
        #allow the user to collapse code        
        self.text.setFolding(1)

        self.create_buttons()
        self.buttons_controler()

    #function to creat buttons    
    def create_buttons(self):
        #create runcode button and add it to the widget              
        self.runcodebutton = QtGui.QPushButton("Run Code",self)
        self.runcodebutton.setGeometry(100,610,70,30)
        
        #create generatecode button and add it to the widget
        self.generatecodebutton = QtGui.QPushButton("Generate Template",self)
        self.generatecodebutton.setGeometry(400,5,100,30)

        #create savecode button and add it to the widget
        self.savecodebutton = QtGui.QPushButton("Save Code",self)
        self.savecodebutton.setGeometry(10,610,70,30)

    #signals which connects buttons to actions     
    def buttons_controler(self):
        self.runcodebutton.clicked.connect(self.run_code_button_clicked)
        self.generatecodebutton.clicked.connect(self.gen_code_button_clicked)
        self.savecodebutton.clicked.connect(self.askQuestion)

    #opens the generated program code    
    def open_generated_code(self):
        self.filename ='marioexample2.py'
        f = open(self.filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()

    #performs action for run code button        
    def run_code_button_clicked(self):
        interpreter = InteractiveInterpreter()
        interpreter.runcode(self.text.text())

    #perfoms action for generate code button
    def gen_code_button_clicked(self):
        #ask if user is sure theu could like to regenerate code, in dialogue
        quit_msg = "Are you sure you would like to regenerate your program code, your current\ncode will be overidden unless you save your code."
        answer = QtGui.QMessageBox.question(self, 'Pygame Simplfied message', 
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        #if the users answer is yes, regenerate the code       
        if answer == QtGui.QMessageBox.Yes:
            self.filename ='marioexample2.py'
            f = open(self.filename, 'r')
            filedata = f.read()
            self.text.setText(filedata)
            f.close()

    #if the user clicks the save button, the code is saved    
    def save(self):
        f = open('mygame.py', 'w')
        #gets the text from the text editor        
        filedata = self.text.text()
        f.write(filedata)
        f.close()

    #check if user wants to save their program    
    def askQuestion(self, event):
        quit_msg = "Are you would like to save your program?\nthis will save as mygame.py"
        answer = QtGui.QMessageBox.question(self, 'Pygame Simplfied message', 
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if answer == QtGui.QMessageBox.Yes:
            self.save()

        
#code to open text editor as a seperate windows
##app = QApplication([])
##main =  PGSTextEditor()
##main.show()
##sys.exit(app.exec_()) 
    
 
    
