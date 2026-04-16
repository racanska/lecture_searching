import os
import json

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
    positions = []
    count = 0
    i = 0

    while i < len(sequence):
        if sequence[i] == the_number:
            positions.append(i)
            count += 1
        i += 1

    return {"positions": positions, "count": count}

def


def main():
    filename = "sequential.json"
    data = read_data(filename, "unordered_numbers")
    print(data)

    searching = linear_search(data, 6)
    print(searching)

if __name__ == '__main__':
    main()