from logic import *
from PyQt6.QtWidgets import QApplication


def main() -> None:
    """
    Launches the Yo Mama Joke Generator GUI application.
    Initializes the application and displays the main window.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
