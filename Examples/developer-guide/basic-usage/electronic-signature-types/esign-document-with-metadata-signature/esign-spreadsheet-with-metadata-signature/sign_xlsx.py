from datetime import datetime

from groupdocs.signature import Signature
from groupdocs.signature.options import MetadataSignOptions
from groupdocs.signature.domain import SpreadsheetMetadataSignature


def sign_xlsx():
    with Signature("sample.xlsx") as signature:
        options = MetadataSignOptions()

        # Create a few Spreadsheet Metadata signatures
        signatures = [
            SpreadsheetMetadataSignature("Author", "Mr.Scherlock Holmes"),
            SpreadsheetMetadataSignature("DateCreated", datetime.now()),
            SpreadsheetMetadataSignature("DocumentId", 123456),
            SpreadsheetMetadataSignature("SignatureId", 123.456),
        ]

        # Add them to the options
        options.signatures.add_range(signatures)

        # Sign the spreadsheet and save the result
        result = signature.sign("signed.xlsx", options)
        print(f"Signed with {len(result.succeeded)} metadata signature(s):")
        for item in result.succeeded:
            print(f"  {item.name}")


if __name__ == "__main__":
    sign_xlsx()