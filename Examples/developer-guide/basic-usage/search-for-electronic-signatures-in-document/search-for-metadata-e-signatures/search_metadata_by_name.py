from groupdocs.signature import Signature
from groupdocs.signature.domain import TextMatchType
from groupdocs.signature.options import MetadataSearchOptions


def search_metadata_by_name():
    with Signature("signed.pdf") as signature:
        options = MetadataSearchOptions()
        # Return only the metadata signature named "Author"
        options.name = "Author"
        options.name_match_type = TextMatchType.EXACT

        result = signature.search([options])

        print(f"Found {len(result.signatures)} matching metadata signature(s)")
        for metadata in result.signatures:
            print(f"{metadata.name} = {metadata.value}")


if __name__ == "__main__":
    search_metadata_by_name()