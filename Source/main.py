from random import randint

dictionary = "qwertyuiopasdfghjklzxcvbnm "

#settings
individuals = 50
sample = 10
mutation = 80


class Gen():
    def __init__(self, _text=None, _len=0):
        if _text:
            self.text = _text
        else:
            self.text = "".join(
                dictionary[randint(0, len(dictionary)-1)] for _ in range(_len))

    def __len__(self):
        return len(self.text)

    def __getitem__(self, val):
        print(val)

    def check(self):
        temp = 0
        for i in range(len(self.text)):
            if self.text[i] != inp.text[i]:
                temp += 1
        return temp

    def mutation(self):
        num = randint(0, len(self.text)-1)
        temp = list(self.text)
        temp[num] = dictionary[randint(0, len(dictionary)-1)]
        self.text = ''.join(temp)


def selection(s1, s2):
    num = randint(1, len(s1)//2)
    text = ""
    for i in range(len(s1)):
        if i % 2:
            text += s1.text[i*num: i*num + num]
        else:
            text += s2.text[i*num: i*num+num]
    newGen = Gen(text, len(s1))
    if randint(0, 100) <= mutation:
        newGen.mutation()
    return newGen


def check(listGens, genSearch):
    result = True
    for i in listGens:
        if i.text == genSearch.text:
            result = False
            break
    return result

def main():
    global population
    while check(population, inp):
        print(population[len(population)-1].text)
        population = sorted(population, key=lambda x: x.check())[0:sample]
        temp = []
        for j in range(len(population)):
            for j2 in range(j+1, len(population)):
                temp.append(selection(population[j], population[j2]))
        population = temp
    print(inp.text)


if __name__ == '__main__':
    temp = input()
    inp = Gen(temp, len(temp))
    population = [Gen(_len=len(temp)) for _ in range(individuals)]
    main()
