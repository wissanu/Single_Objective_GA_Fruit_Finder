# Banana 10 = Ba
# Orange 5 =Or
# Apple. 30 = Ap
# Melon. 50 = Me
# Berry. 55 = Be
# Objective: buy one fruit with in 1000 Baht
# constrain : (x1*ราคา)+(x2*ราคา)+(x_*ราคา)+(xภ*ราคา)+(xถ*ราคา) <= 1,000
# x1,x2,...,x5 = quantity of each product
# ====================

from Fruit.chromosome import Chromosome
from Fruit import reprocude as ga

# -------- Setting parameter --------
gene_num = 5
pop_num = 100
versus = 0.2
max_count_item = 40
number_generation = 100000
# ------------ Don't change ---------------
current_list = []
best_chromosome = []
best_fitness = -1

if __name__ == '__main__':

    # create initial pop
    for _ in range(pop_num):
        g = Chromosome(gene_num, pop_num, max_count_item)
        g.initial_pop()
        current_list.append(g)

    # generation loop start
    for gen in range(1, number_generation+1):
        print('generation', gen)

        next_list = []

        # Do elitism
        if best_fitness != -1:
            current_list[0].chromosome = best_chromosome.copy()
            current_list[0].fitness = best_fitness

        # create next generation
        while len(next_list) < pop_num:

            # select parents
            parent1 = Chromosome.tournament_selection(versus, current_list, pop_num)
            parent2 = Chromosome.tournament_selection(versus, current_list, pop_num)

            # create object child1 and child2
            child1 = Chromosome(gene_num, pop_num, max_count_item)
            child2 = Chromosome(gene_num, pop_num, max_count_item)

            # Do crossover
            child1.chromosome = ga.order_xover_pair(parent1.chromosome, parent2.chromosome)
            child2.chromosome = ga.order_xover_pair(parent2.chromosome, parent1.chromosome)

            # Calculate fitness of child object
            child1.fitness_finder()
            child2.fitness_finder()

            # check duplicate and constraint
            if child1.fitness <= 1000 and len(next_list) < pop_num:
                check_dup = [1 for _ in next_list if child1.chromosome != _.chromosome]
                if sum(check_dup) == len(next_list):
                    next_list.append(child1)

            if child2.fitness <= 1000 and len(next_list) < pop_num:
                check_dup = [1 for _ in next_list if child2.chromosome != _.chromosome]
                if sum(check_dup) == len(next_list):
                    next_list.append(child2)

        # clear memory and reuse current_list
        current_list.clear()
        current_list = next_list.copy()
        del next_list

        # get best chromosome and fitness
        for _ in range(pop_num):
            if best_fitness < current_list[_].fitness:
                best_chromosome = current_list[_].chromosome.copy()
                best_fitness = current_list[_].fitness

        print(current_list)

        # Terminate if meet requirement
        if best_fitness == 1000:
            break

    # ==== Result ====
    print("================")
    print('best chromosome : {!r}'.format(best_chromosome) + '\nbest fitness : {}'.format(best_fitness))
    print('Banana : {} pieces'.format(best_chromosome[0]) + ' per 10 baht')
    print('Orange : {} pieces'.format(best_chromosome[1]) + ' per 5 baht')
    print('Apple : {} pieces'.format(best_chromosome[2]) + ' per 30 baht')
    print('Melon : {} pieces'.format(best_chromosome[3]) + ' per 50 baht')
    print('Berry : {} pieces'.format(best_chromosome[4]) + ' per 55 baht')

