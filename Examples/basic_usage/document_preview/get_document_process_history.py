from groupdocs.signature import Signature
import os
from helpers.utils import get_output_directory_path
from helpers.test_files import sample_history_docx

def run():
    """
    Get document process history information
    """
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # GetDocumentProcessHistory : Get document process history\n")

    # The path to the documents directory.
    file_path = sample_history_docx

    with Signature(file_path) as signature:
        # Get document info including process logs
        document_info = signature.get_document_info()

        # Display document process history information
        print(f"Document Process logs information: count = {len(document_info.process_logs)}")
        for process_log in document_info.process_logs:
            print(f" - operation [{process_log.type}] on {process_log.date.strftime('%Y-%m-%d')}. "
                  f"Succeeded/Failed {process_log.succeeded}/{process_log.failed}. "
                  f"Message: {process_log.message}")

# Call the function
if __name__ == "__main__":
    run()
