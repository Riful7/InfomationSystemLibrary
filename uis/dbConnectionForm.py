# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbConnectionForm.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        if not ConnectionDialog.objectName():
            ConnectionDialog.setObjectName(u"ConnectionDialog")
        ConnectionDialog.resize(534, 318)
        self.verticalLayout_2 = QVBoxLayout(ConnectionDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(ConnectionDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.leHost = QLineEdit(ConnectionDialog)
        self.leHost.setObjectName(u"leHost")

        self.verticalLayout.addWidget(self.leHost)

        self.label_2 = QLabel(ConnectionDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.lePort = QLineEdit(ConnectionDialog)
        self.lePort.setObjectName(u"lePort")

        self.verticalLayout.addWidget(self.lePort)

        self.label_3 = QLabel(ConnectionDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)

        self.leUser = QLineEdit(ConnectionDialog)
        self.leUser.setObjectName(u"leUser")

        self.verticalLayout.addWidget(self.leUser)

        self.label_4 = QLabel(ConnectionDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.lePass = QLineEdit(ConnectionDialog)
        self.lePass.setObjectName(u"lePass")
        self.lePass.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lePass)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAccept = QPushButton(ConnectionDialog)
        self.btnAccept.setObjectName(u"btnAccept")

        self.horizontalLayout.addWidget(self.btnAccept)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ConnectionDialog)

        QMetaObject.connectSlotsByName(ConnectionDialog)
    # setupUi

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(QCoreApplication.translate("ConnectionDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ConnectionDialog", u"\u0425\u043e\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("ConnectionDialog", u"\u041f\u043e\u0440\u0442", None))
        self.lePort.setInputMask(QCoreApplication.translate("ConnectionDialog", u"00000", None))
        self.label_3.setText(QCoreApplication.translate("ConnectionDialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_4.setText(QCoreApplication.translate("ConnectionDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btnAccept.setText(QCoreApplication.translate("ConnectionDialog", u"OK", None))
    # retranslateUi

