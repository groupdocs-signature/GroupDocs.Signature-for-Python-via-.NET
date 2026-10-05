from groupdocs.signature import GroupDocsSignatureException, Signature
from groupdocs.signature.domain import SignatureFont
from groupdocs.signature.options import TextSignOptions


def try_family(source_path, family_name):
    """Return None when the family can be used, otherwise the reason it cannot."""
    try:
        with Signature(source_path) as signature:
            options = TextSignOptions("probe")
            options.left = 10
            options.top = 10
            options.width = 60
            options.height = 20
            font = SignatureFont()
            font.family_name = family_name
            font.size = 10
            options.font = font
            signature.sign("font_probe.pdf", [options])
        return None
    except GroupDocsSignatureException as error:
        # The first line is the engine's message; the rest is the .NET stack trace
        return str(error).splitlines()[0]


def probe_font_family():
    for family_name in ("Times New Roman", "No Such Font"):
        reason = try_family("sample.pdf", family_name)
        print(f"{family_name}: {'usable' if reason is None else reason}")


if __name__ == "__main__":
    probe_font_family()