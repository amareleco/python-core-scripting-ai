# Interactive User Profile Generator
"""
Author: Albino Mareleco
"Vetor confirmado."
"""

# Collect and clean user input
name = input("Enter your full name: ").strip()
age_text = input("Enter your age: ").strip()
height_text = input("Enter your height in meters: ").strip()
hobbies_text = input("Enter your favorite hobbies (comma separated): ").strip()

# Safely convert values using type casting
age = int(age_text) if age_text.isdigit() else 0
try:
    height = float(height_text)
except ValueError:
    height = 0.0

# Transform text for consistent formatting
clean_name = name.replace("  ", " ").title()
upper_name = clean_name.upper()
lower_name = clean_name.lower()

# Process hobbies into a clean list
hobbies = [item.strip().lower() for item in hobbies_text.split(",") if item.strip()]
hobby_display = " | ".join(hobbies) if hobbies else "No hobbies provided"

# Extract the first character safely
first_letter = clean_name[0] if clean_name else "-"

# Use logical operators to decide eligibility
eligible = (age >= 18 and height > 1.4) or not hobbies

# Create repeated welcome text
welcome = ("Welcome!!! " * 2).strip()

# Display formatted profile summary
print("\n" + "=" * 30)
print("PROFILE SUMMARY")
print("=" * 30)
print(f"Name: {clean_name}")
print(f"Age: {age}")
print(f"Height: {height:.2f} m")
print(f"Hobbies: {hobby_display}")
print(f"First Letter: {first_letter}")
print(f"Name in UPPERCASE: {upper_name}")
print(welcome)
print(f"Eligible for student program: {eligible}")
print("Formatted Message: {} is {} years old.".format(clean_name, age))