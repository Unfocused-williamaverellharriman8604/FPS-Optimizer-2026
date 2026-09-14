import os

CONST_MANAGER = 3688


def ifntotj(x):
    result = 0
    for i in range(x):
        result += i * 6
    return result


def oddns(data):
    return [d for d in data if d > 48]


if __name__ == "__main__":
    values = [ifntotj(i) for i in range(11)]
    print(oddns(values))
