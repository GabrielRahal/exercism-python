EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    if EXPECTED_BAKE_TIME > elapsed_bake_time:
        return EXPECTED_BAKE_TIME - elapsed_bake_time
    else:
        return 0


def preparation_time_in_minutes(number_of_layers):
    """
    :param number_of_layers: int - number of layers added to the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers added to the lasagna as an argument
    and returns how many minutes it will take to prepare the lasagna based on
    the 'PREPARATION_TIME' constant.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) derived from preparation and baking times.

    Function that takes the number of layers added to the lasagna and the baking
    time already elapsed as arguments, and returns the total elapsed time based on
    the preparation and baking times.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
