# get_supported_file_formats.py
# This examples demonstrates how to print out all supported file types.

import groupdocs.signature as gs
import groupdocs.signature.domain as gsd

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # GetSupportedFileFormats : Get supported file formats\n")
    
    # Get supported file types and sort them by extension
    supported_file_types = gsd.FileType.get_supported_file_types()
    sorted_file_types = sorted(supported_file_types, key=lambda f: f.extension)
    
    # Loop through and print each supported file type
    for file_type in sorted_file_types:
        print(f"Extension: {file_type.extension}")

if __name__ == "__main__":
    run()