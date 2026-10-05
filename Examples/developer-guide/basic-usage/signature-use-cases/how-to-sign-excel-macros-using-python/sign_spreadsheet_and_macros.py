import zipfile

from groupdocs.signature import Signature
from groupdocs.signature.domain.extensions import DigitalVBA
from groupdocs.signature.options import DigitalSearchOptions, DigitalSignOptions


def sign_spreadsheet_and_macros():
    # Sign the spreadsheet and the macros within it
    with Signature("sample.xlsm") as signature:
        # Setup digital signature options
        sign_options = DigitalSignOptions("certificate.pfx")
        sign_options.password = "1234567890"
        sign_options.signature.comments = "Test Signature"

        # Add extension for signing VBA project digitally
        digital_vba = DigitalVBA("certificate.pfx", "1234567890")
        digital_vba.comments = "Signed VBA macros"
        sign_options.extensions.append(digital_vba)

        # Sign document
        signature.sign("signed_spreadsheet_and_macros.xlsm", sign_options)

    with Signature("signed_spreadsheet_and_macros.xlsm") as signed:
        found = signed.search([DigitalSearchOptions()]).signatures
        print(f"Workbook signatures found: {len(found)}")
    with zipfile.ZipFile("signed_spreadsheet_and_macros.xlsm") as package:
        print("VBA project signed:", "xl/vbaProjectSignature.bin" in package.namelist())


if __name__ == "__main__":
    sign_spreadsheet_and_macros()