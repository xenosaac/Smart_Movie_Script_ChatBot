def divide(int1, int2):
    assert int1 % 2 == 0, "int1 is not even"
    assert int2 % 2 == 0, "int2 is not even"
    assert int2 != 0, "int2 is 0"
    result = int1 / int2
    return result


print(divide(2, 4))
