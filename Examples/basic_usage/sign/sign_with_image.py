import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf, image_handwrite

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithImage : Sign document with image\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        options = gso.ImageSignOptions(image_handwrite)
        options.left = 50
        options.top = 50
        options.all_pages = True

        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()
