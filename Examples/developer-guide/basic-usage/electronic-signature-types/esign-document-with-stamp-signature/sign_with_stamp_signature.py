from groupdocs.signature import Signature
from groupdocs.signature.options import StampSignOptions
from groupdocs.signature.domain import StampLine
from groupdocs.pydrawing import Color


def sign_with_stamp_signature():
    with Signature("sample.docx") as signature:
        # Create stamp signature options
        options = StampSignOptions()

        # Set stamp position and size
        options.left = 380
        options.top = 520
        options.width = 160
        options.height = 160

        # Outer line: a ring of text around the stamp
        outer_line = StampLine()
        outer_line.text = " * European Union * European Union  * European Union  *"
        outer_line.font.size = 12
        outer_line.height = 22
        outer_line.text_bottom_intent = 6
        outer_line.text_color = Color.white_smoke
        outer_line.background_color = Color.dark_slate_blue
        options.outer_lines.append(outer_line)

        # Inner line: a horizontal line of text inside the ring
        inner_line = StampLine()
        inner_line.text = "John"
        inner_line.text_color = Color.medium_violet_red
        inner_line.font.size = 20
        inner_line.font.bold = True
        inner_line.height = 40
        options.inner_lines.append(inner_line)

        # Sign the document and save the result
        result = signature.sign("signed_stamp.docx", options)
        print(f"Signed with {len(result.succeeded)} stamp signature(s)")


if __name__ == "__main__":
    sign_with_stamp_signature()