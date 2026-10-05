from groupdocs.signature import Signature
from groupdocs.signature.options import TextSignOptions
from groupdocs.signature.domain import SignatureFont
from groupdocs.pydrawing import Color


def sign_with_text_signature():
    with Signature("sample.pdf") as signature:
        # Create text signature options
        options = TextSignOptions("John Smith")

        # Set signature position and size
        options.left = 100
        options.top = 400
        options.width = 200
        options.height = 50

        # Set text color and font
        options.fore_color = Color.red
        font = SignatureFont()
        font.family_name = "Arial"
        font.size = 24
        options.font = font

        # Sign the document and save the result
        result = signature.sign("signed_text.pdf", options)
        print(f"Signed with {len(result.succeeded)} text signature(s)")


if __name__ == "__main__":
    sign_with_text_signature()