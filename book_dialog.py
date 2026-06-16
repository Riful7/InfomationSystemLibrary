from datetime import date

from PySide6.QtWidgets import QDialog
from uis.bookDialogForm import Ui_BookDialog

from database import insertBook, updateBook


class BookDialog(QDialog):
    '''Класс формы для добавления/изменения записей книг в БД'''

    def __init__(self, record: tuple = None):
        super(BookDialog, self).__init__()
        self.ui = None
        self.record: tuple = record
        self.load_ui()

        if self.ui:
            self.ui.sboxYearRelease.setMaximum(date.today().year)
            self.ui.buttonBox.accepted.connect(self.onAcceptClick)
            if self.record:
                self.ui.leName.setText(self.record[1])
                self.ui.sboxYearRelease.setValue(self.record[2])
                self.ui.teDescription.setText(self.record[3])
                self.ui.leAuthor.setText(self.record[4])
                self.ui.lePublisher.setText(self.record[5])

    def load_ui(self):
        '''Загрузка интерфейса формы добавления/изменения записей книг в БД'''
        self.ui = Ui_BookDialog()
        self.ui.setupUi(self)

    def onAcceptClick(self):
        '''Подтверждение введенных данных для добавления/изменения записей книг в БД'''
        if not self.record:
            data = {"name": self.ui.leName.text(),
                    "year_release": self.ui.sboxYearRelease.value(),
                    "description": self.ui.teDescription.toPlainText(),
                    "author": self.ui.leAuthor.text(),
                    "publisher": self.ui.lePublisher.text()}
            insertBook(data)
            return

        new_record = {"name": self.ui.leName.text(),
                      "year_release": self.ui.sboxYearRelease.value(),
                      "description": self.ui.teDescription.toPlainText(),
                      "author": self.ui.leAuthor.text(),
                      "publisher": self.ui.lePublisher.text(),
                      "id": self.record[0]}
        updateBook(new_record)
