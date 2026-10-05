from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSignOptions


def sign_spreadsheet_with_certificate():
    # Sign a spreadsheet
    with Signature("sample.xlsx") as signature:
        # Setup digital signature options
        sign_options = DigitalSignOptions("certificate.pfx")
        sign_options.password = "1234567890"
        sign_options.signature.comments = "Test Signature"

        # Sign document
        result = signature.sign("signed_spreadsheet.xlsx", sign_options)
        print(f"Digital signatures added: {len(result.succeeded)}")


if __name__ == "__main__":
    sign_spreadsheet_with_certificate()