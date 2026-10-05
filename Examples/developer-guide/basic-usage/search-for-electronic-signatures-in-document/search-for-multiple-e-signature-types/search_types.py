from groupdocs.signature import Signature
from groupdocs.signature.options import (BarcodeSearchOptions, FormFieldSearchOptions, ImageSearchOptions,
                                         QrCodeSearchOptions, TextSearchOptions)


def search_types():
    with Signature("signed.pdf") as signature:
        # One search call with options for every signature type to find
        options = [
            TextSearchOptions(),
            ImageSearchOptions(),
            BarcodeSearchOptions(),
            QrCodeSearchOptions(),
            FormFieldSearchOptions(),
        ]
        result = signature.search(options)

        print(f"Found {len(result.signatures)} signature(s)")
        for found in result.signatures:
            print(f"{found.signature_type.name} signature on page {found.page_number} "
                  f"at ({found.left}, {found.top})")


if __name__ == "__main__":
    search_types()