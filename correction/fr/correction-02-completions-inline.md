# Correction — Completions inline et contexte

> **Exercice** : [Revoir l'énoncé](../exercices/fr/exercice-02-completions-inline.md)

## Contexte

Des commentaires précis améliorent nettement la qualité des suggestions générées.

## Correction détaillée

### Étape 2 — Stub A vague

**Analyse :** avec un commentaire vague, Copilot propose souvent un algorithme incomplet — insuffisant.

### Étape 3 — Prompt structuré (stub A)

```py
def insertion_sort(values: list[int]) -> list[int]:
 """
 QUOI : Tri par insertion sur liste de nombres.
 COMMENT : parcours O(n²), copie immuable.
 CONTRAINTES : retourne une nouvelle liste triée croissante.
 """
```

**Vérification :** algorithme de tri correct avec copie immuable.

### Étape 5 — Stub B recherche dichotomique

**Corps type :** recherche sur tableau trié, retourne index ou -1.

## Pièges fréquents

| Symptôme | Piste |
| -------- | ----- |
| Tri mutuant le tableau source | Préciser copie immuable dans COMMENT |
| Index -1 non géré | Préciser tableau trié dans COMMENT |


## Documentation

| Sujet | Lien |
| ----- | ---- |
| Bonnes pratiques | [Best practices](https://docs.github.com/copilot/get-started/best-practices-for-using-github-copilot) |
