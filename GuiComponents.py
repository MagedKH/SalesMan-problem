from PyQt5.QtGui import QFont , QPainter , QColor 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

class Cell(QWidget):
    def __init__(self,index,color):
        super().__init__()
        self.index = index
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
        qp.setPen(QColor(255,255,255))
        qp.drawText(event.rect(), Qt.AlignCenter, self.index)
        
        
        
class Text(QWidget):
    def __init__(self,text,color,size,allign):
        super().__init__()
        self.text = text
        self.color = color
        self.size = size
        self.allign = allign
        
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp,event)
        qp.end()
        
    def drawWidget(self,qp,event):
        col = QColor(self.color[0],self.color[1],self.color[2])
        qp.setPen(col)
        fon = QFont('Decorative',self.size)
        qp.setFont(fon)
        if (self.allign == "center"):
            qp.drawText(event.rect(), Qt.AlignCenter, self.text)
        elif (self.allign == "bottom"):
            qp.drawText(event.rect(), Qt.AlignBottom, self.text)
        elif (self.allign == "top"):
            qp.drawText(event.rect(), Qt.AlignTop, self.text)

