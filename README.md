# GH Copilot — laboratoire Python

Formation GitHub Copilot adaptée au **Python** : cours, exercices guidés (FR/EN) et TP mini push_swap.

## Contenu

| Dossier | Description |
| ------- | ----------- |
| `Cours.md` / `Cours.pdf` | Support de formation (6 modules, FR) |
| `exercices/fr/` | Énoncés (FR) + fichiers `.py` à compléter |
| `exercices/en/` | Exercise sheets (EN) + same `.py` stubs |
| `correction/fr/` | Corrections (FR) + code corrigé |
| `correction/en/` | Solutions (EN) + corrected code |
| `TP/fr/SUJET.md` | Énoncé TP push_swap (français) |
| `TP/en/SUJET.md` | push_swap assignment (English) |

## Prérequis

- Python 3.11+
- VS Code + GitHub Copilot + extension Python (Pylance)
- `make` (optionnel)

## Exercices

```bash
make ex01    # tri à bulles (exercices/fr/)
make ex02    # dataclass Employee + sérialisation
make ex03    # parsing CSV

make corr01  # correction
```

Énoncés anglais : `exercices/en/exercice-*.md`.

## TP push_swap

**Fourni :** `TP/fr/SUJET.md` ou `TP/en/SUJET.md`, `TP/checker.py`, `TP/scripts/`.

```bash
cd TP
python3 src/push_swap.py 3 1 2 | python3 checker.py 3 1 2
# attendu : OK (une fois push_swap implémenté)

bash scripts/test_checker_50.sh 3
```
