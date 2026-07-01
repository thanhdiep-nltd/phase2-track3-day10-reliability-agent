"""Generate metrics.csv from metrics.json."""
from __future__ import annotations

import csv
import json
from pathlib import Path


def main() -> None:
    data = json.loads(Path("reports/metrics.json").read_text())
    row: dict[str, str | float | int] = {}
    for key, value in data.items():
        if key == "scenarios":
            scenarios = dict(value)  # type: ignore[arg-type]
            for s_name, s_status in scenarios.items():
                row[f"scenario_{s_name}"] = s_status
        else:
            row[key] = value

    path = Path("reports/metrics.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        writer.writeheader()
        writer.writerow(row)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
