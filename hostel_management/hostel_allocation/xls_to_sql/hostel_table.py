import pandas as pd
import pyodbc

import xlrd

server = 'Hostel Management'
db = 'hostel'

# create Connection and Cursor objects
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
cursor = conn.cursor()

# read data
data = pd.read_excel('hostel_list.xls')

# rename columns
data = data.rename(columns={'Name': 'hostel_name',
                            'Gender': 'hostel_gender',
                            'Course': 'hostel_course',
                            'No Of Floor': 'hostel_no_of_floor',
                            'No Of Room': 'hostel_no_of_room',
                            'No Of Room Available': 'hostel_no_of_room_available',
                            'Warden Name': 'hostel_warden'})

# export
data.to_excel('final_hostel_list.xlsx', index=False)

# Open the workbook and define the worksheet
book = xlrd.open_workbook("final_hostel_list.xlsx")
sheet = book.sheet_by_name("Sheet1")

query = """
INSERT INTO [hostel].[hostel_list] (
    hostel_name,
    hostel_gender,
    hostel_course,
    hostel_no_of_floor,
    hostel_no_of_room,
    hostel_no_of_room_available,
    hostel_warden
) VALUES (?, ?, ?, ?, ?, ?, ?)"""

# grab existing row count in the database for validation later
cursor.execute("SELECT count(*) FROM hostel.hostel_list")
before_import = cursor.fetchone()

for r in range(1, sheet.nrows):
    hostel_name = sheet.cell(r,0).value
    hostel_gender = sheet.cell(r,1).value
    hostel_course = sheet.cell(r,2).value
    hostel_no_of_floor = sheet.cell(r,3).value
    hostel_no_of_room = sheet.cell(r,4).value
    hostel_no_of_room_available= sheet.cell(r,5).value
    hostel_warden = sheet.cell(r,6).value

    # Assign values from each row
    values = (hostel_name,
    hostel_gender,
    hostel_course,
    hostel_no_of_floor,
    hostel_no_of_room,
    hostel_no_of_room_available,
    hostel_warden)

    # Execute sql Query
    cursor.execute(query, values)

# Commit the transaction
conn.commit()

# If you want to check if all rows are imported
cursor.execute("SELECT count(*) FROM LEAF.ZZZ")
result = cursor.fetchone()

print((result[0] - before_import[0]) == len(data.index))  # should be True

# Close the database connection
conn.close()
