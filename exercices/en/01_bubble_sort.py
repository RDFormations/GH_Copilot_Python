def bubble_sort(arr: list[int]) -> None:
    """Tri à bulles sur une liste d'entiers en ordre croissant. Modifie la liste en place."""
    # TODO: Implement avec Copilot
    # Commentaire-prompt : parcourir la liste, comparer paires adjacentes, permuter si nécessaire
    pass


def print_array(arr: list[int]) -> None:
    print(" ".join(str(x) for x in arr))


def main() -> None:
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Tableau avant tri :")
    print_array(arr)
    bubble_sort(arr)
    print("Tableau apres tri :")
    print_array(arr)


if __name__ == "__main__":
    main()
