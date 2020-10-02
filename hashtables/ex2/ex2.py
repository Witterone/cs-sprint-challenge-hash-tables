#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dic = {}
    for i in tickets:
        
            dic[i.source] = i.destination
    route = []
    cur = "NONE"
    while len(route) < length:
        route.append(dic[cur])
        cur = dic[cur]
    
        

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
print(reconstruct_trip(tickets, 3))