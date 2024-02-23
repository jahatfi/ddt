from src import unit_test_generator
from src.unit_test_generator import unit_test_generator_decorator,\
                                generate_all_tests_and_metadata
from pathlib import Path
import logging

fmt_str = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=fmt_str)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

# NOTE:
#logging.disable(logging.CRITICAL)
print("WARNING: ALL LOGGING DISABLED")

# The global below is simply so the update_global() function in
# unit_test_generator.py will be executed, without which that
# unit test will be empty and will raise an exception.
method_call_counter = 0

class Car():
    """
    A simple class with basic methods for testing the
    unit_test_generator_decorator on class methods.
    """
    MAX_ANGLE = 720
    MIN_ANGLE = -720
    def __init__(   self, color: str="black",
                    speed:int=0, steer_angle:int=0):
        """
        Create a new Car class with car color,
        initial speed and steering angle
        """
        self.color = color
        self.speed = speed
        self.steer_angle = steer_angle

    @unit_test_generator_decorator
    def brake(self, rate:float, duration:int=1):
        """
        Apply the brake pedal at some negative "rate"
        (e.g. -N m/s for "duration" seconds)
        """
        logger.debug(f"{rate=} {duration=}")
        if rate > 0:
            raise ValueError("Brake rate (m/s) must be negative.")
        if duration < 0:
            raise ValueError("Duration (s) must be positive.")
        self.speed = max(0, self.speed+rate*duration)

    @unit_test_generator_decorator
    def gas(self, rate:float, duration:int=1):
        """
        Apply the gas pedal at some positive "rate"
        (e.g. +N m/s for "duration" seconds)
        """
        global method_call_counter
        method_call_counter +=1
        logger.debug(f"{rate=:<8} {duration=:<8}")
        if rate < 0:
            raise ValueError("Gas rate (m/s) must be positive.")
        self.speed = max(0, self.speed+rate*duration)
        return self.speed

    @unit_test_generator_decorator
    def change_steer_angle(self, angle:int):
        """
        Add this new steer angle (could be a negative value)
        to the current steer angle, and clamp to restrict
        within the valid range.
        """
        logger.debug(f"{angle=}")
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
    def __str__(self) -> str:
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

    def repr(self):
        return f"Car(\"{self.color}\", {self.speed}, {self.steer_angle})"

    @unit_test_generator_decorator
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
        print(f"Car #{i}".center(80, '-'))
        car = Car(color, speed, angle)
        print(car)
        print(f"Driving {car.repr()}")
        # Note the intentional bug here for the
        # sake of demonstrating the ValueError:
        try:
            car.gas(c_speed, duration)
        except Exception as e:
            logger.error(f"gas({c_speed},{duration}) raised {type(e)}")
            logger.error(e)
        # Instead of a try/except we should do:
        '''
        if c_speed >= 0:
            car.gas(c_speed, duration)
        else:
            car.brake(c_speed, duration)
        '''
        #car.change_steer_angle(c_angle)
        try:
            ...
            car.change_steer_angle(c_angle)
        except Exception as e:
            logger.error(f"change_steer_angle({c_angle}) raised {type(e)}")
            logger.error(e)

        print(car)

def second_test():
    """
    Create two cars and determine which one is going faster
    by using the is_going_faster_than() Car method
    """
    print(f"Test 2.1".center(80, '-'))
    car_1 = Car("Red", 20, 0)
    car_2 = Car("White", 19, 0)

    if car_1.is_going_faster_than(car_2):
        print(f"{car_1} is going faster than {car_2}")
    else:
        print(f"{car_1}'s speed is less than or equal to {car_2}'s speed")

    print(f"Test 2.2".center(80, '-'))
    # The invocation below will also work,
    # demonstrating that the unit_test_generator_decorator works on both
    Car.is_going_faster_than(car_1, car_2)

def main():
    first_test()
    second_test()
    generate_all_tests_and_metadata(Path('.'), Path('.'))

if __name__ == "__main__":
    main()
