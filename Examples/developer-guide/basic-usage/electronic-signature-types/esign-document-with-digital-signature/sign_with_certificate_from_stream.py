from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSignOptions


def sign_with_certificate_from_stream():
    with Signature("sample.pdf") as signature:
        # Load the certificate from a stream
        with open("certificate.pfx", "rb") as certificate_stream:
            options = DigitalSignOptions(certificate_stream)
            options.password = "1234567890"

            # Set signature position and size
            options.left = 100
            options.top = 400
            options.width = 200
            options.height = 60

            result = signature.sign("signed_digital_stream.pdf", options)
            print(f"Signed with {len(result.succeeded)} digital signature(s)")


if __name__ == "__main__":
    sign_with_certificate_from_stream()