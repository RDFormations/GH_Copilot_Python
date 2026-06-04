# GH Copilot — laboratoire Python

Formation GitHub Copilot adaptée au **Python** : cours, exercices guidés et TP mini push_swap.

## Contenu

| Dossier | Description |
| ------- | ----------- |
| `Cours.md` / `Cours.pdf` | Support de formation (6 modules) |
| `exercices/` | Fichiers à compléter avec Copilot |
| `correction/` | Solutions de référence |
| `TP/` | Mini push_swap — sujet + checker standalone |

## Prérequis

- Python 3.11+
- VS Code + GitHub Copilot + extension Python (Pylance)
- `make` (optionnel)

## Exercices

```bash
make ex01    # tri à bulles
make ex02    # dataclass Employee + sérialisation
make ex03    # parsing CSV

make corr01  # correction
```

Ou : `python3 exercices/01_bubble_sort.py`

## TP push_swap

**Fourni aux étudiants :** `TP/SUJET.md`, `TP/checker.py`, `TP/scripts/`.

```bash
cd TP
python3 src/push_swap.py 3 1 2 | python3 checker.py 3 1 2
# attendu : OK (une fois push_swap implémenté)

bash scripts/test_checker_50.sh 3
```

Voir `TP/SUJET.md` pour l'énoncé complet.
