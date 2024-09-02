import argparse
import datetime
import re
from dataclasses import dataclass, asdict

import pandas as pd
import yaml


@dataclass
class ConferenceRecord:
    title: str
    year: int
    id: str
    full_name: str
    link: str
    deadline: str
    abstract_deadline: str
    place: str
    date: str
    sub: str = "ML"
    timezone: str = "UTC-12"
    note: str = ""


def main(input_file: str, output_file: str):
    df = pd.read_csv(input_file).iloc[:, :-2]
    records = []
    for _, row in df.iterrows():
        title = row["Conference Short Name"] + ": " + row["Event Full Name"]
        title = title.replace("\n", "").strip()
        print(title)
        if row["Abstract Submition Deadline"] == "?":
            year = 2025
            abstract_deadline = submission_deadline = "2025-12-31"
        else:
            year = datetime.datetime.strptime(row["Abstract Submition Deadline"], "%m/%d/%Y").year
            abstract_deadline = datetime.datetime.strptime(row["Abstract Submition Deadline"], "%m/%d/%Y").strftime(
                "%Y-%m-%d"
            )
            submission_deadline = datetime.datetime.strptime(row["Paper Submition Deadline"], "%m/%d/%Y").strftime(
                "%Y-%m-%d"
            )

        idx = f"{title}_{year}".replace(" ", "_")
        idx = re.sub(r"[^a-zA-Z0-9_]", "", idx).lower()

        record = ConferenceRecord(
            title=title,
            year=year,
            id=idx,
            full_name=title,
            link=row[" Website"],
            deadline=submission_deadline,
            abstract_deadline=abstract_deadline,
            place=row["Place"],
            date=row["Conference Dates"],
            note=row["Event \nMain Track / Workshop / Challange"],
        )
        records.append(asdict(record))

    with open(output_file, "w+") as f:
        yaml.dump(records, f, allow_unicode=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process conference data.")
    parser.add_argument("input_file", type=str, help="Path to the input CSV file")
    parser.add_argument("output_file", type=str, help="Path to the output YAML file")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
