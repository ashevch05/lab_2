import sys

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def data_manip(data: str):
    numbers = data.split()
    converted_numbers = []

    for num in numbers:
        if '.' not in num:
            converted_numbers.append(int(num))
        else:
            converted_numbers.append(float(num))
    return converted_numbers


def main(data_from_test=None):
    try:
        if data_from_test is None:
            input_data = sys.stdin.readline() # повертає рядок
            data_list = data_manip(input_data) # перетворює в список
        else:
            data_list = data_from_test
        sorted_list = bubble_sort(data_list)
        sys.stdout.write(' '.join(map(str, sorted_list))) # вивід відсортованого списку
        return 0, sorted_list
    except Exception:
        sys.stderr.write(f"Error\n")
        return 1, None


if __name__ == "__main__":
    sys.exit(main())
