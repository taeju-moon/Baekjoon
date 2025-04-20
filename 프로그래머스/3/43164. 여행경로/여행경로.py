
class Ticket:
    from_airport = ""
    to_airport = ""
    index = 0

    def __init__(self, from_, to, idx):
        self.from_airport = from_
        self.to_airport = to
        self.index = idx

answer = None

def solution(tickets):
    global answer

    tickets_hash = {}
    for index, ticket in enumerate(tickets):
        if tickets_hash.get(ticket[0]):
            tickets_hash[ticket[0]].append(Ticket(ticket[0], ticket[1], index))
        else:
            tickets_hash[ticket[0]] = [ Ticket(ticket[0], ticket[1], index) ]

    for key in tickets_hash.keys():
        tickets_hash[key] = sorted(tickets_hash[key], key=lambda x: x.to_airport)

    visited = [0] * len(tickets)
    dfs(tickets_hash, [ "ICN" ], visited)

    return answer

def dfs(tickets_hash, route, visited):
    global answer
    if answer != None: return

    if all(visited):
        answer = route
        return
    if not tickets_hash.get(route[-1]): return

    tickets = tickets_hash.get(route[-1])
    for ticket in tickets:
            if not visited[ticket.index]:
                copied_route = route.copy()
                ciopied_visited = visited.copy()
                ciopied_visited[ticket.index] = 1
                copied_route.append(ticket.to_airport)
                dfs(tickets_hash,copied_route, ciopied_visited)
        