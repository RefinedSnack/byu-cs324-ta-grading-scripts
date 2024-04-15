import csv

def merge_csv(csv1_path, csv2_path, output_csv_path):
    # Read csv1 and create a dictionary mapping names to NetIDs
    name_netid_mapping = {}
    with open(csv1_path, 'r') as csv1_file:
        csv1_reader = csv.reader(csv1_file)
        next(csv1_reader)  # Skip header
        for row in csv1_reader:
            name_netid_mapping[row[0]] = row[1]

    # Read csv2 and create a list of tuples with (Name, NetID, Date)
    merged_data = []
    with open(csv2_path, 'r') as csv2_file:
        csv2_reader = csv.reader(csv2_file)
        next(csv2_reader)  # Skip header
        for row in csv2_reader:
            name = row[1]
            netid = name_netid_mapping.get(name, '')  # Get NetID from the mapping
            date = row[2]
            merged_data.append((name, netid, date))

    # Write the merged data to the output CSV file
    with open(output_csv_path, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        # Write header
        csv_writer.writerow(['Name', 'NetID', 'Date'])
        # Write data
        csv_writer.writerows(merged_data)

if __name__ == "__main__":
    csv1_path = r'C-S 324-student-list.csv'
    # csv2_path = r'C:\Users\walte\Documents\cs324\dev\Shell_Lab_2_-_Signals_and_Job_Control.csv'
    # csv2_path = r'C:\Users\walte\Documents\cs324\dev\Shell_Lab_1_-_Pipelines_and_Redirection.csv'
    # csv2_path = r'C:\Users\walte\Documents\cs324\dev\HW_4_-_Signals.csv'
    # csv2_path = r'C:\Users\walte\Documents\cs324\dev\HTTP_Proxy_Lab_1_-_Threadpool.csv'
    csv2_path = r'C:\Users\walte\Documents\cs324\dev\HTTP_Proxy_Lab_2_-_I_O_Multiplexing.csv'
    # csv2_path = r'C:\Users\walte\Documents\cs324\dev\Socket_Treasure_Hunt.csv'
    output_csv_path = r'merged_data.csv'

    merge_csv(csv1_path, csv2_path, output_csv_path)
