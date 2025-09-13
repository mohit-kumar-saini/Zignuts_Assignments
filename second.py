contacts = {
    "Family": [
        {"name": "GrandMom", "phone": "9876543210"},
        {"name": "Mom", "phone": "1234567890"},
        {"name": "Dad", "phone": "2345678901"}
    ],
    "Friends": [
        {"name": "Nishant", "phone": "3456789012"},
        {"name": "Vinayak", "phone": "4567890123"},
        {"name": "Rahul", "phone": "7890123456"},
        {"name": "Satyam", "phone": "8901234567"}
    ],
    "Company": [
        {"name": "Sr. Manager", "phone": "5678901234"},
        {"name": "H.R.", "phone": "6789012345"}
    ]
}
print("Contact List:")
for group in contacts:
    print("\nGroup:", group)
    people = contacts[group]
    for person in people:
        print("Name:", person["name"], ", Phone:", person["phone"])