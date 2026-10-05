from groupdocs.signature import Signature
from groupdocs.signature.options import ImageSignOptions


def sign_with_image_from_stream():
    with Signature("sample.pdf") as signature:
        # Load the signature image from a stream
        with open("signature.jpg", "rb") as image_stream:
            options = ImageSignOptions(image_stream)
            options.left = 100
            options.top = 400
            options.width = 120
            options.height = 100

            result = signature.sign("signed_image_stream.pdf", options)
            print(f"Signed with {len(result.succeeded)} image signature(s)")


if __name__ == "__main__":
    sign_with_image_from_stream()