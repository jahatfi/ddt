"""See accompanying repo for full code"""
from pathlib import Path
from typing import Optional, List

class FunctionMetaData(Jsonable):
    """
    Class to track metadata when testing 
    functions and methods
    
    "Jsonable" is another class defined elsewhere 
    that permits easy creation of the string 
    representation of any class.
    """
    # pylint: disable-next=too-many-arguments
    def __init__(   
        self,
        name:str,
        parameter_names:List[str],
        is_method:bool,
        source_file:Path,
        lines:Optional[List[int]] = None,
        non_code_lines:Optional[List[int]] = None,
        global_vars_read_from:Optional[set] = None,
        global_vars_written_to:Optional[set] = None,
        coverage_io:Optional[dict[str, CoverageInfo]] = None,
        coverage_percentage:float=0.0,
        types_in_use:Optional[set] = None,
        unified_test_coverage:Optional[set] = None,
        needs_pytest:bool = False,
        exceptions_raised:Optional[set] = None,
        callable_files: Optional[dict[str, str]] = None
        ):
        pass
        # See accompanying repo for full code