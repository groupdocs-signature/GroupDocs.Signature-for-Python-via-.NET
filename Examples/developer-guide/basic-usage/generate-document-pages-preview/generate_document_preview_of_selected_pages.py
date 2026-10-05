from groupdocs.signature import Signature
from groupdocs.signature.options import PreviewOptions


def create_page_stream(page_data):
    return open(f"preview_page_{page_data.page_number}.png", "wb")


def release_page_stream(page_data, page_stream):
    print(f"Image file {page_stream.name} is ready for preview")


def generate_document_preview_of_selected_pages():
    with Signature("sample.pdf") as signature:
        preview_options = PreviewOptions(create_page_stream, release_page_stream)
        # Page numbers are 0-based: [1] is the second page
        preview_options.page_numbers = [1]
        signature.generate_preview(preview_options)


if __name__ == "__main__":
    generate_document_preview_of_selected_pages()