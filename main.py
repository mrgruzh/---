import sys
import os

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, \
    QComboBox, QScrollArea, QPushButton, QVBoxLayout, QAction, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt

from src.tree import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.maximizingPlayer = True
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()

        extractAction = QAction("&Открыть", self)
        extractAction.triggered.connect(self.showDialog)
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(extractAction)

        extractAction = QAction("&Минимакс", self)
        extractAction.triggered.connect(lambda: self.minimax())
        fileMenu = menubar.addMenu('&Алгоритмы')
        fileMenu.addAction(extractAction)

        extractAction = QAction("&Альфа-бета отсечение", self)
        extractAction.triggered.connect(lambda: self.alphaBeta())
        fileMenu.addAction(extractAction)

        self.lbl = QLabel("Первый ход", self)
        combo = QComboBox(self)
        combo.addItems(["MAX", "MIN"])
        combo.move(100, 20)
        self.lbl.move(10, 20)
        combo.activated[str].connect(self.onActivated)

        minimaxButton = QPushButton("Минимакс", self)
        minimaxButton.clicked.connect(lambda: self.minimax())
        minimaxButton.move(10, 60)

        alphaBetaButton = QPushButton("Альфа-бета отсечение", self)
        alphaBetaButton.clicked.connect(lambda: self.alphaBeta())
        alphaBetaButton.move(10, 90)

        self.setGeometry(300, 300, 1366, 720)
        self.setWindowTitle('Редактор деревьев')
        self.show()

    def showDialog(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file',
                                               os.getcwd(), "Python files (*.py)")[0]
        if fileName:
            exec(open(fileName).read(), globals())
            tree.calculateNodesPostion()

    def minimax(self):
        if tree.root:
            tree.minimaxMoves = {}
            tree.minimax(tree.root, tree.depth(tree.root), self.maximizingPlayer)
        self.update()

    def alphaBeta(self):
        if tree.root:
            tree.alphaBetaMoves = {}
            tree.alphaBeta(tree.root, tree.depth(tree.root), maximizingPlayer=self.maximizingPlayer)
        self.update()

    def onActivated(self, text):
        tree.minimaxMoves = None
        tree.alphaBetaMoves = None
        self.maximizingPlayer = (text == 'MAX')
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        self.drawMinimaxMoves(qp)
        self.drawAlphaBetaMoves(qp)
        self.drawTree(qp)

        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Decorative', 12))
        qp.end()

    def drawMinimaxMoves(self, qp):
        pen = QPen(Qt.red, 2, Qt.DashLine)
        qp.setPen(pen)
        if tree.minimaxMoves:
            nodeFrom = tree.root
            while tree.minimaxMoves.get(nodeFrom):
                nodeTo = tree.minimaxMoves[nodeFrom]
                qp.drawLine(nodeFrom.position['x'] + 10, nodeFrom.position['y'] + 5,
                            nodeTo.position['x'] + 10, nodeTo.position['y'] + 5)
                if nodeTo.isLeaf():
                    break
                nodeFrom = nodeTo

    def drawAlphaBetaMoves(self, qp):
        pen = QPen(Qt.blue, 2, Qt.DashLine)
        qp.setPen(pen)
        if tree.alphaBetaMoves:
            nodeFrom = tree.root
            while tree.alphaBetaMoves.get(nodeFrom):
                nodeTo = tree.alphaBetaMoves[nodeFrom]
                qp.drawLine(nodeFrom.position['x'] - 10, nodeFrom.position['y'] - 5,
                            nodeTo.position['x'] - 10, nodeTo.position['y'] - 5)
                if nodeTo.isLeaf():
                    break
                nodeFrom = nodeTo

    def drawTree(self, qp):
        if tree.root:
            qp.setPen(QColor(0, 0, 0))
            qp.setBrush(QColor(0, 0, 0))
            tree.drawMoveLines(qp, self.maximizingPlayer)
            tree.drawNodes(qp)
            qp.setPen(QColor(255, 255, 255))
            tree.drawNodesValues(qp)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
