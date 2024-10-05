# set_metered_license.py
# This example demonstrates how to set a Metered license.
# Learn more about Metered license at https://purchase.groupdocs.com/faqs/licensing/metered.

import groupdocs.signature as gs

def run():
    public_key = "*****"  # Your public key
    private_key = "*****"  # Your private key

    gs.Metered().set_metered_key(public_key, private_key)

    print("License set successfully.")

if __name__ == "__main__":
    run()
