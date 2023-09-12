from src.logger import logging
import sys 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # execution info - 3rd one exc_tb so first  2 we
    file_name =  exc_tb.tb_frame.f_code.co_filename         # from documentation for custom error handling  # noqa: E501
    error_message ="error occured in script [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))  # noqa: E501
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message


