from groupdocs.signature import Signature
from groupdocs.signature.options import QrCodeSearchOptions


def search_qr_codes():
    with Signature("signed.pdf") as signature:
        result = signature.search([QrCodeSearchOptions()])

        print(f"Found {len(result.signatures)} QR code signature(s)")
        for qr_code in result.signatures:
            print(f"QR code signature found at page {qr_code.page_number} "
                  f"with type {qr_code.encode_type.type_name} and text '{qr_code.text}'")


if __name__ == "__main__":
    search_qr_codes()