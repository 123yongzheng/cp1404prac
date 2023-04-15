import csv

def read_csv_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        return [row for row in reader]

def get_champions(data):
    champions = {}
    for row in data:
        if row[1] in champions:
            champions[row[1]] += 1
        else:
            champions[row[1]] = 1
    return champions

def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[2])
    return sorted(list(countries))

def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champions = get_champions(data)
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    countries = get_countries(data)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()