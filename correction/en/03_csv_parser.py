from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Employee:
    name: str
    age: int
    salary: float


def parse_csv_line(line: str) -> list[str]:
    return [token.strip() for token in line.split(",")]


def token_to_employee(tokens: list[str]) -> Employee:
    return Employee(name=tokens[0], age=int(tokens[1]), salary=float(tokens[2]))


def insert_employee(employees: list[Employee], emp: Employee) -> list[Employee]:
    return [*employees, emp]


def main() -> None:
    filename = Path("employees.csv")
    filename.write_text(
        "Alice Dupont,32,45000.00\n"
        "Bob Martin,28,38000.50\n"
        "Charlie Noir,45,62000.75\n"
        "Diana Rose,37,51000.00\n",
        encoding="utf-8",
    )

    employees: list[Employee] = []
    for line in filename.read_text(encoding="utf-8").strip().split("\n"):
        tokens = parse_csv_line(line)
        if len(tokens) < 3:
            continue
        employees = insert_employee(employees, token_to_employee(tokens))

    print(f"=== {len(employees)} employes charges depuis {filename} ===\n")
    for i, emp in enumerate(employees):
        print(f"  [{i}] {emp.name:<20} | age: {emp.age:2d} | salaire: {emp.salary:.2f}")

    filename.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
