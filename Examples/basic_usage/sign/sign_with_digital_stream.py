import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf, certificate_pfx

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithDigitalStream : Sign document with digital certificate from stream\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Load certificate from stream
        with open(certificate_pfx, "rb") as cert_stream:
            # Create digital signature options
            options = gso.DigitalSignOptions(cert_stream)
            
            # Set certificate password
            options.password = "1234567890"
            
            # Set signature position
            options.left = 100
            options.top = 100
            
            # Sign document
            result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

