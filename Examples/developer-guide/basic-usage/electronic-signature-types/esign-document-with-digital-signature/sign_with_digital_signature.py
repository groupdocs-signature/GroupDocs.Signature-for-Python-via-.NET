from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSignOptions


def sign_with_digital_signature():
    with Signature("sample.pdf") as signature:
        # Create digital signature options with the certificate file
        options = DigitalSignOptions("certificate.pfx")

        # Set the certificate password
        options.password = "1234567890"

        # Optional: an image that shows the signature on the page
        options.image_file_path = "signature.jpg"

        # Set signature position
        options.left = 100
        options.top = 400

        # Sign the document and save the result
        result = signature.sign("signed_digital.pdf", options)
        print(f"Signed with {len(result.succeeded)} digital signature(s)")


if __name__ == "__main__":
    sign_with_digital_signature()