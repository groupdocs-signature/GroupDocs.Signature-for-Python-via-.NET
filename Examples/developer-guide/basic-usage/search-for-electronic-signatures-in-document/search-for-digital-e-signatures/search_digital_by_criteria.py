from datetime import datetime

from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSearchOptions


def search_digital_by_criteria():
    with Signature("signed.docx") as signature:
        options = DigitalSearchOptions()
        # Return only signatures made in 2026...
        options.sign_date_time_from = datetime(2026, 1, 1)
        options.sign_date_time_to = datetime(2026, 12, 31)
        # ...whose comment is equal to this text
        options.comments = "Approved by John Smith"

        result = signature.search([options])

        print(f"Found {len(result.signatures)} matching digital signature(s)")
        for digital in result.signatures:
            print(f"Signed on {digital.sign_time}, comment: '{digital.comments}', valid: {digital.is_valid}")


if __name__ == "__main__":
    search_digital_by_criteria()