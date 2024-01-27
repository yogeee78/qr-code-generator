import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data_to_encode = input("Enter the data to be encoded in the QR code: ")
    output_filename = input("Enter the output filename (with extension, e.g., my_qr_code.png): ")

    generate_qr_code(data_to_encode, output_filename)

    print(f"QR code generated and saved as '{output_filename}'.")
