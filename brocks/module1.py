# brocks/module1.py

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

# دالة لإنشاء نافذة رئيسية
def create_window(title, width=400, height=300):
    app = QApplication(sys.argv)  # تطبيق PyQt
    window = QWidget()  # نافذة رئيسية
    window.setWindowTitle(title)  # تعيين العنوان
    window.setGeometry(100, 100, width, height)  # تعيين الحجم والموقع
    return window, app

# دالة لإضافة Label في النافذة
def add_label(window, text):
    label = QLabel(text, window)
    return label

# دالة لإضافة Button في النافذة
def add_button(window, text, function):
    button = QPushButton(text, window)
    button.clicked.connect(function)  # ربط الوظيفة مع الزر
    return button

# دالة لعرض نافذة تنبيه
def show_message(title, message, message_type="info"):
    from PyQt5.QtWidgets import QMessageBox
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)

    if message_type == "info":
        msg.setIcon(QMessageBox.Information)
    elif message_type == "warning":
        msg.setIcon(QMessageBox.Warning)
    elif message_type == "error":
        msg.setIcon(QMessageBox.Critical)

    msg.exec_()

# دالة لعرض نافذة مع بعض العناصر
def create_example_gui():
    window, app = create_window("Brocks GUI Example", 500, 400)
    
    # تخطيط عمودي للعناصر
    layout = QVBoxLayout()

    # إضافة Label
    label = add_label(window, "Welcome to Brocks GUI using PyQt5!")
    layout.addWidget(label)

    # دالة زر الضغط
    def button_clicked():
        show_message("Hello", "You clicked the button!", "info")

    # إضافة Button
    button = add_button(window, "Click me", button_clicked)
    layout.addWidget(button)

    # تعيين التخطيط للنافذة
    window.setLayout(layout)

    # عرض النافذة
    window.show()

    # بدء التطبيق
    sys.exit(app.exec_())

# تشغيل مثال للواجهة
if __name__ == "__main__":
    create_example_gui()
