from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont , QPainter , QColor 
from PyQt5.QtCore import Qt 
class Cell(QWidget):
    x = 0
    y = 0
    index = 0
    def __init__(self,index,x,y,color,parent = None):
        super().__init__()
        self.index = index
        self.x = x
        self.y = y
        self.move(self.x , self.y)
        self.resize(30,30)
        self.setParent(parent)
        self.color = color
        
        
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp,event)
        qp.end()
        
    def drawWidget(self,qp,event):
        size = self.size()
        col = QColor(self.color[0],self.color[1],self.color[2])
        qp.setPen(col)
        qp.setBrush(col)
        qp.drawRect(0,0,size.width(),size.height())
        fon = QFont('Decorative', 13)
        qp.setFont(fon)
        qp.setPen(QColor(0,0,0))
        qp.drawText(event.rect(), Qt.AlignCenter, self.index)

