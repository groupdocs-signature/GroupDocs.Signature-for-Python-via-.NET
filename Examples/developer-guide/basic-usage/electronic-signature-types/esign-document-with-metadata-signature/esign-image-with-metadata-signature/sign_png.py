from datetime import datetime

from groupdocs.signature import Signature
from groupdocs.signature.options import MetadataSignOptions
from groupdocs.signature.domain import ImageMetadataSignature


def sign_png():
    with Signature("sample.png") as signature:
        options = MetadataSignOptions()

        # Image metadata entries are identified by a number, not a name
        metadata_id = 41996

        # Add several Image Metadata signatures with values of different types
        options.add(ImageMetadataSignature(metadata_id, "Mr.Scherlock Holmes"))  # text
        options.add(ImageMetadataSignature(metadata_id + 1, datetime.now()))      # date and time
        options.add(ImageMetadataSignature(metadata_id + 2, 123456))              # whole number
        options.add(ImageMetadataSignature(metadata_id + 3, 123.456))             # floating-point number

        # Sign the image and save the result
        result = signature.sign("signed.png", options)
        print(f"Signed with {len(result.succeeded)} metadata signature(s):")
        for item in result.succeeded:
            print(f"  {item.id}")


if __name__ == "__main__":
    sign_png()