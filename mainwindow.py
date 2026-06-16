from PySide6.QtWidgets import QMainWindow, QPushButton, QDialog, QHeaderView, QFileDialog, QMessageBox
from PySide6.QtGui import QAction
from PySide6.QtCore import QModelIndex, Qt, QDir
import pandas as pd

import database
from uis.mainWindowForm import Ui_MainWindow
from book_dialog import BookDialog
from database import DBConnectionDialog
from book_model import BookModel


class MainWindow(QMainWindow):
    '''Класс главного окна'''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui: Ui_MainWindow = None
        self.bookModel: BookModel = None

        self.load_ui()
        if self.ui:
            self.setWindowTitle("Библиотека")

            btnAddBook: QPushButton = self.ui.btnAddBook
            btnAddBook.clicked.connect(self.onAddBook)

            self.ui.actConDB.triggered.connect(self.onActConDB)
            self.ui.actImportXLSX.triggered.connect(self.onActImportXLSX)

            self.actDeleteBook = QAction("Удалить")
            self.actDeleteBook.triggered.connect(self.onActDeleteBookClick)

            self.actUpdateViewBook = QAction("Обновить")
            self.actUpdateViewBook.triggered.connect(self.loadBookView)

            self.ui.mainViewBook.doubleClicked.connect(self.onDoubleClickViewBook)
            self.ui.mainViewBook.addAction(self.actDeleteBook)
            self.ui.mainViewBook.addAction(self.actUpdateViewBook)
            self.ui.mainViewBook.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
            self.ui.mainViewBook.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.ui.mainViewBook.setSortingEnabled(True)

            self.loadBookView()

    def load_ui(self):
        '''Загрузка интерфейса главного окна'''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def onAddBook(self):
        '''Вызов формы для добавления книги в БД'''
        bookDialog: QDialog = BookDialog()
        bookDialog.setWindowTitle("Добавить книгу")
        dialogRes: int = bookDialog.exec()
        if dialogRes == 1:
            self.loadBookView()

    def onActConDB(self):
        '''Вызов формы для настройки подключения к БД'''
        connectionDialog: QDialog = DBConnectionDialog()
        connectionDialog.setWindowTitle("Подключение к БД")
        connectionDialog.exec()

    def loadBookView(self):
        '''Загрузка записей в таблицу главного окна'''
        records = database.selectBook()
        if not records:
            self.actDeleteBook.setDisabled(True)
        self.actDeleteBook.setDisabled(False)
        self.bookModel = BookModel(records)
        self.ui.mainViewBook.setModel(self.bookModel)

    def onDoubleClickViewBook(self, index: QModelIndex):
        '''Вызов формы для изменения книги в БД двойным нажатием мыши по записи в таблице'''
        record = self.bookModel.getRecordByRow(index.row())
        bookDialog: QDialog = BookDialog(record)
        bookDialog.setWindowTitle("Обновить книгу")
        dialogRes: int = bookDialog.exec()
        if dialogRes == 1:
            self.loadBookView()

    def onActDeleteBookClick(self):
        '''Удаление записей книг из БД'''
        indexes: set[int] = set(ind.row() for ind in self.ui.mainViewBook.selectedIndexes() if ind.isValid())
        for index in indexes:
            record = self.bookModel.getRecordByRow(index)
            del_record = {"id": record[0]}
            database.deleteBook(del_record)
        self.loadBookView()

    def onActImportXLSX(self):
        '''Импорт данных из файла XLSX'''
        filePath: str = QFileDialog.getOpenFileName(None, "Выберите файл XLSX", QDir.currentPath(), "*.xlsx")[0]
        if filePath:
            df = pd.read_excel(filePath)
            if len(df.columns) != 5:
                msgIcon = QMessageBox.Icon.Warning
                msgText = "Неверное количество параметров. Проверьте файл"
                msg: QMessageBox = QMessageBox(msgIcon, "Импорт XLSX", msgText, QMessageBox.StandardButton.Ok)
                msg.exec()
                return

            records = df.to_dict(orient='records')
            corruptedRecords = 0
            for record in records:
                res = database.insertBook(record)
                if res:
                    corruptedRecords += 1
            if corruptedRecords:
                msgIcon = QMessageBox.Icon.Warning
                msgText = "Не удалось добавить {0} записей. Проверьте данные файла".format(corruptedRecords)
                msg: QMessageBox = QMessageBox(msgIcon, "Импорт XLSX", msgText, QMessageBox.StandardButton.Ok)
                msg.exec()
            self.loadBookView()
