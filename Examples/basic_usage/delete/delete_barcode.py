import os
import shutil
import groupdocs.signature as gs
import groupdocs.signature.domain as gsd
import groupdocs.signature.options as gso
import helpers.utils as utils
from helpers.test_files import sample_signed_multi

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # DeleteBarcode : Delete Barcode signature from the document \n")
    
    # Path to the documents directory.
    file_path = sample_signed_multi  # Update this to your sample signed document path
    file_name = os.path.basename(file_path)
    
    # Copy source file since the Delete method works on the same document.
    output_directory = utils.get_output_directory_path()
    output_file_path = os.path.join(output_directory, file_name)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    shutil.copyfile(file_path, output_file_path)

    # Open the copied file and work with it.
    with gs.Signature(output_file_path) as signature:
        # Create Barcode search options
        options = gso.BarcodeSearchOptions()
        
        # Search for Barcode signatures in the document
        signatures = signature.search([options])
        
        if signatures:
           for barcode_signature in signatures:
               result = signature.delete(barcode_signature)
               if result:
                   print(f"Signature was deleted.")
               else:
                   print(f"Signature was not deleted! Signature was not found!")
        else:
            print("No barcode signatures found in the document.")
            

if __name__ == "__main__":
    run()
