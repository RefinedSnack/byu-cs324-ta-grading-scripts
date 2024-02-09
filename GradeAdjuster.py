from datetime import date, timedelta, datetime, timedelta
from Configs import MAX_EARLY_DAYS, MAX_LATE_DAYS, POINTS_PER_DAY_EARLY, POINTS_PER_DAY_LATE, COUNT_SATURDAY, COUNT_SUNDAY, COUNT_HOLIDAYS, HOLIDAYS, SKIPPED_DAYS_FALL_BACK, CUTOFF_DATE
import csv
from copy import deepcopy

class GradeAdjuster:
    def __init__(self, verbose: bool, grade_adjuster_csv: str) -> None:
        self.verbose: bool = verbose
        self.grade_adjuster_csv: str = grade_adjuster_csv
        
        data_to_write = ["Student", "Project Number", "Number of Days Early", "Raw Score", "Final Score", "Points Available"]
        with open(self.grade_adjuster_csv, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(data_to_write)
        
    def calc_number_early_days(self, submission_date: date, due_date: date) -> float:
        delta: timedelta = due_date - submission_date

        curr_date: date = None
        end_date: date = None
        is_early: bool = None

        if delta.days > 0:
            curr_date = submission_date
            end_date = due_date
            is_early = True
        else:
            curr_date = due_date
            end_date = submission_date
            is_early = False

        count = 0.0
        skipped_day_count = 0.0
        
        while curr_date < end_date:
            if self.is_skip_day(curr_date):
                skipped_day_count += 1
            else:
                count += 1
            curr_date += timedelta(days=1)
        
        if SKIPPED_DAYS_FALL_BACK and self.is_skip_day(submission_date):
            if not is_early:
                count -= 1
            else:
                count += 1
                
        if not is_early:
            count *= -1
            
        return count

    def is_skip_day(self, date: date):
        if not COUNT_SATURDAY and date.weekday() == 5:  # Saturday
            return True
        elif not COUNT_SUNDAY and date.weekday() == 6:  # Sunday
            return True
        elif not COUNT_HOLIDAYS and date in HOLIDAYS:  # it is a holidays
            return True
        else:
            return False

    def calc_number_bonus_points(self, num_days_early: int):
        if num_days_early > 0:
            return min(MAX_EARLY_DAYS * POINTS_PER_DAY_EARLY, num_days_early * POINTS_PER_DAY_EARLY)
        else:
            return max(MAX_LATE_DAYS * POINTS_PER_DAY_LATE * -1, num_days_early * POINTS_PER_DAY_LATE)

    def __is_after_cutoff(self, submission_date: date) -> bool:
        return submission_date > CUTOFF_DATE
    
    def generate_range(self, due_date: date, is_hw: bool) -> str:
        result: str = ""
        submission_date: date = deepcopy(due_date)
        count: float = 0.0
        sign = "-"
        
        time_format = "%m-%d"
        if self.verbose: time_format = "%a, %m-%d"
        # Grace Days Block
        while True:
            count = self.calc_number_early_days(submission_date, due_date)
            if is_hw: count *= 0.5
            if count >= 0: sign = "+"
            else: sign = ""
            num_str: str = f'{sign}{count}'
            if num_str == '+-0.0': num_str = '+0.0'
            line: str = f'{submission_date.strftime(time_format)}: {num_str}'
            result = f'{result}{line}\n'
            # if self.verbose: print(line)
            if count == MAX_EARLY_DAYS: break
            submission_date = submission_date - timedelta(days=1)
        
        submission_date = deepcopy(due_date)
        submission_date = submission_date + timedelta(days=1)
        # Late Days Block
        while True:
            count = self.calc_number_early_days(submission_date, due_date)
            if is_hw: count *= 0.5
            if count >= 0: sign = "+"
            else: sign = ""
            num_str: str = f'{sign}{count}'
            if num_str == '+-0.0': num_str = '+0.0'
            line: str = f'{submission_date.strftime(time_format)}: {num_str}'
            result = f'{line}\n{result}'
            # if self.verbose: print(line)
            if count == -1 * MAX_LATE_DAYS: break
            submission_date = submission_date + timedelta(days=1)
        
        result = self.reverse_lines(result)
        due_date_str: str = f'due_date: {due_date.strftime(time_format)}'
        result = f'{due_date_str}{result}'
        return result

    def reverse_lines(self, input_string: str) -> str:
        lines = input_string.split('\n')
        reversed_lines = reversed(lines)
        reversed_string = '\n'.join(reversed_lines)
        return reversed_string