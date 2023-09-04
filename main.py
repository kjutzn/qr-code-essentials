import sys
import qrcode
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, \
    QInputDialog
import PIL

class QRCodeGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel("Generate QR Code")
        self.layout.addWidget(self.label)

        self.choice_label = QLabel("Choose QR Code Type:")
        self.layout.addWidget(self.choice_label)

        self.wifi_button = QPushButton("Wi-Fi")
        self.wifi_button.clicked.connect(self.generate_wifi_qr)
        self.layout.addWidget(self.wifi_button)

        self.url_button = QPushButton("URL")
        self.url_button.clicked.connect(self.generate_url_qr)
        self.layout.addWidget(self.url_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def generate_wifi_qr(self):
        ssid, ok1 = QInputDialog.getText(self, "Enter the Wi-Fi SSID", "SSID:")
        if not ok1:
            return
        password, ok2 = QInputDialog.getText(self, "Enter the Wi-Fi Password", "Password:")
        if not ok2:
            return

        wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(wifi_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        filename, _ = QFileDialog.getSaveFileName(self, "Save QR Code as PNG", "", "PNG Files (*.png)")
        if filename:
            img.save(filename)
            self.show_qr_code(filename)

    def generate_url_qr(self):
        url, ok = QInputDialog.getText(self, "Enter the URL", "URL:")
        if not ok:
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        filename, _ = QFileDialog.getSaveFileName(self, "Save QR Code as PNG", "", "PNG Files (*.png)")
        if filename:
            img.save(filename)
            self.show_qr_code(filename)

    def show_qr_code(self, filename):
        pixmap = QPixmap(filename)
        self.result_label.setPixmap(pixmap)
        self.result_label.show()

def main():
    app = QApplication(sys.argv)
    window = QRCodeGeneratorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
