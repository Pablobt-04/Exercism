"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 60
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes, multiplies number of layers by 2.

    Function that calculates the preparation time for the lasagna, considering that every          layer takes 2 minutes to prepare .
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate how long has it taken to prepare the lasagna.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - time the lasagna has been baking in the oven.
    :return: int - sum of minutes taken to prepare each layer + time baking.

    Function that calculates the total elapsed minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
