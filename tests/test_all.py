import pytest
import logging
from .example_all_types.all_types import main as at_main

fmt_str = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=fmt_str)
logger = logging.getLogger(__name__)

def test_all():
    print("Punch it")
    at_main()
