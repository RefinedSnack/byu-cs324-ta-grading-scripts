import pytz
from datetime import datetime

# this may change per professor, these are the max number of days that can be earned for early points or late points
# the code will allow for 0 to be used if EARLY or LATE points are allowed
MAX_EARLY_DAYS = 4
MAX_LATE_DAYS = 4

# these are the number of points that will be earned per day for early or late submissions
POINTS_PER_DAY_EARLY = 1
POINTS_PER_DAY_LATE = 1

# these are the days that will be counted as late or early, if true it will count as a day early or late
# if you want to configure this further check GradeAdjust.py
# if you change the code update this documentation for the next team
COUNT_SATURDAY = False
COUNT_SUNDAY = False
COUNT_HOLIDAYS = False

# True is more lenient option, if the assignment is turned in on a skipped day 
# it will be treated as being turned in on the last school day
# Example: Saturday submission will be treated the same as 
#   Monday if False and same as 
#   Friday if True
SKIPPED_DAYS_FALL_BACK = False

# add in the holidays that will be counted as late or early
# use the YEAR, MONTH, DAY format
HOLIDAYS = {
    datetime(2024, 1, 15).date(),  # MLK Day
    datetime(2024, 2, 19).date(),  # Presidents Day
    datetime(2024, 3, 15).date(),  # No Classes
}
# This is the last day to submit work
# use the YEAR, MONTH, DAY format
CUTOFF_DATE = datetime(2024, 4, 17).date()
