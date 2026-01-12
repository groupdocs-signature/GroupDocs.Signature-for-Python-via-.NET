import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SearchForBarcode : Search document for Barcode signature\n")

    # The path to the signed document
    file_path = sample_pdf
    file_name = os.path.basename(file_path)

    # Open the document for searching
    with gs.Signature(file_path) as signature:
        options = gso.BarcodeSearchOptions()
        options.all_pages = True  # This value is set by default

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

