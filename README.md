# Single_Objective_GA_Fruit_Finder

Finding a total pieces of five fruit that won't exceed 1000 baht.
In each of fruit has cost.


Method included
- cycle crossover
- Tournament Selection ( the candidate is 20% from total population )
- Elitism


Constrain
- 0 <= x1,x2,x3,x4,x5 <= 15
- (x1*cost1) + (x2*cost2) + (x2*cost3) + (x3*cost4) + (x4*cost5) <= 1000
- cost1 = 10
- cost2 = 5
- cost3 = 30
- cost4 = 50
- cost5 = 55
