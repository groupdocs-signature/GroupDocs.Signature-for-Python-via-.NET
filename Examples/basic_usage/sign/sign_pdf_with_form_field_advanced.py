import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignPdfWithFormFieldAdvanced : Sign PDF document with multiple form field signatures\n")

    output_directory = get_output_directory_path()
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, "SignedWithFormFieldAdvanced.pdf")

    with gs.Signature(sample_pdf) as signature:
        # Create first form field options
        ff_options1 = gso.TextSignOptions("Document is approved")
        ff_options1.signature_implementation = gs.TextSignatureImplementation.FORM_FIELD
        ff_options1.form_text_field_type = gsd.FormTextFieldType.PLAIN_TEXT
        
        # Create second form field options
        ff_options2 = gso.TextSignOptions("John Smith")
        ff_options2.signature_implementation = gs.TextSignatureImplementation.FORM_FIELD
        ff_options2.form_text_field_type = gsd.FormTextFieldType.RICH_TEXT
        ff_options2.form_text_field_title = "UserSignatureFullName"
        
        # Create list of options
        list_options = [ff_options1, ff_options2]
        
        # Sign document
        result = signature.sign(output_file_path, list_options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

