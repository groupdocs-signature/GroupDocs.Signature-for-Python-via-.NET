import os
import sys
import traceback
import subprocess

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# output that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Signature for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to sign documents, and search, verify, update and delete signatures, with GroupDocs.Signature for Python via .NET.
Each example demonstrates different use cases and functionalities such as:

- Signing documents with text, image, barcode, QR code, stamp, metadata, form-field and digital signatures.
- Searching documents for existing signatures.
- Verifying signatures against expected values.
- Updating and deleting signatures.
- Generating document page and signature previews.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def announce_license():
    """Report whether GROUPDOCS_LIC_PATH points at a usable license file."""
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        print(f"{GREEN}License available at: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example as a subprocess via the _run_example.py wrapper.

    A fresh subprocess per example resets the evaluation build's documents-per-
    process budget; the wrapper applies the license and makes evaluation-mode and
    missing-font errors non-fatal so the suite stays green unlicensed."""
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)
    wrapper = os.path.join(base_dir, "_run_example.py")
    result = subprocess.run(
        [sys.executable, wrapper, full_path], cwd=example_dir, env=os.environ.copy())
    if result.returncode != 0:
        raise RuntimeError(f"subprocess exited with code {result.returncode}")

examples = [
    "use-cases/sign-password-protected-pdf/sign_protected_pdf_without_password.py",
    "use-cases/sign-password-protected-pdf/sign_protected_pdf_with_wrong_password.py",
    "use-cases/sign-password-protected-pdf/sign_protected_pdf_keeping_password.py",
    "use-cases/sign-password-protected-pdf/sign_protected_pdf_with_new_password.py",
    "use-cases/sign-password-protected-pdf/inspect_protected_pdf.py",
    "use-cases/sign-password-protected-pdf/verify_signed_protected_pdf.py",
    "use-cases/signing-documents-linux-container-fonts/count_font_files.py",
    "use-cases/signing-documents-linux-container-fonts/probe_font_family.py",
    "use-cases/signing-documents-linux-container-fonts/sign_with_resolved_fonts.py",
    "use-cases/signing-documents-linux-container-fonts/verify_text_signatures.py",
    "getting-started/quick-start-guide/sign_pdf_with_text_signature.py",
    "getting-started/quick-start-guide/search_document_for_signatures.py",
    "getting-started/quick-start-guide/verify_text_signature.py",
    "developer-guide/basic-usage/delete-signatures-from-documents/delete-barcode-signatures-from-documents/delete_barcode_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-barcode-signature/sign_with_barcode_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-barcode-signature/sign_with_barcode_signature_advanced.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-barcode-signature/sign_with_different_barcode_types.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-metadata-signature/esign-image-with-metadata-signature/sign_png.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-barcode-e-signatures/search_barcodes.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-barcode-e-signatures/search_barcodes_with_filters.py",
    "developer-guide/basic-usage/update-signatures-in-documents/update-barcode-signatures-in-document/update_barcode_signature.py",
    "developer-guide/basic-usage/delete-signatures-from-documents/delete-image-signatures-from-documents/delete_image_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-digital-signature/sign_with_digital_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-digital-signature/sign_with_digital_signature_advanced.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-digital-signature/sign_with_certificate_from_stream.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-metadata-signature/esign-pdf-with-metadata-signature/sign_pdf.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-metadata-signature/esign-pdf-with-metadata-signature/sign_pdf_standard.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-form-field-e-signatures/search_form_fields.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-form-field-e-signatures/search_form_fields_by_name.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-generate-barcode-and-sign-document-using-python/sign_pdf_with_codabar.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-generate-barcode-and-sign-document-using-python/generate_barcode_image.py",
    "developer-guide/basic-usage/update-signatures-in-documents/update-image-signatures-in-document/update_image_signature.py",
    "developer-guide/basic-usage/delete-signatures-from-documents/delete-qr-code-signatures-from-documents/delete_qr_code_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-form-field-signature/sign_with_form_field_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-form-field-signature/fill_existing_form_fields.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-metadata-signature/esign-presentation-with-metadata-signature/sign_ppsx.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-image-e-signatures/search_images.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-image-e-signatures/extract_image_signatures.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-qr-code-e-signatures/search_qr_codes.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-qr-code-e-signatures/search_qr_codes_with_filters.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-generate-qrcode-and-sign-document-using-python/sign_pdf_with_event_qr_code.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-generate-qrcode-and-sign-document-using-python/generate_qr_code_image.py",
    "developer-guide/basic-usage/update-signatures-in-documents/update-qr-code-signatures-in-document/update_qr_code_signature.py",
    "developer-guide/basic-usage/delete-signatures-from-documents/delete-text-signatures-from-documents/delete_text_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-image-signature/sign_with_image_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-image-signature/sign_with_image_signature_advanced.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-image-signature/sign_with_image_from_stream.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-metadata-signature/esign-spreadsheet-with-metadata-signature/sign_xlsx.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-multiple-e-signature-types/search_types.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-multiple-e-signature-types/search_types_with_filters.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-sign-excel-macros-using-python/sign_spreadsheet_with_certificate.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-sign-excel-macros-using-python/sign_spreadsheet_macros_only.py",
    "developer-guide/basic-usage/signature-use-cases/how-to-sign-excel-macros-using-python/sign_spreadsheet_and_macros.py",
    "developer-guide/basic-usage/update-signatures-in-documents/update-text-signatures-in-document/update_text_signature.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-barcode-signatures-in-the-document/verify_barcode_signatures.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-barcode-signatures-in-the-document/verify_code128_barcode_signature.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-text-signatures-in-the-document/verify_text_signatures.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-text-signatures-in-the-document/verify_text_signature_exact_match.py",
    "developer-guide/basic-usage/delete-signatures-from-documents/delete-signatures-of-the-certain-type/delete_signatures_by_type.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-metadata-signature/esign-word-processing-document-with-metadata-signature/sign_docx.py",
    "developer-guide/basic-usage/generate-signatures-preview/generate_signature_preview_to_file.py",
    "developer-guide/basic-usage/generate-signatures-preview/generate_signature_preview_to_memory.py",
    "developer-guide/basic-usage/generate-signatures-preview/generate_signature_previews_in_different_formats.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-metadata-e-signatures/search_metadata.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-metadata-e-signatures/search_metadata_by_name.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-digital-signatures-in-the-document/verify_digital_signatures.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-digital-signatures-in-the-document/verify_document_modified_after_signing.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-for-multiple-signatures/verify_multiple_signature_types.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-qr-code-signatures-in-the-document/verify_qr_codes.py",
    "developer-guide/basic-usage/verify-document-for-signatures/verify-qr-code-signatures-in-the-document/verify_qr_codes_exact_match.py",
    "developer-guide/basic-usage/delete-signatures-from-documents/delete-digital-signatures-from-documents/delete_digital_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-qr-code-signature/sign_with_qr_code_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-qr-code-signature/sign_with_qr_code_signature_advanced.py",
    "developer-guide/basic-usage/generate-document-pages-preview/generate_document_preview.py",
    "developer-guide/basic-usage/generate-document-pages-preview/generate_document_preview_from_stream.py",
    "developer-guide/basic-usage/generate-document-pages-preview/generate_document_preview_of_selected_pages.py",
    "developer-guide/basic-usage/generate-document-pages-preview/generate_document_preview_with_resolution.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-digital-e-signatures/search_digital.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-digital-e-signatures/search_digital_by_criteria.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-text-e-signatures/search_text.py",
    "developer-guide/basic-usage/search-for-electronic-signatures-in-document/search-for-text-e-signatures/search_text_with_filters.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-text-signature/sign_with_text_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-text-signature/sign_with_text_signature_advanced.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-stamp-signature/sign_with_stamp_signature.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-stamp-signature/sign_with_stamp_signature_advanced.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-multiple-signatures/sign_with_multiple_signatures.py",
    "developer-guide/basic-usage/electronic-signature-types/esign-document-with-multiple-signatures/sign_with_multiple_signatures_advanced.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
]

print_intro()
announce_license()

base_dir = os.path.dirname(os.path.abspath(__file__))
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

sys.exit(1 if failed else 0)
