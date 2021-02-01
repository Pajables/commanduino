from . import CommandDevice

class CommandLinearAccelStepper(CommandDevice):
    def __init__(self, speed: int, max_speed: int, acceleration: int, homing_speed: int,
                 enabled_acceleration: bool = True, reverted_direction: bool = False, reverted_switch: bool = False): ...
    def wait_until_idle(self) -> None: ...
    def home(self, wait: bool = True) -> None: ...
    def move_to(self, steps: float, wait: bool = True) -> None: ...
    def move(self, steps: float, wait: bool = True): ...
    def stop(self, wait: bool = True) -> None: ...

    # Acceleration
    def get_acceleration(self) -> float: ...
    def set_acceleration(self, steps_per_second_per_second: float) -> None: ...

    # Current position
    def get_current_position(self) -> float: ...
    def set_current_position(self, steps: float) -> None: ...

    # Distance to go
    def get_distance_to_go(self) -> float: ...

    # Enabled acceleration
    enabled_acceleration: bool
    def enable_acceleration(self) -> None: ...
    def disable_acceleration(self) -> None: ...

    # Moving state
    @property
    def is_moving(self) -> bool: ...
    def get_moving_state(self) -> bool: ...

    # Max speed
    def get_max_speed(self) -> float: ...
    def set_max_speed(self, steps_per_second: float) -> None: ...

    # Speed
    # Ok so this might be confusing...
    # _set_speed() sets the speed in the Arduino before actually moving the motor [e.g. in move(), move_to() or home()]
    # set_running_speed sets the value of the running_speed variable, used for set_speed before normal movements
    # set_homing_speed sets the value of the homing_speed variable, used for set_speed before homing movements in home()
    def get_speed(self) -> float: ...
    def _set_speed(self, steps_per_second: float) -> None: ...

    # Running speed
    def set_running_speed(self, steps_per_second: int) -> None: ...

    # Homing speed
    def set_homing_speed(self, steps_per_second: int) -> None: ...

    # Homing switch state
    def get_switch_state(self) -> bool: ...
    """ True means the linear actuator is in home position """

    # Target position
    def get_target_position(self) -> float: ...