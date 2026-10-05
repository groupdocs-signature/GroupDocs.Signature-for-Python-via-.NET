from groupdocs.signature import IncorrectPasswordException, Signature
from groupdocs.signature.domain import QrCodeTypes
from groupdocs.signature.options import LoadOptions, QrCodeSignOptions


def sign_protected_pdf_with_wrong_password():
    load_options = LoadOptions()
    load_options.password = "wrong-password"
    options = QrCodeSignOptions("Approved by John Smith", QrCodeTypes.QR)
    try:
        with Signature("protected.pdf", load_options) as signature:
            signature.sign("signed_wrong_password.pdf", options)
    except IncorrectPasswordException:
        print("IncorrectPasswordException: the password is wrong")


if __name__ == "__main__":
    sign_protected_pdf_with_wrong_password()