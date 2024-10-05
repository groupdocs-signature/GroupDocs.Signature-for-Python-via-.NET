import groupdocs.signature as gs 
import groupdocs.signature.options as gso 
import sys 
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Quick Start] # HelloWorld : Basic example of GroupDocs.Signature usage\n")

    # The path to the documents directory.
    file_name = os.path.basename(sample_pdf)

    output_directory = get_output_directory_path()  # Update this with your output directory path
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Sign document with text signature.
    with gs.Signature(sample_pdf) as signature:
        text_sign_options = gso.TextSignOptions("Hello world!")
        signature.sign(output_file_path, text_sign_options)

    print(f"\nSource document signed successfully.\nFile saved at {output_file_path}")

if __name__ == "__main__":
    run()