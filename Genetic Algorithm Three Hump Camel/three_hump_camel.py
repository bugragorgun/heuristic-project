from math import trunc
import random
import matplotlib.pyplot as plt
import numpy as np

# Variables
# Problemdeki değişkenlerin bu sınırlar arasında olması gerekmektedir.
# X input boundaries
lowerB = -5
upperB = 5

# target function solution
minF = 0

# string lenght
stringLenght = 14

# the precision represented as number of decimals for parameters of the function
populationSize = 200

# maximum number of iterations for each run of algorithm
maxIterations = 200

# probability of mutation for each chromosome
mutationRate = 0.4


# THREE-HUMP CAMEL FUNCTION
def fitnessFunction(x1, x2):
    """
    Calculates THREE-HUMP CAMEL FUNCTION with given two parameters x1 and x2.
    """

    x1dv = decodeFunction(x1)
    x2dv = decodeFunction(x2)
    x1real = scalingFunction(x1dv)
    x2real = scalingFunction(x2dv)

    f = (
        2 * (x1real**2)
        - 1.05 * (x1real**4)
        + ((x1real**6) / 6)
        + (x1real * x2real)
        + (x2real**2)
    )

    return f


def decodeFunction(binaryString):
    ans = 0
    exp = 0

    for i in range(stringLenght):
        if binaryString[i] == "1":
            ans += 2**exp
        exp += 1
    return ans


def scalingFunction(dv):
    precision = (upperB - lowerB) / ((2**stringLenght) - 1)
    return lowerB + precision * dv


def createBinaryString():
    binaryString = ""
    for i in range(stringLenght):
        r = random.randint(0, 1)
        if r == 1:
            binaryString += "1"
        else:
            binaryString += "0"

    return binaryString


def twoPointCrossover(p1, p2):
    """
    Creates two child chromosomes by doing two-point crossover. On the given chromosomes it picks two random points
    and swaps the bits in between the two positions between the parent chromosomes.

    :param h1: first parent chromosome
    :param h2: second parent chromosome
    :return: two new child chromosomes
    """
    # r1 ve r2 noktaların indexi belirlediği

    r1 = random.randrange(1, len(p1) - 1)
    while True:
        r2 = random.randrange(1, len(p1) - 1)
        if r1 != r2:
            break

    c3 = p1[0 : min(r1, r2)] + p2[min(r1, r2) : max(r1, r2)] + p1[max(r1, r2) : len(p1)]
    c4 = p2[0 : min(r1, r2)] + p1[min(r1, r2) : max(r1, r2)] + p2[max(r1, r2) : len(p2)]

    return c3, c4


def localMutation(chromosome, probability):
    """
    Creates a mutated chromosome by doing inversion with given probability. It is done by picking two random points on
    chromosome and flipping its bits in between the two points.

    :param chromosome: chromosome for mutation
    :param probability: mutation probability level
    :return: mutated chromosome
    """
    if random.random() <= probability:
        r1 = random.randrange(1, len(chromosome) - 1)
        if chromosome[r1] == "1":
            chromosome[r1] == "0"
        else:
            chromosome[r1] == "1"
    return chromosome


def tournamentSelection(fitnessFunction, population, t_size):
    """
    Returns parameters of chromosome that won the competition (has the best loss function) from specified number of
    chromosomes in population, where each of them have equal chances to participate in competition.

    :param f_loss: loss function
    :param population: chromosomes population
    :param t_size: size of tournament for selection
    :return: parameters with best loss
    """
    chosen_x1 = []
    chosen_x2 = []
    for i in range(t_size):
        # chooses random t_size chromosomes from population
        r = random.randrange(len(population))
        chosen_x1.append(population[r][0])
        chosen_x2.append(population[r][1])

    best_x1 = 0
    best_x2 = 0
    best_result = 0
    for i in range(t_size):
        curr_result = fitnessFunction(chosen_x1[i], chosen_x2[i])
        if best_x1 == 0 or curr_result < best_result:
            best_result = curr_result
            best_x1 = chosen_x1[i]
            best_x2 = chosen_x2[i]
    return best_x1, best_x2


def elitistMethod(n_pop):
    # en iyi 200 birey her zaman elinde
    # elitist
    # bir önceki popülasyonla ürettiğim popülasyonu bir arrayde topluyorum --- n_pop
    # fitnessFunction değerine göre
    # 2D array [[birey(x1,x2)],[fitnessresult]]
    # hem x1,x2 yi hemde fitness sonucu tek bir arraya atılır
    fitnessCalculation = []
    for i in n_pop:
        arr = []
        arr.append(i[0])
        arr.append(i[1])
        arr.append(fitnessFunction(i[0], i[1]))
        fitnessCalculation.append(arr)

    # array numpy array olmak zorundadır çünkü sadece numpy array bir sütuna göre sıralamamızı sağlar
    fitnessCalculation = np.array(fitnessCalculation)
    # sıralama yapılır ve populasyon sizeı kadarı tutulur sadece. Bu sıralama fitnessdan gelen sonuca göre yapılır ve en iyi 200 popülasyonumuz olucaktır
    fitnessCalculation = fitnessCalculation[fitnessCalculation[:, 2].argsort()][
        :populationSize
    ]
    # yeni popülasyon variable oluşturulur
    population = []
    for i in fitnessCalculation:
        population.append((i[0], i[1]))
    return population


def geneticAlgorithm():
    best = None
    best_result = None
    population = []
    t = 0

    # popülasyonun oluşturulması 200 tane random (x1 ve x2) değerleri oluşturulur..
    for j in range(populationSize):
        x1 = createBinaryString()
        x2 = createBinaryString()
        population.append((x1, x2))

    # iterasyon sayısını tutmak için t değişkeni arttırılıyor
    # max iterasyona kadar
    while t < maxIterations:
        # new populasyona oluşturulan popülasyon kopyalanır
        n_pop = population[:]

        # yeni gen için bir 200 bireyin daha eklenmesi lazım
        while len(n_pop) < populationSize * 2:
            # tournament selection
            p1 = tournamentSelection(fitnessFunction, population, 2)
            p2 = tournamentSelection(fitnessFunction, population, 2)
            # crossover
            c3, c4 = twoPointCrossover(p1[0] + p1[1], p2[0] + p2[1])
            # mutation
            c3 = localMutation(c3, mutationRate)
            c4 = localMutation(c4, mutationRate)
            # adding new chromosomes to population
            n_pop.append((c3[:stringLenght], c3[stringLenght:]))
            n_pop.append((c4[:stringLenght], c4[stringLenght:]))

        population = elitistMethod(n_pop)

        # elimizdeki en iyi sonucun fitness fonksiyon cevap -- curr_loss
        curr_result = fitnessFunction(population[0][0], population[0][1])

        # eğer elimizdeki en iyi ---best_loss mevcutsa ve curr_lossdan daha kötüyse o zaman en iyisi artık elimizdekidir.
        # o yüzden en iyi sonucu değiştiririz ve yeni bestimiz elimizdeki olur
        if best_result is None or curr_result < best_result:
            best_result = curr_result
            best = population[0]

        # elimizdeki en iyi sonuç ekrana yazdır her iterasyon için
        # decode
        x1dv = decodeFunction(best[0])
        x2dv = decodeFunction(best[1])
        x1real = scalingFunction(x1dv)
        x2real = scalingFunction(x2dv)
        print(
            "Gen:", t, "\nBest chromosome:", best, "\nx:", x1real, "\ny:", x2real, "\n"
        )

        # iterasyonu b,r artırırız
        t += 1

        # en iyisini bulursan sal
        if best_result <= minF:
            break

    print("------------------------------------------------")
    print("--> Total Iterations:", t)
    print("------------------------------------------------")
    x1dv = decodeFunction(best[0])
    x2dv = decodeFunction(best[1])
    x1real = scalingFunction(x1dv)
    x2real = scalingFunction(x2dv)

    print("--> Best Solution:", best, "\nx1:", x1real, "\nx2:", x2real)
    print("------------------------------------------------")
    print("--> Best Fitness Function Result:", best_result)
    print("------------------------------------------------")


if __name__ == "__main__":
    geneticAlgorithm()
