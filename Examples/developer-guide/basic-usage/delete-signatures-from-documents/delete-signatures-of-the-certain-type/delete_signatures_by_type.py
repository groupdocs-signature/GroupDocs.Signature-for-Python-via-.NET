import shutil

from groupdocs.signature import Signature
from groupdocs.signature.domain import SignatureType


def delete_signatures_by_type():
    # delete() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "all_text_signatures_deleted.docx")

    with Signature("all_text_signatures_deleted.docx") as signature:
        # Delete every text signature in the document
        result = signature.delete(SignatureType.TEXT)
        print(f"Deleted {len(result.succeeded)} text signature(s), {len(result.failed)} failed")
        for number, deleted in enumerate(result.succeeded, 1):
            print(f"  #{number}: '{deleted.text}' (id {deleted.signature_id})")


if __name__ == "__main__":
    delete_signatures_by_type()