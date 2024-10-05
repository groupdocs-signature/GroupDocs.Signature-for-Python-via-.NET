import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithStamp : Sign document with stamp\n")

    # The path to the documents directory
    file_name = os.path.basename(sample_pdf)

    output_directory = get_output_directory_path()  # Update with your output directory path
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    # Open the document for signing
    with gs.Signature(sample_pdf) as signature:
        # Define StampSignOptions
        options = gso.StampSignOptions()
        options.left = 50
        options.top = 150
        options.width = 200
        options.height = 200

        # Setup the outer line of the stamp
        outer_line = gsd.StampLine()
        outer_line.text = " * European Union "
        outer_line.text_repeat_type = gsd.StampTextRepeatType.FULL_TEXT_REPEAT
        outer_line.font = gsd.SignatureFont()
        outer_line.height = 22
        outer_line.text_bottom_intent = 6
        options.outer_lines.append(outer_line)

        # Setup the inner line of the stamp
        inner_line = gsd.StampLine()
        inner_line.text = "John Smith"
        inner_line.font = gsd.SignatureFont()
        inner_line.font.bold = True
        inner_line.height = 40
        options.inner_lines.append(inner_line)

        # Sign the document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()
