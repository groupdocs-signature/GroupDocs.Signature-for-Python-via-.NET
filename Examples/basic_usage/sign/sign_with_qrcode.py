import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithQRCode : Sign document with QR-Code\n")

    # The path to the documents directory
    file_name = os.path.basename(sample_pdf)

    output_directory = get_output_directory_path()  # Update with your output directory path
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Open the document for signing
    with gs.Signature(sample_pdf) as signature:
        # Create QRCodeSignOptions with predefined QRCode text
        options = gso.QrCodeSignOptions("JohnSmith")
        options.encode_type = gsd.QrCodeTypes.QR
        options.left = 50
        options.top = 150
        options.width = 200
        options.height = 200

        # Sign the document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()
