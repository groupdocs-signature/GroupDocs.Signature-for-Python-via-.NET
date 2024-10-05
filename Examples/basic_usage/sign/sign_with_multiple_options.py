import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.utils import get_output_directory_path
from helpers.test_files import *

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMultipleOptions : Sign document with multiple signature types \n")

    file_name = os.path.basename(sample_word)

    output_directory = get_output_directory_path()
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, sample_multiple_signatures_docx)

    with gs.Signature(sample_word) as signature:
        text_options = gso.TextSignOptions("Text signature")
        text_options.vertical_alignment = gsd.VerticalAlignment.TOP
        text_options.horizontal_alignment = gsd.HorizontalAlignment.LEFT

        barcode_options = gso.BarcodeSignOptions("1234567")
        barcode_options.encode_type = gsd.BarcodeTypes.CODE128
        barcode_options.left = 0
        barcode_options.top = 150
        barcode_options.height = 50
        barcode_options.width = 200

        qrcode_options = gso.QrCodeSignOptions("JohnSmith")
        qrcode_options.encode_type = gsd.QrCodeTypes.QR
        qrcode_options.left = 0
        qrcode_options.top = 220

        digital_options = gso.DigitalSignOptions(certificate_pfx)
        digital_options.image_file_path = image_handwrite
        digital_options.left = 20
        digital_options.top = 400
        digital_options.height = 100
        digital_options.width = 100
        digital_options.password = "1234567890"

        image_options = gso.ImageSignOptions(image_stamp)
        image_options.left = 20
        image_options.top = 550
        image_options.height = 100
        image_options.width = 100

        list_options = [
            text_options,
            barcode_options,
            qrcode_options,
            digital_options,
            image_options
        ]

        result = signature.sign(output_file_path, list_options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()
