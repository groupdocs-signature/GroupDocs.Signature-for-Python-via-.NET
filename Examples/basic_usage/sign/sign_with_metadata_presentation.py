import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMetadataPresentation : Sign Presentation document with metadata signature\n")

    # Note: Using sample_pdf as placeholder - replace with actual presentation file path
    file_name = "sample.ppsx"
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Initialize with presentation file (update path as needed)
    presentation_path = os.path.join(os.path.dirname(sample_pdf), "sample.pptx")
    
    if not os.path.exists(presentation_path):
        print(f"Warning: Presentation file not found at {presentation_path}")
        print("Please update the file path in the example.")
        return

    with gs.Signature(presentation_path) as signature:
        # Create metadata options
        options = gso.MetadataSignOptions()
        
        # Create few Presentation Metadata signatures
        signatures = [
            gsd.PresentationMetadataSignature("Author", "Mr.Scherlock Holmes"),
            gsd.PresentationMetadataSignature("DateCreated", datetime.now()),
            gsd.PresentationMetadataSignature("DocumentId", 123456),
            gsd.PresentationMetadataSignature("SignatureId", 123.456)
        ]
        
        # Add signatures to options
        options.signatures.extend(signatures)
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

