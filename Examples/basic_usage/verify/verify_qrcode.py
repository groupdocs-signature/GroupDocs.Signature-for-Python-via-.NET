import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # VerifyQRCode : Verify document with QR-Code signature\n")

    # The path to the signed document
    file_path = sample_signed_multi

    # Open the document for verification
    with gs.Signature(file_path) as signature:
        options = gso.QrCodeVerifyOptions()
        options.all_pages = True  # This value is set by default
        options.text = "John"
        options.match_type = gsd.TextMatchType.CONTAINS

        # Verify document signatures
        result = signature.verify(options)

        if result.is_valid:
            print(f"\nDocument {file_path} was verified successfully!")
        else:
            print(f"\nDocument {file_path} failed verification process.")

if __name__ == "__main__":
    run()
