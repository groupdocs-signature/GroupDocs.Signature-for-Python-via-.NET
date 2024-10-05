import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
import shutil
from helpers.test_files import sample_signed_multi
from helpers.utils import get_output_directory_path

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # UpdateImage : Update Image signature from the document\n")

    # The path to the documents directory.
    file_path = sample_signed_multi
    file_name = os.path.basename(file_path)

    output_directory = get_output_directory_path()  # Update this with your output directory path
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)
    shutil.copyfile(file_path, output_file_path)

    # Open the document
    with gs.Signature(output_file_path) as signature:
        options = gso.ImageSearchOptions()
        
        # Search for image signatures in the document
        signatures = signature.search([options])

        if signatures: 
            for image_signature in signatures:
                # Change position
                image_signature.left = 200
                image_signature.top = 250
                # Change size. Please note not all documents support changing signature size
                image_signature.width = 200
                image_signature.height = 200

                # Update the signature
                result = signature.update(image_signature)
                if result:
                    print(f"Image signature at location {image_signature.left}x{image_signature.top} was updated in the document ['{file_name}'].")
                else:
                    print("Image signature was not updated in the document!")
        else:
            print("No image signatures were found in the document.")

if __name__ == "__main__":
    run()
