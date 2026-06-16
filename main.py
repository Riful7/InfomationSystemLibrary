"""
Проект информационной системы по теме "Информационная система управления библиотекой (книги)"
Разработал: студент группы УБВТ2402, Вагапов Е.В
"""

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLibraryInfo

from mainwindow import MainWindow

# Точка входа в программу
if __name__ == "__main__":
    app: QApplication = QApplication([])

    translator = QTranslator()
    translator.load("qtbase_ru", QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath))
    app.installTranslator(translator)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
