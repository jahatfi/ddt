"""
Object-oriented test sample
"""

import argparse
import logging
import os
from pathlib import Path

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

class Car:
    """
    A simple class with basic methods for testing the
    unit_test_generator_decorator on class methods.
    """
    MAX_ANGLE = 720
    MIN_ANGLE = -720
    def __init__(   self,
                    color:str="black",# pylint: disable= used-before-assignment
                    speed:float=0.0,
                    steer_angle:int=0):
        """
        Create a new Car class with car color,
        initial speed and steering angle
        """
        self.color = color
        self.speed = speed
        self.steer_angle = steer_angle

    def brake(self, rate:float, duration:int=1)-> float:
        """
        Apply the brake pedal at some negative "rate"
        (e.g. -N m/s for "duration" seconds)
        """
        logger.debug("rate=%.2f duration=%d", rate, duration)
        if rate > 0:
            raise ValueError("Brake rate (m/s) must be negative.")
        if duration < 0:
            raise ValueError("Duration (s) must be positive.")
        self.speed = max(0.0, self.speed+rate*duration)
        return self.speed

    def gas(self,
            rate:float,
            duration:int=1):
        """
        Apply the gas pedal at some positive "rate"
        (e.g. +N m/s for "duration" seconds)
        """
        global method_call_counter # pylint: disable=global-statement
        method_call_counter +=1
        logger.debug("rate=%.2f duration=%d", rate, duration)
        if rate < 0:
            raise ValueError("Gas rate (m/s) must be positive.")
        self.speed = max(0.0, self.speed+rate*duration)
        return self.speed

    def change_steer_angle(self, angle:int):
        """
        Add this new steer angle (could be a negative value)
        to the current steer angle, and clamp to restrict
        within the valid range.
        """
        logger.debug("angle=%d", angle)
        if angle > self.MAX_ANGLE or angle < self.MIN_ANGLE:
            raise AssertionError(f"{angle=:<8} out of bounds!")

        self.steer_angle += angle
        # Simple clamp from Sven Marnach
        # https://stackoverflow.com/questions/9775731
        self.steer_angle =  max(min(self.steer_angle,
                                    self.MAX_ANGLE),
                                self.MIN_ANGLE
                                )
        return self.steer_angle


    def str(self) -> str:
        """
        Return a string representation of this Car object
        Create string in a list and join it to keep the
        line lengths short.
        """
        result = [
            f"\'{self.color} car: {self.speed} m/s; ",
            f"steer angle = {self.steer_angle} degrees\'"
        ]
        return ''.join(result)

    def __repr__(self):
        """
        Return this objective as a valid Python string that can
        be used to recreate this object.
        """
        return f"Car(\"{self.color}\", {self.speed}, {self.steer_angle})"

    def repr(self):
        """
        Simply call the magic __repr__ method
        """
        return self.__repr__() # pylint: disable=unnecessary-dunder-call


    def is_going_faster_than(self, other_car):
        """
        Return True if this car (self) has a higher value
        in its "speed" property compared to other_car.speed;
        else return False.
        """
        return self.speed > other_car.speed
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
        if file.suffix in (".py", ".json") and file.absolute() != this_file:
            logger.debug("%s != %s", file.absolute().name, this_file.name)
            logger.debug("Deleting %s to ensure clean start", file.name)
            os.remove(file)

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
    main()
