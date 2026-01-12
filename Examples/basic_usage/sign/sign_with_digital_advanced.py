import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf, image_handwrite, certificate_pfx

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithDigitalAdvanced : Sign document with digital certificate (advanced options)\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Create digital signature options
        options = gso.DigitalSignOptions(certificate_pfx)
        
        # Set certificate password
        options.password = "1234567890"
        
        # Set signature appearance
        options.visible = True
        options.image_file_path = image_handwrite
        
        # Set signature position and size
        options.left = 100
        options.top = 100
        options.width = 200
        options.height = 100
        
        # Set additional information
        options.contact = "John Smith"
        options.reason = "Approval"
        options.location = "New York"
        
        # Set XAdES type
        options.xades_type = gs.XAdESType.XAdES
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

