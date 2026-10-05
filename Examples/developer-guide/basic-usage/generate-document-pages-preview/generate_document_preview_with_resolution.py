from groupdocs.signature import Signature
from groupdocs.signature.options import PreviewOptions


def create_page_stream(page_data):
    return open(f"preview_page_{page_data.page_number}_150dpi.jpg", "wb")


def release_page_stream(page_data, page_stream):
    print(f"Image file {page_stream.name} is ready for preview")


def generate_document_preview_with_resolution():
    with Signature("sample.pdf") as signature:
        resolution = 150
        # Create preview options object: 150 DPI instead of the default 96
        preview_options = PreviewOptions(create_page_stream, release_page_stream, resolution)
        preview_options.preview_format = PreviewOptions.PreviewFormats.JPEG
        # Generate preview
        signature.generate_preview(preview_options)


if __name__ == "__main__":
    generate_document_preview_with_resolution()