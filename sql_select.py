import csv

data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Alice", 30, "Los Angeles"],
    ["Bob", 22, "Chicago"]
]

with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

loaded_data = []
with open('people.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        loaded_data.append(row)

def sql_select(columns, condition=None):
    results = []
    for row in loaded_data:
        if condition:
            if condition(row):
                selected_row = {col: row[col] for col in columns}
                results.append(selected_row)
        else:
            selected_row = {col: row[col] for col in columns}
            results.append(selected_row)
    return results

# Example usage: Select Name and Age where Age is greater than 23
selected_data = sql_select(["Name", "Age"], lambda row: int(row["Age"]) > 23)

print(selected_data)
