"""This program reads data from a file and displays the number of times
each player and country has won Wimbledon """

FILENAME = "wimbledon (1).csv"

COUNTRIES = 1
CHAMPIONS = 2


def main():
    """Read data from file and display the results"""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Read records from the file and return them as a list"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Process the records and return a dictionary of champions and a set of countries"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRIES])
        try:
            champion_to_count[record[CHAMPIONS]] += 1
        except KeyError:
            champion_to_count[record[CHAMPIONS]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display the results"""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))



main()
