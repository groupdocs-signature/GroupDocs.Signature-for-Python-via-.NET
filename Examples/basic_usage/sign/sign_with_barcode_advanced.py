import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithBarcodeAdvanced : Sign document with barcode (different encoding types)\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Create barcode signature options
        options = gso.BarcodeSignOptions("1234567890")
        
        # Setup different Barcode encoding types
        # For numeric data
        options.encode_type = gsd.BarcodeTypes.EAN_13
        
        # For alphanumeric data
        # options.encode_type = gsd.BarcodeTypes.CODE_128
        
        # For QR codes
        # options.encode_type = gsd.BarcodeTypes.QR
        
        # For 2D barcodes
        # options.encode_type = gsd.BarcodeTypes.DATA_MATRIX
        
        # Set signature position
        options.left = 100
        options.top = 100
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

