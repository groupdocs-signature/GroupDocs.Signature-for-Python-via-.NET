import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SearchForTextAdvanced : Search document for Text signature with advanced options\n")

    # The path to the signed document
    file_path = sample_signed_multi
    file_name = os.path.basename(file_path)

    # Open the document for searching
    with gs.Signature(file_path) as signature:
        search_options = gso.TextSearchOptions()
        
        # Search only page with specified number (None for all pages)
        search_options.page_number = None
        
        # Specify as True to search all pages of a document
        search_options.all_pages = True
        
        # Specify text to search
        search_options.text = "JS_"
        
        # Specify text match type
        search_options.match_type = gsd.TextMatchType.CONTAINS

        # Search document
        signatures = signature.search([search_options])
        
        print(f"\nSource document ['{file_name}'] contains the following text signature(s):")
        
        # Output signatures
        for text_signature in signatures:
            print(f"Found Text signature: {text_signature.signature_implementation} "
                  f"with text {text_signature.text}.")
            print(f"  Location at {text_signature.left}-{text_signature.top}. "
                  f"Size is {text_signature.width}x{text_signature.height}.")

if __name__ == "__main__":
    run()

