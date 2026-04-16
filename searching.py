import os
import json
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence

# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as f:
        data = json.load(f)

    if field in data.keys():
        return data[field]
    else:
        print(f"Field {field} not exist")
        return None

def linear_search(sequence, the_number):
    dictionary = {}
    count = 0
    position = []

    for j in range(len(sequence)-1):
        if sequence[j] == the_number:
            count += 1
            position.append(j)

    dictionary["positions"] = position
    dictionary["count"] = count

    return dictionary

def binary_search(list_of_numbers, the_number):
    min_i = 0
    max_i = len(list_of_numbers) - 1

    while min_i <= max_i:
        mid_i = (min_i + max_i) // 2

        if list_of_numbers[mid_i] == the_number:
            return mid_i
        elif list_of_numbers[mid_i] < the_number:
            min_i = mid_i + 1
        else:
            max_i = mid_i -1
    return None

def measure_time_of_run():
    sizes = [100, 500, 1000, 5000, 10000]
    linear = []
    binary = []

    for size in sizes:
        data = unordered_sequence(size)
        the_number = data[0]

        start = time.perf_counter()
        linear_search(data,the_number)
        end = time.perf_counter()
        result_1 = end - start
        linear.append(result_1)

        start = time.perf_counter()
        ordered_sequence = sorted(data)
        binary_search(ordered_sequence, the_number)
        end = time.perf_counter()
        result_2 = end - start
        binary.append(result_2)

    return sizes, linear, binary

def graph_plot():
    values = measure_time_of_run()
    sizes = values[0]
    linear = values[1]
    binary = values[2]

    plt.plot(sizes, linear, label="Lineární vyhledávání")
    plt.plot(sizes, binary, label="Binární vyhledávání")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření")
    plt.show()


def main():
    filename = "sequential.json"
    data_unordered = read_data(filename, "unordered_numbers")
    print(data_unordered)

    searching = linear_search(data_unordered, 2)
    print(searching)

    data_ordered = read_data(filename, "ordered_numbers")
    print(data_ordered)

    binary = binary_search(data_ordered, 14)
    print(binary)

    time = measure_time_of_run()
    print(time)

    graph_plot()

if __name__ == '__main__':
    main()