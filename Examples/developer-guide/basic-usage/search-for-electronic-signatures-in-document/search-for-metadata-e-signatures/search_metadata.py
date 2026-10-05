from groupdocs.signature import Signature
from groupdocs.signature.options import MetadataSearchOptions


def search_metadata():
    with Signature("signed.pdf") as signature:
        result = signature.search([MetadataSearchOptions()])

        print(f"Found {len(result.signatures)} metadata signature(s)")
        for metadata in result.signatures:
            print(f"{metadata.name} = {metadata.value} ({metadata.type.name})")


if __name__ == "__main__":
    search_metadata()