import groupdocs.signature as gs
import groupdocs.signature.options as gso
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignPdfWithFormField : Sign pdf document with form-field signature\n")

    output_directory = get_output_directory_path()
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, "SignedWithFormField.pdf")

    with gs.Signature(sample_pdf) as signature:
        # instantiate text form field signature
        text_signature = gs.domain.TextFormFieldSignature("FieldText", "Value1")
        # instantiate options based on text form field signature
        options = gso.FormFieldSignOptions(text_signature)
        options.top = 150
        options.left = 50
        options.height = 50
        options.width = 200

        # sign document to file
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()
