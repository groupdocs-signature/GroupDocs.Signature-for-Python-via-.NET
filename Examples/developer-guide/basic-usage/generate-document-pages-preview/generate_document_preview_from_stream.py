import io

from groupdocs.signature import Signature
from groupdocs.signature.options import PreviewOptions


def create_page_stream(page_data):
    # Keep each page image in memory instead of writing a file
    return io.BytesIO()


def release_page_stream(page_data, page_stream):
    # page_stream is the BytesIO returned above, already holding the whole image
    image = page_stream.getvalue()
    print(f"Page {page_data.page_number}: {len(image)} bytes of JPEG")


def generate_document_preview_from_stream():
    with open("sample.pdf", "rb") as stream:
        with Signature(stream) as signature:
            # Create preview options object with both functions
            preview_options = PreviewOptions(create_page_stream, release_page_stream)
            preview_options.preview_format = PreviewOptions.PreviewFormats.JPEG
            # Generate preview
            signature.generate_preview(preview_options)


if __name__ == "__main__":
    generate_document_preview_from_stream()