import pyqrcode
import png
from pyqrcode import QRCode


def generate_qrcode(data):
    try:
        # Generate QR code
        url = pyqrcode.create(data)
        print(type(url))
        # Create and save the png file naming "myqr.png"
        url.png('media/qrcodes/{fname}.png'.format(fname = data), scale=6)
        return True
    except Exception as e:
        print("FAILED")
        return False