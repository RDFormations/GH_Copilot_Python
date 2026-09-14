def bubble_sort(arr: list[int]) -> None:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


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
