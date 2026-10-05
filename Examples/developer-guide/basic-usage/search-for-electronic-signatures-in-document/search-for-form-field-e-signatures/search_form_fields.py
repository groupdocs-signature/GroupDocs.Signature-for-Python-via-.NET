from groupdocs.signature import Signature
from groupdocs.signature.options import FormFieldSearchOptions


def search_form_fields():
    with Signature("signed.pdf") as signature:
        result = signature.search([FormFieldSearchOptions()])

        print(f"Found {len(result.signatures)} form field signature(s)")
        for field in result.signatures:
            print(f"Page {field.page_number}: {field.type.name} field {field.name!r}, value: {field.value!r}")


if __name__ == "__main__":
    search_form_fields()