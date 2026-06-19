"""
Signal Visualiser – Entry Point
================================
Creates the Qt application, instantiates the ViewModel and the main View,
then starts the event loop.

Usage
-----
    python main.py
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from viewmodels.main_viewmodel import MainViewModel
from views.main_window import MainWindow


def main() -> None:
    # High-DPI scaling (Qt 6 default is enabled, but explicit for clarity)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setApplicationName("Signal Visualiser")
    app.setOrganizationName("FAU Erlangen-Nürnberg")

    # Wire ViewModel → View (no direct Model reference in the View)
    viewmodel = MainViewModel()
    window = MainWindow(viewmodel)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
