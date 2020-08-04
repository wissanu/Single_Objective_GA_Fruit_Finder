from random import sample, randint


class Chromosome:

    def __init__(self, x_gene, x_pop, max_count_item):
        self.chromosome = []
        self.gene_num = x_gene
        self.pop_num = x_pop
        self.fitness = 0
        self.equation_input = [10, 5, 30, 50, 55]
        self.max_count_item = max_count_item

    def __repr__(self):
        return '\nchromosome :{!r}'.format(self.chromosome) + '\nfitness: {!r}'.format(self.fitness)

    def initial_pop(self):
        while True:
            self.chromosome = sample(range(0, self.max_count_item), self.gene_num)
            self.fitness_finder()
            if self.fitness <= 1000:
                break

    def fitness_finder(self):
        temp = []
        for x, y in zip(self.chromosome, self.equation_input):
            k = x * y
            temp.append(k)
        self.fitness = sum(temp)

    @staticmethod
    def tournament_selection(versus, chromosome, pop_num, max_count_item):
        k = [randint(0, max_count_item) for _ in range(int(versus * pop_num))]
        best = []
        for _ in k:
            if not best or best.fitness < chromosome[_].fitness:
                best = chromosome[_]
            return best
