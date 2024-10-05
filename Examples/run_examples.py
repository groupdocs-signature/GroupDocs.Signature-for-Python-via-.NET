from quick_start import hello_world 
from quick_start import set_license_from_file
from quick_start import set_license_from_stream
from quick_start import set_metered_license
from basic_usage.common import get_supported_file_formats
from basic_usage.document_preview import *
from basic_usage.verify import *
from basic_usage.delete import *
from basic_usage.search import *
from basic_usage.update import *
from basic_usage.sign import *


if __name__ == '__main__':
    
    ## Quick Start
    set_license_from_file.run()  
    #set_license_from_stream.run()
    #set_metered_license.run()
    hello_world.run()

    ### Basic Usage
    
    ## Common 
    get_supported_file_formats.run()  

    ## Sign
    sign_with_text.run() 
    sign_with_stamp.run()
    sign_with_stamp.run() 
    sign_with_qrcode.run() 
    sign_with_multiple_options.run() 
    sign_with_image.run() 
    sign_with_digital.run() 
    sign_with_barcode.run() 
    sign_pdf_with_form_field.run()

    ## Signature verify
    verify_text.run()
    verify_barcode.run()
    verify_digital.run()
    verify_qrcode.run()
    verify_with_multiple_options.run()


    ## Signature preview
    get_document_info.run()
    get_document_process_history.run()
    
    ## Signature delete
    delete_text.run()
    delete_barcode.run()
    delete_by_type.run()
    delete_image.run() 
    delete_qrcode.run()

    ## Signature search
    search_for_text.run()

    ## Signature update
    update_qrcode.run()
    update_barcode.run()
    update_image.run()
