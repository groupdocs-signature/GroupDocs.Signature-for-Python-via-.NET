from groupdocs.signature import Metered


def set_metered_license():
    public_key = "*****"  # Your public key
    private_key = "*****"  # Your private key

    # Skip the call while the placeholder keys are still in place
    if "*" in public_key or "*" in private_key:
        print("Provide your real metered keys to activate metered licensing.")
        return

    # Activate metered (pay-as-you-go) billing for this process
    Metered().set_metered_key(public_key, private_key)
    print("Metered license set successfully.")

    # ... process your documents here ...

    print(f"MB processed: {Metered.get_consumption_quantity()}")
    print(f"Credits used: {Metered.get_consumption_credit()}")


if __name__ == "__main__":
    set_metered_license()