"""
Object-oriented test sample
"""

import argparse
import logging
import os
from pathlib import Path
import coverage
import sys
import time

from car import Car
from src import unit_test_generator
from src.unit_test_generator import ( 
    generate_all_tests_and_metadata,
    unit_test_generator_decorator,
)

FMT_STR = '%(levelname)-8s|%(module)-16s|%(funcName)-25s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=FMT_STR)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

# The global below is simply so the update_global() function in
# unit_test_generator.py will be executed, without which that
# unit test will be empty and will raise an exception.
method_call_counter = 0 # pylint: disable=invalid-name

def first_test():
    """
    Create a bunch of cars to test all the Car class methods
    except for is_going_faster_than()
    """
    # Create a bunch of cars in a loop for testing:
    colors = ["Red", "White", "Blue", "Green"]
    init_speeds = [10,12,14,16]
    init_angles = [0, -30, 30, 90 ]
    change_angles = [30, 90, 180, -1080]
    change_speed = [-1, 2, 3, 4]
    durations = [1,2,-3,4]
    lists = [
        colors,
        init_speeds,
        init_angles,
        change_angles,
        change_speed,
        durations
    ]
    for i, (color, speed, angle, c_angle, c_speed, duration) in enumerate(zip(*lists)):
        logger.info(f"Car #{i}".center(80, '-'))
        this_car = Car(color, speed, angle)
        if this_car is None or not this_car:
            raise ValueError("this_car is None!")

        logger.info(this_car)
        logger.info("Driving %s", {this_car.repr()})
        # Note the intentional bug here for the
        # sake of demonstrating the ValueError:
        try:
            this_car.gas(c_speed, duration)
        except ValueError as e:
            logger.error("gas(%.2f,%d) raised %s", c_speed, duration, type(e))
        # Instead of a try/except we should do:
        if c_speed >= 0:
            this_car.gas(c_speed, duration)
        else:
            this_car.brake(c_speed, duration)

        #car.change_steer_angle(c_angle)
        try:
            this_car.change_steer_angle(c_angle)
        except AssertionError as e:
            logger.error("change_steer_angle(%s) raised %s", c_angle, type(e))

        logger.info(this_car)

def second_test():
    """
    Create two cars and determine which one is going faster
    by using the is_going_faster_than() Car method
    """
    logger.info("Test 2.1".center(80, '-'))
    car_1 = Car("Red", 20, 0)
    car_2 = Car("White", 19, 0)

    if car_1.is_going_faster_than(car_2):
        logger.info("%s is going faster than %s", car_1, car_2)
    else:
        logger.info("%s's speed is less than or equal to %s's speed", car_1, car_2)

    logger.info("Test 2.2".center(80, '-'))
    # The invocation below will also work,
    # demonstrating that the unit_test_generator_decorator works on both
    Car.is_going_faster_than(car_1, car_2)

def main():
    """
    Call test functions for Car class, then generate test files for each
    method.
    """

    first_test()
    second_test()
    generate_all_tests_and_metadata(Path('.'), Path('.'))

if __name__ == "__main__":

    log_levels = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }

    # Create the parser and add argument(s)
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level',
                        "-l",
                        help='log level',
                        type=str,
                        choices=log_levels.keys(),
                        default='info')
    parser.add_argument("--disable-unit-test-generation", "-d",
                        action="store_true",
                        help="Set this flag to deactivate unit test generation for this code")
    args = parser.parse_args()
    logger.info("args=%s", args)

    this_file = Path(__file__).absolute()
    for file in this_file.parent.rglob("*"):
        if file.name == "car.py":
            continue
        if file.suffix in (".py", ".json") and file.absolute() != this_file:
            logger.debug("%s != %s", file.absolute().name, this_file.name)
            logger.debug("Deleting %s to ensure clean start", file.name)
            logger.warning(f"Removing {file=}")
            os.remove(file)
    logger.info("Sleep 1 s...")
    time.sleep(1)
    if args.disable_unit_test_generation:
        main()
        sys.exit(0)
    # The code below applies the CLI arg above to selectively enable/disable
    # automatic unit test generation (Could not use the syntactic sugar method
    # of applying decorators as the user's input isn't parsed until now.)
    # Alternatively, move the argument parsing to the very top of this file.
    # NOTE:
    # Decorating all functions programmatically is left as an exercise to the reader:
    # Hint: https://stackoverflow.com/questions/3467526/
    Car.brake = unit_test_generator_decorator(110, 100)(Car.brake)
    Car.gas = unit_test_generator_decorator(110, 100)(Car.gas)
    Car.change_steer_angle = unit_test_generator_decorator(110, 100, True)(Car.change_steer_angle)
    Car.is_going_faster_than = unit_test_generator_decorator(110, 110)(Car.is_going_faster_than)
    Car.__init__ = unit_test_generator_decorator(110, 110)(Car.__init__)

    cov = coverage.Coverage()
    with cov.collect():
        main()
    cov.save()
