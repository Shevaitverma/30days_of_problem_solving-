'''
Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C/Aux) and N disks. 
Initially, all the disks are stacked in decreasing value of diameter i.e., 
the smallest disk is placed on the top and they are on rod A. 
The objective of the puzzle is to move the entire stack to another rod B with the help of C/Aux, 
and print minimum number of moves as well all setps of disk movement

obeying the following simple rules: 
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack 
i.e. a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.

Input:
N = 2
Output:
move disk 1 from rod A to rod B
move disk 2 from rod A to rod Aux
move disk 1 from rod B to rod Aux
minimum moves = 3
Explanation: For N=2 , steps will be
as follows in the example and total
3 steps will be taken.

Input:
N = 3
Output:
move disk 1 from rod A to rod Aux
move disk 2 from rod A to rod B
move disk 1 from rod Aux to rod B
move disk 3 from rod A to rod Aux
move disk 1 from rod B to rod A
move disk 2 from rod B to rod Aux
move disk 1 from rod A to rod Aux
minimum moves =  7
Explanation: For N=3 , steps will be
as follows in the example and total
7 steps will be taken.

'''

def TowerOfHanoi(N, A_rod, B_rod, Aux_rod):

    # suppose disks are in decreasing order i.e 3 > 2 > 1 (1 is on the top)   

    # case of 0 disks
    if N == 0:
        return 0
    
    # for case of 1 disks
    if N == 1:
        print("Move disk", N, "from ", A_rod, "to ", B_rod)
        return 1
    
    step_count = 0
    # transfer 2 disks from A to C using B
    step_count += TowerOfHanoi(N-1, A_rod, Aux_rod, B_rod)
    print("Move disk", N, "from ", A_rod, "to ", B_rod)
    step_count += 1
    # transfer 2 disks from C to B using A
    step_count += TowerOfHanoi(N-1, Aux_rod, B_rod, A_rod)
    
    return step_count



def main():
    N = 4

    res = TowerOfHanoi(N, "A", "B", "Aux")
    print("minimum moves = ",res)

if __name__ == "__main__":
     main()