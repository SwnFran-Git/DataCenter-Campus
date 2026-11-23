import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "Src"))

from PyQt6.QtWidgets import QApplication
from Views.Monitoreo import ServerView


def main():
    app = QApplication(sys.argv)
    ventana = ServerView()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()