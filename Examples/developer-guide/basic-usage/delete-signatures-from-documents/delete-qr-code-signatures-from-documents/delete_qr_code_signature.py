import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import QrCodeSearchOptions


def delete_qr_code_signature():
    # delete() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.pptx", "qr_code_signature_deleted.pptx")

    with Signature("qr_code_signature_deleted.pptx") as signature:
        signatures = signature.search([QrCodeSearchOptions()]).signatures
        print(f"Found {len(signatures)} QR-Code signature(s)")
        if not signatures:
            return

        qr_code_signature = signatures[0]
        if signature.delete(qr_code_signature):
            print(f"Deleted QR-Code '{qr_code_signature.text}' ({qr_code_signature.encode_type.type_name}) "
                  f"at ({qr_code_signature.left}, {qr_code_signature.top})")
        else:
            print(f"QR-Code '{qr_code_signature.text}' was not deleted")


if __name__ == "__main__":
    delete_qr_code_signature()