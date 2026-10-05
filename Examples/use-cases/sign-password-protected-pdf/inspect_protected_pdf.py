from groupdocs.signature import Signature
from groupdocs.signature.options import LoadOptions


def inspect_protected_pdf():
    load_options = LoadOptions()
    load_options.password = "1234567890"
    with Signature("protected.pdf", load_options) as signature:
        info = signature.get_document_info()
        print(f"{info.file_type.file_format}, {info.page_count} page(s), {info.size} bytes")


if __name__ == "__main__":
    inspect_protected_pdf()