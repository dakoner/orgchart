from PyQt6 import QtWidgets
from PyQt6 import QtCore


class GraphicsView(QtWidgets.QGraphicsView):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.setSceneRect(-100, -100, 200, 200)
        #self.fitInView(-100, -100, 200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        #self.setMouseTracking(True)
        #self.setCacheMode(QtWidgets.QGraphicsView.CacheNone)
        #self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)

        
    def keyPressEvent(self, event):
        print("keyPress", event)
        key = event.key()
        print(key)
        if key == QtCore.Qt.Key.Key_Down:
            self.scale(0.5,0.5)
        elif key == QtCore.Qt.Key.Key_Up:
            self.scale(2,2)
