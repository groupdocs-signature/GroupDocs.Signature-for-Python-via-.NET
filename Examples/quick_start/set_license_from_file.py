import os
import groupdocs.signature as gs
import helpers.utils as utils


def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Quick Start] # SetLicenseFromFile : Set license from file\n")
    
    # Replace with your actual license file path
    license_path = utils.license_path
    print(license_path)       

    
    if os.path.exists(license_path):
        license = gs.License()
        license.set_license(license_path)

        print("License set successfully.")
    else:
        print("\nWe do not ship any license with this example. "
              "\nVisit the GroupDocs site to obtain either a temporary or permanent license. "
              "\nLearn more about licensing at https://purchase.groupdocs.com/faqs/licensing."
              "\nLearn how to request a temporary license at https://purchase.groupdocs.com/temporary-license.")

if __name__ == "__main__":
    run()