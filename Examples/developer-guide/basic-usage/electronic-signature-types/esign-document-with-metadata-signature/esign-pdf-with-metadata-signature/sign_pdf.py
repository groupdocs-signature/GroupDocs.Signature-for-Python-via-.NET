from datetime import datetime

from groupdocs.signature import Signature
from groupdocs.signature.options import MetadataSignOptions
from groupdocs.signature.domain import PdfMetadataSignature


def sign_pdf():
    with Signature("sample.pdf") as signature:
        options = MetadataSignOptions()

        # Add metadata signatures with values of different types
        options.add(PdfMetadataSignature("Author", "Mr.Scherlock Holmes"))  # text
        options.add(PdfMetadataSignature("CreatedOn", datetime.now()))      # date and time
        options.add(PdfMetadataSignature("DocumentId", 123456))             # whole number
        options.add(PdfMetadataSignature("SignatureId", 123.456))           # floating-point number

        # Sign the document and save the result
        result = signature.sign("signed.pdf", options)
        print(f"Signed with {len(result.succeeded)} metadata signature(s):")
        for item in result.succeeded:
            print(f"  {item.name}")


if __name__ == "__main__":
    sign_pdf()