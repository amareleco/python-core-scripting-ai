raw_contacts = [
    ("Alice", "555-0101"),
    ("Bob", "555-0102"),
    ("Alice", "555-0101"),
    ("Cara", "555-0103"),
    ("Bob", "555-0102")
]

# Store immutable contact pairs and remove duplicates with a set
unique_pairs = set()
for contact in raw_contacts:
    name, number = contact  # Tuple unpacking keeps data organized
    unique_pairs.add(contact)

unique_pairs.remove(("Bob", "555-0102"))  # Remove an unwanted record safely
unique_pairs.add(("Bob", "555-0102"))  # Add the corrected record back

# Create a dictionary for quick name-to-number lookup
contacts = {}
for name, number in unique_pairs:
    contacts[name] = number

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Registry:")
for name, number in contacts.items():
    print(name, "->", number)

# Use get() to avoid errors when a key does not exist
print("Unknown:", contacts.get("David", "Not found"))

# Use update() to safely add new relationship data
contacts.update({"David": "555-0104"})

# Compare datasets using mathematical set operations
group_a = set(["Alice", "Cara"])
group_b = set(contacts.keys())
print("Common:", group_a.intersection(group_b))
print("Only new:", group_b.difference(group_a))
print("All contacts:", group_a.union(group_b))
print("Different:", group_a.symmetric_difference(group_b))