from groupdocs.signature import Signature
from groupdocs.signature.options import ImageSignOptions


def sign_with_image_signature():
    with Signature("sample.pdf") as signature:
        # Create image signature options with the image file
        options = ImageSignOptions("signature.jpg")

        # Set signature position and size
        options.left = 100
        options.top = 400
        options.width = 120
        options.height = 100

        # Sign the document and save the result
        result = signature.sign("signed_image.pdf", options)
        print(f"Signed with {len(result.succeeded)} image signature(s)")


if __name__ == "__main__":
    sign_with_image_signature()