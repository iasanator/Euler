n = 100

costs = {}

def make_key(base, span):
    return str(base) + ',' + str(span)

for span in range(2, 4):
    for base in range(1, n - span + 2):
        if span is 2:
            costs[make_key(base, span)] = base
        elif span is 3:
            costs[make_key(base, span)] = base + 1

for span in range(4, n + 1):
    for base in range(0, n - span):
        print('hi')
        #for each x from 0 to span,
        #x such that max(C(base, x) + x, C(base + x, base + span) + x) is minimized
        #x+ that max is the cost to add