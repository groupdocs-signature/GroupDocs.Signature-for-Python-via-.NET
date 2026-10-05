from groupdocs.signature import Signature
from groupdocs.signature.options import TextSignOptions


def sign_pdf_with_text_signature():
    # Open the document; the with-block releases the file when it ends
    with Signature("sample.pdf") as signature:
        # A text signature 100 pixels from the left and top edges of the first page
        options = TextSignOptions("John Smith")
        options.left = 100
        options.top = 100

        # Sign and save the result to a new file; the source stays unchanged
        result = signature.sign("signed_sample.pdf", options)
        print(f"Signatures added: {len(result.succeeded)}")


if __name__ == "__main__":
    sign_pdf_with_text_signature()