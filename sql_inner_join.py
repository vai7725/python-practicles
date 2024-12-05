import csv

data1 = [
    ["ID", "Name", "Age"],
    [1, "John", 25],
    [2, "Alice", 30],
    [3, "Bob", 22]
]

data2 = [
    ["ID", "City"],
    [1, "New York"],
    [2, "Los Angeles"],
    [3, "Chicago"]
]

with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

with open('cities.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data2)

people_data = []
with open('people.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people_data.append(row)

cities_data = []
with open('cities.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cities_data.append(row)

def sql_inner_join(table1, table2, on_column):
    joined_data = []
    for row1 in table1:
        for row2 in table2:
            if row1[on_column] == row2[on_column]:
                joined_row = {**row1, **row2}
                joined_data.append(joined_row)
    return joined_data

# Example usage: Inner join on 'ID' column
inner_joined_data = sql_inner_join(people_data, cities_data, "ID")

print(inner_joined_data)
