from GradeAdjuster import GradeAdjuster
from datetime import datetime
import re
def generate_google_sheets_formula(input_string):
    close_parenthesis: str = ""
    # Parse input string and create a dictionary
    lines = input_string.strip().split('\n')
    due_date = lines[0].split(': ')[1]
    score_dict = {line.split(': ')[0]: float(line.split(': ')[1]) for line in lines[1:]}

    # Generate Google Sheets formula
    formula = '='
    
    # is empty
    formula += f'IF(ISBLANK(INDIRECT("RC[-1]", FALSE)), "", '
    close_parenthesis += ')'

    # Add conditions for cases when the date is lower or higher than the defined range
    min_score = min(score_dict.values())
    max_score = max(score_dict.values())
    formula += f'IF(INDIRECT("RC[-1]", FALSE) < DATEVALUE("{min(score_dict.keys())}"), {max_score}, '
    formula += f'IF(INDIRECT("RC[-1]", FALSE) > DATEVALUE("{max(score_dict.keys())}"), {min_score}, '
    close_parenthesis += "))"
    
    # add the middle values
    for line in lines[1:]:
        date, score = line.split(': ')
        formula += f'IF(TEXT(INDIRECT("RC[-1]", FALSE), "mm-dd")="{date}", {score}, '
        close_parenthesis += ")"
    formula += "\"FAILED\""

    return formula + close_parenthesis

if __name__ == "__main__":
    date_hw_labs = {
        "hw1": datetime(2024, 1, 16).date(),
        "hw2": datetime(2024, 1, 19).date(),
        "hw3": datetime(2024, 1, 27).date(),
        "hw4": datetime(2024, 2, 9).date(),
        "hw5": datetime(2024, 3, 1).date(),
        "hw6": datetime(2024, 3, 18).date(),
        "hw7": datetime(2024, 4, 5).date(),
        "hw8": datetime(2024, 4, 17).date(),
        "lab1": datetime(2024, 1, 5).date(),
        "lab2": datetime(2024, 2, 16).date(),
        "lab3": datetime(2024, 3, 12).date(),
        "lab4": datetime(2024, 3, 29).date(),
        "lab5": datetime(2024, 4, 12).date(),
    }
    # Create and open a text file for writing
    with open('output.txt', 'w') as textfile:
        # Iterate over date_hw_labs dictionary
        for key, value in date_hw_labs.items():
            is_hw = bool(re.compile(r'^hw', re.IGNORECASE).match(key))
            adjuster: GradeAdjuster = GradeAdjuster(False, "grade_adjuster.csv")
            mapping: str = adjuster.generate_range(value, is_hw)
            print(mapping)
            formula = generate_google_sheets_formula(mapping)

            # Write data to text file
            textfile.write(f"{key},{formula}\n")