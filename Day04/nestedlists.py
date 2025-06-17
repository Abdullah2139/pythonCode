fruits = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry"
]
vegetables = [
    "Asparagus",
    "Broccoli",
    "Carrot",
    "Daikon",
    "Eggplant"
]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# Accessing elements in a nested list
print(dirty_dozen[0])  # Access the first list (fruits)
print(dirty_dozen[1])  # Access the second list (vegetables)
# Accessing elements within the nested lists
print(dirty_dozen[0][2])  # Access the third fruit (Cherry)
print(dirty_dozen[1][3])  # Access the fourth vegetable (Daikon)