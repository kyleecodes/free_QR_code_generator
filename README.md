# Kylee's Free QR Code Generator

Simple Python script using [Pillow](https://pillow.readthedocs.io/en/stable/) and [qrcode](https://pypi.org/project/qrcode/) to generate free QR codes, with no expiration.

Saves generated QR codes as `.png` files in the `/QR_codes` directory. Automatically assigns the url domain name and current month / year as the filename. If the filename already exists, numbers are added to maintain uniqueness.

### Directions

Prerequisites: Python, pip

1. First install requirements:

   `pip install requirements.txt`

2. Input URLS in `qr_code_script.py` as args in main() function.

3. Ta Da! You made free QR codes. 🎉
