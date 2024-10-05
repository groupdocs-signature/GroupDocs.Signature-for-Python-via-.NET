import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime
from helpers.test_files import sample_signed_multi, certificate_pfx

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # VerifyWithMultipleOptions : Verify document with multiple signature types\n")

    # The path to the signed document
    file_path = sample_signed_multi

    # Open the document for verification
    with gs.Signature(file_path) as signature:
        # Define TextVerifyOptions
        text_verify_options = gso.TextVerifyOptions()
        text_verify_options.all_pages = True  # This value is set by default
        text_verify_options.signature_implementation = gsd.TextSignatureImplementation.NATIVE
        text_verify_options.text = "Text signature"
        text_verify_options.match_type = gsd.TextMatchType.CONTAINS

        # Define BarcodeVerifyOptions
        barcode_verify_options = gso.BarcodeVerifyOptions()
        barcode_verify_options.all_pages = True  # This value is set by default
        barcode_verify_options.text = "12345"
        barcode_verify_options.match_type = gsd.TextMatchType.CONTAINS

        # Define QrCodeVerifyOptions
        qrcode_verify_options = gso.QrCodeVerifyOptions()
        qrcode_verify_options.all_pages = True  # This value is set by default
        qrcode_verify_options.text = "John"
        qrcode_verify_options.match_type = gsd.TextMatchType.CONTAINS

        # Define DigitalVerifyOptions
        digital_verify_options = gso.DigitalVerifyOptions(certificate_pfx)
        digital_verify_options.sign_date_time_from = datetime(2020, 1, 1)
        digital_verify_options.sign_date_time_to = datetime(2020, 12, 31)
        digital_verify_options.password = "1234567890"

        # Verify document signatures with multiple options
        verify_options_list = [text_verify_options, barcode_verify_options, qrcode_verify_options, digital_verify_options]
        result = signature.verify(verify_options_list)

        if result.is_valid:
            print("\nDocument was verified successfully!")
            print(f"\n{len(result.succeeded)} signatures have passed through the verification process.")
        else:
            print("\nDocument failed verification process.")

if __name__ == "__main__":
    run()
