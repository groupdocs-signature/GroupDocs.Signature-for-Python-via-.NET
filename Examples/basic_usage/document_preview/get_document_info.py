from groupdocs.signature import Signature
from helpers.test_files import sample_signed_multi
import os


def run():
    """
    Get document basic info
    """
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # GetDocumentInfo : Get document basic info\n")

    # The path to the documents directory.
    file_path = sample_signed_multi

    with Signature(file_path) as signature:
        document_info = signature.get_document_info()
        print(f"Document properties {os.path.basename(file_path)}:")
        print(f" - format : {document_info.file_type.file_format}")
        print(f" - extension : {document_info.file_type.extension}")
        print(f" - size : {document_info.size}")
        print(f" - page count : {document_info.page_count}")
        print(f" - Form Fields count : {len(document_info.form_fields)}")
        print(f" - Text signatures count : {len(document_info.text_signatures)}")
        print(f" - Image signatures count : {len(document_info.image_signatures)}")
        print(f" - Digital signatures count : {len(document_info.digital_signatures)}")
        print(f" - Barcode signatures count : {len(document_info.barcode_signatures)}")
        print(f" - QrCode signatures count : {len(document_info.qr_code_signatures)}")
        print(f" - FormField signatures count : {len(document_info.form_field_signatures)}")
        for page_info in document_info.pages:
            print(f" - page-{page_info.page_number} Width {page_info.width}, Height {page_info.height}")

if __name__ == "__main__":
    run()
