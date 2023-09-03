import qrcode
from PIL import Image


def create_wifi_qr(ssid, password):
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
    return img


def create_url_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def main():
    print("QR Code Generator")
    print("1. Wi-Fi QR Code")
    print("2. URL QR Code")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        ssid = input("Enter the Wi-Fi SSID: ")
        password = input("Enter the Wi-Fi Password: ")
        qr_img = create_wifi_qr(ssid, password)
    elif choice == "2":
        url = input("Enter the URL: ")
        qr_img = create_url_qr(url)
    else:
        print("Invalid choice")
        return

    filename = input("How do you want file to be named? ")
    qr_img.save(f"{filename}.png")

    print(f"QR Code saved as {filename}.png")


if __name__ == "__main__":
    main()
