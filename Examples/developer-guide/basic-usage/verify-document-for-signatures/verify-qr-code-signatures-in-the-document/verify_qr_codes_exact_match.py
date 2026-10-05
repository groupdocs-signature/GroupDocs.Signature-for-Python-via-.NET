from groupdocs.signature import Signature
from groupdocs.signature.domain import QrCodeTypes, TextMatchType
from groupdocs.signature.options import QrCodeVerifyOptions


def verify_qr_codes_exact_match():
    with Signature("signed.pdf") as signature:
        options = QrCodeVerifyOptions()
        options.text = "John Smith"
        options.match_type = TextMatchType.EXACT  # require exact match
        # If the encode type is not set, any QR code type is accepted
        options.encode_type = QrCodeTypes.QR
        # Verify the first page only (page numbers start at 1)
        options.all_pages = False
        options.page_number = 1

        result = signature.verify(options)

        print(f"Document is valid: {result.is_valid}")
        for qr_code in result.succeeded:
            print(f"Verified {qr_code.encode_type.type_name} code '{qr_code.text}'")


if __name__ == "__main__":
    verify_qr_codes_exact_match()