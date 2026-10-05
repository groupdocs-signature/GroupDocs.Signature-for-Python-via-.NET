from groupdocs.signature import Signature
from groupdocs.signature.domain import QrCodeTypes, TextMatchType
from groupdocs.signature.options import QrCodeSearchOptions


def search_qr_codes_with_filters():
    with Signature("signed.pdf") as signature:
        options = QrCodeSearchOptions()
        # Search the first page only (page numbers start at 1)
        options.all_pages = False
        options.page_number = 1
        # Return only QR codes of the QR type...
        options.encode_type = QrCodeTypes.QR
        # ...whose text contains "John"
        options.text = "John"
        options.match_type = TextMatchType.CONTAINS

        result = signature.search([options])

        print(f"Found {len(result.signatures)} matching QR code signature(s)")
        for qr_code in result.signatures:
            print(f"Text: {qr_code.text}")
            print(f"Page number: {qr_code.page_number}")
            print(f"Position: X={qr_code.left}, Y={qr_code.top}")
            print(f"Size: {qr_code.width}x{qr_code.height}")
            print(f"Encode type: {qr_code.encode_type.type_name}")


if __name__ == "__main__":
    search_qr_codes_with_filters()