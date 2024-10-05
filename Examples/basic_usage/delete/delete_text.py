import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
import shutil
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # DeleteText : Delete Text signature from the document\n")

    # The path to the documents directory
    file_name = os.path.basename(sample_signed_multi)

    output_directory = get_output_directory_path()  # Update with your output directory path
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Copy source file since Delete method works with the same Document
    shutil.copyfile(sample_signed_multi, output_file_path)

    # Open the document to delete the text signature
    with gs.Signature(output_file_path) as signature:
        text_search_options = gso.TextSearchOptions()

        # Search for text signatures in the document
        signatures = signature.search([text_search_options])
        if signatures:
            for text_signature in signatures:
                result = signature.delete(text_signature)
                if result:
                    print(f"Signature was deleted.")
                else:
                    print(f"Signature was not deleted! Signature was not found!")
        else:
            print("No text signatures found in the document.")

if __name__ == "__main__":
    run()
