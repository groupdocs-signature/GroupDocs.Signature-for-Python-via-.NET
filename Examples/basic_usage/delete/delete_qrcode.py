import os
import shutil
import groupdocs.signature as gs
from groupdocs.signature.options import QrCodeSearchOptions
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # DeleteQRCode : Delete QR-Code signature from the document\n")

    file_path = sample_signed_multi
    file_name = os.path.basename(file_path)

    output_directory = get_output_directory_path()
    output_file_path = os.path.join(output_directory, file_name)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    shutil.copyfile(file_path, output_file_path)

    with gs.Signature(output_file_path) as signature:
        qr_code_options = QrCodeSearchOptions()

        # Search for QR-Code signatures in the document
        signatures = signature.search([qr_code_options])
        
        if signatures:
            for qr_code_signature in signatures:
                result = signature.delete(qr_code_signature)
                if result:
                    print(f"Signature was deleted.")
                else:
                    print(f"Signature was not deleted! Signature was not found!")   
        else:
            print("No QR-Code signatures were found in the document.")

if __name__ == "__main__":
    run()
