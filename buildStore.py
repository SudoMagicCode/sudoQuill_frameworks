import csv
import json
from dataclasses import dataclass

OUTPUT_FILE = "sudoFrameworks.json"


@dataclass
class FrameworkVersion:
    id: str
    release_date: str
    stable: bool

    def to_dict(self) -> dict:
        info = {
            "id": self.id,
            "release_date": self.release_date,
            "stable": self.stable,
        }
        return info


@dataclass
class FramworkEntry:
    name: str
    publisher: str
    url: str
    version: FrameworkVersion

    def to_dict(self) -> dict:
        info = {
            "name": self.name,
            "publisher": self.publisher,
            "url": self.url,
            "version": self.version.to_dict(),
        }

        return info

    @staticmethod
    def from_row(info: list):
        return FramworkEntry(
            name=info[0],
            publisher=info[1],
            url=info[2],
            version=FrameworkVersion(
                id=info[3],
                release_date=info[4],
                stable=True if info[5] == "true" else False,
            ),
        )


def read_file() -> list[FramworkEntry]:
    entries = []
    with open("quillFrameworks.csv", newline="") as csvFile:
        frameworkReader = csv.reader(csvFile, delimiter=",")
        # skip header row
        next(frameworkReader)
        for eachRow in frameworkReader:
            entry = FramworkEntry.from_row(eachRow)
            entries.append(entry)

    return entries


def output_file(entries: list[FramworkEntry]):
    frameworks = []

    for each in entries:
        frameworks.append(each.to_dict())

    output_json = {"frameworks": frameworks}

    with open(OUTPUT_FILE, "w") as json_file:
        json.dump(output_json, json_file)


def main() -> None:
    entries = read_file()
    output_file(entries)


if __name__ == "__main__":
    main()
