import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SearchForQrCode : Search document for QR Code signature\n")

    # The path to the signed document
    file_path = sample_pdf
    file_name = os.path.basename(file_path)

    # Open the document for searching
    with gs.Signature(file_path) as signature:
        # Search for QR code signatures in the document
        signatures = signature.search(gsd.SignatureType.QR_CODE)
        
        print(f"\nSource document ['{file_name}'] contains the following QR Code signature(s):")
        
        # Enumerate all signatures for output
        for qr_code_signature in signatures:
            print(f"Found QR Code signature at page {qr_code_signature.page_number}.")
            print(f"  Encode type: {qr_code_signature.encode_type}")
            print(f"  Text: {qr_code_signature.text}")

if __name__ == "__main__":
    run()

