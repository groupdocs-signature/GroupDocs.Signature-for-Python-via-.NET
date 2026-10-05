from groupdocs.signature import Signature
from groupdocs.signature.domain import TextMatchType, TextSignatureImplementation
from groupdocs.signature.options import TextSearchOptions


def search_text_with_filters():
    with Signature("signed.pdf") as signature:
        options = TextSearchOptions()
        # Search the first page only (page numbers start at 1)
        options.all_pages = False
        options.page_number = 1
        # Return only text signatures that contain "John"...
        options.text = "John"
        options.match_type = TextMatchType.CONTAINS
        # ...and are part of the page content
        options.signature_implementation = TextSignatureImplementation.NATIVE

        result = signature.search([options])

        print(f"Found {len(result.signatures)} matching text signature(s)")
        for text_signature in result.signatures:
            print(f"'{text_signature.text}' on page {text_signature.page_number} "
                  f"at ({text_signature.left}, {text_signature.top}), "
                  f"size {text_signature.width}x{text_signature.height}")


if __name__ == "__main__":
    search_text_with_filters()