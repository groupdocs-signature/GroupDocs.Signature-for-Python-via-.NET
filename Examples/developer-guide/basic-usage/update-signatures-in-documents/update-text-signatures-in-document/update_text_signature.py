import shutil

from groupdocs.signature import Signature
from groupdocs.signature.options import TextSearchOptions


def update_text_signature():
    # update() saves the changes into the opened document, so work on a copy
    shutil.copy("signed.docx", "updated_text_signature.docx")

    with Signature("updated_text_signature.docx") as signature:
        options = TextSearchOptions()
        # Return only signatures added by GroupDocs.Signature, not the document's own text
        options.skip_external = True
        signatures = signature.search([options]).signatures
        print(f"Found {len(signatures)} text signature(s)")
        if not signatures:
            return

        text_signature = signatures[0]
        old_text = text_signature.text
        # Change the text
        text_signature.text = "John Walkman"
        # Change the position
        text_signature.left = text_signature.left + 10
        text_signature.top = text_signature.top + 10
        # Change the size. Not all document formats support resizing a signature
        text_signature.width = 200
        text_signature.height = 100

        if signature.update(text_signature):
            print(f"Updated '{old_text}' to '{text_signature.text}' at "
                  f"({text_signature.left}, {text_signature.top}), "
                  f"size {text_signature.width}x{text_signature.height}")
        else:
            print(f"Text signature '{old_text}' was not updated")


if __name__ == "__main__":
    update_text_signature()