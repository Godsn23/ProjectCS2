from gui import *


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Bank1App()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

