from groupdocs.signature import Signature
from groupdocs.signature.options import FormFieldSignOptions
from groupdocs.signature.domain import TextFormFieldSignature


def sign_with_form_field_signature():
    with Signature("sample.pdf") as signature:
        # Create a text form field named "FieldText" with the value "Value1"
        text_field = TextFormFieldSignature("FieldText", "Value1")

        # Create form field options for it
        options = FormFieldSignOptions(text_field)

        # Set form field position and size
        options.left = 100
        options.top = 400
        options.width = 200
        options.height = 20

        # Sign the document and save the result
        result = signature.sign("signed_form_field.pdf", options)
        for field in result.succeeded:
            print(f"Added form field '{field.name}' with value '{field.value}'")


if __name__ == "__main__":
    sign_with_form_field_signature()