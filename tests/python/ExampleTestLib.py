import ipdb.stdout
from robot.api.deco import keyword
from NestedLogger import NestedLogger

class ExampleTestLib:

    @keyword("Do Something")
    def do_something(self):
        return "Did something!"
    
    @keyword("Do Something With My Logger")
    def do_something_with_my_logger(self, *params_and_values):
        """ Fills form parameters with provided prameters and values.

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | params_and_values | Alternating parameter names and values | "Full Name"    "Artur Ziolkowski" |

        *Return*
        | String | Done |
        """
        

        my_logger = NestedLogger()

        lib_name = self.__class__.__name__
        for param, value in zip(params_and_values[::2], params_and_values[1::2]):
            kw_name =   "Do operation for {param} with value {value}".format(param=param, value=value)
            my_logger.start_keyword(kw_name, lib_name)
            
            status = 'PASS'
            error = None
            try:
                print("do your code")
                if value == 'Value3':
                    raise ValueError("Simulated error for testing")
            except Exception as e:
                status = 'FAIL'
                error = e
            finally:
                my_logger.end_keyword(kw_name, lib_name, status)
                if error:
                    raise error
        return "Done"

    @keyword("Do Something With Context Manager")
    def do_something_with_context_manager(self, *params_and_values):
        """ Fills form parameters with provided parameters and values using context manager.

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | params_and_values | Alternating parameter names and values | "Full Name"    "Artur Ziolkowski" |

        *Return*
        | String | Done |
        """
        lib_name = self.__class__.__name__
        
        for param, value in zip(params_and_values[::2], params_and_values[1::2]):
            kw_name = "Do operation for {param} with value {value}".format(param=param, value=value)
            
            # Using NestedLogger as context manager
            with NestedLogger(kw_name, lib_name, 'PASS'):
                if value == 'admin@example.com':
                    raise ValueError("Simulated error for testing")
                print(f"Processing {param} with value {value}")
                # Your code here - if exception occurs, status will be automatically set to FAIL
                
        return "Done"