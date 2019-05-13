from PyQt4 import QtCore


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


# Within your main window class...

def __init__(self, parent=None, **kwargs):
    # ...

    # Install the custom output stream
    sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)


def __del__(self):
    # Restore sys.stdout
    sys.stdout = sys.__stdout__


def normalOutputWritten(self, text):
    """Append text to the QTextEdit."""
    # Maybe QTextEdit.append() works as well, but this is how I do it:
    cursor = self.textEdit.textCursor()
    cursor.movePosition(QtGui.QTextCursor.End)
    cursor.insertText(text)
    self.textEdit.setTextCursor(cursor)
    self.textEdit.ensureCursorVisible()
