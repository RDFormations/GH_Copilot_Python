# Exercices — Completions inline et contexte

> **Contexte** — Vous implémentez des fonctions utilitaires en **Python**. Des commentaires trop vagues produisent du code générique.

## Exercice — Commentaires-prompts algorithmiques

**Notions mobilisées :** sections 2.5–2.6 (Quoi/Comment/Contraintes, itération).

### Énoncé

1. Créez `src/utils/sort.py`.
2. **Stub A** — copiez le stub vague, déclenchez une complétion (`Alt + \`), notez pourquoi la suggestion est insuffisante :

```py
# trier un tableau
def insertion_sort(values: list[int]) -> list[int]:
```

3. Remplacez par un commentaire structuré Quoi/Comment/Contraintes (tri par insertion, copie immuable) :

```py
def insertion_sort(values: list[int]) -> list[int]:
 """
 QUOI : Tri par insertion sur liste de nombres.
 COMMENT : parcours O(n²), copie immuable.
 CONTRAINTES : retourne une nouvelle liste triée croissante.
 """
```

4. **Stub B** — même démarche pour la recherche dichotomique (tableau trié, retourne index ou -1) :

```py
# recherche dichotomique
def binary_search(values: list[int], target: int) -> int:
```

5. Pour chaque stub, documentez le nombre d itérations avant une suggestion acceptable.

**Critère de réussite :** deux fonctions avec prompts précis ; algorithme correct ; bilan d itération documenté.

**Documentation :** [Best practices](https://docs.github.com/copilot/get-started/best-practices-for-using-github-copilot)

> **Correction** : [Accéder à la correction](../correction/fr/correction-02-completions-inline.md)
