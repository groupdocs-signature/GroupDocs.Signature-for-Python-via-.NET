import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
import shutil
from helpers.test_files import sample_pdf
from helpers.utils import get_output_directory_path

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithText : Sign document with text signature\n")

    # The path to the documents directory.
    file_path = sample_pdf
    # The path to the documents directory
    file_name = os.path.basename(sample_pdf)

    output_directory = get_output_directory_path()  # Update with your output directory path
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Open the document
    with gs.Signature(file_path) as signature:
        # Set up text signature options
        options = gso.TextSignOptions("John Smith")
        options.left = 50
        options.top = 200
        options.width = 100
        options.height = 30

        # Sign document and save
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()
