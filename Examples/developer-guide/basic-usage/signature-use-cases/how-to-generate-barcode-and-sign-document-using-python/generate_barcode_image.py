import io

from groupdocs.signature import Signature
from groupdocs.signature.domain import BarcodeTypes
from groupdocs.signature.options import BarcodeSignOptions, PreviewSignatureOptions


def generate_barcode_image():
    # Create a memory stream to store the barcode image
    result = io.BytesIO()

    # Setup barcode signature options
    barcode_options = BarcodeSignOptions()
    barcode_options.encode_type = BarcodeTypes.CODE93
    barcode_options.text = "Case 148-01"

    # Create preview options
    preview_options = PreviewSignatureOptions(
        barcode_options,
        lambda options: result,  # Create the image stream
        lambda options, stream: None,  # Release the image stream
    )

    # Generate image to stream; no document is needed
    Signature.generate_signature_preview(preview_options)

    # Use the barcode image, for example save it for a third-party tool
    with open("barcode_result.png", "wb") as image_file:
        image_file.write(result.getvalue())
    print(f"Barcode image: {len(result.getvalue())} bytes")


if __name__ == "__main__":
    generate_barcode_image()