from src.unit_test_generator import unit_test_generator_decorator,\
                                generate_all_tests_and_metadata
from pathlib import Path
import logging
from src import unit_test_generator

fmt_str = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=fmt_str)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

@unit_test_generator_decorator
def get_item_at_index(iterable, index: int):
    """
    Used to test unit_test_generator_decorator with
    string, tuple, list, and int arguments.

    """
    if not iterable:
        raise ValueError(f"iterable cannot be empty!")
    if index >= len(iterable):
        raise ValueError(f"index must be in range [0, {len(iterable)-1}], was {index}")
    elif  index < 0:
        raise ValueError(f"index must be in range [0, {len(iterable)-1}], was {index}")

    return iterable[index]

@unit_test_generator_decorator
def get_key_to_set_with_highest_value(dictionary:dict):
    """
    Used to test unit_test_generator_decorator with
    dictionary and set arguments.

    Given a dictionary mapping arbitary numeric keys to
    sets of numbers, return the key to the set with the
    overall highest value.  In case of ties, return the
    lowest key.
    """
    # Sort the keys so lowest key is kept in case of ties
    # The linear search will therefore use '>', not '>=
    keys = sorted(list(dictionary.keys()))
    # Take the first key, max(set) pair as the initial best value
    best_key = keys[0]
    highest_value = max(dictionary[keys[0]])
    # Now conduct linear search over the rest of the dictionary
    # Skip the first key since we started with that one
    for this_key in keys[1:]:
        this_highest_value = max(dictionary[this_key])
        if this_highest_value > highest_value:
            best_key = this_key
            highest_value = this_highest_value
    return best_key

def main():
    # Begin ad hoc tests
    # Test get_item_at_index
    iterables = [
                    "The quick red fox jumped over the lazy brown dog",
                    tuple([x for x in range(5,15)]),
                    [-1,-2,-3,-4],
                    "a test string",
                    #set([])
                ]
    indices = [3,50,3,-5,3]
    for iterable, index in zip(iterables, indices):
        logger.info(f"{index=} {iterable=}")
        try:
            logger.info(f"{get_item_at_index(iterable, index)=}")
        except Exception as e:
            logger.error(e)

    my_dict = {
        10: set([90, 95, 100]),
        3: set([20, 40, 80]),
        -1: set([x*x for x in range(10)]),
    }

    logger.info(f"{get_key_to_set_with_highest_value(my_dict)=}")

    """
    The generate_all_tests_and_metadata() function takes 2 Paths:
    1. The output directory for the unit tests (.py)
    2. The output directory for the .json files (I/O for each test)
    """
    generate_all_tests_and_metadata(Path('.'), Path('.'))

if __name__ == "__main__":
    main()
