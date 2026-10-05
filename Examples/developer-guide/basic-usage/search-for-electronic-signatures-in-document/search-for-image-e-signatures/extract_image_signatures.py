from groupdocs.signature import Signature
from groupdocs.signature.domain import FileType
from groupdocs.signature.options import ImageSearchOptions


def extract_image_signatures():
    with Signature("signed.pdf") as signature:
        options = ImageSearchOptions()
        # Search the first page only
        options.all_pages = False
        options.page_number = 1
        # Skip images smaller than 1 KB
        options.min_content_size = 1024
        # Return the image data as PNG
        options.return_content = True
        options.return_content_type = FileType.PNG

        result = signature.search([options])

        print(f"Found {len(result.signatures)} matching image signature(s)")
        for number, image in enumerate(result.signatures, start=1):
            file_name = f"image_signature_{number}.png"
            with open(file_name, "wb") as output:
                output.write(image.content)
            print(f"Saved {file_name} ({len(image.content)} bytes)")


if __name__ == "__main__":
    extract_image_signatures()