from groupdocs.signature import Signature
from groupdocs.signature.domain import TextMatchType, TextSignatureImplementation
from groupdocs.signature.options import (BarcodeVerifyOptions, DigitalVerifyOptions, QrCodeVerifyOptions,
                                         TextVerifyOptions)


def verify_multiple_signature_types():
    with Signature("signed.pdf") as signature:
        # Text signature that contains "John"
        text_options = TextVerifyOptions()
        text_options.all_pages = True  # this value is set by default
        text_options.signature_implementation = TextSignatureImplementation.NATIVE
        text_options.text = "John"
        text_options.match_type = TextMatchType.CONTAINS

        # Barcode signature that contains "12345"
        barcode_options = BarcodeVerifyOptions()
        barcode_options.text = "12345"
        barcode_options.match_type = TextMatchType.CONTAINS

        # QR code signature that contains "John"
        qr_code_options = QrCodeVerifyOptions()
        qr_code_options.text = "John"
        qr_code_options.match_type = TextMatchType.CONTAINS

        # Digital signature made with this certificate for the reason "Approved"
        digital_options = DigitalVerifyOptions("certificate.pfx")
        digital_options.password = "1234567890"
        digital_options.reason = "Approved"

        result = signature.verify([text_options, barcode_options, qr_code_options, digital_options])

        if result.is_valid:
            print("Document was verified successfully!")
        else:
            print("Document failed verification process.")
        for verified in result.succeeded:
            print(f"Verified {verified.signature_type.name} signature")


if __name__ == "__main__":
    verify_multiple_signature_types()