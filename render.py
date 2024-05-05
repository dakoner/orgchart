# -*- coding: utf-8 -*-

# from PySide2 import QtCore  # type: ignore
# from PySide2 import QtGui  # type: ignore
# from PySide2 import QtWidgets  # type: ignore
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtSvgWidgets

from PyQt6.uic import loadUi
import signal
import sys

    

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi("render.ui", self)

        self.graphics_view = self.findChild(QtWidgets.QGraphicsView, "graphicsView")
        self.scene = QtWidgets.QGraphicsScene(self)
        self.item = QtSvgWidgets.QGraphicsSvgItem("orgchart.svg")
        self.scene.addItem(self.item)

        
        self.graphics_view.setScene(self.scene)
        #self.graphics_view.fitInView(self.scene.sceneRect(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        #self.graphics_view.centerOn(self.item)
        #self.graphics_view.scale(4, 4)


class QApplication(QtWidgets.QApplication):
    def __init__(self, *argv):
        super().__init__(*argv)

        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)    
    app.exec()
