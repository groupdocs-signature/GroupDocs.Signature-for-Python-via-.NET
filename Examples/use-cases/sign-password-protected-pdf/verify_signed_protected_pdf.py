from groupdocs.signature import Signature
from groupdocs.signature.options import LoadOptions, QrCodeVerifyOptions


def verify_signed_protected_pdf():
    load_options = LoadOptions()
    load_options.password = "1234567890"
    with Signature("signed_protected.pdf", load_options) as signature:
        options = QrCodeVerifyOptions()
        options.text = "Approved by John Smith"
        options.all_pages = True
        result = signature.verify(options)
        print(f"Verified: {result.is_valid}, matching QR codes: {len(result.succeeded)}")


if __name__ == "__main__":
    verify_signed_protected_pdf()