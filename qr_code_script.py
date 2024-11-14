import qrcode
from urllib.parse import urlparse
from datetime import datetime
import os

def make_qr_code(url):
    # Create a QR code instance
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )   
    qr.add_data(url)
    qr.make(fit=True)

    # Generate an image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Extract the main domain name without "www" and the top-level domain (.com, .org, etc.)
    domain_parts = urlparse(url).netloc.replace("www.", "").split('.')
    domain_name = domain_parts[0]  # Get the primary part of the domain

    # Get the current date in "Month_Year" format
    date_str = datetime.now().strftime("%b_%Y")
    base_filename = f"My_QR_Code_{domain_name}_{date_str}"

    # Check for existing files with the same base name and add an incrementing number if necessary
    filename = f"{base_filename}.png"
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}.png"
        counter += 1
    
    # Save png in directory
    image_path = "QR_codes"
    img.save(f"{image_path}/{filename}")
    print(f"QR code saved as {image_path}/{filename}")
    

def main():
    # enter URLS here
    website = 'https://www.communaltech.com/'
    linkedin = 'https://www.linkedin.com/in/kyleecodes/'
    
    make_qr_code(website)
    make_qr_code(linkedin)
    

if __name__ == "__main__":
    main()