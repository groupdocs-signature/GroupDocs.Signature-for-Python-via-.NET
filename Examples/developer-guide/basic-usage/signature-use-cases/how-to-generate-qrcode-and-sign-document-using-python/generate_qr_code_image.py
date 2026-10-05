import io

from groupdocs.signature import Signature
from groupdocs.signature.domain import QrCodeTypes
from groupdocs.signature.options import PreviewSignatureOptions, QrCodeSignOptions


def generate_qr_code_image():
    # Create a memory stream to store the QR code image
    result = io.BytesIO()

    # Setup QR code signature options
    qr_options = QrCodeSignOptions()
    qr_options.encode_type = QrCodeTypes.QR
    qr_options.text = "Case 148-01"

    # Create preview options
    preview_options = PreviewSignatureOptions(
        qr_options,
        lambda options: result,  # Create the image stream
        lambda options, stream: None,  # Release the image stream
    )

    # Generate image to stream; no document is needed
    Signature.generate_signature_preview(preview_options)

    # Use the QR code image, for example save it for a third-party tool
    with open("qr_code_result.png", "wb") as image_file:
        image_file.write(result.getvalue())
    print(f"QR code image: {len(result.getvalue())} bytes")


if __name__ == "__main__":
    generate_qr_code_image()