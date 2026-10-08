# GroupDocs.Signature for Python via .NET - Code Examples

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-signature-python-net-banner.png)](https://releases.groupdocs.com/signature/python-net/)

[Product Page](https://products.groupdocs.com/signature/python-net/) | [Docs](https://docs.groupdocs.com/signature/python-net/) | [Demos](https://products.groupdocs.app/signature/family) | [API Reference](https://reference.groupdocs.com/signature/python-net/) | [Blog](https://blog.groupdocs.com/category/signature/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/signature) | [Temporary License](https://purchase.groupdocs.com/temporary-license)

[GroupDocs.Signature for Python via .NET](https://products.groupdocs.com/signature/python-net/) is an electronic signature API that adds, searches, verifies, updates and removes text, image, barcode, QR code, stamp, metadata, form-field and digital signatures in PDF, Word, Excel, PowerPoint, OpenDocument and image files.

## Features

- **Many Signature Types**: Text, image, barcode, QR code, stamp, metadata, form-field and digital (certificate) signatures.
- **Search, Verify, Update, Delete**: Find existing signatures, check them against criteria, move or change them, and remove them.
- **Previews**: Render document pages and individual signatures to images through your own Python callbacks.
- **Security**: Digital signatures with certificates, SHA-256 PDF signing, custom encryption for QR code and metadata signatures.
- **Popular Formats**: PDF, Word, Excel, PowerPoint, OpenDocument and image files.
- **On-Premise**: No cloud or internet connection required.

## Supported File Formats

GroupDocs.Signature for Python via .NET supports a wide range of file formats, including Word, Excel, PowerPoint, PDF, OpenDocument, Image, and many others. See the [full list of supported formats](https://docs.groupdocs.com/signature/python-net/supported-file-formats/) for details.

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.6+](https://www.python.org/downloads/) is installed on your system. The examples use f-strings, which need 3.6; the `groupdocs-signature-net` package itself supports Python 3.5 - 3.14.

2. **Get the Code**: Clone or download this repository.

   ```bash
   git clone git@github.com:groupdocs-signature/GroupDocs.Signature-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd ./GroupDocs.Signature-for-Python-via-.NET/Examples
   ```

4. **Install Package**: install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, download the platform-specific `.whl` file from the [GroupDocs Releases](https://releases.groupdocs.com/signature/python-net/) website and install it directly (adjust the filename to your platform — `win_amd64`, `manylinux*_x86_64`, `macosx_*_arm64`, `macosx_*_x86_64`):

   ```bash
   pip install ./groupdocs_signature_net-26.10.0-py3-none-win_amd64.whl
   ```

5. **Configure License (Optional)**: `run_all_examples.py` applies a license automatically when the `GROUPDOCS_LIC_PATH` environment variable holds the absolute path of your `.lic` file.

   With a license applied, examples run with the full feature set; without one, documents of more than two pages are refused, signed pages carry an evaluation line, and found signatures report masked values, so verification fails. Get a free 30-day [temporary license](https://purchase.groupdocs.com/temporary-license) for evaluation.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python ./run_all_examples.py
   ```

   You can also run individual examples by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script file.

## Run with Docker

The repository ships a `Dockerfile` that builds a Linux image with Python 3.13, the system packages the examples need (`libicu-dev`, `libfontconfig1`, `fontconfig`, `libgdiplus`, `ttf-mscorefonts-installer`), and the `groupdocs-signature-net` package preinstalled.

```bash
# Build the image
docker build -t signature-examples .

# Run unlicensed (evaluation mode)
docker run --rm signature-examples

# Run with a license mounted from the host
docker run --rm \
    -v /path/to/license:/lic:ro \
    -e GROUPDOCS_LIC_PATH=/lic/your-license.lic \
    signature-examples
```

On Windows with Git Bash, set `export MSYS_NO_PATHCONV=1` before `docker run` to prevent MSYS from rewriting the mounted license path.

## AI agents and LLM integration

The `groupdocs-signature-net` wheel ships a bundled `AGENTS.md` reference for AI coding assistants (Claude Code, Cursor, GitHub Copilot in agent mode, and similar). Once the package is installed, the reference is discovered automatically at `groupdocs/signature/AGENTS.md` — it covers canonical imports, quick-start usage, licensing, the API surface table, and troubleshooting.

For on-demand documentation lookups, combine the bundled `AGENTS.md` with the GroupDocs MCP server at `https://docs.groupdocs.com/mcp`. See the [AI agents and LLM integration](https://docs.groupdocs.com/signature/python-net/agents-and-llm-integration/) page for the per-tool setup snippets. When the agent itself should sign or verify documents, use the [GroupDocs.Signature MCP server](https://docs.groupdocs.com/signature/mcp/).

## Continuous integration

The `.github/workflows/` directory contains the CI matrix that runs the full example suite on every push. The matrix is reproducible locally via the `Dockerfile` above.

## More Resources

Find additional details and examples in the [GroupDocs.Signature for Python via .NET documentation](https://docs.groupdocs.com/signature/python-net/).

We also offer **GroupDocs.Signature** packages for other platforms:
* [**GroupDocs.Signature for .NET**](https://products.groupdocs.com/signature/net/)
* [**GroupDocs.Signature for Java**](https://products.groupdocs.com/signature/java/)
* [**GroupDocs.Signature for Node.js via Java**](https://products.groupdocs.com/signature/nodejs-java/)

---

[Product Page](https://products.groupdocs.com/signature/python-net/) | [Docs](https://docs.groupdocs.com/signature/python-net/) | [Demos](https://products.groupdocs.app/signature/family) | [API Reference](https://reference.groupdocs.com/signature/python-net/) | [Blog](https://blog.groupdocs.com/category/signature/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/signature) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
