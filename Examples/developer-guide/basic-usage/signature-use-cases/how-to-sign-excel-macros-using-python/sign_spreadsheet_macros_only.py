import zipfile

from groupdocs.signature import Signature
from groupdocs.signature.domain.extensions import DigitalVBA
from groupdocs.signature.options import DigitalSignOptions


def sign_spreadsheet_macros_only():
    # Sign macros within the spreadsheet
    with Signature("sample.xlsm") as signature:
        # Create digital signature options without digital certificate
        sign_options = DigitalSignOptions()

        # Add extension for signing VBA project digitally
        digital_vba = DigitalVBA("certificate.pfx", "1234567890")
        # Set to True only for signing VBA project
        digital_vba.sign_only_vba_project = True
        digital_vba.comments = "Signed VBA macros"
        sign_options.extensions.append(digital_vba)

        # Sign document
        result = signature.sign("signed_macros.xlsm", sign_options)
        print(f"Signatures added: {len(result.succeeded)}")

    # The VBA project signature is a separate part of the package
    with zipfile.ZipFile("signed_macros.xlsm") as package:
        print("VBA project signed:", "xl/vbaProjectSignature.bin" in package.namelist())


if __name__ == "__main__":
    sign_spreadsheet_macros_only()