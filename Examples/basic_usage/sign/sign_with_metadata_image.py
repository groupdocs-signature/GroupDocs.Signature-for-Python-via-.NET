import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMetadataImage : Sign Image document with metadata signature\n")

    # Note: Using sample_pdf as placeholder - replace with actual image file path
    file_name = "sample.png"
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Initialize with image file (update path as needed)
    image_path = os.path.join(os.path.dirname(sample_pdf), "sample.png")
    
    if not os.path.exists(image_path):
        print(f"Warning: Image file not found at {image_path}")
        print("Please update the file path in the example.")
        return

    with gs.Signature(image_path) as signature:
        # Create metadata options
        options = gso.MetadataSignOptions()
        
        # Specify different Metadata Signatures and add them to options signature collection
        imgs_metadata_id = 41996
        
        # Create several Image Metadata signatures with different types
        options.add(gsd.ImageMetadataSignature(imgs_metadata_id, "Mr.Scherlock Holmes"))  # String value
        imgs_metadata_id += 1
        options.add(gsd.ImageMetadataSignature(imgs_metadata_id, datetime.now()))         # Date Time value
        imgs_metadata_id += 1
        options.add(gsd.ImageMetadataSignature(imgs_metadata_id, 123456))                 # Integer value
        imgs_metadata_id += 1
        options.add(gsd.ImageMetadataSignature(imgs_metadata_id, 123.456))                # Double value
        imgs_metadata_id += 1
        options.add(gsd.ImageMetadataSignature(imgs_metadata_id, 123.456))                # Decimal value
        imgs_metadata_id += 1
        options.add(gsd.ImageMetadataSignature(imgs_metadata_id, 123.456))                # Float value
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

