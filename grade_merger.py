from net_id_mapper import *
import os

def display_csv_files():
    # Get a list of CSV files in the current directory
    csv_files = [file for file in os.listdir() if file.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return None
    
    print("List of CSV files in the current directory:")
    for i, file in enumerate(csv_files):
        print(f"{i+1}. {file}")
    
    while True:
        try:
            choice = int(input("Enter the number corresponding to the file you want to use: "))
            if 1 <= choice <= len(csv_files):
                return csv_files[choice-1]
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    student_list_csv = 'C-S 324-student-list.csv'
    submission_csv = display_csv_files()
    output_csv_path = 'merged_data.csv'
    ls_grade_download = display_csv_files()
    
    print(f"student_list_csv: {student_list_csv}")
    print(f"submission_csv: {submission_csv}")
    print(f"output_csv_path: {output_csv_path}")
    print(f"ls_grade_download: {ls_grade_download}")


    merge_csv(submission_csv, ls_grade_download, output_csv_path)