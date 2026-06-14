#!/usr/bin/env python3
"""
Pet Adoption Center - CSV Reader
Displays adoptable animals based on user-specified animal type.
"""

import csv
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def load_animals(animal_type: str) -> list[dict]:
    """Read and return all animals of the given type from the matching CSV file."""
    filepath = os.path.join(DATA_DIR, f"{animal_type}.csv")
    with open(filepath, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def format_animal(animal: dict) -> str:
    """Format a single animal's data as a readable English sentence."""
    name = animal["name"]
    age = animal["age"]
    breed = animal["breed"]
    years = "year" if age == "1" else "years"
    return f"{name} is a {age} {years} old {breed}."


def display_animals(animal_type: str):
    """Load and print all animals for the given type."""
    animals = load_animals(animal_type)
    if not animals:
        print(f"We have no {animal_type}s available right now.")
        return
    print(f"\nHere are our adoptable {animal_type}s:\n")
    for animal in animals:
        print(f"  {format_animal(animal)}")
    print()


def main():
    animal_type = input("What type of animal are you looking for? ").strip().lower()
    # Remove trailing 's' so "dogs" and "dog" both work
    if animal_type.endswith("s"):
        animal_type = animal_type[:-1]
    try:
        display_animals(animal_type)
    except FileNotFoundError:
        print(f"\nSorry, we don't have any {animal_type}s here.\n")


if __name__ == "__main__":
    main()
