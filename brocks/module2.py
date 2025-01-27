# brocks/module2.py

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import QTimer
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

# دالة لإضافة Entry (حقل نصي قابل للتحرير)
def add_entry(window):
    entry = QLineEdit(window)
    return entry

# دالة لعرض رسالة تنبيه
def show_message(title, message, message_type="info"):
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

# دالة لعرض نافذة غريبة عندما يتم كتابة الكود المحدد
def show_glitch_window():
    glitch_window, glitch_app = create_window("Glitch Window", 500, 400)
    
    # إضافة بعض التأثيرات الغريبة
    label = add_label(glitch_window, "!!! ERROR !!!\nSystem Failure\n\nPOrt8:\"63621GG*5\" detected!\nInitiating Glitch Mode...")

    # تغيير النص لشيء مش طبيعي
    label.setStyleSheet("font-size: 20px; color: red; font-family: Courier New; background-color: black;")

    def glitch_effect():
        label.setText("!!!!! ERROR !!!!!\nSystem Failure... Please restart!\n\nPOrt8:\"63621GG*5\" Detected\nGlitch mode active...")
        label.setStyleSheet("font-size: 18px; color: green; font-family: 'Comic Sans MS'; background-color: yellow;")
    
    # تشغيل التأثير الغريب بعد 2 ثانية
    QTimer.singleShot(2000, glitch_effect)

    glitch_window.setLayout(QVBoxLayout())
    glitch_window.layout().addWidget(label)
    glitch_window.show()

    # بدأ التطبيق في نافذة الغلث
    sys.exit(glitch_app.exec_())

# دالة لعمل نافذة مع بعض العناصر
def create_example_gui():
    window, app = create_window("Brocks GUI Example", 500, 400)
    
    # تخطيط عمودي للعناصر
    layout = QVBoxLayout()

    # إضافة العناصر
    label = add_label(window, "Welcome to Brocks GUI using PyQt5!")
    layout.addWidget(label)

    def button_clicked():
        show_message("Hello", "You clicked the button!", "info")

    button = add_button(window, "Click me", button_clicked)
    layout.addWidget(button)

    entry = add_entry(window)
    layout.addWidget(entry)

    def submit_clicked():
        user_input = entry.text()
        if user_input == 'POrt8:"63621GG*5"':
            show_glitch_window()  # فتح نافذة الغريبة لو الكود مكتوب
        else:
            show_message("Submission", f"You entered: {user_input}", "info")

    submit_button = add_button(window, "Submit", submit_clicked)
    layout.addWidget(submit_button)

    # تعيين التخطيط للنافذة
    window.setLayout(layout)

    # عرض النافذة
    window.show()

    # بدء التطبيق
    sys.exit(app.exec_())

# تشغيل مثال للواجهة
if __name__ == "__main__":
    create_example_gui()
