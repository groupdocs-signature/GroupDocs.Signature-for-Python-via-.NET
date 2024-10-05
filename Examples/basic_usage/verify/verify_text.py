import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_multiple_signatures_docx

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # VerifyText : Verify document with text signature\n")

    # The path to the documents directory
    file_name = os.path.basename(sample_multiple_signatures_docx)

    # Open the document for verification
    with gs.Signature(sample_multiple_signatures_docx) as signature:
        # Create text verification options
        options = gso.TextVerifyOptions()
        options.all_pages = True  # This value is set by default
        options.signature_implementation = gsd.TextSignatureImplementation.NATIVE
        options.text = "signature"
        options.match_type = gsd.TextMatchType.CONTAINS

        # Verify document signatures
        result = signature.verify(options)
        if result.is_valid:
            print(f"\nDocument {file_name} was verified successfully with {len(result.succeeded)} valid signature(s).")
        else:
            print(f"\nDocument {file_name} failed the verification process.")

if __name__ == "__main__":
    run()
