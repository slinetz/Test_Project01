#Given an array of integers, return indices of the two numbers such that they add up to a specific target
#Input: [1,3,9,5,6,4], k = 8
#Output: 1, 3
def mathmatic_question(a:list, b:int) -> tuple: 
    a.sort()
    sum = 0
    for index, num in enumerate(a):
        for index2, num2 in enumerate(a[index+1:]):
            sum = a[index] + a[index2]
            if sum == b:
                return index, index2

if __name__ == "__main__":
    list_a = [1,3,9,5,6,4]
    k = 8
    result = mathmatic_question(list_a, k)
    print(result)

    assert mathmatic_question(list_a, 0b1111111111111111111)
    assert mathmatic_question(["st"], 3), "the list should not contain string"