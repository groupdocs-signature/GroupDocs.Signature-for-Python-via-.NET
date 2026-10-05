from groupdocs.signature import Signature
from groupdocs.signature.domain import BarcodeTypes, HorizontalAlignment
from groupdocs.signature.options import BarcodeSignOptions


def sign_pdf_with_codabar():
    # Initialize signature handler
    with Signature("sample.pdf") as signature:
        # Create barcode signature options
        barcode_options = BarcodeSignOptions()
        barcode_options.horizontal_alignment = HorizontalAlignment.RIGHT
        barcode_options.top = 150
        barcode_options.encode_type = BarcodeTypes.CODABAR
        barcode_options.text = "19/06/2022"

        # Sign document
        result = signature.sign("signed_codabar.pdf", barcode_options)
        print(f"Barcodes added: {len(result.succeeded)}")


if __name__ == "__main__":
    sign_pdf_with_codabar()