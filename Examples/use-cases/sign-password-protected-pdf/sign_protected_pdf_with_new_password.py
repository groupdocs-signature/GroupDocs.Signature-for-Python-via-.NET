from groupdocs.signature import PasswordRequiredException, Signature
from groupdocs.signature.domain import QrCodeTypes
from groupdocs.signature.options import LoadOptions, PdfSaveOptions, QrCodeSignOptions


def sign_protected_pdf_with_new_password():
    load_options = LoadOptions()
    load_options.password = "1234567890"
    save_options = PdfSaveOptions()
    save_options.password = "new-password"
    save_options.permissions_password = "new-owner-password"
    save_options.use_original_password = False
    options = QrCodeSignOptions("Approved by John Smith", QrCodeTypes.QR)
    with Signature("protected.pdf", load_options) as signature:
        result = signature.sign("signed_new_password.pdf", options, save_options)
        print(f"Signatures added: {len(result.succeeded)}")

    # The copy must not open without a password
    try:
        with Signature("signed_new_password.pdf") as signed:
            signed.get_document_info()
        print("The signed copy opens without a password!")
    except PasswordRequiredException:
        print("The signed copy asks for a password")


if __name__ == "__main__":
    sign_protected_pdf_with_new_password()