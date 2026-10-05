from datetime import datetime

from groupdocs.signature import Signature
from groupdocs.signature.domain import HorizontalAlignment, QrCodeTypes, VerticalAlignment
from groupdocs.signature.domain.extensions import Event
from groupdocs.signature.options import QrCodeSignOptions


def sign_pdf_with_event_qr_code():
    # Initialize signature handler
    with Signature("sample.pdf") as signature:
        # Provide event data
        event_qr = Event()
        event_qr.title = "Meeting"
        event_qr.description = "Productivity issues"
        event_qr.location = "room 408"
        event_qr.start_date = datetime(2022, 6, 19, 15, 30, 0)
        event_qr.end_date = datetime(2022, 6, 19, 17, 0, 0)

        # Setup QR code signature options
        qr_options = QrCodeSignOptions()
        qr_options.horizontal_alignment = HorizontalAlignment.RIGHT
        qr_options.vertical_alignment = VerticalAlignment.BOTTOM
        qr_options.encode_type = QrCodeTypes.QR
        qr_options.data = event_qr

        # Sign document
        result = signature.sign("signed_event.pdf", qr_options)
        print(f"QR codes added: {len(result.succeeded)}")


if __name__ == "__main__":
    sign_pdf_with_event_qr_code()