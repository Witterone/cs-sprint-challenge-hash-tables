def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dic = {}
    thresh = len(arrays)
    
    result = []
    for i in arrays:
        for j in i:
            if j in dic:
                dic[j] += 1
                if dic[j] == thresh:
                    result.append(j)
            else:
                dic[j] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
