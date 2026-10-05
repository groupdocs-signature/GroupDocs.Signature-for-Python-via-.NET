from groupdocs.signature import Signature
from groupdocs.signature.options import QrCodeSignOptions
from groupdocs.signature.domain import QrCodeTypes


def sign_with_qr_code_signature():
    with Signature("sample.pdf") as signature:
        # Create QR code signature options with the text to encode
        options = QrCodeSignOptions("John Smith")

        # Set the QR code type
        options.encode_type = QrCodeTypes.QR

        # Set QR code position and size
        options.left = 100
        options.top = 400
        options.width = 100
        options.height = 100

        # Sign the document and save the result
        result = signature.sign("signed_qr_code.pdf", options)
        print(f"Signed with {len(result.succeeded)} QR code signature(s)")


if __name__ == "__main__":
    sign_with_qr_code_signature()