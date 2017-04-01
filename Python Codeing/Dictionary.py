people ={"A": ["Rajesh", 27, "USA"],
         "B": ["Umesh", 26, "INDIA"],
         "C": ["Mangesh", 31, "INDIA"],
         "D": ["Harsh", 6, "INDIA"]}
print(people["D"])

print("A" in people)

print(people.get("C"))
print(people.get("E", "Data is unavilble"))