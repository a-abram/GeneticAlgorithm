from random import randint
import time

dictionary = "qwertyuiopasdfghjklzxcvbnm "
inp = input()
population = []
good = {}
quantity = 0
generation = 0
GEN = {'individuals': 50, 'sample': 10, 'mutation': 80}


def randStr():
    return "".join(
        dictionary[randint(0, len(dictionary)-1)] for _ in range(len(inp)))


def check(s):
    temp = 0
    for i in range(len(s)):
        if s[i] != inp[i]:
            temp += 1
    good[s] = temp


def mutation(s):
    num = randint(0, len(s)-1)
    temp = list(s)
    temp[num] = dictionary[randint(0, len(dictionary)-1)]
    s = ''.join(temp)
    return s


def selection(s1, s2):
    num = randint(1, len(s1)//2)
    res = ""
    for i in range(len(s1)):
        if i % 2:
            res += s1[i*num: i*num + num]
        else:
            res += s2[i*num: i*num+num]
    if randint(0, 100) <= GEN["mutation"]:
        res = mutation(res)
    return res

start_time = time.time()
population = [randStr() for _ in range(GEN["individuals"])]
while inp not in population:
    print(population[len(population)-1])
    quantity += len(population)
    good = {}
    for j in range(len(population)):
        check(population[j])
    population = sorted(good, key=lambda x: good[x])[0: GEN["sample"]]
    temp = []
    for j in range(len(population)):
        for j2 in range(j+1, len(population)):
            temp.append(selection(population[j], population[j2]))
    population = temp
    generation += 1
    t = time.time() - start_time
print(inp)
print("Individuals: ", quantity)
print("Generations: ", generation)
print("Time: ", t)
