# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "abc123@gmail.com2021-09-1219:55betu@tempmailin.com"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('qrcode.png', scale=6)
