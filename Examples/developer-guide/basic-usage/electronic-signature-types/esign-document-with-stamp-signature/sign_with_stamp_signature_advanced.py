from groupdocs.signature import Signature
from groupdocs.signature.options import StampSignOptions
from groupdocs.signature.domain import StampLine, StampTextRepeatType, StampTypes
from groupdocs.pydrawing import Color


def create_stamp_line(text, font_size, height, text_color):
    line = StampLine()
    line.text = text
    line.font.size = font_size
    line.font.bold = True
    line.height = height
    line.text_color = text_color
    return line


def sign_with_stamp_signature_advanced():
    with Signature("sample.docx") as signature:
        options = StampSignOptions()

        # Set stamp position, size and type
        options.left = 340
        options.top = 480
        options.width = 220
        options.height = 160
        options.stamp_type = StampTypes.SQUARE

        # Two outer lines: frames of repeated text around the stamp
        for text, font_size, height in ((" APPROVED *", 11, 22), (" 2026 *", 9, 18)):
            line = create_stamp_line(text, font_size, height, Color.white)
            line.background_color = Color.dark_blue
            line.text_bottom_intent = 4
            line.text_repeat_type = StampTextRepeatType.FULL_TEXT_REPEAT
            options.outer_lines.append(line)

        # Two inner lines of text in the middle of the stamp
        options.inner_lines.append(create_stamp_line("John Smith", 16, 32, Color.dark_blue))
        options.inner_lines.append(create_stamp_line("CEO", 12, 24, Color.dark_blue))

        result = signature.sign("signed_stamp_advanced.docx", options)
        print(f"Signed with {len(result.succeeded)} stamp signature(s)")


if __name__ == "__main__":
    sign_with_stamp_signature_advanced()