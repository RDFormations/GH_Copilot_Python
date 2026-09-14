# TP — mini_push_swap (Python)

## Contexte

Le **push_swap** est un exercice classique de manipulation de structures de données : trier des entiers en n'utilisant que **deux piles** (`a` et `b`) et un petit ensemble d'**opérations** (`sa`, `pb`, `ra`, etc.). On ne trie pas directement un tableau : chaque déplacement passe par les piles.

Ce TP en propose une **version réduite**, adaptée à un cours **Python** et à l'usage de GitHub Copilot.

---

## Fichiers fournis

| Fichier | Rôle |
| ------- | ---- |
| `fr/SUJET.md` | Énoncé (ce document) |
| `checker.py` | Vérificateur **standalone** — lit les opérations sur stdin |
| `scripts/` | Scripts de test (`test_checker_50.sh`, `run_batch_50.sh`) |

**Tout le reste est à développer** : `push_swap`, piles, opérations, parsing des arguments.

---

## Objectif

Écrire un programme **`push_swap`** qui :

1. Reçoit entre **2 et 50** entiers **strictement positifs**, tous **distincts**, en arguments.
2. Affiche sur la sortie standard une **suite d'opérations** (une par ligne).
3. Applique ces opérations sur deux piles pour que **`a` soit triée** (convention du checker fourni).

### Exemple

```bash
python3 src/push_swap.py 3 1 2
```

Sortie possible :

```
ra
pb
pb
pa
pa
```

Vérification avec le checker fourni :

```bash
python3 src/push_swap.py 3 1 2 | python3 checker.py 3 1 2
# attendu : OK
```

---

## Périmètre du TP

| Version « complète » classique      | Ce TP                                                  |
| ----------------------------------- | ------------------------------------------------------ |
| Centaines de valeurs                | **2 à 50** valeurs                                     |
| Optimisation du nombre d'opérations | **Tri correct** obligatoire ; score d'ops en **bonus** |
| Checker à écrire                    | **Checker fourni** (`checker.py`)                      |
| Algorithmes avancés                 | Piles, opérations et **stratégie de tri à concevoir**  |

---

## Modèle des piles

- **`a`** : contient tous les nombres au départ. Le **premier argument** est en **bas**, le **dernier** au **sommet**.
- **`b`** : vide au départ.

```
python3 src/push_swap.py 2 1 3

Pile a (bas → haut) :  2  1  3     ← sommet = 3
Pile b                : (vide)
```

Représentation au choix : **tableau**, **liste chaînée**, ou structure custom — tant que les opérations respectent la sémantique ci-dessous.

---

## Opérations à implémenter

Chaque opération modifie les piles. Si l'opération est **valide**, `push_swap` l'**affiche** sur `stdout` (une ligne par opération). Sinon, elle ne fait rien et **n'est pas affichée**.

| Op    | Effet                                                        |
| ----- | ------------------------------------------------------------ |
| `sa`  | Échange les **2 premiers** éléments de `a` (les 2 au sommet) |
| `sb`  | Échange les **2 premiers** éléments de `b`                   |
| `ss`  | `sa` + `sb` (une seule ligne `ss`)                           |
| `pa`  | Retire le sommet de `b`, l'empile sur `a`                    |
| `pb`  | Retire le sommet de `a`, l'empile sur `b`                    |
| `ra`  | Sommet de `a` envoyé en **bas** de `a`                       |
| `rb`  | Idem sur `b`                                                 |
| `rr`  | `ra` + `rb` (une seule ligne `rr`)                           |
| `rra` | Élément du **bas** de `a` remonté au sommet                  |
| `rrb` | Idem sur `b`                                                 |
| `rrr` | `rra` + `rrb` (une seule ligne `rrr`)                        |

## Parsing et gestion d'erreurs

| Entrée                                                                      | Comportement                       |
| --------------------------------------------------------------------------- | ---------------------------------- |
| Aucun argument                                                              | Pas de sortie, code `0`            |
| Argument non entier, `≤ 0`, doublon, ou **moins de 2 / plus de 50** valeurs | `Error\n` sur **stderr**, code `1` |

Exemples :

```bash
python3 src/push_swap.py          # rien, exit 0
python3 src/push_swap.py 1 1      # Error, exit 1
python3 src/push_swap.py -3 2     # Error, exit 1
python3 src/push_swap.py 1 2 abc  # Error, exit 1
python3 src/push_swap.py 42       # Error (un seul entier), exit 1
```

---

## Organisation du code (recommandée)

```
TP/
├── fr/SUJET.md
├── checker.py           # fourni — ne pas modifier
├── scripts/
│   ├── test_checker_50.sh
│   └── run_batch_50.sh
└── src/                 # à créer
    ├── stack.py         # pile : init, push, pop, triée ?, etc.
    ├── operations.py    # sa, sb, … rrr
    ├── parse.py         # validation des arguments
    ├── sort.py          # stratégie de tri
    └── push_swap.py     # point d'entrée
```

---

## Vérification

```bash
cd TP


# Test unitaire manuel
python3 src/push_swap.py 5 2 8 1 4 | python3 checker.py 5 2 8 1 4
# OK

# 50 valeurs aléatoires (configurez PUSH_SWAP si besoin)
bash scripts/test_checker_50.sh

# Comptage d'opérations (bonus)
bash scripts/run_batch_50.sh 5
```

Variables utiles pour les scripts :

```bash
export PUSH_SWAP="python3 src/push_swap.py"
export CHECKER="python3 checker.py"
./scripts/test_checker_50.sh 3
```

---

## GitHub Copilot — consignes du TP

1. **Commentaires-prompts** docstrings avant chaque bloc (`"""pb : dépile le sommet de a, empile sur b"""`).
2. Garder les modules (`stack.py`, `operations.py`) ouverts pendant l'écriture des opérations.
3. Utiliser le **Chat** pour expliquer le tri à 3 éléments, pas pour livrer une solution non comprise.
4. **Valider** avec le checker et `mypy src`.

---

## Rendu

- Dépôt ou archive contenant votre `push_swap` exécutable avec `python3 src/push_swap.py`.
- Court `README` : nom, commandes de compilation et de test.

---

## Schéma

```
     push_swap (étudiant)              checker.py (fourni)
  ┌─────────────┐                  ┌─────────────┐
  │ argv → pile │  ops sur stdout  │ argv → pile │
  │ tri → ops   │ ───────────────► │ lit stdin   │
  └─────────────┘                  │ exécute ops │
                                   │ vérifie tri │
                                   └─────────────┘
```
