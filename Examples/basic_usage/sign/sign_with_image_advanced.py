import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf, image_handwrite

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithImageAdvanced : Sign document with image (advanced options)\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Create image signature options
        image_options = gso.ImageSignOptions(image_handwrite)
        
        # Set signature position and size
        image_options.left = 100
        image_options.top = 100
        image_options.width = 200
        image_options.height = 100
        
        # Set advanced options
        image_options.opacity = 0.8
        image_options.rotation_angle = 45
        
        # Set image alignment
        image_options.horizontal_alignment = gsd.HorizontalAlignment.CENTER
        image_options.vertical_alignment = gsd.VerticalAlignment.CENTER
        
        # Add border
        image_options.border_color = gsd.Color.BLACK
        image_options.border_style = gsd.DashStyle.SOLID
        image_options.border_width = 2
        
        # Sign document
        result = signature.sign(output_file_path, image_options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

