import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import DigitalSearchOptions


def delete_digital_signature():
    # delete() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.pdf", "digital_signature_deleted.pdf")

    with Signature("digital_signature_deleted.pdf") as signature:
        signatures = signature.search([DigitalSearchOptions()]).signatures
        print(f"Found {len(signatures)} digital signature(s)")
        if not signatures:
            return

        digital_signature = signatures[0]
        subject = digital_signature.certificate.subject
        if signature.delete(digital_signature):
            print(f"Deleted the digital signature of '{subject}', signed on {digital_signature.sign_time}")
        else:
            print(f"Digital signature of '{subject}' was not deleted")


if __name__ == "__main__":
    delete_digital_signature()