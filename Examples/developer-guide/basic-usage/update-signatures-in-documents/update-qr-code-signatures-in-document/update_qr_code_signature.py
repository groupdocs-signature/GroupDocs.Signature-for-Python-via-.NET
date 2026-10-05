import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import QrCodeSearchOptions


def update_qr_code_signature():
    # update() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "updated_qr_code_signature.docx")

    with Signature("updated_qr_code_signature.docx") as signature:
        signatures = signature.search([QrCodeSearchOptions()]).signatures
        print(f"Found {len(signatures)} QR code signature(s)")
        if not signatures:
            return

        qr_code_signature = signatures[0]
        # Change the position
        qr_code_signature.left = 440
        qr_code_signature.top = 600
        # Change the size. Not all document formats support resizing a signature
        qr_code_signature.width = 140
        qr_code_signature.height = 140

        if signature.update(qr_code_signature):
            print(f"QR code '{qr_code_signature.text}' ({qr_code_signature.encode_type.type_name}) "
                  f"moved to ({qr_code_signature.left}, {qr_code_signature.top}) "
                  f"and resized to {qr_code_signature.width}x{qr_code_signature.height}")
        else:
            print(f"QR code '{qr_code_signature.text}' was not updated")


if __name__ == "__main__":
    update_qr_code_signature()