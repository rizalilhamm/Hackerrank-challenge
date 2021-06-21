"""
sources: https://www.hackerrank.com/challenges/list-comprehensions/problem

Given three integer x, y, z that represent the dimentions of a cuboid along with an Integer n
print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum i+j+k of is not equal to n
example:
x = 1
y = 1
z = 1
n = 2

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]   
"""

# USING MANUAL LOOP
def using_loop():
    """ return list that i+j+k not equal to n using manual loop proccess """
    end_result = []
    print("USING MANUAL LOOP")
    x = int(input("i value: "))
    y = int(input("y value: "))
    z = int(input("z value: "))
    n = int(input("n value: "))
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                # all value that i+j+k not equal to n append to end_result
                if i+j+k != n:
                    value = [i, j, k]
                    end_result.append(value)
                else:
                    continue
    
    return end_result


def using_list_compherention():
    """ return list that i+j+k not equal to n using list compherension proccess """
    print("USING LIST COMPHERENTION")
    x = int(input("i value: "))
    y = int(input("y value: "))
    z = int(input("z value: "))
    n = int(input("n value: "))

    end_result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

    return end_result

if __name__ == '__main__':
    # Code driver
    print(using_loop())
    print(using_list_compherention())