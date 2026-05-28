from points_decorator import points
import os
import pandas as pd

class TestProblem2:
    @points(1, "Problem 2, Part 2: Variable 'selected' has incorrect length or columns!")
    def test_problem_2_part_2_length(self, problem2):
        section_data, namespace = problem2
        #section_data = problem1[0]

        # Check if section exists in the dictionary
        #assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        #variables = section_data[section]['variables']

        # Ensure 'data' is a DataFrame
        #assert isinstance(namespace['data'], pd.DataFrame)

        # Select from the data columns USAF, YR--MODAHRMN, TEMP, MAX, MIN and assign them into a new variable called selected
        # Select from the data columns USAF, YR--MODAHRMN, TEMP, MAX, MIN and assign them into a new variable called selected
        selected = namespace['selected']
        assert all(col in selected.columns for col in ['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN'])

        # Check the length of 'selected'
        assert len(selected) == 11691

        # Ensure 'data' is a DataFrame
        assert isinstance(selected, pd.DataFrame)

    @points(0.5, "Problem 2, Part 3: First value of 'celsius' is not correctly converted!")
    def test_problem_2_part_3_conversion(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        #variables = section_data[section]['variables']
        selected = namespace['selected']

        # Check the first value of 'Celsius'
        assert(selected.loc[0, "Celsius"]) == -1

    @points(0.25, "Problem 2, Part 3: Did you round the celsius values to 0 decimal places?")
    def test_problem_2_part_3_round(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        #variables = section_data[section]['variables']
        selected = namespace['selected']

        # Check the mean of 'Celsius' rounded to 3 decimal places
        assert(round(selected["Celsius"].mean(), 3)) == 11.245

    @points(0.25, "Problem 2, Part 3: Column 'Celsius' should be of type int!")
    def test_problem_1_part_3_int(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        #variables = section_data[section]['variables']
        selected = namespace['selected']

        # Check the dtype of 'Celsius'
        assert(selected['Celsius'].dtype) == 'int32' or selected['Celsius'].dtype == 'int64'

    @points(1, "Problem 2, Part 4: Did you divide 'selected' into two separate DataFrames?")
    def test_problem_2_part_4(self, problem2):
        section_data, namespace = problem2
        section = "Part 4"  # Define the section key
        # Check if section exists in the dictionary
        #assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        #variables = section_data[section]['variables']

        # Check the lengths of 'kumpula' and 'rovaniemi'
        assert len(namespace['kumpula']) == 2924
        assert len(namespace['rovaniemi']) == 8767

    @points(1, "Problem 2, Part 5: Did you save the dataframes 'kumpula' and 'rovaniemi' into separate dataframes?")
    def test_problem_2_part_5(self, problem2):
        section_data, namespace = problem2
        section = "Part 5"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        #variables = section_data[section]['variables']

        # Check if the CSV files exist
        assert os.path.exists('Kumpula_temps_May_Aug_2017.csv')
        assert os.path.exists('Rovaniemi_temps_May_Aug_2017.csv')

            

        