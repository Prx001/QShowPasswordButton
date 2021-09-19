import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from QShowPasswordButton import ShowPasswordButton
class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.resize(240, 80)
        self.setWindowTitle("Test")
        self.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.line_edit = QLineEdit(self)
        self.line_edit.setStyleSheet("""QLineEdit {
	color: rgb(0, 0, 0);
	background-color: rgb(222, 222, 222);
	border: 2px solid;
	border-radius: 6px;
	border-color: rgba(0, 0, 0, 0);
	padding-left: 10px;
	padding-right: 30px;
	lineedit-password-mask-delay: 1000;
}
QLineEdit:hover {
	background-color: rgb(200, 200, 200);
	border-color: rgb(116, 116, 116);
}
QLineEdit:focus {
	background-color: rgb(240, 240, 240);
	border-color: rgb(138, 21, 211);
}""")
        self.line_edit.resize(200, 40)
        self.line_edit.move(20, 20)
        self.show_password_button = ShowPasswordButton(self)
        self.show_password_button.move(194, 29)
        self.show_password_button.visibilityChanged.connect(self.change_visibility)
        self.show()
    def change_visibility(self):
        if self.show_password_button.enabled:
            self.line_edit.setEchoMode(QLineEdit.Normal)
        elif not self.show_password_button.enabled:
            self.line_edit.setEchoMode(QLineEdit.Password)
        # Or using lambda:
        # self.show_password_button.visibilityChanged.connect(lambda: self.password_line_edit.setEchoMode(QLineEdit.Normal) if self.show_password_button.enabled else self.password_line_edit.setEchoMode(QLineEdit.Password))
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
