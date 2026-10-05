import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import TextSearchOptions


def delete_text_signature():
    # delete() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "text_signature_deleted.docx")

    with Signature("text_signature_deleted.docx") as signature:
        options = TextSearchOptions()
        # Return only signatures added by GroupDocs.Signature, not the document's own text
        options.skip_external = True
        signatures = signature.search([options]).signatures
        print(f"Found {len(signatures)} text signature(s)")
        if not signatures:
            return

        text_signature = signatures[0]
        if signature.delete(text_signature):
            print(f"Deleted text signature '{text_signature.text}' at "
                  f"({text_signature.left}, {text_signature.top})")
        else:
            print(f"Text signature '{text_signature.text}' was not deleted")


if __name__ == "__main__":
    delete_text_signature()