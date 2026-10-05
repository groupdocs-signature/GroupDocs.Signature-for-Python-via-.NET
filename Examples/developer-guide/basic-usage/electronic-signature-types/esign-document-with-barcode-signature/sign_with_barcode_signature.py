from groupdocs.signature import Signature
from groupdocs.signature.options import BarcodeSignOptions
from groupdocs.signature.domain import BarcodeTypes


def sign_with_barcode_signature():
    with Signature("sample.pdf") as signature:
        # Create barcode signature options with the text to encode
        options = BarcodeSignOptions("John Smith")

        # Set the barcode type
        options.encode_type = BarcodeTypes.CODE128

        # Set barcode position and size
        options.left = 100
        options.top = 400
        options.width = 300
        options.height = 100

        # Sign the document and save the result
        result = signature.sign("signed_barcode.pdf", options)
        print(f"Signed with {len(result.succeeded)} barcode signature(s)")


if __name__ == "__main__":
    sign_with_barcode_signature()