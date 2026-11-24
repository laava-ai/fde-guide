"""Score service desk suggestions against a labelled CSV of fictional cases."""
import argparse
import csv
from pathlib import Path

ROUTES = {"billing", "access", "review"}
CASES = Path(__file__).with_name("cases.csv")


def read_routes(path, value_column):
    records = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not {"id", value_column}.issubset(reader.fieldnames or []):
            raise ValueError(f"{path.name} needs id and {value_column} columns")
        for row in reader:
            case, route = row["id"], row[value_column]
            if not case or case in records or route not in ROUTES:
                raise ValueError(f"{path.name}, row {reader.line_num}: invalid ID or route")
            records[case] = route
    if not records:
        raise ValueError(f"{path.name} contains no cases")
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", type=Path)
    parser.add_argument("--cases", type=Path, default=CASES)
    args = parser.parse_args()
    try:
        expected = read_routes(args.cases, "expected")
        suggested = read_routes(args.predictions, "route")
        if expected.keys() != suggested.keys():
            raise ValueError("The case IDs in both files must match")
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"{error}\n")

    errors = [case for case, route in expected.items() if suggested[case] != route]
    for case in errors:
        print(f"{case}: expected {expected[case]}, got {suggested[case]}")
    review_count = sum(route == "review" for route in expected.values())
    missed = sum(expected[case] == "review" for case in errors)
    queue_count = sum(route != "review" for route in suggested.values())
    print(f"Exact matches: {len(expected) - len(errors)}/{len(expected)}")
    print(f"Required reviews missed: {missed}/{review_count}")
    print(f"Queue suggestions: {queue_count}/{len(expected)}")


if __name__ == "__main__":
    main()
