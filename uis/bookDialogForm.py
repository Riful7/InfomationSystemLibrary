# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookDialogForm.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_BookDialog(object):
    def setupUi(self, BookDialog):
        if not BookDialog.objectName():
            BookDialog.setObjectName(u"BookDialog")
        BookDialog.resize(540, 512)
        self.verticalLayout_2 = QVBoxLayout(BookDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(BookDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.leName = QLineEdit(BookDialog)
        self.leName.setObjectName(u"leName")

        self.verticalLayout.addWidget(self.leName)

        self.label_3 = QLabel(BookDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)

        self.leAuthor = QLineEdit(BookDialog)
        self.leAuthor.setObjectName(u"leAuthor")

        self.verticalLayout.addWidget(self.leAuthor)

        self.label_2 = QLabel(BookDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.sboxYearRelease = QSpinBox(BookDialog)
        self.sboxYearRelease.setObjectName(u"sboxYearRelease")
        self.sboxYearRelease.setMaximum(20000)

        self.verticalLayout.addWidget(self.sboxYearRelease)

        self.label_5 = QLabel(BookDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.lePublisher = QLineEdit(BookDialog)
        self.lePublisher.setObjectName(u"lePublisher")

        self.verticalLayout.addWidget(self.lePublisher)

        self.label_4 = QLabel(BookDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.teDescription = QTextEdit(BookDialog)
        self.teDescription.setObjectName(u"teDescription")

        self.verticalLayout.addWidget(self.teDescription)

        self.buttonBox = QDialogButtonBox(BookDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(BookDialog)
        self.buttonBox.accepted.connect(BookDialog.accept)
        self.buttonBox.rejected.connect(BookDialog.reject)

        QMetaObject.connectSlotsByName(BookDialog)
    # setupUi

    def retranslateUi(self, BookDialog):
        BookDialog.setWindowTitle(QCoreApplication.translate("BookDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("BookDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("BookDialog", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.label_2.setText(QCoreApplication.translate("BookDialog", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("BookDialog", u"\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("BookDialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

