from typing import Any, Dict, List
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QWidget,
)


class Initializer:
    def __init__(self) -> None:
        self.instances: Dict[str, object] = {}

    def register(self, instance_name: str, instance: object) -> None:
        self.instances[instance_name] = instance

    def get_instance(self, instance_name: str) -> object:
        return self.instances.get(instance_name)


################################################################################

INIT: Initializer = Initializer()

####################################################################################


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manga MetaData")
        self.resize(1052, 539)

        self.Main_Container = Main_Container(INIT)

        self.setupUI()
        self.show()

    def setupUI(self):
        if not self.objectName():
            self.setObjectName("Manga_Metadata")
        self.setCentralWidget(self.Main_Container)

class Main_Container(QWidget):
    def __init__(self, init: Initializer) -> None:
        super().__init__()  
        self.init = init
        self.init.register("Main_Container", self)
        
        self.Search_Panel = Search_Panel(INIT)
        self.setup()

    def setup(self) -> None:
        self.setObjectName("Main_Window")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.Search_Panel, 0, 0, 1, 1)

class Search_Panel(QFrame):
    def __init__(self, init: Initializer) -> None:
        super().__init__()  
        self.init = init
        self.init.register("Search_Panel", self)
        
        self.search_bar = Search_Bar(INIT)
        self.welcome_header = Welcome_Home_Label(INIT)

        self.setup()

    def setup(self) -> None:
        self.setObjectName(u"SearchPanel")
        self.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Down_Home_Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_2.addItem(self.Down_Home_Spacer, 4, 1, 1, 1)

        self.Up_Home_Sapcer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_2.addItem(self.Up_Home_Sapcer, 0, 1, 1, 1)

        self.Left_Home_Spacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.Left_Home_Spacer, 1, 0, 1, 1)

        self.Right_Home_Spacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.Right_Home_Spacer, 1, 2, 1, 1)

        self.gridLayout_2.addWidget(self.search_bar, 2, 1, 1, 1)

        self.gridLayout_2.addWidget(self.welcome_header, 1, 1, 1, 1)



class Search_Bar(QLineEdit):
    def __init__(self, init: Initializer) -> None:
        super().__init__() 
        self.init = init
        self.init.register("Search_Bar", self)
        self.setup()

    def setup(self) -> None:
        self.setObjectName(u"SearchBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)
        self.setMinimumSize(QSize(400, 50))
        self.setPlaceholderText("Search For Manga...")

class Welcome_Home_Label(QLabel):
    def __init__(self, init: Initializer) -> None:
        super().__init__()  
        self.init = init
        self.init.register("Welcome_Home_Label", self)

        self.setup()
        self.signals()
    def setup(self) -> None:
        self.setObjectName(u"Welcome_Header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)
        self.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"FreeSerif"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        self.setFont(font)
        self.setAlignment(Qt.AlignCenter)
        self.setText("Welcome To Manga Library")

    def signals(self) -> None:
        self.returnPressed()
