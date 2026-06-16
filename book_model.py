from PySide6.QtCore import QModelIndex, QAbstractTableModel, Qt


class BookModel(QAbstractTableModel):
    '''Класс модели для представления в главном окне'''

    def __init__(self, records: list[tuple]):
        super(BookModel, self).__init__()
        self.__records = records
        self.__headers = ["Название", "Год выпуска", "Автор", "Издательство"]

    def data(self, index, role=...):
        '''Получить заголовок модели по индексу и роли'''
        if not index.isValid():
            return None

        numCol = index.column()
        if role == Qt.ItemDataRole.DisplayRole:
            if numCol == 0:
                return self.__records[index.row()][1]
            elif numCol == 1:
                return self.__records[index.row()][2]
            elif numCol == 2:
                return self.__records[index.row()][4]
            elif numCol == 3:
                return self.__records[index.row()][5]

        return None

    def rowCount(self, parent: QModelIndex = ...) -> int:
        '''Получить количество строк'''
        return len(self.__records)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        '''Получить количество колонн'''
        return len(self.__headers)

    def headerData(self, section, orientation, role=...):
        '''Получить заголовок модели по номеру колонны, ориентации и роли'''
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.__headers[section]

        return super().headerData(section, orientation, role)

    def getRecordByRow(self, row: int):
        '''Получить запись по номеру строки'''
        return self.__records[row] if row < len(self.__records) else None
