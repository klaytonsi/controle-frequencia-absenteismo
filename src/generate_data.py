"""Synthetic attendance data generator / Gerador de dados sintéticos de frequência."""
from __future__ import annotations

import numpy as np
import pandas as pd

SEED = 42  # EN: fixed seed = same data every run / PT: seed fixa = mesmos dados sempre
DEPARTMENTS = ["Administrativo", "TI", "Financeiro", "RH", "Logística", "Atendimento"]
FIRST_NAMES = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Felipe", "Gabriela", "Hugo"]
LAST_NAMES = ["Alves", "Barros", "Costa", "Dias", "Ferraz", "Gomes", "Lima", "Moraes"]
STATUS = ["Presente", "Atraso", "Falta", "Atestado"]
BASE_PROBS = [0.90, 0.04, 0.03, 0.03]


def create_employees(n: int, rng: np.random.Generator) -> pd.DataFrame:
    """Create fictional employees / Cria funcionários fictícios."""
    # EN: each employee has a personal absence tendency
    # PT: cada funcionário tem uma tendência pessoal de faltar
    return pd.DataFrame(
        {
            "employee_id": [f"F{i:03d}" for i in range(1, n + 1)],
            "name": [
                f"{rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)}" for _ in range(n)
            ],
            "department": rng.choice(DEPARTMENTS, size=n),
            "absence_factor": rng.uniform(0.5, 2.0, size=n),
        }
    )


def create_attendance(
    employees: pd.DataFrame, start: str, end: str, rng: np.random.Generator
) -> pd.DataFrame:
    """Create daily attendance records / Cria registros diários de frequência."""
    # EN: business days only / PT: apenas dias úteis
    days = pd.bdate_range(start, end)
    rows = []
    for emp in employees.itertuples():
        # EN: scale non-present probabilities by the employee's factor
        # PT: escala as probabilidades de não presença pelo fator do funcionário
        bad = np.array(BASE_PROBS[1:]) * emp.absence_factor
        probs = np.concatenate([[1 - bad.sum()], bad])
        status = rng.choice(STATUS, size=len(days), p=probs)
        minutes_late = np.where(status == "Atraso", rng.integers(5, 61, len(days)), 0)
        rows.append(
            pd.DataFrame(
                {
                    "employee_id": emp.employee_id,
                    "date": days,
                    "status": status,
                    "minutes_late": minutes_late,
                }
            )
        )
    return pd.concat(rows, ignore_index=True)


def generate_dataset(n_employees: int = 50) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (employees, attendance) / Retorna (funcionários, frequência)."""
    rng = np.random.default_rng(SEED)
    employees = create_employees(n_employees, rng).drop(columns="absence_factor")
    # EN: recreate with the factor to build attendance, then drop it
    # PT: recria com o fator para gerar a frequência e depois remove
    rng = np.random.default_rng(SEED)
    full = create_employees(n_employees, rng)
    attendance = create_attendance(full, "2025-01-01", "2025-12-31", rng)
    return employees, attendance


if __name__ == "__main__":
    emp, att = generate_dataset()
    print(emp.head())
    print(att["status"].value_counts(normalize=True).round(3))
