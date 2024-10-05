import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.test_files import sample_signed_multi, certificate_pfx

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # VerifyDigital : Verify document with digital signature\n")

    # The path to the signed document
    file_path = sample_signed_multi

    # Open the document for verification
    with gs.Signature(file_path) as signature:
        options = gso.DigitalVerifyOptions(certificate_pfx)
        options.contact = "Mr.Smith"
        options.password = "1234567890"

        # Verify document signatures
        result = signature.verify(options)

        if result.is_valid:
            print(f"\nDocument {file_path} was verified successfully!")
            for item in result.succeeded:
                print(f"\nValid signature is found.")
        else:
            print(f"\nDocument {file_path} failed verification process.")

if __name__ == "__main__":
    run()
