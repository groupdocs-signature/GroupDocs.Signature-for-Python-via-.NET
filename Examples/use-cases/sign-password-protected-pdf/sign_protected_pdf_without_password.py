import os

from groupdocs.signature import PasswordRequiredException, Signature
from groupdocs.signature.domain import QrCodeTypes
from groupdocs.signature.options import QrCodeSignOptions


def sign_protected_pdf_without_password():
    options = QrCodeSignOptions("Approved by John Smith", QrCodeTypes.QR)
    try:
        with Signature("protected.pdf") as signature:
            signature.sign("signed_no_password.pdf", options)
    except PasswordRequiredException:
        print("PasswordRequiredException: the document needs a password")
    print(f"Output written: {os.path.exists('signed_no_password.pdf')}")


if __name__ == "__main__":
    sign_protected_pdf_without_password()