# GroupDocs.Signature for Python

![PyPI](https://img.shields.io/pypi/v/groupdocs-signature-cloud)
![Python](https://img.shields.io/badge/Python-3.6+-informational)

**Create, apply, and verify digital signatures** in documents with an advanced Python **e-signature API**. Add electronic, barcode, QR-code, image, text, metadata, and form field signatures to **90+ document formats** including PDFs, Word, Excel, Images, and more.

> ✅ Supports `create digital signature`, `esign pdf`, `sign pdf doc`, `verify signature`, and `remove signatures` features across multiple platforms.


## Key Features

- Add [**electronic signatures**](https://docs.groupdocs.com/signature/python-net/esign-document-with-barcode-signature/) to **90+ document formats** including PDF, DOCX, XLSX, PPTX, PNG, TIFF, and more
- [Create signatures](https://docs.groupdocs.com/signature/python-net/esign-document-with-image-signature/) from **image, barcode, QR code, stamp, text, metadata, or form fields**
- Support for **signature validation**, [**verification**](https://docs.groupdocs.com/signature/python-net/verify-barcode-signatures-in-the-document/), and [**removal**](https://docs.groupdocs.com/signature/python-net/delete-barcode-signatures-from-documents/)
- [**Search and remove**](https://docs.groupdocs.com/signature/python-net/delete-barcode-signatures-from-documents/) existing signatures from documents
- Apply [**multiple signatures**](https://docs.groupdocs.com/signature/python-net/esign-document-with-multiple-signatures/) of different types to a single document
- Built-in support for [**digital certificates**](https://docs.groupdocs.com/signature/python-net/sign-document-with-digital-signature/#advanced-digital-signature-options) (X.509, PKCS#7) for legally binding signatures
- [**Metadata signatures**](https://docs.groupdocs.com/signature/python-net/esign-document-with-metadata-signature/) for document tracking and authentication
- [**Form field signatures**](https://docs.groupdocs.com/signature/python-net/esign-document-with-form-field-signature/) for interactive document workflows
- Integrate into your **signature app** or web-based **e-sign platform**
- **Cloud-based API** with Python SDK for scalable document processing


## 🔧 Supported Signature Types

| Signature Type     | Description                                |
|--------------------|--------------------------------------------|
| **Digital Signatures** | X.509 certificate-based signatures for legal compliance |
| **Image Signatures**   | Draw or upload images (PNG, JPEG, SVG, BMP)    |
| **Text Signatures**    | Add custom text annotations with fonts & styles |
| **QR-Code Signatures** | Generate QR codes with custom data/format   |
| **Barcode Signatures** | Add/search/remove barcodes from documents         |
| **Stamp Signatures**   | Custom stamps with date/user info/company logos |
| **Metadata Signatures** | Hidden signatures for document tracking & authentication |
| **Form Field Signatures** | Interactive signature fields for workflows |

## 📁 Supported Document Formats (90+)

**Office Documents:**
- Microsoft Word (DOC, DOCX, DOCM, DOT, DOTX, DOTM)
- Excel (XLS, XLSX, XLSM, XLSB, XLT, XLTX, XLTM)
- PowerPoint (PPT, PPTX, PPTM, PPS, PPSX)
- Visio (VSD, VSDX, VSS, VSSX, VST, VSTX)

**PDFs & Images:**
- PDF (Portable Document Format)
- Images (PNG, JPG, JPEG, BMP, TIFF, GIF, SVG, WEBP)

**Other Formats:**
- OpenDocument (ODT, ODS, ODP)
- Text files (TXT, RTF, CSV)
- Web formats (HTML, HTM)
- And many [more...](https://docs.groupdocs.com/signature/python-net/supported-file-formats/)

## 💡 Use Cases

- **Sign PDF documents** with digital certificates (X.509, PKCS#7)
- **E-sign Word documents** with image signatures or typed names
- **Add signatures to Excel spreadsheets** and CSV files
- **Verify and validate e-signatures** for authenticity
- **Search and remove** existing signatures from documents
- **Metadata signatures** for document versioning and tracking
- **Form field signatures** for interactive document workflows
- **Batch processing** multiple documents with signatures
- **Web applications** with Python Flask/Django integration
- **Automated document workflows** in Python scripts


## 🚀 How to run examples

* Call the following command from the root folder of repository   
`python .\Examples\run_examples.py`
* Review rendered files in `.\Examples\Output` folder



## 📦 Installation

Install via pip:

```bash
pip install groupdocs-signature-net
```

## How to sign a PDF document with a digital e-signature

```python
import groupdocs.signature as signature
from groupdocs.signature.options import DigitalSignOptions

# Initialize signature
with signature.Signature("sample.pdf") as sign:
    # Create digital signature options
    options = DigitalSignOptions("certificate.pfx")
    
    # Set certificate password
    options.password = "1234567890"
    
    # Optional: setup image file path
    options.image_file_path = "sample.jpg"
    
    # Set signature position
    options.left = 100
    options.top = 100
    
    # Sign document
    sign.sign("sampleSigned.pdf", options)
```

## How to verify barcode signatures in a document

```python
import groupdocs.signature as signature
from groupdocs.signature.options import BarcodeVerifyOptions

# Initialize signature
with signature.Signature("sample_signed.pdf") as sign:
    # Create verification options
    options = BarcodeVerifyOptions()
    options.text = "123456789"
    options.match_type = signature.TextMatchType.Contains
    options.all_pages = True  # verify on all pages
    
    # Verify signatures
    result = sign.verify(options)
    
    if result.is_valid:
        print("Document was verified successfully!")
    else:
        print("Document failed verification process.")
```

## 📚 Documentation & Resources

- [Official Documentation](https://docs.groupdocs.com/signature/python-net/)
- [API Reference](https://reference.groupdocs.com/signature/python-net/)
- [Code Examples](https://github.com/groupdocs-signature/GroupDocs.Signature-for-Python-via-.NET?tab=readme-ov-file)
- [PyPI Package](https://pypi.org/project/groupdocs-signature-net/)
- [Free Support Forum](https://forum.groupdocs.com/c/signature)
- [Live Demos](https://products.groupdocs.app/signature/total)


## 🖥️ Python Version Support

GroupDocs.Signature for Python supports:

- **Python 3.6+** (including Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12)
- **Frameworks:** Django, Flask, FastAPI, Pyramid
- **Platforms:** Windows, Linux, macOS
- **Cloud:** AWS Lambda, Google Cloud Functions, Azure Functions
- **Containers:** Docker, Kubernetes


## 📈 Why Choose GroupDocs.Signature for Python?

- **Cloud-based API** with high availability and scalability
- **No software installation** required - everything runs in the cloud
- **RESTful API** with comprehensive Python SDK
- **High-performance** signature processing for enterprise applications
- **Memory-efficient** processing of large documents
- **Thread-safe** operations for multi-threaded Python applications
- **Comprehensive API** with 90+ supported document formats
- **Easy integration** into existing Python signature applications
- **Regular updates** with new features and format support
- **Async/await support** for modern Python applications


## 🔒 Security & Compliance

- **Digital Certificate Support**: RSA, DSA, ECDSA algorithms
- **Standards Compliance**: PKCS#7, X.509, PDF/A compatibility
- **Signature Validation**: Timestamp verification and certificate chain validation
- **Legal Compliance**: Suitable for legally binding digital signatures worldwide
- **Audit Trail**: Complete signature history and document integrity verification
- **Secure Cloud Storage**: Enterprise-grade security with data encryption
- **GDPR Compliant**: Data processing complies with European privacy regulations


## Looking for Other Platforms?

- [GroupDocs.Signature for .NET](https://github.com/groupdocs-signature/GroupDocs.Signature-for-.NET)
- [GroupDocs.Signature for Java](https://github.com/groupdocs-signature/GroupDocs.Signature-for-Java)
- [GroupDocs.Signature for Node.js](https://github.com/groupdocs-signature/GroupDocs.Signature-for-Node.js-via-Java)
- [GroupDocs.Signature for PHP](https://github.com/groupdocs-signature/GroupDocs.Signature-for-Python-via-.NET)


## 🙌 Contribute

This repository contains **examples and demos** for GroupDocs.Signature for Python. We welcome contributions and feedback! 

- [Report Issues](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-python/issues)
- Fork the repo and submit pull requests with improvements
- Help improve documentation and examples
- Share your integration experiences


## Support & Contact

- [Free Support Forum](https://forum.groupdocs.com/c/signature) - Community help
- [Paid Support](https://helpdesk.groupdocs.com/) - Priority technical support
- [Sales Inquiry](https://purchase.groupdocs.com/contact-sales) - Licensing questions
- [Documentation](https://docs.groupdocs.com/signature/python-net/) - Complete guides

<!--
SEO Keywords:
python digital signature, python document signing, python e-signature, python pdf signature, electronic signature python, digital signature api python, sign pdf python, document signature python, python signature library, esign python, pdf signing python, python barcode signature, python qr code signature, python image signature, verify signature python, remove signature python, python signature verification, django signature, flask signature, python signature app, signature api python, python document automation, electronic signature sdk python, python signature integration
-->

## 📜 License

This project is licensed under the [GroupDocs EULA](https://purchase.groupdocs.com/policies/license).


**© 2025 GroupDocs. All rights reserved.**

*Transform your Python applications with powerful electronic signature capabilities. Start your free trial today!*