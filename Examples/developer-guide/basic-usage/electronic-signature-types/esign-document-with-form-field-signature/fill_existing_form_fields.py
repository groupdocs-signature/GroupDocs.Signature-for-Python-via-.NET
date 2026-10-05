from groupdocs.signature import Signature
from groupdocs.signature.options import TextSignOptions
from groupdocs.signature.domain import FormTextFieldType, TextSignatureImplementation


def fill_existing_form_fields():
    with Signature("sample_form.pdf") as signature:
        # Put a note into the plain-text field "ApprovalNote"
        note_options = TextSignOptions("Document is approved")
        note_options.signature_implementation = TextSignatureImplementation.FORM_FIELD
        note_options.form_text_field_type = FormTextFieldType.PLAIN_TEXT
        note_options.form_text_field_title = "ApprovalNote"

        # Put the signer's name into the rich-text field "UserSignatureFullName"
        name_options = TextSignOptions("John Smith")
        name_options.signature_implementation = TextSignatureImplementation.FORM_FIELD
        name_options.form_text_field_type = FormTextFieldType.RICH_TEXT
        name_options.form_text_field_title = "UserSignatureFullName"

        # Sign the document with both options at once
        result = signature.sign("filled_form.pdf", [note_options, name_options])
        print(f"Filled {len(result.succeeded)} form field(s)")


if __name__ == "__main__":
    fill_existing_form_fields()