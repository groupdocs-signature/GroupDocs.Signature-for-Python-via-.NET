import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SearchForBarcodeAdvanced : Search document for Barcode signature with advanced options\n")

    # The path to the signed document
    file_path = sample_pdf
    file_name = os.path.basename(file_path)

    # Open the document for searching
    with gs.Signature(file_path) as signature:
        options = gso.BarcodeSearchOptions()
        
        # Specify pages to search
        options.pages = [1, 2]  # Search only on pages 1 and 2
        
        # Specify barcode types to search for
        options.barcode_type = "Code128"  # Search only for Code128 barcodes

        # Search for barcode signatures in the document
        signatures = signature.search([options])
        print(f"\nSource document ['{file_name}'] contains the following barcode signature(s):")
        
        # Enumerate all signatures for output
        for barcode_signature in signatures:
            print(f"Found Barcode signature at page {barcode_signature.page_number}.")
            print(f"  Barcode type: {barcode_signature.barcode_type}")
            print(f"  Barcode text: {barcode_signature.text}")
            print(f"  Position: X={barcode_signature.left}, Y={barcode_signature.top}")
            print(f"  Size: Width={barcode_signature.width}, Height={barcode_signature.height}")

if __name__ == "__main__":
    run()

