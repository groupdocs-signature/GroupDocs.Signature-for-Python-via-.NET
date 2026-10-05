from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalVerifyOptions


def verify_digital_signatures():
    with Signature("signed.pdf") as signature:
        options = DigitalVerifyOptions("certificate.pfx")
        options.password = "1234567890"
        # The subject of the signing certificate must contain this text
        options.subject_name = "ProfJamesMoriarty"
        # The signing reason stored in the PDF signature must be equal to this text
        options.reason = "Approved"

        result = signature.verify(options)

        if result.is_valid:
            print(f"Document was verified successfully: {len(result.succeeded)} valid digital signature(s).")
        else:
            print("Document failed verification process.")


if __name__ == "__main__":
    verify_digital_signatures()