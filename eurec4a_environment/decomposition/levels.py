# %% IMPORTING MODULES
######################################################
import sys
import numpy as np
import pandas as pd
import xarray as xr
from tqdm import tqdm

# %% DICTIONARIES
######################################################
default_functions = {
    "near_surface": "default_function_here",
    "mixed_layer": "default_function_here",
    "cloud_layer": "default_function_here",
    "inversion": "default_function_here",
    "free_lower_troposphere": "default_function_here",
    "middle_troposphere": "default_function_here",
    "upper_troposphere": "default_function_here",
}

list_of_functions_here = []  # temporary filler till actual functions are linked

level_functions = {
    "near_surface": [list_of_functions_here],
    "mixed_layer": [list_of_functions_here],
    "cloud_layer": [list_of_functions_here],
    "inversion": [list_of_functions_here],
    "free_lower_troposphere": [list_of_functions_here],
    "middle_troposphere": [list_of_functions_here],
    "upper_troposphere": [list_of_functions_here],
}

# %% TEMPLATE FUNCTION
######################################################


def estimate_level():  # Temporary function till actual functions are linked in to default_functions dictionary
    return 700


def scalar(
    profile,
    level_name,  # e.g. "mixed_layer","near_surface"
    dim="height",  # Could also be "pressure"
    level_definition="default",  # preferred definition of the level (default value provided for all level_names)
    cell_type="bin",  # bin or point
    upper=50,  # in meter / Pa
    lower=50,  # in meter / Pa
    cell_method="mean",
    drop_na=True,
):
    """
    Function takes a profile(s) and estimates a scalar quantity based on the specified level and method.
    User can specify by which definition they want the level to be calculated. Ideally, the profile is provided
    as a DataArray with altitude as dimension. 
    """

    level_value = estimate_level()

    try:
        default_functions[level_name]
    except KeyError as err:
        print(
            f"{err} : This level is not currently included. Do you want to use custom_level instead?"
        )
        return

    try:
        default_functions[level_name]
    except KeyError as err:
        print(
            f"{err} : This level is not currently included. Do you want to use custom_level instead?"
        )
        return

    if drop_na is True:
        cell_method = "nan" + cell_method

    method = getattr(np, cell_method)

    if cell_type == "bin":
        scalar = method(profile.sel(height=slice(lower, upper)))
    elif cell_type == "point":
        scalar = method(profile.sel(height=level))

    return scalar


# %%
