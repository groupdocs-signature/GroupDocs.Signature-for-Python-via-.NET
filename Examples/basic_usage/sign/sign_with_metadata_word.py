import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_word

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMetadataWord : Sign Word document with metadata signature\n")

    file_name = os.path.basename(sample_word)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_word) as signature:
        # Create metadata options
        options = gso.MetadataSignOptions()
        
        # Create few WordProcessing Metadata signatures
        signatures = [
            gsd.WordProcessingMetadataSignature("Author", "Mr.Scherlock Holmes"),
            gsd.WordProcessingMetadataSignature("DateCreated", datetime.now()),
            gsd.WordProcessingMetadataSignature("DocumentId", 123456),
            gsd.WordProcessingMetadataSignature("SignatureId", 123.456)
        ]
        
        # Add signatures to options
        options.signatures.extend(signatures)
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

