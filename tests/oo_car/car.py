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

    def __repr__(self, **kwargs):
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
    
    def __eq__(self, other_car:object) -> bool:
        """
        Return True if and only if the two Car classes
        are identical, doesn't compare private variables.
        """
        if self.color != other_car.color:
            return False
        if self.speed != other_car.speed:
            return False
        if self.steer_angle != other_car.steer_angle:
            return False
        return True
