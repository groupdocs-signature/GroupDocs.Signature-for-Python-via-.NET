import os

FONT_EXTENSIONS = (".ttf", ".otf", ".ttc")


def font_roots():
    home = os.path.expanduser("~")
    roots = [
        "/usr/share/fonts",
        "/usr/local/share/fonts",
        os.path.join(home, ".fonts"),
        os.path.join(home, ".local", "share", "fonts"),
        "/System/Library/Fonts",
        "/Library/Fonts",
    ]
    windir = os.environ.get("WINDIR")
    if windir:
        roots.append(os.path.join(windir, "Fonts"))
    return roots


def count_font_files():
    count = 0
    for root in font_roots():
        for _, _, files in os.walk(root):
            count += sum(1 for name in files if name.lower().endswith(FONT_EXTENSIONS))
    print(f"Font files found: {count}")


if __name__ == "__main__":
    count_font_files()