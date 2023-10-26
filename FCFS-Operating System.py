# Import necessary libraries
import time
import statistics
from scipy.stats import chisquare
import colorama

# Lists to store Average Waiting Time and Average Turn-Around Time for each trial
awt_list = []
atat_list = []

# Function to generate random numbers following a distribution using the chi-square test
def random(n, floor, ceil):
    import random
    while True:
        random.seed(time.time())
        duplication = []
        for i in range(n):
            duplication.append(random.randint(floor, ceil))

        duplicate_dict = {i: duplication.count(i) for i in duplication}
        values = duplicate_dict.values()
        values_list = list(values)
        chi_sq = chisquare(values_list)

        alpha = 0.05
        if chi_sq[1] >= alpha:
            return duplication
        else:
            continue

# Function to calculate Turn-Around Time for each process
def calc_TurnAroundTime(n, burst_time, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Function to calculate Waiting Time for each process
def calc_WaitingTime(n, burst_time, waiting_time, arrival_time):
    waste_time = [0] * n
    waiting_time[0] = 0

    for i in range(1, n):

        waste_time[i] = waste_time[i - 1] + burst_time[i - 1]
        waiting_time[i] = waste_time[i] - arrival_time[i] + arrival_time[0]

        if (waiting_time[i] < 0):
            waiting_time[i] = 0

# Function to calculate and print the average time statistics
def calc_AverageTime(processes, n, burst_time, arrival_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n

    calc_WaitingTime(n, burst_time, waiting_time, arrival_time)
    calc_TurnAroundTime(n, burst_time, waiting_time, turnaround_time)

    print("Processes   Burst Time   Arrival Time   Waiting Time   Turn-Around Time   Completion Time \n")

    total_waiting_time = 0
    total_turnaround_time = 0

    for i in range(n):

        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turnaround_time = total_turnaround_time + turnaround_time[i]
        complete_time = turnaround_time[i] + arrival_time[i]
        
        # Print process details
        print("   P" + str(processes[i]), (10-len(str(processes[i])))*' ', burst_time[i],
              (12-len(str(burst_time[i])))*' ', arrival_time[i], (13-len(str(arrival_time[i])))*' ', waiting_time[i],
              (15-len(str(waiting_time[i])))*' ', turnaround_time[i], (16-len(str(turnaround_time[i])))*' ', complete_time)

    print('\n', "Average waiting time = %.3f " % (total_waiting_time / n))
    awt_list.append(total_waiting_time / n)
    print(" Average turn around time = %.3f " % (total_turnaround_time / n), '\n')
    atat_list.append(total_turnaround_time / n)

# Main program
if __name__ == "__main__":

    n = int(input('enter number of processes: '))
    test = int(input('enter number of trials: '))

    burst_range_ceil = int(input('enter burst time ceiling(for random generation): '))
    arrival_range_ceil = int(input('enter arrival time ceiling(for random generation): '))

    processes = []

    # Generate a list of processes
    for i in range(1, n + 1):
        processes.append(i)

    for j in range(1, test + 1):

        burst_time = random(n, 1, burst_range_ceil)
        time.sleep(1/(test * n))
        arrival_time = random(n, 0, arrival_range_ceil)
        
        # Sort processes based on arrival time
        burst_times = [x for _, x in sorted(zip(arrival_time, burst_time))]
        processes = [y for _, y in sorted(zip(arrival_time, processes))]
        arrival_time.sort()

        # Calculate and display average time statistics for this trial
        calc_AverageTime(processes, n, burst_time, arrival_time)

    # Print summary results
    print(colorama.Fore.RED + "\nRESULTS:")
    print(colorama.Fore.BLUE + "Mean of Average Waiting Time = %.3f " % statistics.mean(awt_list))
    print("Mean of Average Turn-Around Time = %.3f " % statistics.mean(atat_list))
    if test >= 2:
        print("\nStandard deviation of Average Waiting Time = %.3f " % statistics.stdev(awt_list))
        print("Standard deviation of Average Turn-Around Time = %.3f " % statistics.stdev(atat_list))
    print("\nMode of Average Turn-Around Time = %.3f " % statistics.mode(awt_list))
    print("Mode of Average Turn-Around Time = %.3f " % statistics.mode(atat_list))