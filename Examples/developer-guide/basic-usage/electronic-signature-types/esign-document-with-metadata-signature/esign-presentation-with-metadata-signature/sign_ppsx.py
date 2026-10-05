from datetime import datetime

from groupdocs.signature import Signature
from groupdocs.signature.options import MetadataSignOptions
from groupdocs.signature.domain import PresentationMetadataSignature


def sign_ppsx():
    with Signature("sample.ppsx") as signature:
        options = MetadataSignOptions()

        # Create a few Presentation Metadata signatures
        signatures = [
            PresentationMetadataSignature("Author", "Mr.Scherlock Holmes"),
            PresentationMetadataSignature("DateCreated", datetime.now()),
            PresentationMetadataSignature("DocumentId", 123456),
            PresentationMetadataSignature("SignatureId", 123.456),
        ]

        # Add them to the options
        options.signatures.add_range(signatures)

        # Sign the presentation and save the result
        result = signature.sign("signed.ppsx", options)
        print(f"Signed with {len(result.succeeded)} metadata signature(s):")
        for item in result.succeeded:
            print(f"  {item.name}")


if __name__ == "__main__":
    sign_ppsx()