# Exercices — Inline completions and context

> **Context** — You implement utility functions in **Python**. Vague comments produce generic code.

## Exercise — Algorithm comment-prompts

**Topics :** sections 2.5–2.6 (What/How/Constraints, iteration).

### Instructions

1. Create `src/utils/sort.py`.
2. **Stub A** — copy the vague stub, trigger completion (`Alt + \\`), note why the suggestion is insufficient:

```py
# trier un tableau
def insertion_sort(values: list[int]) -> list[int]:
```

3. Replace with structured What/How/Constraints (insertion sort, immutable copy):

```py
def insertion_sort(values: list[int]) -> list[int]:
    """
    QUOI : Tri par insertion sur liste de nombres.
    COMMENT : parcours O(n²), copie immuable.
    CONTRAINTES : retourne une nouvelle liste triée croissante.
    """
```

4. **Stub B** — same approach for binary search (sorted array, return index or -1):

```py
# recherche dichotomique
def binary_search(values: list[int], target: int) -> int:
```

5. For each stub, document iterations before an acceptable suggestion.

**Success criteria :** two functions with precise prompts; correct algorithm; iteration log documented.

**Documentation :** [Best practices](https://docs.github.com/copilot/get-started/best-practices-for-using-github-copilot)

> **Solution** : [View solution](../correction/en/correction-02-completions-inline.md)
