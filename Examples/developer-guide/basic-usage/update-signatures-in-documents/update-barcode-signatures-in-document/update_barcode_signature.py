import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import BarcodeSearchOptions


def update_barcode_signature():
    # update() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "updated_barcode_signature.docx")

    with Signature("updated_barcode_signature.docx") as signature:
        options = BarcodeSearchOptions()
        # Return only signatures added by GroupDocs.Signature, not barcodes that are part of the document
        options.skip_external = True
        signatures = signature.search([options]).signatures
        print(f"Found {len(signatures)} barcode signature(s)")
        if not signatures:
            return

        barcode_signature = signatures[0]
        # Change the position
        barcode_signature.left = 60
        barcode_signature.top = 700
        # Change the size. Not all document formats support resizing a signature
        barcode_signature.width = 320
        barcode_signature.height = 80

        if signature.update(barcode_signature):
            print(f"Barcode '{barcode_signature.text}' ({barcode_signature.encode_type.type_name}) "
                  f"moved to ({barcode_signature.left}, {barcode_signature.top}) "
                  f"and resized to {barcode_signature.width}x{barcode_signature.height}")
        else:
            print(f"Barcode '{barcode_signature.text}' was not updated")


if __name__ == "__main__":
    update_barcode_signature()