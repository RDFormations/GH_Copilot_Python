# Exercices — Completions inline et contexte

> **Context** — Vous implémentez des fonctions utilitaires en **Python**. Des commentaires trop vagues produisent du code générique.

## Exercice — Commentaires-prompts algorithmiques

### Instructions

1. Créez `src/utils/algorithms.py`.
2. **Stub A** — commentaire vague `# trier` puis prompt structuré :

```python
def insertion_sort(arr: list[int]) -> list[int]:
    """QUOI : tri par insertion. COMMENT : O(n²), copie immuable. CONTRAINTES : ordre croissant."""
```

3. **Stub B** — recherche dichotomique :

```python
def binary_search(arr: list[int], target: int) -> int:
    """QUOI : recherche dichotomique. CONTRAINTES : tableau trié, retourne index ou -1."""
```

4. Documentez les itérations pour chaque stub.

> **Solution** : [View solution](../correction/en/correction-02-completions-inline.md)
