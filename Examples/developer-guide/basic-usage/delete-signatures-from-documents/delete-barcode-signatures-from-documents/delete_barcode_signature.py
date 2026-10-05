import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import BarcodeSearchOptions


def delete_barcode_signature():
    # delete() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "barcode_signature_deleted.docx")

    with Signature("barcode_signature_deleted.docx") as signature:
        options = BarcodeSearchOptions()
        # Return only signatures added by GroupDocs.Signature, not barcodes that are part of the document
        options.skip_external = True
        signatures = signature.search([options]).signatures
        print(f"Found {len(signatures)} barcode signature(s)")
        if not signatures:
            return

        barcode_signature = signatures[0]
        if signature.delete(barcode_signature):
            print(f"Deleted barcode '{barcode_signature.text}' ({barcode_signature.encode_type.type_name})")
        else:
            print(f"Barcode '{barcode_signature.text}' was not deleted")


if __name__ == "__main__":
    delete_barcode_signature()