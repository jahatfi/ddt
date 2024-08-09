"""See accompanying repo for full code"""
from dataclasses import field
from dataclasses import dataclass
from typing import Any

@dataclass
# pylint: disable-next=too-many-instance-attributes
class CoverageInfo:
    """
    Holds all data gathered from single recording
    of a function or class method execution
    """
    args_before: list[str] = field(default_factory=list)
    args_after: dict[str, Any] = field(default_factory=dict)
    kwargs: dict[str, Any] = field(default_factory=dict)
    globals_before: dict[str, Any] = field(default_factory=dict)
    globals_after: dict[str, Any] = field(default_factory=dict)
    expected_result: str  = ""
    expected_type: str = ""
    coverage: list[int] = field(default_factory=list)
    exception_type: str = ""
    exception_message: str = ""
    constructor: str = ""
    cost:float = 0.0