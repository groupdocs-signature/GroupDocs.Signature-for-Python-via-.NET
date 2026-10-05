from groupdocs.signature import Signature
from groupdocs.signature.options import ImageSearchOptions


def search_images():
    with Signature("signed.pdf") as signature:
        result = signature.search([ImageSearchOptions()])

        print(f"Found {len(result.signatures)} image signature(s)")
        for image in result.signatures:
            print(f"Page {image.page_number}: {image.size} bytes at ({image.left}, {image.top}), "
                  f"size {image.width}x{image.height}")


if __name__ == "__main__":
    search_images()