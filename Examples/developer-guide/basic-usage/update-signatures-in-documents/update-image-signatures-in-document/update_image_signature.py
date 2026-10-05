import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import ImageSearchOptions


def update_image_signature():
    # update() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "updated_image_signature.docx")

    with Signature("updated_image_signature.docx") as signature:
        options = ImageSearchOptions()
        # Return only signatures added by GroupDocs.Signature, not the document's own images
        options.skip_external = True
        signatures = signature.search([options]).signatures
        print(f"Found {len(signatures)} image signature(s)")
        if not signatures:
            return

        image_signature = signatures[0]
        # Change the position
        image_signature.left = 240
        image_signature.top = 450
        # Change the size. Not all document formats support resizing a signature
        image_signature.width = 150
        image_signature.height = 125

        if signature.update(image_signature):
            print(f"Image signature moved to ({image_signature.left}, {image_signature.top}) "
                  f"and resized to {image_signature.width}x{image_signature.height}")
        else:
            print("Image signature was not updated")


if __name__ == "__main__":
    update_image_signature()