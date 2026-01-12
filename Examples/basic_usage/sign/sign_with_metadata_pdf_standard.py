import groupdocs.signature as gs
import groupdocs.signature.options as gso
import groupdocs.signature.domain as gsd
import os
from datetime import datetime, timedelta
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_pdf

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SignWithMetadataPdfStandard : Sign PDF document with standard metadata signatures\n")

    file_name = os.path.basename(sample_pdf)
    output_directory = get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, file_name)

    with gs.Signature(sample_pdf) as signature:
        # Create metadata options
        options = gso.MetadataSignOptions()
        
        # Using standard Pdf Metadata Signatures with new values
        signatures = [
            gsd.PdfMetadataSignatures.AUTHOR.clone("Mr.Scherlock Holmes"),
            gsd.PdfMetadataSignatures.CREATE_DATE.clone(datetime.now() - timedelta(days=1)),
            gsd.PdfMetadataSignatures.METADATA_DATE.clone(datetime.now() - timedelta(days=2)),
            gsd.PdfMetadataSignatures.CREATOR_TOOL.clone("GD.Signature-Test"),
            gsd.PdfMetadataSignatures.MODIFY_DATE.clone(datetime.now() - timedelta(days=13)),
            gsd.PdfMetadataSignatures.PRODUCER.clone("GroupDocs-Producer"),
            gsd.PdfMetadataSignatures.ENTRY.clone("Signature"),
            gsd.PdfMetadataSignatures.KEYWORDS.clone("GroupDocs, Signature, Metadata, Creation Tool"),
            gsd.PdfMetadataSignatures.TITLE.clone("Metadata Example"),
            gsd.PdfMetadataSignatures.SUBJECT.clone("Metadata Test Example"),
            gsd.PdfMetadataSignatures.DESCRIPTION.clone("Metadata Test example description"),
            gsd.PdfMetadataSignatures.CREATOR.clone("GroupDocs.Signature")
        ]
        
        # Add signatures to options
        options.signatures.extend(signatures)
        
        # Sign document
        result = signature.sign(output_file_path, options)

        print(f"\nSource document signed successfully with {len(result.succeeded)} signature(s).\nFile saved at {output_file_path}.")

if __name__ == "__main__":
    run()

