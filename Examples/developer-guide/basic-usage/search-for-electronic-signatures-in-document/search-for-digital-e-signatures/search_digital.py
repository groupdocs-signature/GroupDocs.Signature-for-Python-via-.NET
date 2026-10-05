from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSearchOptions


def search_digital():
    with Signature("signed.pdf") as signature:
        result = signature.search([DigitalSearchOptions()])

        print(f"Found {len(result.signatures)} digital signature(s)")
        for digital in result.signatures:
            print(f"Signed on {digital.sign_time} with the certificate of {digital.certificate.subject}")
            print(f"Valid: {digital.is_valid}")


if __name__ == "__main__":
    search_digital()