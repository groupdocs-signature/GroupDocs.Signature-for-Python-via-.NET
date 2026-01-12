import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf, image_handwrite

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithImageStream : Sign document with image from stream\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Load image from stream
        with open(image_handwrite, "rb") as image_stream:
            # Create image signature options
            image_options = gso.ImageSignOptions(image_stream)
            
            # Set signature position
            image_options.left = 100
            image_options.top = 100
            
            # Sign document
            result = signature.sign(output_file_path, image_options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

