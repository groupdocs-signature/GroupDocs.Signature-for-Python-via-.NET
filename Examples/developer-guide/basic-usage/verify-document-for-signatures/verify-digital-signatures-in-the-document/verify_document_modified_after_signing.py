from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalVerifyOptions, TextSignOptions


def verify_document_modified_after_signing():
    # Change a copy of the digitally signed document
    with Signature("signed.pdf") as signature:
        signature.sign("modified.pdf", TextSignOptions("Changed after signing"))

    for file_name in ("signed.pdf", "modified.pdf"):
        with Signature(file_name) as signature:
            options = DigitalVerifyOptions("certificate.pfx")
            options.password = "1234567890"
            result = signature.verify(options)
            print(f"{file_name}: valid = {result.is_valid}")


if __name__ == "__main__":
    verify_document_modified_after_signing()