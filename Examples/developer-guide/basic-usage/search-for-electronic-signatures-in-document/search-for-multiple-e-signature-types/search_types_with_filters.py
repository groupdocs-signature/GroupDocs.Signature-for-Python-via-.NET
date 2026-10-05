from groupdocs.signature import Signature
from groupdocs.signature.domain import BarcodeTypes, QrCodeTypes, SignatureType, TextMatchType
from groupdocs.signature.options import BarcodeSearchOptions, MetadataSearchOptions, QrCodeSearchOptions


def search_types_with_filters():
    with Signature("signed.pdf") as signature:
        # Code 128 barcodes only
        barcode_options = BarcodeSearchOptions()
        barcode_options.encode_type = BarcodeTypes.CODE128
        # QR codes whose text contains "John"
        qr_code_options = QrCodeSearchOptions()
        qr_code_options.encode_type = QrCodeTypes.QR
        qr_code_options.text = "John"
        qr_code_options.match_type = TextMatchType.CONTAINS
        # The "Author" metadata property
        metadata_options = MetadataSearchOptions()
        metadata_options.name = "Author"

        result = signature.search([barcode_options, qr_code_options, metadata_options])

        print(f"Found {len(result.signatures)} signature(s)")
        for found in result.signatures:
            if found.signature_type == SignatureType.METADATA:
                print(f"METADATA: {found.name} = {found.value}")
            else:
                print(f"{found.signature_type.name} on page {found.page_number}: {found.text}")


if __name__ == "__main__":
    search_types_with_filters()