import main
import speak
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui        import QIcon, QPixmap, QResizeEvent
from PyQt5.QtWidgets    import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, 
                              QLineEdit, QSizePolicy , QScrollArea,QGroupBox, QLabel, QLayout, QAction)

from PyQt5.QtCore       import Qt, QObject, QThread, pyqtSignal, pyqtSlot, QSize


global soundManager
class soundManagerClass(QObject):
    #wrapper for speak.py
    ttsActive = pyqtSignal(bool)

    @pyqtSlot(str)
    def speak(self,words):
        self.ttsActive.emit(True)
        speak.speak(words)
        self.ttsActive.emit(False)
soundManager = soundManagerClass()




class designSettingsClass():

    def resetToDefault(self):
        self.window_name = "TSA PHS 2025-26 software dev"
        self.program_name = "temp name"
        self.window_start_size = [400,300]

    def __init__(self):

        self.resetToDefault()

class mainWindowClass(QMainWindow):
    ttsRequest = pyqtSignal(str)

    def tts(self,words : str):
        self.ttsRequest.emit(words)

    def __init__(self):
        super().__init__()

        #region setup
        self.setWindowTitle(current_settings.window_name)

        #center the window when first booting up the program
        windowX = app.desktop().size().width() // 2 - current_settings.window_start_size[0] // 2
        windowY = app.desktop().size().height() // 2 - current_settings.window_start_size[1] // 2
        self.setGeometry(windowX,windowY, current_settings.window_start_size[0], current_settings.window_start_size[1])  # (x, y, width, height)
        self.setMinimumSize(current_settings.window_start_size[0],current_settings.window_start_size[1])

        #endregion


        #region ui

        #region NO FUCKING TOUCHING
        self.main_layout_wrapper= QGroupBox()
        self.main_layout = QVBoxLayout()
        self.main_layout_wrapper.setLayout(self.main_layout)
        #endregion

        self.program_title_widget = QLabel()
        self.program_title_widget.setText(current_settings.program_name)
        self.program_title_widget.textFormat()
        self.program_title_widget.setContentsMargins(0,1,0,1)
        self.main_layout.addWidget(self.program_title_widget,alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop )
        


        self.readbox = QHBoxLayout()

        self.readLineEdit = QLineEdit()
        self.readButton = QPushButton()
        self.readLineEdit.returnPressed.connect(lambda: self.tts(self.readLineEdit.text()))
        self.readButton.pressed.connect(lambda: self.tts(self.readLineEdit.text()))

        self.readButton.setMinimumSize(100,100)

        self.readButtonIcon = QIcon("assets\\img\\readButton.jpg")
        
        self.readButton.setIcon(self.readButtonIcon)
        self.readButton.setIconSize(QSize(100,100))

        self.readbox.addWidget(self.readButton)
        self.readbox.addWidget(self.readLineEdit)


        
        self.main_layout.addLayout(self.readbox)





        #endregion

        #region threading

        self.soundThread = QThread()
        soundManager.moveToThread(self.soundThread)

        self.ttsRequest.connect(soundManager.speak)

        self.soundThread.start()
        #endregion

        self.setCentralWidget(self.main_layout_wrapper)
        # self.setLayout(self.main_layout)
        self.show()



def startApp():
    global app, current_settings, main_window
    app = QtWidgets.QApplication(sys.argv)

    # Create a QMainWindow (main window)
    current_settings = designSettingsClass()
    main_window = mainWindowClass()
    
    # speak.speak("testing testing testing")

    # Show the window
    sys.exit(app.exec_())
