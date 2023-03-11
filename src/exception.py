import sys



def error_msg_detail(error,error_detail:sys):
    _,_,error_info=error_detail.exc_info()
    file_name=error_info.tb_frame.f_code.co_filenmae
    line_number=error_info.tb_lineno
    error_name=error_info.str(error)
    error_message='error has occured in python script name [{0}] line number [{1}] error message [{2}]',format(
file_name,line_number,error_message

    )
    return error_message


#string format() function has been introduced for handling complex

class customexception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    

