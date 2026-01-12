import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMetadataSpreadsheet : Sign Spreadsheet document with metadata signature\n")

    # Note: Using sample_pdf as placeholder - replace with actual spreadsheet file path
    # For example: sample_xlsx = get_sample_file_path("sample.xlsx")
    file_name = "sample.xlsx"
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Initialize with spreadsheet file (update path as needed)
    spreadsheet_path = os.path.join(os.path.dirname(sample_pdf), "sample.xlsx")
    
    if not os.path.exists(spreadsheet_path):
        print(f"Warning: Spreadsheet file not found at {spreadsheet_path}")
        print("Please update the file path in the example.")
        return

    with gs.Signature(spreadsheet_path) as signature:
        # Create metadata options
        options = gso.MetadataSignOptions()
        
        # Create few Spreadsheet Metadata signatures
        signatures = [
            gsd.SpreadsheetMetadataSignature("Author", "Mr.Scherlock Holmes"),
            gsd.SpreadsheetMetadataSignature("DateCreated", datetime.now()),
            gsd.SpreadsheetMetadataSignature("DocumentId", 123456),
            gsd.SpreadsheetMetadataSignature("SignatureId", 123.456)
        ]
        
        # Add signatures to options
        options.signatures.extend(signatures)
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

