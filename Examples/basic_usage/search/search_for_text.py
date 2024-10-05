import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SearchForText : Search document for Text signature\n")

    # The path to the signed document
    file_path = sample_signed_multi
    file_name = os.path.basename(file_path)

    # Open the document for searching
    with gs.Signature(file_path) as signature:
        options = gso.TextSearchOptions()
        options.all_pages = True  # This value is set by default

        # Search for text signatures in the document
        signatures = signature.search([options])
        print(f"\nSource document ['{file_name}'] contains the following text signature(s):")
        
        # Enumerate all signatures for output
        for text_signature in signatures:
            print(f"Found Text signature at page {text_signature.page_number}.")

if __name__ == "__main__":
    run()
