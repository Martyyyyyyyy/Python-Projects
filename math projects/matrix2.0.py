def is_reflexive(rel, set_a):
    return {(a, a) for a in set_a} <= rel 

def is_transitive(rel):
    seconds_elements = {b for (a, b) in rel}
    for (a, b) in rel:
        for c in seconds_elements:
            if (b, c) in rel and (a, c) not in rel:
                return False
    return True

def is_antisymmetric(rel):
    for a in range(len(rel)):
        for b in range(a, len(rel)):
            rel = list(rel)
            if rel[a][b] and rel[b][a]:
                if a != b:
                    return False
    return True

def partial_order():
    if(is_reflexive and is_transitive and is_antisymmetric):
        return True
    else:
        return False

def test(rel, set_a):
    print("Set:         ", set_a)
    print("Relation:    ", rel)
    print("Reflexivity: ", is_reflexive(rel, set_a))
    print("Transitivity: ", is_transitive(rel))
    print("Antisymmetric: ", is_antisymmetric(rel))
    if(is_reflexive == True and is_transitive == True and is_antisymmetric == True):
        print("Partial order")
    else:
        print("Not a partial order")
    
    print(80 * "-")    
    set_a = (1, 2, 3, 4)


set_a = (1, 2, 3, 4)
rel = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (1, 3), (1, 4), (2, 4)}
test(rel, set_a)

rel = {(1, 2), (1, 2)}
test(rel, set_a)

rel = {(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (4, 4)}
test(rel, set_a)

rel = {(1, 2), (2, 3)}
test(rel, set_a)