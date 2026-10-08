<!-- generator:skip -->
# GroupDocs.Signature for Python via .NET -- AGENTS.md

> Instructions for AI agents working with this package.

Add, search, verify, update and delete text, image, digital, barcode, QR code, stamp, form-field and metadata signatures in PDF, Word, Excel, PowerPoint, OpenDocument and image files (40+ formats).

## Install

```bash
pip install groupdocs-signature-net
```

**Python**: 3.5 - 3.14 (pip 20.3+) | **Platforms**: Windows x64, Linux x64 (glibc 2.27+), macOS 12+ (x64, ARM64)

## Resources

| Resource | URL |
|---|---|
| Documentation | https://docs.groupdocs.com/signature/python-net/ |
| LLM-optimized docs | https://docs.groupdocs.com/signature/python-net/llms-full.txt |
| API reference | https://reference.groupdocs.com/signature/python-net/ |
| Code examples | https://docs.groupdocs.com/signature/python-net/developer-guide/ |
| Release notes | https://releases.groupdocs.com/signature/python-net/release-notes/ |
| PyPI | https://pypi.org/project/groupdocs-signature-net/ |
| Free support forum | https://forum.groupdocs.com/c/signature/ |
| Temporary license | https://purchase.groupdocs.com/temporary-license |

## MCP Server

If your environment has MCP configured, you can connect your AI tool to the GroupDocs documentation server for on-demand API lookups:

```json
{
  "mcpServers": {
    "groupdocs-docs": {
      "url": "https://docs.groupdocs.com/mcp"
    }
  }
}
```

Works with Claude Code (`~/.claude/settings.json`), Cursor (`.cursor/mcp.json`), VS Code Copilot (`.vscode/mcp.json`), and any MCP-compatible client. If MCP is unavailable, fall back to the LLM-optimized docs URL above and this file -- both are shipped inside the wheel.

## Imports

```python
from groupdocs.signature import License, ProcessEventArgs, ProcessCompleteEventArgs, ProcessCompleteEventHandler, ProcessProgressEventArgs, ProcessProgressEventHandler, ProcessStartEventArgs, ProcessStartEventHandler, Signature, SignatureSettings, GroupDocsSignatureException
from groupdocs.signature.domain import Background, BaseSignature, BarcodeSignature, BarcodeType, BarcodeTypes, ...
from groupdocs.signature.logging import ConsoleLogger, FileLogger, LogLevel
from groupdocs.signature.options import SearchOptions, BarcodeSearchOptions, SignOptions, TextSignOptions, BarcodeSignOptions, ...
```

## Text Signature

```python
from groupdocs.signature import Signature
from groupdocs.signature.options import TextSignOptions

with Signature("document.pdf") as signature:
    options = TextSignOptions("Approved")
    options.left = 100
    options.top = 100
    signature.sign("signed.pdf", options)
```

## Callbacks: pass Python functions and objects

Wherever the engine takes a callback type, pass plain Python. The shapes are the .NET signatures in `snake_case`:

| .NET type | Pass |
|---|---|
| `PreviewOptions.CreateDocPageStream` / `ReleaseDocPageStream` | `create(page_data) -> stream`, `release(page_data, stream)` |
| `CreateSignatureStream` / `ReleaseSignatureStream` | `create(preview_options) -> stream`, `release(preview_options, stream)` |
| `ILogger` (`SignatureSettings(logger)`) | an object with `trace(message)`, `warning(message)`, `error(message, exception)` -- or a function `fn(level, message, exception)` |
| `IDataEncryption` (`data_encryption` on QR/metadata options) | an object with `encode(source) -> str` and `decode(source) -> str` |
| `ICustomSignHash` (`DigitalSignOptions.custom_sign_hash`) | a function `fn(signable_hash, hash_algorithm, signature_context) -> bytes`, or an object with that `custom_sign_hash` method |

- `signable_hash` is already the digest, computed with `hash_algorithm` (SHA-256 unless set otherwise). Sign it as it is, e.g. `key.sign(signable_hash, padding.PKCS1v15(), Prehashed(hashes.SHA256()))` with `cryptography`. Hashing it again gives a signature that does not verify.
- A create callback returns a writable file object (`open(path, "wb")`), an `io.BytesIO`, or a .NET `Stream`.
- The release callback gets back **the same object** create returned. The bytes are already complete by then: a file is closed and a `BytesIO` is filled.
- A `release` taking one argument (`release(page_data)`) is accepted too.
- An exception raised in a callback reaches your code with its own type, so `except ValueError` works.
- Failures in release and logger callbacks are ignored, so cleanup and logging cannot break signing.

```python
import io
from groupdocs.signature import Signature
from groupdocs.signature.options import PreviewOptions

def create_page_stream(page_data):
    return open("page-%d.png" % page_data.page_number, "wb")

def release_page_stream(page_data, page_stream):
    page_stream.close()

with Signature("document.pdf") as signature:
    options = PreviewOptions(create_page_stream, release_page_stream)
    options.preview_format = PreviewOptions.PreviewFormats.PNG
    signature.generate_preview(options)
```

```python
import base64
from groupdocs.signature.options import QrCodeSignOptions

class Base64Encryption:                  # any object with encode/decode
    def encode(self, source):
        return base64.b64encode(source.encode()).decode()
    def decode(self, source):
        return base64.b64decode(source).decode()

options = QrCodeSignOptions("Private text")
options.data_encryption = Base64Encryption()   # search with the same object to decode
```

## Upgrading from 26.1

26.1 was built by an earlier toolchain. The modules are the same, but some details changed:

| 26.1 | 26.10 |
|---|---|
| `options.z_order` (all sign options) | `options.zorder` |
| `x_ad_es_type` (`DigitalSignOptions`, `DigitalSignature`, `PdfDigitalSignature`) | `xad_es_type` |
| `PdfTextAnnotationAppearance.h_corner_radius` / `v_corner_radius` | `hcorner_radius` / `vcorner_radius` |
| `BarcodeTypes.GS1_CODE_128`, `DATA_LOGIC_2OF_5`, `IATA2OF_5`, `INTERLEAVED_2OF_5`, `MATRIX_2OF_5`, `STANDARD_2OF_5`, `GS1_MICRO_PDF_417`, `UPCA_GS_1_CODE_128_COUPON`, `UPCA_GS_1_DATABAR_COUPON` | `GS1_CODE128`, `DATA_LOGIC_2OF5`, `IATA2OF5`, `INTERLEAVED_2OF5`, `MATRIX_2OF5`, `STANDARD_2OF5`, `GS1_MICRO_PDF417`, `UPCA_GS1_CODE_128_COUPON`, `UPCA_GS1_DATABAR_COUPON` |
| `FileType.G_ZIP`, `L_ZIP` | `FileType.GZIP`, `LZIP` |
| engine errors: `RuntimeError("Proxy error(GroupDocsSignatureException): ...")` | `GroupDocsSignatureException`, `IncorrectPasswordException`, `PasswordRequiredException` (import from `groupdocs.signature`); they do **not** derive from `RuntimeError` |

- **Assigning an attribute a class does not have raises `AttributeError`** ("... Did you mean: 'zorder'?"). In 26.1 a misspelled or renamed property was assigned silently and had no effect.
- `search(options)` with one options object returns a plain list of signatures; `search([options])` returns a `SearchResult` with `.signatures`.
- Preview page numbers are 0-based: `page_data.page_number` is 0 for the first page, and `PreviewOptions(..., page_numbers=[0])` previews it. So is `get_document_info().pages[i].page_number`. Sign options (`page_number = 1`) and search results (`signature.page_number`) count from 1.
- The licence in `GROUPDOCS_LIC_PATH` is applied at import; 26.1 ignored the variable.

## Security defaults (engine 26.9)

- **Expired or not-yet-valid certificates are rejected.** Signing raises `GroupDocsSignatureException` unless `DigitalSignOptions.allow_expired` / `allow_not_yet_valid` is set; validity is checked against the current UTC time.
- **External resources are not loaded.** `LoadOptions.skip_external_resources` defaults to `True`; list trusted addresses in `LoadOptions.whitelisted_resources`. `load_external_resources` is obsolete and means the opposite.
- **PDF signatures use SHA-256** unless `DigitalSignOptions.hash_algorithm` says otherwise, and `verify` now checks PDF signatures cryptographically.

## Licensing

```python
from groupdocs.signature import License

# From file
License().set_license("path/to/license.lic")

# From stream
with open("license.lic", "rb") as f:
    License().set_license(f)
```

Or auto-apply: `export GROUPDOCS_LIC_PATH="path/to/license.lic"`

**Evaluation vs licensed** (measured on engine 26.9). Without a license:

- **Documents of more than 2 pages are refused.** Every operation (`sign`, `search`, `verify`, `generate_preview`, `get_document_info`) raises `GroupDocsSignatureException`: "The number of pages cannot exceed 2 in a trial version".
- **Signed pages carry an evaluation line**: "Created with evaluation version of GroupDocs.Signature".
- **Search results are masked.** A text signature's `text` is replaced by the evaluation notice, and barcode and QR code values keep their first 6 characters followed by an evaluation notice.
- **Verification fails as a result**: text, barcode and QR code `verify` returns `is_valid == False` even for a correctly signed document.

Set `GROUPDOCS_LIC_PATH` (or call `License().set_license(...)`) and re-run to lift all of these. A 30-day full license is free: https://purchase.groupdocs.com/temporary-license

**A bad licence fails silently.** `set_license` raises only when the file does not exist ("License file not found"); a damaged or wrong file is accepted without an error and the process stays in evaluation mode. A missing file in `GROUPDOCS_LIC_PATH` is ignored too (by design: a licence problem must not break `import`). Never infer licensing from the absence of an error: check a signed page for the evaluation line.

## API Reference

### Signature

| Method | Returns | Description |
|---|---|---|
| `__init__(document)` | | Constructor |
| `sign(document, sign_options)` | `SignResult` |  |
| `verify(verify_options)` | `VerificationResult` |  |
| `get_document_info()` | `IDocumentInfo` |  |
| `generate_preview(preview_options)` | `None` |  |
| `search(search_options_list)` | `SearchResult` |  |
| `update(signature)` | `bool` |  |
| `delete(signature)` | `bool` |  |
| `generate_signature_preview(preview_options)` | `None` | static |

## Key Patterns

- **Properties**: use `snake_case` -- auto-mapped to .NET `PascalCase`
- **Context managers**: `with Signature(...) as x:` ensures resources are released
- **Streams**: pass `open("file", "rb")` or `io.BytesIO(data)` where .NET expects Stream
- **Stream write-back**: `BytesIO` objects are updated after .NET writes to them
- **Enums**: case-insensitive, lazy-loaded (e.g., `FileType.DOCX`)
- **Collections**: `for item in result` and `len(result)` work on .NET collections
- **Lists pick the overload by their contents**: `search([TextSearchOptions(), QrCodeSearchOptions()])`, `search([SignatureType.QR_CODE, SignatureType.BARCODE])`, `delete([SignatureType.TEXT])`, `delete([signature.signature_id, ...])`, and `update(result.signatures)` / `delete(result.signatures)` straight from a search
- **Dates and decimals keep their type**: a `datetime`/`date` or `decimal.Decimal` passed as a metadata signature's value (an `object` parameter) arrives as a .NET `DateTime`/`decimal`; `WordProcessingMetadataSignature("DateCreated", datetime(...)).type` is `MetadataType.DATE_TIME`

## Platform Requirements

| Platform | Requirements |
|---|---|
| Windows x64 | None |
| Linux x64 (glibc 2.27+: Ubuntu 18.04+, Debian 10+, RHEL 8+) | `apt install libicu-dev libfontconfig1 libgdiplus ttf-mscorefonts-installer` (Debian: enable `contrib` first) |
| macOS 12+ (x64, ARM64) | `brew install mono-libgdiplus` |

What each one is for, measured on the 26.9 engine:
- **libgdiplus** -- stamp and text-as-image signatures (any format), barcode/QR/image signatures with a `border` or `transparency`, every signature on PowerPoint and image (PNG/JPG/WEBP) files, and text/stamp signature previews. Text, barcode, QR, image and digital signatures on PDF and Office documents work without it, background/rotation/colors/margins included.
- **Microsoft core fonts** -- PDF text and digital signatures, whose default fonts are Times New Roman and Arial. Metric-compatible substitutes (Liberation) are not picked up.

The wheel tags state the OS floors (`manylinux_2_27_x86_64`, `macosx_12_0_x86_64`, `macosx_12_0_arm64`), so pip 20.3+ refuses an older OS up front.

## Troubleshooting

**`The type initializer for 'Gdip' threw an exception` / `DllNotFoundException: libgdiplus` while signing** (Linux/macOS) -- install libgdiplus: `sudo apt install libgdiplus` (Linux) / `brew install mono-libgdiplus` (macOS). Only the features listed under Platform Requirements need it; `import` and the other signatures work without it

**`Font Times New Roman was not found` / `Font Arial was not found`** -- install the Microsoft core fonts: `sudo apt install ttf-mscorefonts-installer fontconfig && sudo fc-cache -f` (Debian: enable `contrib`)

**`The signing certificate expired on ...`** -- 26.9 rejects expired and not-yet-valid certificates; renew it, or set `allow_expired` / `allow_not_yet_valid` on the `DigitalSignOptions`

**`search(options)` returns a plain list** -- one search-options object binds the generic `Search<T>`; pass a list (`search([options])`) to get a `SearchResult` with `.signatures`

**`DllNotFoundException: libSkiaSharp`** -- stale system copy conflicts with bundled version. Rename it: `sudo mv /usr/local/lib/libSkiaSharp.dylib /usr/local/lib/libSkiaSharp.dylib.bak`

**The process aborts on first use with `Couldn't find a valid ICU package`** (Linux; exit code 134, no Python exception) -- install ICU: `sudo apt install libicu-dev`, and do NOT set `DOTNET_SYSTEM_GLOBALIZATION_INVARIANT`

**`TypeLoadException`** -- reinstall: `pip install --force-reinstall groupdocs-signature-net`

**Still stuck?** Post your question at https://forum.groupdocs.com/c/signature/ -- the development team responds directly.
