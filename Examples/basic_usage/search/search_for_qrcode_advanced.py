import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SearchForQrCodeAdvanced : Search document for QR Code signature with advanced options\n")

    # The path to the signed document
    file_path = sample_pdf
    file_name = os.path.basename(file_path)

    # Open the document for searching
    with gs.Signature(file_path) as signature:
        search_options = gso.QrCodeSearchOptions()
        
        # Search on specific pages
        search_options.page_number = 1
        search_options.all_pages = False
        
        # Search for specific QR code type
        search_options.encode_type = gsd.QrCodeTypes.QR
        
        # Search for specific text in QR code
        search_options.text = "John"

        # Search document
        signatures = signature.search([search_options])
        
        print(f"\nSource document ['{file_name}'] contains the following QR Code signature(s):")
        
        # Process found signatures
        for qr_code_signature in signatures:
            print(f"Found QR Code signature: {qr_code_signature.text}")
            print(f"  Page number: {qr_code_signature.page_number}")
            print(f"  Position: X={qr_code_signature.left}, Y={qr_code_signature.top}")
            print(f"  Size: {qr_code_signature.width}x{qr_code_signature.height}")
            print(f"  Encode type: {qr_code_signature.encode_type}")
            print(f"  Error correction level: {qr_code_signature.error_correction_level}")

if __name__ == "__main__":
    run()

