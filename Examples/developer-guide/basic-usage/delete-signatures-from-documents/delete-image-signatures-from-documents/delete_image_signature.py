import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import ImageSearchOptions


def delete_image_signature():
    # delete() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.pptx", "image_signature_deleted.pptx")

    with Signature("image_signature_deleted.pptx") as signature:
        options = ImageSearchOptions()
        # Return only signatures added by GroupDocs.Signature, not the slide's own pictures
        options.skip_external = True
        signatures = signature.search([options]).signatures
        print(f"Found {len(signatures)} image signature(s)")
        if not signatures:
            return

        image_signature = signatures[0]
        if signature.delete(image_signature):
            print(f"Deleted image signature at ({image_signature.left}, {image_signature.top}), "
                  f"{image_signature.size} bytes")
        else:
            print("Image signature was not deleted")


if __name__ == "__main__":
    delete_image_signature()