import os
import shutil
import groupdocs.signature as gs
from groupdocs.signature.domain import ImageSignature
from groupdocs.signature.options import ImageSearchOptions
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # DeleteImage : Delete Image signature from the document\n")

    # The path to the documents directory.
    file_path = sample_signed_multi  # Update this to your signed document path
    file_name = os.path.basename(file_path)

    # Copy the source file since Delete method works with the same document
    output_directory = get_output_directory_path()
    output_file_path = os.path.join(output_directory, file_name)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    shutil.copyfile(file_path, output_file_path)

    # Process image signatures
    with gs.Signature(output_file_path) as signature:
        options = ImageSearchOptions()

        # Search for image signatures in the document
        image_signatures = signature.search([options])

        if image_signatures:
            for qr_code_signature in image_signatures:
                result = signature.delete(qr_code_signature)
                if result:
                    print(f"Signature was deleted.")
                else:
                    print(f"Signature was not deleted! Signature was not found!")   
        else:
            print("No Image signatures were found in the document.")

if __name__ == "__main__":
    run()
