def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dic = {}
    if len(weights) <2:
        return None
    for i in range(len(weights)):
        dic[weights[i]] = i
    for x in dic:
        
        if (limit -x) in dic:
                if dic[limit-x] == dic[x]:
                    win = (dic[x],(dic[(limit -x)]-1))
                else:
                    win = (dic[x],dic[(limit -x)])
            

    return win
weights_2 = [4, 4]

print(get_indices_of_item_weights(weights_2, 2, 8))