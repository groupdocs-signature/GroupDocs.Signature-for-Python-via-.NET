from groupdocs.signature import Signature
from groupdocs.signature.options import TextSearchOptions


def search_document_for_signatures():
    with Signature("signed.pdf") as signature:
        # Look for text signatures on every page
        result = signature.search([TextSearchOptions()])
        for found in result.signatures:
            print(f"Text signature '{found.text}' on page {found.page_number}")


if __name__ == "__main__":
    search_document_for_signatures()