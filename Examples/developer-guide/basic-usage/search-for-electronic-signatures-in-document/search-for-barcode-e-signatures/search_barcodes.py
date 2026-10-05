from groupdocs.signature import Signature
from groupdocs.signature.options import BarcodeSearchOptions


def search_barcodes():
    with Signature("signed.pdf") as signature:
        # Search all pages of the document for barcode signatures
        result = signature.search([BarcodeSearchOptions()])

        print(f"Found {len(result.signatures)} barcode signature(s)")
        for barcode in result.signatures:
            print(f"Page {barcode.page_number}: {barcode.encode_type.type_name} barcode '{barcode.text}' "
                  f"at ({barcode.left}, {barcode.top}), size {barcode.width}x{barcode.height}")


if __name__ == "__main__":
    search_barcodes()