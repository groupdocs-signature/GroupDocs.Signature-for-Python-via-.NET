from groupdocs.signature import Signature
from groupdocs.pydrawing import Color
from groupdocs.signature.domain import SignatureFont
from groupdocs.signature.options import PreviewSignatureOptions, TextSignOptions


def create_signature_stream(preview_options):
    # Name the image after the signature_id set below
    return open(f"{preview_options.signature_id}.png", "wb")


def release_signature_stream(preview_options, signature_stream):
    print(f"Image file {signature_stream.name} is ready for preview")


def generate_signature_preview_to_file():
    # Describe the signature exactly as you would for signing
    sign_options = TextSignOptions("John Smith")
    sign_options.width = 200
    sign_options.height = 50
    sign_options.fore_color = Color.dark_blue
    font = SignatureFont()
    font.family_name = "Arial"
    font.size = 24
    sign_options.font = font

    # Create preview options object
    preview_options = PreviewSignatureOptions(sign_options, create_signature_stream, release_signature_stream)
    preview_options.signature_id = "text_signature"
    preview_options.preview_format = PreviewSignatureOptions.PreviewFormats.PNG

    # Generate preview; no document is involved
    Signature.generate_signature_preview(preview_options)


if __name__ == "__main__":
    generate_signature_preview_to_file()