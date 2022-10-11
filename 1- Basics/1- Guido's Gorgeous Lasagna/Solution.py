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
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    
    if remaining_bake_time >= 0:
        return remaining_bake_time
    return "Lasagna is overcooked!"

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers for the lasagna.
    :return: int - preparation_total (in minutes) derived from 'number_of_layers'.

    Function that takes the 'number_of_layers' and the 'PREPARATION_TIME' for lasagna and returns
    how many minutes the lasagna needs to be prepared.
    """
    
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param1 number_of_layers: int - number of layers for the lasagna.
    :param2 elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time for the whole process (preparation + bake).

    Function that takes the 'elapsed_bake_time' and 'preparation_total' and returns the total
    elapsed cooking time (preparation + bake) in minutes.
    """
    
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
  
