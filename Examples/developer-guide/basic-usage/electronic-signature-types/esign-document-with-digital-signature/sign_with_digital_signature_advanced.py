from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSignOptions


def sign_with_digital_signature_advanced():
    with Signature("sample.pdf") as signature:
        # Pass the certificate and the appearance image to the constructor
        options = DigitalSignOptions("certificate.pfx", "signature.jpg")
        options.password = "1234567890"

        # Show the signature on the page, at this position and size
        options.visible = True
        options.left = 100
        options.top = 400
        options.width = 200
        options.height = 100

        # Information stored in the signature
        options.contact = "John Smith"
        options.reason = "Approval"
        options.location = "New York"

        result = signature.sign("signed_digital_advanced.pdf", options)
        print(f"Signed with {len(result.succeeded)} digital signature(s)")


if __name__ == "__main__":
    sign_with_digital_signature_advanced()