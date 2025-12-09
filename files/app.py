import main
import speak
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui        import QIcon, QPixmap, QResizeEvent, QFont, QColor
from PyQt5.QtWidgets    import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, 
                              QLineEdit, QSizePolicy , QScrollArea,QGroupBox, QLabel, QLayout, QAction, QFrame)

from PyQt5.QtCore       import Qt, QObject, QThread, pyqtSignal, pyqtSlot, QSize


global soundManager
class soundManagerClass(QObject):
    #wrapper for speak.py
    ttsActive = pyqtSignal(bool)

    @pyqtSlot(str)
    def speak(self,words):
        if(len(words) > 0):
            self.ttsActive.emit(True)
            speak.speak(words)
            self.ttsActive.emit(False)
soundManager = soundManagerClass()




class designSettingsClass():

    def resetToDefault(self):
        self.window_name = "TSA PHS 2025-26 software dev"
        self.program_name = "audio-visual disablity helper"
        self.window_start_size = [600,600]
        

        self.program_title_spacing = 0
        self.main_font = QFont("Helvetica",27)

        self.appBorder = 10

        self.backgroundColor = "#d6ffe1"


    def __init__(self):

        self.resetToDefault()
        app.setFont(self.main_font)

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

        #region NO TOUCHING
        self.main_layout_wrapper= QGroupBox()
        self.main_layout = QVBoxLayout()
        self.main_layout_wrapper.setLayout(self.main_layout)

        self.buttonSizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.sectionBoxPolicy = QSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        #endregion

        #region title
        self.titleBox = QVBoxLayout()
        self.program_title_widget = QLabel(current_settings.program_name)
        self.program_title_widget.setContentsMargins(0,current_settings.program_title_spacing,0,current_settings.program_title_spacing)
        self.program_title_widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Minimum))

        self.titleBox.addWidget(self.program_title_widget,0,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.titleBox.setContentsMargins(0,0,0,0)
        # self.program_title_widget.setFixedHeight(self.program_title_widget.minimumSizeHint().height())

        #endregion
        
        #region help

        self.helpBox = QHBoxLayout()
        
        self.helpButton = QPushButton()
        self.helpHeader = QLabel("<= help button")
        self.helpButton.setMinimumSize(100,100)
        self.helpButton.setSizePolicy(self.buttonSizePolicy)


        self.helpButtonIcon = QIcon("assets\\img\\helpButton.jpg")
        self.helpButton.setIcon(self.helpButtonIcon)
        self.helpButton.setIconSize(QSize(100,100))
        self.helpBox.setContentsMargins(0,0,0,0)

        self.helpBox.addWidget(self.helpButton)
        self.helpBox.addWidget(self.helpHeader)
        
        #endregion

        #region listener

        self.listenBox = QHBoxLayout()

        self.listenHeader = QLabel("listener")
        self.listenLineEdit = QLineEdit()
        self.listenButtonMic = QPushButton()
        self.listenButtonMic.setSizePolicy(self.buttonSizePolicy)
        self.listenButtonFile = QPushButton()
        self.listenButtonFile.setSizePolicy(self.buttonSizePolicy)

        self.listenButtonMic.setMinimumSize(100,100)
        self.listenButtonFile.setMinimumSize(100,100)

        self.listenButtonMicIcon = QIcon("assets\\img\\listenerButton.jpg")
        self.listenButtonFileIcon = QIcon("assets\\img\\listenerButton.jpg")

        self.listenButtonMic.setIcon(self.listenButtonMicIcon)
        self.listenButtonMic.setIconSize(QSize(100,100))
        self.listenButtonFile.setIcon(self.listenButtonFileIcon)
        self.listenButtonFile.setIconSize(QSize(100,100))


        self.listenTextLayout = QVBoxLayout()
        self.listenTextLayout.addWidget(self.listenHeader,alignment=Qt.AlignmentFlag.AlignBottom)
        self.listenTextLayout.addWidget(self.listenLineEdit,alignment=Qt.AlignmentFlag.AlignTop)
        self.listenTextLayout.setContentsMargins(0,0,0,0)

        self.listenBox.setContentsMargins(0,0,0,0)
        self.listenBox.addWidget(self.listenButtonMic,alignment=Qt.AlignmentFlag.AlignVCenter)
        self.listenBox.addWidget(self.listenButtonFile,alignment=Qt.AlignmentFlag.AlignVCenter)
        self.listenBox.addLayout(self.listenTextLayout)

        #endregion

        #region reader
        self.readBox = QHBoxLayout()

        self.readLineEdit = QLineEdit()
        self.readButton = QPushButton()
        self.readHeader = QLabel("Reader")
        self.readLineEdit.returnPressed.connect(lambda: self.tts(self.readLineEdit.text()))
        self.readButton.pressed.connect(lambda: self.tts(self.readLineEdit.text()))
        self.setSizePolicy(self.buttonSizePolicy)

        self.readButton.setMinimumSize(100,100)
        self.readButtonIcon = QIcon("assets\\img\\readButton.jpg")
        self.readButton.setIcon(self.readButtonIcon)
        self.readButton.setIconSize(QSize(100,100))

        self.readTextLayout = QVBoxLayout()
        self.readTextLayout.addWidget(self.readHeader, alignment= Qt.AlignmentFlag.AlignBottom)
        self.readTextLayout.addWidget(self.readLineEdit, alignment= Qt.AlignmentFlag.AlignTop)
        self.readTextLayout.setContentsMargins(0,0,0,0)

        self.readBox.addWidget(self.readButton, alignment= Qt.AlignmentFlag.AlignVCenter)
        self.readBox.addLayout(self.readTextLayout)
        self.readBox.setContentsMargins(0,0,0,0)

        #endregion

        #region main layout
        self.titleFrame = QFrame()
        self.titleFrame.setLayout(self.titleBox)
        self.titleFrame.setStyleSheet("margin-bottom: 0px")

        self.helpFrame = QFrame()
        self.helpFrame.setLayout(self.helpBox)

        self.listenFrame = QFrame()
        self.listenFrame.setLayout(self.listenBox)

        self.readFrame = QFrame()
        self.readFrame.setLayout(self.readBox)

        self.main_layout.setContentsMargins(current_settings.appBorder,current_settings.appBorder,current_settings.appBorder,current_settings.appBorder)
        self.main_layout.setSpacing(0)
        app.setStyleSheet(f"background-color: {current_settings.backgroundColor};")

        self.main_layout.addWidget(self.titleFrame ,stretch=0)
        self.main_layout.addWidget(self.helpFrame  ,stretch=999)
        self.main_layout.addWidget(self.listenFrame,stretch=999)
        self.main_layout.addWidget(self.readFrame  ,stretch=999)

        #endregion
        


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
