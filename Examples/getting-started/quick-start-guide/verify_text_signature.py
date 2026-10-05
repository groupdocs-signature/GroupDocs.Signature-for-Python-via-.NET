from groupdocs.signature import Signature
from groupdocs.signature.options import TextVerifyOptions


def verify_text_signature():
    with Signature("signed.pdf") as signature:
        options = TextVerifyOptions("John Smith")
        result = signature.verify(options)
        print(f"Document is signed by John Smith: {result.is_valid}")


if __name__ == "__main__":
    verify_text_signature()