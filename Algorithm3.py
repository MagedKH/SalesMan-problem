#Solvin SalesMan problem using Tabu algorithm 
#Done by: Asmaa Mostafa El-Ziady




import math
from random import randint
import shared

best_Order = []


def read_file():
    
    inputs = [[i * j for j in range(2)] for i in range(shared.number_Elements)]
    for i in range(0,shared.number_Elements,1) :
        inputs[i][0] = shared.generated_nodes[i].x
        inputs[i][1] = shared.generated_nodes[i].y
        #print (inputs)
    return inputs

def euc_2d(c1, c2):
    return math.sqrt((pow((c1[0] - c2[0]), 2)) + (pow((c1[1] - c2[1]), 2)))


def cost(perm, cities):
    distance = 0
    for i in range(len(perm)):

        c1 = perm[i]
        if i == len(perm) - 1:
            c2 = perm[0]
        else:
            c2 = perm[i + 1]

        distance += euc_2d(cities[c1], cities[c2])
    #    print(distance)
    return distance


def random_permutation(cities):
    temp = 0
    perm = []
    for i in range(len(cities)):
        perm.append(i)
    for i in range(len(perm)):
        r = randint(0, len(perm) - 1)  # + i
        temp = perm[r]
        perm[r] = perm[i]
        perm[i] = temp
    return perm


def stochastic_two_opt(parent):
    #print(parent)
    perm = []
    exclude = []
    temp = 0
    ret = []
    for i in range(len(parent)):
        perm.append(parent[i])
    c1 = randint(1, len(perm) - 1)  # عدلت هنا
    c2 = randint(1, len(perm) - 1)  # وهنا
    exclude.append(c1)  # وتقريبا هنا
    if c1 == 0:
        exclude.append(len(perm) - 1)
    else:
        exclude.append(c1)  # وهنا
    if c1 == (len(perm) - 1):
        exclude.append(0)
    else:
        exclude.append(c1 + 1)
    firstPass = 1
    while firstPass or (c2 in exclude):
        c2 = randint(1, len(perm) - 1)
        firstPass = 0
    if c2 < c1:
        temp = c1
        c1 = c2
        c2 = temp
    #perm[c1:c2].reverse()
    ret.append(perm)
    
    ret.append([[parent[c1 - 1], parent[c1]], [parent[c2 - 1], parent[c2]]])
    return ret


def is_tabu(permutation, tabu_list):
    for i in range(len(permutation)):
        c1 = permutation[i]
        if i == (len(permutation) - 1):
            c2 = permutation[0]
        else:
            c2 = permutation[i + 1]
    for tabu_list_element in tabu_list:
        if tabu_list_element == [c1, c2]:
            return 1
    return 0


def generate_candidate(best, tabu_list, cities):
    ret = []
    perm = []
    edges = []
    firstPass = 1
    x = []
    candidate = []
    while firstPass or (is_tabu(perm, tabu_list)):
        x = list(stochastic_two_opt(best[0]))
        #print(x)
        #print("++++")
        perm.append(x[0])

        edges.append(x[1])
        firstPass = 0

        candidate = list(x)  # عدلت هنا

        candidate.append(cost(candidate[0], cities))
    ret.append(candidate)
    ret.append(edges)

    return ret


def search(cities, tabu_list_size, candidate_list_size, max_iter, irrrr):
    current = []
    current.append(random_permutation(cities))

    x = cost(current[0], cities)
    current.append([])
    current[1].append(x)
    best = current
    tabu_list = []
    candidates = []

    for i in range(max_iter):

        # candidates = [0 for z in range(candidate_list_size)]
        for j in range(candidate_list_size):
            candidates.append((generate_candidate(current, tabu_list, cities))[0])

        candidates.sort(key=lambda candidates: int(candidates[0][1]), reverse=True)
        ##		candidates.sort(key = sortSecond, reverse = True) ######
        best_candidate = candidates[0][0]
        best_candidate_edges = candidates[0][1]

        if best_candidate[1] < current[0][1]:
            current = best_candidate

            if best_candidate[1] < best[1]:
                best = best_candidate
            for i in range(len(best_candidate_edges)):
                tabu_list.append(best_candidate_edges[i])
            while len(tabu_list) > len(tabu_list_size):
                tabu_list.pop()
        #print("iteration/"+ str(irrrr) + ": " + str(i + 1) + "  , Current best: " + str(best[1]))
        #'''''''''
        #print("iteration: ")
        #thisIrr = i + 1
        #print(thisIrr)
        #print("  , best: ")
        #print(best[1])
#'''
    return best


def main_Loop() :
        
    # problem configuration
    berlin52 = read_file()
    
    # algorithm configuration
    max_iter = 1
    tabu_list_size = 30
    max_candidates = 100
    # execute the algorithm
    bestList = []
    bestIndex = 0
    costsList = []
    for i in range(1000):
        bestList.append(search(berlin52, tabu_list_size, max_candidates, max_iter, i))
        costsList.append(bestList[i][1])
    bestIndex = costsList.index(min(costsList))
    best = bestList[bestIndex]
    
    FinalSolutionArr = []
    for i in range(len(best)):
        for j in range(len(best[i])):
            FinalSolutionArr.append(best[i][j])
    global best_Order
    best_Order = list(best[0])
    best_Order.append(int(best[1][0]))
    print(best_Order)
    


    
    
#main_Loop()
    
