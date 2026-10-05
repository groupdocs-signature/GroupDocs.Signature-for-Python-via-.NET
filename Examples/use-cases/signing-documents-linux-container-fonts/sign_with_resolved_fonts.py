from groupdocs.signature import GroupDocsSignatureException, Signature
from groupdocs.signature.domain import SignatureFont
from groupdocs.signature.options import TextSignOptions

LATIN_TEXT = "John Smith"
CJK_TEXT = "山田太郎"
LATIN_CANDIDATES = ["Arial", "Times New Roman", "DejaVu Sans", "Liberation Sans"]
CJK_CANDIDATES = ["Noto Sans CJK JP", "Noto Sans CJK SC", "MS Gothic", "SimSun", "Microsoft YaHei", "Malgun Gothic"]


def build_text_options(text, family_name, top):
    options = TextSignOptions(text)
    options.left = 100
    options.top = top
    options.width = 200
    options.height = 40
    font = SignatureFont()
    font.family_name = family_name
    font.size = 14
    options.font = font
    return options


def try_family(source_path, family_name):
    try:
        with Signature(source_path) as signature:
            signature.sign("font_probe.pdf", [build_text_options("probe", family_name, 10)])
        return None
    except GroupDocsSignatureException as error:
        return str(error).splitlines()[0]


def resolve_family(source_path, candidates):
    for candidate in candidates:
        if try_family(source_path, candidate) is None:
            return candidate
    return None


def sign_with_resolved_fonts():
    latin_family = resolve_family("sample.pdf", LATIN_CANDIDATES)
    cjk_family = resolve_family("sample.pdf", CJK_CANDIDATES)
    print(f"Latin family: {latin_family}, CJK family: {cjk_family}")
    if latin_family is None:
        print("No usable Latin font: install the Microsoft core fonts")
        return
    with Signature("sample.pdf") as signature:
        options = [build_text_options(LATIN_TEXT, latin_family, 500)]
        if cjk_family:
            options.append(build_text_options(CJK_TEXT, cjk_family, 560))
        result = signature.sign("signed_fonts.pdf", options)
        print(f"Signatures added: {len(result.succeeded)}")


if __name__ == "__main__":
    sign_with_resolved_fonts()