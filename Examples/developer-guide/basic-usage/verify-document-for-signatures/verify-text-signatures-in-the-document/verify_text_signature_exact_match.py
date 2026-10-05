from groupdocs.signature import Signature
from groupdocs.signature.domain import TextMatchType, TextSignatureImplementation
from groupdocs.signature.options import TextVerifyOptions


def verify_text_signature_exact_match():
    with Signature("signed.pdf") as signature:
        options = TextVerifyOptions()
        options.text = "John Smith"
        options.match_type = TextMatchType.EXACT  # require exact match
        # Check text signatures that are part of the page content
        options.signature_implementation = TextSignatureImplementation.NATIVE
        # Verify the first page only (page numbers start at 1)
        options.all_pages = False
        options.page_number = 1

        result = signature.verify(options)

        print(f"Document is valid: {result.is_valid}")
        for text_signature in result.succeeded:
            print(f"Verified {text_signature.signature_implementation.name} text signature '{text_signature.text}'")


if __name__ == "__main__":
    verify_text_signature_exact_match()