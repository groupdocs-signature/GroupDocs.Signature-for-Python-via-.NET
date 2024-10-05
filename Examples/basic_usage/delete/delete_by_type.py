import os
import shutil
import groupdocs.signature as gs
from groupdocs.signature.domain import SignatureType
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_signed_multi

def run():
    print("--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # DeleteBySignatureType : Delete signatures of a certain type \n")

    # The path to the documents directory.
    file_path = sample_signed_multi  # Update this to your signed document path
    file_name = os.path.basename(file_path)

    # Copy the source file since the Delete method works on the same document.
    output_directory = get_output_directory_path()
    output_file_path = os.path.join(output_directory, file_name)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    shutil.copyfile(file_path, output_file_path)

    # Process QR-Code signatures
    with gs.Signature(output_file_path) as signature:
        # Delete QR-Code signatures from the document
        result = signature.delete(SignatureType.QR_CODE)

        if result.succeeded:
            print("The following QR-Code signatures were deleted:")
            for number, qr_signature in enumerate(result.succeeded, 1):
                print(f"Signature #{number}: Id: {qr_signature.signature_id}")
        else:
            print("No QR-Code signatures were deleted.")

if __name__ == "__main__":
    run()
