import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMetadataPdf : Sign PDF document with metadata signature\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Create metadata options
        options = gso.MetadataSignOptions()
        
        # Add metadata signatures
        options.add(gsd.PdfMetadataSignature("Author", "Mr.Scherlock Holmes"))  # String value
        options.add(gsd.PdfMetadataSignature("CreatedOn", datetime.now()))      # DateTime values
        options.add(gsd.PdfMetadataSignature("DocumentId", 123456))            # Integer value
        options.add(gsd.PdfMetadataSignature("SignatureId", 123.456))          # Double value
        options.add(gsd.PdfMetadataSignature("Amount", 123.456))               # Decimal value
        options.add(gsd.PdfMetadataSignature("Total", 123.456))                # Float value
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

