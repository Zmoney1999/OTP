import pyotp
import qrcode
import sys
from PIL import Image
import time


def generate_qr(secret):
    otp_auth_url = pyotp.TOTP(secret).provisioning_uri(name="user@example.com", issuer_name="Secure App")
    qr = qrcode.make(otp_auth_url)
    qr.save("totp_qr.png")
    Image.open("totp_qr.png").show()

def get_otp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: main.py --generate-qr or --get-otp")
    else:

      command = sys.argv[1]
      secret = pyotp.random_base32()
  
      if command == "--generate-qr":
          generate_qr(secret)
      elif command == "--get-otp":
          print(f"One-Time Password: {get_otp(secret)}")
      else:
          print("Invalid command.")


