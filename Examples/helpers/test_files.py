# test_files.py
# This module defines paths to test files.

import os
from os.path import join
import platform
from .utils import *

def get_sample_file_path(file_path):
    if platform.system() == 'Windows':
        return join(samples_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, samples_path, file_path)
    
def get_images_file_path(file_path):
    if platform.system() == 'Windows':
        return join(images_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, images_path, file_path)
    
def get_certificates_file_path(file_path):
    if platform.system() == 'Windows':
        return join(certificates_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, certificates_path, file_path)


# Archives
sample_zip = get_sample_file_path("sample.zip")

# PDFs
sample_pdf = get_sample_file_path("sample.pdf")
sample_pdf_signed_formfield = get_sample_file_path("sample_formfields.pdf")

# signature delete
sample_signed_multi = get_sample_file_path("sample_multiple_signatures.docx")

# Words
sample_word = get_sample_file_path("sample.docx")
sample_multiple_signatures_docx = get_sample_file_path("sample_multiple_signatures.docx")

# Images
image_handwrite = get_images_file_path("signature_handwrite.jpg")
image_stamp = get_images_file_path("stamp.png")

# Certificates
certificate_pfx = get_certificates_file_path("MrSmithSignature.pfx")
    



sample_history_docx = get_sample_file_path("sample_history.docx")

sample_pdf_signed_digital = get_sample_file_path("sample_signed_digital.pdf")