from points_decorator import points
import os
import pandas as pd

class TestProblem3:
    @points(0, "Problem 3, Part 1: Dataframes 'kumpula' and 'rovaniemi' are not correctly defined!")
    def test_problem_3_part_1_length(self, problem3):
        section_data, namespace = problem3

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        assert isinstance(variables['kumpula'], pd.DataFrame)
        assert isinstance(variables['rovaniemi'], pd.DataFrame)

    @points(1, "Problem 3, Part 3: Variable 'kumpula_median' or 'rovaniemi_median' is not correctly defined!")
    def test_problem_3_part_2_columns(self, problem3):
        section_data, namespace = problem3
        section = "Part 2"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        assert variables['kumpula_median'] == 14.0
        assert variables['rovaniemi_median'] == 11.0

    @points(2, "Problem 3, Part 3: Variables 'kumpula_may' !")
    def test_problem_1_part_3_median(self, problem3):
        section_data, namespace = problem3
        section = "Part 3"
        assert section in section_data, f"Section '{section}' not found in section_data"
        variables = section_data[section]['variables']

        assert len(variables['kumpula_may']) == 741
        assert len(variables['kumpula_june']) == 714
                            
        assert len(variables['rovaniemi_may']) == 2220
        assert len(variables['rovaniemi_june']) == 2127
                            
    @points(1, "Problem 3, Part 4: Print statement not found in source code!")
    def test_problem_1_part_4_may(self, problem3):
        section_data, namespace = problem3
        section = "Part 4"
        assert section in section_data, f"Section '{section}' not found in section_data"
        source = section_data[section]['source']
        assert 'print(' in source


