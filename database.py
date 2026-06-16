from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from uis.dbConnectionForm import Ui_ConnectionDialog


class DBConnectionDialog(QDialog):
    '''Класс формы для настройки подключения к БД'''

    def __init__(self):
        super(DBConnectionDialog, self).__init__()
        self.ui: Ui_ConnectionDialog = None
        self.load_ui()

        if self.ui:
            dbConf: QSettings = QSettings("Mtuci", "Library")
            dbConf.beginGroup("Connection")
            self.ui.leHost.setText(dbConf.value("Host"))
            self.ui.lePort.setText(dbConf.value("Port"))
            self.ui.leUser.setText(dbConf.value("User"))
            self.ui.lePass.setText(dbConf.value("Pass"))
            dbConf.endGroup()

            self.ui.btnAccept.clicked.connect(self.onAcceptClick)

    def load_ui(self):
        '''Загрузка интерфейса окна настройки покдлючения к БД'''
        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)

    def onAcceptClick(self):
        '''Подтверждение введенных параметров для подключения к БД'''
        msgIcon = QMessageBox.Warning
        msgText = "Ошибка подключения: {0}".format("Неккоректные параметры подключения")
        if self.ui.lePort.text() == "":
            msg: QMessageBox = QMessageBox(msgIcon, "Подключение к БД", msgText, QMessageBox.Ok)
            msg.exec()
            return

        db = tryConnect(self.ui.leHost.text(),
                        int(self.ui.lePort.text()),
                        self.ui.leUser.text(),
                        self.ui.lePass.text())

        if db.open():
            msgIcon = QMessageBox.Information
            msgText = "Подключение выполнено"

            db.close()
            dbConf: QSettings = QSettings("Mtuci", "Library")
            dbConf.beginGroup("Connection")
            dbConf.setValue("Host", self.ui.leHost.text())
            dbConf.setValue("Port", self.ui.lePort.text())
            dbConf.setValue("User", self.ui.leUser.text())
            dbConf.setValue("Pass", self.ui.lePass.text())
            dbConf.endGroup()

            self.close()
        else:
            msgText = "Ошибка подключения: {0}".format(db.lastError().driverText())

        msg: QMessageBox = QMessageBox(msgIcon, "Подключение к БД", msgText, QMessageBox.Ok)
        msg.exec()


def tryConnect(host: str, port: int, user: str, password: str) -> QSqlDatabase:
    '''Подключение к БД'''
    db: QSqlDatabase = QSqlDatabase.addDatabase("QPSQL")

    db.setHostName(host)
    db.setDatabaseName("InfoSysLibrary")
    db.setUserName(user)
    db.setPassword(password)
    db.setPort(port)

    return db


def insertBook(data: dict):
    '''Добавление записи книги в БД'''
    dbConf: QSettings = QSettings("Mtuci", "Library")
    dbConf.beginGroup("Connection")
    db = tryConnect(dbConf.value("Host"),
                    int(dbConf.value("Port")),
                    dbConf.value("User"),
                    dbConf.value("Pass"))
    dbConf.endGroup()

    workRes = 0
    if db.open():

        query = QSqlQuery()
        queryStr = "insert into Book(b_name, year_release, description, author, publisher) values (:name,:year_release,:description,:author,:publisher);"

        query.prepare(queryStr)
        query.bindValue(":name", data["name"])
        query.bindValue(":year_release", data["year_release"])
        query.bindValue(":description", data["description"])
        query.bindValue(":author", data["author"])
        query.bindValue(":publisher", data["publisher"])

        if query.exec():
            print("inserted")
            workRes = 0
        else:
            print("insert error", query.lastError().text())
            workRes = 1
        db.close()

    return workRes


def selectBook():
    '''Выборка записей книг из БД'''
    records = []
    try:
        dbConf: QSettings = QSettings("Mtuci", "Library")
        dbConf.beginGroup("Connection")
        db = tryConnect(dbConf.value("Host"),
                        int(dbConf.value("Port")),
                        dbConf.value("User"),
                        dbConf.value("Pass"))
        dbConf.endGroup()

        if db.open():
            query = QSqlQuery()
            query.prepare("select * from Book;")
            if query.exec():
                while query.next():
                    records.append(tuple(query.value(i) for i in range(query.record().count())))
            else:
                print("select error", query.lastError().text())
            db.close()

    except Exception as _:
        msgIcon = QMessageBox.Warning
        msgText = "Ошибка подключения: {0}".format("Неккоректные параметры подключения")
        msg: QMessageBox = QMessageBox(msgIcon, "Подключение к БД", msgText, QMessageBox.Ok)
        msg.exec()

    return records


def updateBook(record: dict):
    '''Обновление записи книги в БД'''
    dbConf: QSettings = QSettings("Mtuci", "Library")
    dbConf.beginGroup("Connection")
    db = tryConnect(dbConf.value("Host"),
                    int(dbConf.value("Port")),
                    dbConf.value("User"),
                    dbConf.value("Pass"))
    dbConf.endGroup()

    if db.open():
        query = QSqlQuery()
        queryStr = "update Book set b_name=:name , year_release=:year_release, description=:description, author=:author, publisher=:publisher where b_id=:id ;"

        query.prepare(queryStr)
        query.bindValue(":name", record["name"])
        query.bindValue(":year_release", record["year_release"])
        query.bindValue(":description", record["description"])
        query.bindValue(":author", record["author"])
        query.bindValue(":publisher", record["publisher"])
        query.bindValue(":id", record["id"])

        if query.exec():
            print("updated")
        else:
            print("update error", query.lastError().text())
        db.close()


def deleteBook(record: dict):
    '''Удаление записи книги в БД'''
    dbConf: QSettings = QSettings("Mtuci", "Library")
    dbConf.beginGroup("Connection")
    db = tryConnect(dbConf.value("Host"),
                    int(dbConf.value("Port")),
                    dbConf.value("User"),
                    dbConf.value("Pass"))
    dbConf.endGroup()

    if db.open():
        query = QSqlQuery()
        query.prepare("delete from Book where b_id=:id ;")
        query.bindValue(":id", record["id"])
        if query.exec():
            print("deleted")
        else:
            print("delete error", query.lastError().text())
        db.close()
