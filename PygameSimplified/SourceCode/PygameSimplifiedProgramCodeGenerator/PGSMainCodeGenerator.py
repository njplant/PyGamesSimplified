import sys,os
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui, Qsci
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import PGSTextEdit
from PGSTextEdit import PGSTextEditor
from PGSTextEdit import FromWidget

class MainWindow(QMainWindow):
    
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.setGeometry(200, 40, 920, 790)
        self.setWindowTitle('Pygame Simplified Code Generator')
        
        #GroupBox
        self.set_world_Group = GroupedBox(self, QRect(20, 110,450, 200),  'Set World')
        self.set_actor_Group = GroupedBox(self, QRect(20, 350,600, 350),  'Set Actors')
        self.your_actor_Group = GroupedBox(self, QRect(650, 350,200, 250),  'Your Actors')


        #changes
        layout = QVBoxLayout(self) # create layout out
        layout.addWidget(self.set_world_Group) # add world rectangle to widget
        layout.addWidget(self.set_actor_Group) # add actor rectangle to widget
        layout.addWidget(self.your_actor_Group) # add youractor rectangle to widget
        self.setLayout(layout)
        
        #call textarea, button, image and labels function     
        self.create_text_areas()
        self.set_pgs_logo_image()
        self.set_background_colour()
        self.create_labels()
        self.create_buttons()
        
        #add buttons to widget     
        layout.addWidget(self.create_buttons())
        
        self.newWindow = None
        self.widget=None
        
        self.initialise_actors_details()

    '*----------------------------View function------------------------------*'  
    def disable_actor_details(self):
        self.set_actors_number.setEnabled(False)
        self.set_number_of_actors.setEnabled(False)
        #if the user sets their number of actors, they can set their actors details as these buttons are enabled.        
        self.draw_actor_x.setEnabled(True)
        self.draw_actor_y.setEnabled(True)
        self.set_actor.setEnabled(True)
        self.set_actor_image.setEnabled(True)
        self.add_actors_image.setEnabled(True)
        self.add_another_actor.setEnabled(True)
        
    #add text areas to GUI.    
    def create_text_areas(self):
        self.set_world = QtGui.QLineEdit(self)
        self.set_world.setGeometry(120, 130,100, 20)
            
        self.set_world_width = QtGui.QLineEdit(self)
        self.set_world_width.setGeometry(120, 170,100, 20)

        self.set_world_height = QtGui.QLineEdit(self)
        self.set_world_height.setGeometry(120,210,100, 20)

        self.draw_actor_x = QtGui.QLineEdit(self)
        self.draw_actor_x.setGeometry(230,500,100, 20)
        self.draw_actor_x.setEnabled(False)

        self.draw_actor_y = QtGui.QLineEdit(self)
        self.draw_actor_y.setGeometry(230,530,100, 20)
        self.draw_actor_y.setEnabled(False)

        self.set_actor = QtGui.QLineEdit(self)
        self.set_actor.setGeometry(230,430,150, 20)
        self.set_actor.setEnabled(False)

        self.set_actor_image = QtGui.QLineEdit(self)
        self.set_actor_image.setGeometry(230,570,250,20)
        self.set_actor_image.setEnabled(False)

        self.set_world_image = QtGui.QLineEdit(self)
        self.set_world_image.setGeometry(200,250,250,20)

        self.set_actors_number = QtGui.QLineEdit(self)
        self.set_actors_number.setGeometry(230,390,100,20)

    #add buttons to GUI.
    def create_buttons(self):
        self.add_another_actor = QtGui.QPushButton("Add actor", self)
        self.add_another_actor.setGeometry(450,670,150,20)
        self.add_another_actor.setEnabled(False)

        self.set_number_of_actors = QtGui.QPushButton("Set number of actors", self)
        self.set_number_of_actors.setGeometry(380,390,150,20)
        
        self.generate_template_btn = QPushButton("Generate template", self.centralWidget)
        self.generate_template_btn.setGeometry(450,730,150,25)
        self.generate_template_btn.setEnabled(False)

        self.add_actors_image = QtGui.QPushButton("Set actors image", self)
        self.add_actors_image.setGeometry(25, 570,150, 25)
        self.add_actors_image.setEnabled(False)
        
        self.add_world_image = QtGui.QPushButton("Set worlds image", self)
        self.add_world_image.setGeometry(25, 250,150, 25)
        self.signals()

    #add text labels to GUI        
    def create_labels(self):
        self.setStyleSheet('font-size: 10pt; font-family: Comic Sans MS;')
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtGui.QColor(0,128,0))
        
        self.details_text = QtGui.QLabel(self)
        self.details_text.setGeometry(510, 110,900, 70)
        self.details_text.setText("Instructions: Enter the your world and actors details. \nYou can generate only one world and the number of actors\nset. For example, if you set 10 actors you can only generate\n10 actors.")

        self.program_name_text = QtGui.QLabel(self)
        self.program_name_text.setGeometry(640, 10, 900, 100)
        self.program_name_text.setText("Program code generator!")
        self.program_name_text.setPalette(palette)
        self.program_name_text.setStyleSheet('font-size: 15pt; font-family: Comic Sans MS;')
        
        self.world_name_text = QtGui.QLabel(self)
        self.world_name_text.setGeometry(25, 130,150, 20)
        self.world_name_text.setText("World name:")

        self.world_width_text = QtGui.QLabel(self)
        self.world_width_text.setGeometry(25, 170,150, 20)
        self.world_width_text.setText("World width:")

        self.world_height_text = QtGui.QLabel(self)
        self.world_height_text.setGeometry(25, 210,150, 20)
        self.world_height_text.setText("World height:")

        
        self.actors_name_text = QtGui.QLabel(self)
        self.actors_name_text.setGeometry(25, 430,150, 20)
        self.actors_name_text.setText("Actor name:")

        self.draw_actor_text = QtGui.QLabel(self)
        self.draw_actor_text.setGeometry(25, 440,800, 70)
        self.draw_actor_text.setText("Set the x and y location of your actor:")

        self.draw_actor_x_text = QtGui.QLabel(self)
        self.draw_actor_x_text.setGeometry(25, 500,150, 20)
        self.draw_actor_x_text.setText("x location")

        self.draw_actor_y_text = QtGui.QLabel(self)
        self.draw_actor_y_text.setGeometry(25, 530,150, 20)
        self.draw_actor_y_text.setText("y location")

        self.number_of_actors_label = QtGui.QLabel(self)
        self.number_of_actors_label.setGeometry(25, 380,200, 35)
        self.number_of_actors_label.setText("Number of actors\nyou would like to generate")

        self.actors_name_label = QtGui.QLabel(self)
        self.actors_name_label.heightForWidth(500)
        self.actors_name_label.setMinimumSize(200, 200)
        self.actors_name_label.setMaximumSize(200, 200)
        self.actors_name_label.setGeometry(QRect(655, 300, self.width(), self.height()))

    #set the background colour of GUI        
    def set_background_colour(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255,255, 255))
        self.setPalette(p)
        
    #add the Pygame Simplified logo to the GUI
    def set_pgs_logo_image(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(250, 10, 400, 100)
        pic.setPixmap(QtGui.QPixmap("images/pgs.png"))

   

    #clear all the text areas. 
    def clear_text_areas(self):
        self.set_actor.clear()
        self.draw_actor_x.clear()
        self.draw_actor_y.clear()
        self.set_actor_image.clear()
        
    '*----------------------------Model functions------------------------------*'
    #get the number of actors from the number of actors button    
    def number_of_actors(self):
        self.no_actors= int(self.set_actors_number.text())
        self.disable_actor_details()

    #create arrays which store the details of actors        
    def initialise_actors_details(self):
        self.numberofactors=0
        self.labels_array=[]
        self.set_image_array=[]
        self.locationx=[]
        self.locationy=[]
        self.i=0

    #check if the actor inputted into the actors text area has already been inputted            
    def check_actor_exsits(self):
        actorText = self.set_actor.text()
        worldText = self.set_world.text()
        if actorText:
            if actorText not in self.labels_array:
                self.actors_name_label.setText('%s\n%s' % (self.actors_name_label.text(), actorText))
                self.labels_array.append(actorText)
                self.set_image_array.append(self.set_actor_image.text())
                self.locationx.append(self.draw_actor_x.text())
                self.locationy.append(self.draw_actor_y.text())
                self.i=self.i+1
            else:
                QMessageBox.about(self, "Error!", "You have already created the actor "+ actorText)
            if worldText in self.labels_array:
                QMessageBox.about(self, "Warning!", " Warning! Your World's name is an Actors name\nChange your World's name to something different.")
                
  
        #if the number of actors set is the same as number of actors generated, disable
        #add actor button and enable generate actor button.        
        self.no_actors= int(self.set_actors_number.text())
        if self.i ==self.no_actors:
            self.add_another_actor.setEnabled(False)
            self.generate_template_btn.setEnabled(True)
        self.clear_text_areas()
        
    

    #generates the code after user has set detail of actors and world.
    def generate_code(self):
        with open('template.py') as fin, open('marioexample2.py','w') as fout:
            space="    "
            for line in fin:
                fout.write(line)
                if line == 'from PGS.PygameSimplified import*\n':
                    next_line = next(fin)
                    if next_line == '\n':
                        fout.write('\n')
                        fout.write(self.set_world.text()+'= World('+self.set_world_width.text()+","+self.set_world_height.text()+')\r\n')
                        fout.write(self.set_world.text()+'.set_background("'+self.set_world_image.text()+'")\r\n')
                        for i in range(self.no_actors):
                            fout.write(self.labels_array[i]+'= Actor()\n')
                        fout.write('\n')
                        for  i in range(self.no_actors):
                            fout.write(self.labels_array[i]+'.set_image("' + self.set_image_array[i]+ '")\n')
                        fout.write('\n')
                        for  i in range(self.no_actors):
                            fout.write(self.labels_array[i]+'.set_location(' + self.locationx[i]+","+self.locationy[i]+')\n')
                        fout.write(next_line)
                if line == 'while running:\n':
                    next_line = next(fin)
                    if next_line == '\n':
                        for i in range(self.no_actors):
                            fout.write(space+self.labels_array[i]+'.update()\n')
                        fout.write('\n')
                        fout.write(space+"#---Enter your game logic below here!---\n")
                        fout.write('\n')
                        fout.write(space+self.set_world.text()+'.draw_background('+ '0'+','+'0)\n')
                        for i in range(self.no_actors):
                            fout.write(space+self.set_world.text()+'.draw_actor('+self.labels_array[i]+','+ self.labels_array[i]+'.x'+','+self.labels_array[i]+'.y)\n')
                        fout.write('\n')
                      
            
                
          
    '*----------------------------Controller function------------------------------*'
    #when the user clicks the generate code button, this function is called    
    def open_text_edit_window(self):
        #generate the program code       
        self.generate_code()
        #closes current window
        self.close()
        #open the text editor window        
        self.newWindow = PGSTextEditor()
        #show this window      
        self.newWindow.show()
        
    #open a file image if the clicks 'actor image' button      
    def open_actor_image_file(self):
        a = QFileDialog.getOpenFileName()
        i1 = os.path.basename(a) # image.png 
        i2 = os.path.basename(os.path.dirname(a)) # images 
        r = '/'.join((i2,i1)) # images\image.png
        self.set_actor_image.setText(r)

    #open a file image if the clicks 'world image' button     
    def open_world_image_file(self):
        a =QFileDialog.getOpenFileName()
        i1 = os.path.basename(a) # image.png 
        i2 = os.path.basename(os.path.dirname(a)) # images 
        r = '/'.join((i2,i1)) # images\image.png
        self.set_world_image.setText(r)

    #signals which connect button to action performed.          
    def signals(self):
        self.generate_template_btn.clicked.connect(self.open_text_edit_window)
        self.add_actors_image.clicked.connect(self.open_actor_image_file)
        self.add_world_image.clicked.connect(self.open_world_image_file)
        self.set_number_of_actors.clicked.connect(self.number_of_actors)
        self.add_another_actor.clicked.connect(self.check_actor_exsits)
        
#creates rectangle for each group box, the position and name are passed as arguments in constructor
class GroupedBox(QWidget): 
    def __init__(self, parent,  geometry,  title): 
        QWidget.__init__(self, parent)
        gb = QGroupBox(parent)
        gb.setGeometry(geometry)
        gb.setTitle(title)
        
#show main window
app = QApplication([])
main =  MainWindow()
main.show()
sys.exit(app.exec_())
        

