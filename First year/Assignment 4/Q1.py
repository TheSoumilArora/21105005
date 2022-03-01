count = 0
def towerofhanoi(n, initial_rod, final_rod, extra_rod):
    global count
    if n == 0:                                                                                          #Base case
        return
    count += 1
    towerofhanoi(n-1, initial_rod, extra_rod, final_rod)                                                #Recursive call
    print("Move disk",n,"from rod",initial_rod,"to rod",final_rod)
    towerofhanoi(n-1, extra_rod, final_rod, initial_rod)

no_of_discs = int(input("Number of discs: "))
print("\nA is the initial rod\nB is the extra rod\nC is the final rod\n\nSteps:")
towerofhanoi(no_of_discs, 'A', 'C', 'B')
print("\nNumber of steps will be: %d" % (count))