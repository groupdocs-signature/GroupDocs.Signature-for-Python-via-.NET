from groupdocs.signature import Signature
from groupdocs.signature.options import PreviewOptions


def create_page_stream(page_data):
    # Page numbers are 0-based: preview_page_0.png is the first page
    image_name = f"preview_page_{page_data.page_number}.png"
    print(f"Saving page {page_data.page_number + 1} to {image_name}")
    return open(image_name, "wb")


def generate_document_preview():
    with Signature("sample.pdf") as signature:
        # Create preview options object: one PNG image per page
        preview_options = PreviewOptions(create_page_stream)
        preview_options.preview_format = PreviewOptions.PreviewFormats.PNG
        # Generate preview
        signature.generate_preview(preview_options)


if __name__ == "__main__":
    generate_document_preview()