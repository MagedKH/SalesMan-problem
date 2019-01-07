#Display SalesMan problem'solution using GUI
#files related to this code : shared.py ,city.py ,GuiComponents.py 
#Done by: Mahmoud Gertallah
#Communication between GUI and Algorithms done by : Maged Khaled Ahmed 
#Communication between java and python done by : Asmaa Abd El_Naser


from PyQt5.QtWidgets import (QApplication,QWidget,QGridLayout,QHBoxLayout,QVBoxLayout,
QPushButton,QLabel,QLineEdit,QLCDNumber,QFrame,QSplitter,QDesktopWidget)
from PyQt5.QtGui import QFont , QPainter , QPen , QPixmap , QColor
from PyQt5.QtCore import Qt 
import sys , random , time
from GuiComponents import Text
from city import Cell
import shared



 # Window of GUI application       
class Window(QWidget):
    # Constructor
    result = []
    def __init__(self):
        super().__init__()
        self.initWin()
  ##########################################################################################      
    def run_algorithm(self):
         if(self.sender() is self.srgBtn1): #Run Gentic Algorithm
             import genticA , variables
             genticA.main_Loop() 
             shared.algorithm1 = variables.best_Order
             self.result = shared.algorithm1_result()
             pass 
         
         elif(self.sender() is self.srgBtn2): #Run Simulated Annealing Algorithm 
             import salesman 
             salesman.main_Loop() 
             shared.algorithm2 = salesman.best_Order
             self.result = shared.algorithm2_result()
             pass
         
            
         elif(self.sender() is self.srgBtn3): #Run tabu Algorithm 
             import Algorithm3 
             Algorithm3.main_Loop() 
             shared.algorithm3 = Algorithm3.best_Order
             self.result = shared.algorithm3_result()
             pass
################################################################################################
        
         #self.result = [5,1,12,9,7,13,4,8,10,3,0,11,6,2,14,5,80]  # test list 
         cost = self.result.pop()
         for index , seq  in zip(self.result[1:] , range(1,self.cities_no)):
            self.nodes[index].color = (255, 165, 0)
            self.nodes[index].index = str(seq)
            self.nodes[index].repaint()
            time.sleep(.2)
         self.lcd1.display(cost)
        
    def get_input(self,text):
        if(self.sender() is self.iptEdt1):
            ipt = []
            for char in text :
                if(char.isdigit()):
                    ipt.append(char)
            if(len(ipt) == 2):
                self.cities_no = int(ipt[0] + ipt[1])
            else:
                self.cities_no = int(ipt[0])
            shared.number_Elements = self.cities_no
        elif(self.sender() is self.iptEdt2):
            if(text.isupper()):
                self.start = text
            elif(text.islower()):
                self.start = text.upper()
            
        
        
        
    def bulid_map(self):
        self.hint.setParent(None)
        self.char = [chr(x) for x in range(65,91)]
        w = [x for x in range(10,1000,36)]
        h = [y for y in range(10,680,24)]
        for i in range(self.cities_no):
            x = w.pop(random.randint(0,len(w)-1))
            y = h.pop(random.randint(0,len(h)-1))
            if(self.char[i] == self.start):
                n = Cell(self.char[i],x,y,(218, 112, 214),self)
                n.show()
                shared.initial_state = i
            else:
                n = Cell(self.char[i],x,y,(0, 255, 0),self)
                n.show()
            #print(x,y)
            self.nodes[i] = n
        
        shared.generated_nodes = self.nodes.copy()
        #print(shared.initial_state)
        self.update()
        
    def get_initial(self):
        for i in range(self.cities_no):
            self.nodes[i].setParent(None)
        self.flag = False
        self.repaint()
        self.hint.setParent(self)
        self.hint.show()
        self.lcd1.display(0)
        self.iptEdt1.clear()
        self.iptEdt2.clear()
        self.flag = False
        self.repaint()
        self.mapFrame.setParent(self)
        self.mapFrame.show()
        
    def reset(self):
        for i in range(self.cities_no):
            if(self.nodes[i].index == self.start):
                self.nodes[i].color = (218, 112, 214)
                self.nodes[i].index = self.start
                self.nodes[i].repaint()
            else:
                self.nodes[i].color = (0,255,0)
                self.nodes[i].index = self.char[i] 
                self.nodes[i].repaint()
        self.lcd1.display(0)
        self.flag = False
        self.repaint()
        self.mapFrame.setParent(self)
        self.mapFrame.show()
        
            
        
        
    # Function to intialize the window 
    def initWin(self):
        iptGrid = QGridLayout()
        title = Text("TSP",(255,0,0),16,"center")
        pic = QPixmap("C:\\tsp.png");
        picLbl = QLabel(); picLbl.setPixmap(pic); picLbl.setScaledContents(True)
        titleLayout = QVBoxLayout()
        titleLayout.addWidget(title); titleLayout.addWidget(picLbl);
        titleFrame = QFrame()
        titleFrame.setFrameShape(QFrame.StyledPanel)
        titleFrame.setAutoFillBackground(True)
        p5 = titleFrame.palette()
        p5.setColor(titleFrame.backgroundRole(), QColor(255,255,255))
        titleFrame.setPalette(p5)
        titleFrame.setLayout(titleLayout)
        iptTitle = Text("Program Input",(255,0,0),12,"center")
        iptTxt1 = QLabel("Cities No:") ; iptTxt1.setFont(QFont("Decorative" , 12))
        iptTxt2 = QLabel("start:") ; iptTxt2.setFont(QFont("Decorative" , 12))
        self.iptEdt1 = QLineEdit() ; self.iptEdt1.textChanged[str].connect(self.get_input)
        self.iptEdt2 = QLineEdit() ; self.iptEdt2.textChanged[str].connect(self.get_input)
        self.iptBtn1 = QPushButton("Build") ; self.iptBtn1.clicked.connect(self.bulid_map);
        self.iptBtn2 = QPushButton("Rturn") ; self.iptBtn2.clicked.connect(self.get_initial);
        iptH = QHBoxLayout()
        iptH.addWidget(self.iptBtn1) ; iptH.addWidget(self.iptBtn2)
        iptGrid.addWidget(iptTitle,1,0,1,5)
        iptGrid.addWidget(iptTxt1,2,0)
        iptGrid.addWidget(self.iptEdt1,2,1)
        iptGrid.addWidget(iptTxt2,3,0)
        iptGrid.addWidget(self.iptEdt2,3,1)
        iptGrid.setVerticalSpacing(10)
        iptV = QVBoxLayout()
        iptV.addLayout(iptGrid) ; iptV.addLayout(iptH);
        iptFrame = QFrame()
        iptFrame.setAutoFillBackground(True)
        p6 = iptFrame.palette()
        p6.setColor(iptFrame.backgroundRole(), QColor(220,225,255))
        iptFrame.setPalette(p6)
        iptFrame.setFrameShape(QFrame.StyledPanel)
        iptFrame.setLayout(iptV)
        srgGrid = QGridLayout()
        #srgGrid.setVerticalSpacing(10)
        srgTitle = Text("Algorithms",(255,0,0),12,"center")
        self.srgBtn1 = QPushButton("Genetic") ; self.srgBtn1.clicked.connect(self.run_algorithm)
        self.srgBtn2 = QPushButton("Simulated") ; self.srgBtn2.clicked.connect(self.run_algorithm)
        self.srgBtn3 = QPushButton("Tabu") ; self.srgBtn3.clicked.connect(self.run_algorithm)
        self.srgBtn4 = QPushButton("reset") ; self.srgBtn4.clicked.connect(self.reset)
        srgGrid.addWidget(srgTitle,1,0,1,6)
        srgGrid.addWidget(self.srgBtn1,2,1,2,4)
        srgGrid.addWidget(self.srgBtn2,3,1,3,4)
        srgGrid.addWidget(self.srgBtn3,4,1,4,4)
        srgGrid.addWidget(self.srgBtn4,5,1,5,4)
        srgFrame = QFrame()
        srgFrame.setFrameShape(QFrame.StyledPanel)
        srgFrame.setAutoFillBackground(True)
        p7 = srgFrame.palette()
        p7.setColor(srgFrame.backgroundRole(), QColor(255,255,255))
        srgFrame.setPalette(p7)
        srgFrame.setLayout(srgGrid)
        otpGrid = QGridLayout()
        otpTitle = Text("Program Output",(255,0,0),12,"center")
        otpTxt1 = QLabel("The Cost"); otpTxt1.setFont(QFont("Decorative" , 12))
        self.lcd1 = QLCDNumber() 
        otpGrid.addWidget(otpTitle,1,0,1,2)
        otpGrid.addWidget(otpTxt1,2,0) 
        otpGrid.addWidget(self.lcd1,2,1)
        otpFrame = QFrame()
        otpFrame.setFrameShape(QFrame.StyledPanel)
        otpFrame.setAutoFillBackground(True)
        p8 = otpFrame.palette()
        p8.setColor(otpFrame.backgroundRole(), QColor(220,225,255))
        otpFrame.setPalette(p8)
        otpFrame.setLayout(otpGrid)
        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(titleFrame); splitter1.addWidget(iptFrame);
        splitter1.setSizes([240,135])
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(srgFrame) ;  splitter2.addWidget(otpFrame)
        splitter2.setSizes([200,92])
        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1) ;  splitter3.addWidget(splitter2)
        splitter3.setSizes([382,291])
        splitter3.resize(260,685) ; splitter3.move(1100,5)
        splitter3.setParent(self)
        splitter3.setAutoFillBackground(True)
        p3 = splitter3.palette()
        p3.setColor(splitter3.backgroundRole(), QColor(255, 255, 255))
        splitter3.setPalette(p3)
        self.mapFrame = QFrame() ;   self.mapFrame.setFrameShape(QFrame.StyledPanel)
        self.mapFrame.move(5,5) ; self.mapFrame.resize(1090,685)
        self.mapFrame.setParent(self)
        self.setAutoFillBackground(True)
        p2 = self.palette()
        p2.setColor(self.backgroundRole(), QColor(0, 0, 0))
        self.setPalette(p2)
        self.mapFrame.setParent(self)
        self.hint = Text("Click the bulid button to bulid a random map",(255,0,0),23,"center")
        self.hint.move(230,100)
        self.hint.setParent(self)
        self.setWindowTitle("TSP")
        self.width = QDesktopWidget().availableGeometry().width()
        self.height = QDesktopWidget().availableGeometry().height() - 40
        self.resize(self.width,self.height)
        self.show()
        self.nodes = {}
        self.points = {}
        self.flag = True
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.animation(qp)
        qp.end()
        
    def animation(self,qp):
        if(self.flag):
            pen = QPen(QColor(255,255,255), 2, Qt.DotLine)
            qp.setPen(pen)
            for i in range(len(self.result) - 1) :
                x1 = self.nodes[self.result[i]].x + 15
                y1 = self.nodes[self.result[i]].y + 15
                x2 = self.nodes[self.result[i + 1]].x + 15
                y2 = self.nodes[self.result[i + 1]].y + 15
                qp.drawLine(x1,y1,x2,y2)
                
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_D:
            self.mapFrame.setParent(None)
            self.repaint()
            self.flag = not self.flag
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
        
        
        