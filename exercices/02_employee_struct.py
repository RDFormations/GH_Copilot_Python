from __future__ import annotations

import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Employee:
    name: str
    age: int
    salary: float


def employee_create(name: str, age: int, salary: float) -> Employee:
    return Employee(name=name, age=age, salary=salary)


def employee_print(emp: Employee) -> None:
    print(f"Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary:.2f}")


def employee_serialize(emp: Employee) -> str:
    return f"{emp.name};{emp.age};{emp.salary:.2f}"


def employee_deserialize(line: str) -> Employee | None:
    # TODO: Implement avec Copilot
    # Commentaire-prompt : split sur ';', valider 3 champs, parser age et salary
    return None


def main() -> None:
    data_path = Path(tempfile.gettempdir()) / "gh-copilot-python-employees.dat"
    employees = [
        employee_create("Alice Dupont", 32, 45000.0),
        employee_create("Bob Martin", 28, 38000.0),
        employee_create("Charlie Noir", 45, 62000.0),
    ]

    print("=== Employes crees ===")
    for emp in employees:
        employee_print(emp)

    print("\n=== Serialisation dans fichier ===")
    data_path.write_text("\n".join(employee_serialize(e) for e in employees) + "\n", encoding="utf-8")
    print(f"3 employes ecrits dans {data_path}")

    print("\n=== Deserialisation depuis fichier ===")
    for line in data_path.read_text(encoding="utf-8").strip().split("\n"):
        loaded = employee_deserialize(line)
        if loaded:
            employee_print(loaded)

    data_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
