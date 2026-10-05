from groupdocs.signature import Signature
from groupdocs.signature.domain import QrCodeTypes
from groupdocs.signature.options import LoadOptions, QrCodeSignOptions


def sign_protected_pdf_keeping_password():
    load_options = LoadOptions()
    load_options.password = "1234567890"
    options = QrCodeSignOptions("Approved by John Smith", QrCodeTypes.QR)
    options.left = 420
    options.top = 560
    options.width = 120
    options.height = 120
    with Signature("protected.pdf", load_options) as signature:
        result = signature.sign("signed_original_password.pdf", options)
        print(f"Signatures added: {len(result.succeeded)}")


if __name__ == "__main__":
    sign_protected_pdf_keeping_password()