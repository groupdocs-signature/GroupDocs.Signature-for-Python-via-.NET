from groupdocs.signature import Signature
from groupdocs.signature.options import TextVerifyOptions


def verify_text_signatures():
    with Signature("signed.pdf") as signature:
        for label, text in (("Latin", "John Smith"), ("CJK", "山田太郎")):
            options = TextVerifyOptions(text)
            options.all_pages = True
            result = signature.verify(options)
            print(f"{label} signature verified: {result.is_valid} ({len(result.succeeded)} match)")


if __name__ == "__main__":
    verify_text_signatures()