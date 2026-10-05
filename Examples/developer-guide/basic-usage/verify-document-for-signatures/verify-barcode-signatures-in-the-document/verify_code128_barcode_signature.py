from groupdocs.signature import Signature
from groupdocs.signature.domain import BarcodeTypes, TextMatchType
from groupdocs.signature.options import BarcodeVerifyOptions


def verify_code128_barcode_signature():
    with Signature("signed.pdf") as signature:
        options = BarcodeVerifyOptions()
        options.text = "123456789012"
        options.match_type = TextMatchType.EXACT  # require exact match
        # If the encode type is not set, any barcode type is accepted
        options.encode_type = BarcodeTypes.CODE128
        # Verify the first page only (page numbers start at 1)
        options.all_pages = False
        options.page_number = 1

        result = signature.verify(options)

        print(f"Document is valid: {result.is_valid}")
        for barcode in result.succeeded:
            print(f"Verified {barcode.encode_type.type_name} barcode '{barcode.text}'")


if __name__ == "__main__":
    verify_code128_barcode_signature()