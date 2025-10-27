import datetime
from robot.output.logger import LOGGER
from robot.result.model import Keyword as result_Keyword
from robot.running import Keyword as running_Keyword
from robot.libraries.BuiltIn import BuiltIn




class NestedLogger:

    def __init__(self, kwname=None, libname=None, status='PASS'):
        """Initialize OperationsLogger."""  # noqa:E501
        self.builtin = BuiltIn()
        self.start_time = None
        self.kwname = kwname
        self.libname = libname
        self.status = status
    
    def __enter__(self):
        """Enter context manager - start keyword if configured."""
        if self.kwname and self.libname:
            self.start_keyword(self.kwname, self.libname, self.status)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager - end keyword if configured."""
        if self.kwname and self.libname:
            # Set status to FAIL if an exception occurred
            final_status = 'FAIL' if exc_type else self.status
            self.end_keyword(self.kwname, self.libname, final_status)
        # Return False to propagate exceptions
        return False
        
    def start_keyword(self, kwname, libname, status='FAIL'):
        """Start keyword."""
        run_keyword = running_Keyword(name=kwname)

        keyword = result_Keyword(name=kwname, owner=libname, status=status, start_time=self.__get_time())
        LOGGER.start_keyword(run_keyword, keyword)

    def end_keyword(self, kwname, libname, status):
        """End keyword."""
        run_keyword = running_Keyword(name=kwname)
        keyword = result_Keyword(name=kwname, owner=libname, status=status, start_time=self.start_time, end_time=self.__get_time())
        LOGGER.end_keyword(run_keyword, keyword)

    @staticmethod
    def __get_time():
        """Get Time."""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")