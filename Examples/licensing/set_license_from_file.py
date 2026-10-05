import os

from groupdocs.signature import License


def set_license_from_file():
    # The license file next to the script; change the name to match yours
    license_path = os.path.abspath("GroupDocs.Signature.lic")
    if os.path.exists(license_path):
        # Apply the license once, before using any other GroupDocs.Signature API
        License().set_license(license_path)
        print("License set successfully.")
    else:
        print("License file not found; running in evaluation mode.")


if __name__ == "__main__":
    set_license_from_file()