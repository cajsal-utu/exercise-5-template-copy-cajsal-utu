#!/usr/bin/env python
from points_decorator import points
import inspect
import pandas as pd
import os

class TestProblem1:
    @points(0.5, "Problem 1, Part 1: Variable 'Data' is not correctly defined!")
    def test_problem_1_part_1_fuction(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert that 'data' is a DataFrame
        assert isinstance(variables['data'], pd.DataFrame)

    @points(0.5, "Problem 1, Part 2: Variable 'Data' length, columns or dtypes incorrectly defined!")
    def test_problem_1_part_2(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert the length of 'data'
        assert len(variables['data']) == 11694

        # Assert the columns of 'data'
        assert variables['data'].columns.tolist() == [
            'USAF', 'WBAN', 'YR--MODAHRMN', 'DIR', 'SPD', 'GUS', 'CLG', 'SKC', 'L', 'M', 'H',
            'VSB', 'MW', 'MW.1', 'MW.2', 'MW.3', 'AW', 'AW.1', 'AW.2', 'AW.3', 'W', 'TEMP',
            'DEWP', 'SLP', 'ALT', 'STP', 'MAX', 'MIN', 'PCP01', 'PCP06', 'PCP24', 'PCPXX', 'SD'
        ]

        # Assert the data types of 'data'
        assert variables['data'].dtypes.tolist() == [
            'int64', 'int64', 'int64', 'float64', 'float64', 'float64', 'float64', 'object',
            'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
            'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
            'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
            'float64'
        ]

    @points(1, "Problem 1, Part 3: Variable 'temp_mean', 'temp_max_std' or 'station_count' incorrectly defined!")
    def test_problem_1_part_3(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert the value of 'temp_mean'
        assert round(variables['temp_mean'], 1) == 52.2

        # Assert the value of 'temp_max_std'
        assert round(variables['temp_max_std'], 1) == 10.3

        # Assert the value of 'station_count'
        assert variables['station_count'] == 2
