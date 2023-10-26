# Processor Scheduling Algorithms

A typical program requires both CPU and I/O for execution. In multi-programming systems, it's possible to manage programs in a way where one program utilizes the CPU while another one waits for I/O. This situation is achieved through the use of processor scheduling algorithms. In this documentation, we will discuss the First-Come-First-Serve (FCFS) algorithm.

## FCFS Algorithm

The FCFS (First-Come-First-Serve) algorithm is one of the processor scheduling algorithms that operates based on the arrival time of programs. It assigns CPU time to programs in the order they arrive. It is implemented using a First-In-First-Out (FIFO) queue. When programs enter the ready queue, their control block is placed at the end of the queue. When the CPU becomes available, it is allocated to the program at the front of the queue.

As the program executes, it is removed from the queue. FCFS is a non-preemptive scheduling algorithm, meaning it doesn't interrupt the execution of a program once it has started.

## Code Simulation

The purpose of the provided code is to simulate the execution of the FCFS algorithm and analyze the resulting time metrics in various scenarios.

Please refer to the code for a practical implementation of the FCFS algorithm and its analysis in different situations.

# Example Input and Output

Here's an example of the program's input and output:

- Number of processes: 10
- Number of trials: 100
- Upper limit for randomly generated numbers: 10
- Randomly generated numbers range between 1 and 0 in this case.

This example demonstrates how the program operates with the provided input values.
![image](https://github.com/Hossein-Nzari/OS-FSCS-algorithm/assets/64418976/4c93be6d-a03f-44f8-80b3-294813865a0d)


In the image below, the results of an experiment are visible, where programs and their information have been displayed in priority order. At the end, the average waiting time and turnaround time for this experiment have been calculated.
![image](https://github.com/Hossein-Nzari/OS-FSCS-algorithm/assets/64418976/9023a6d2-2c02-4653-a645-eef990338a19)


In the final output, the results of all experiments are examined, and their averages, standard deviations, and modes are carefully printed with three decimal places.
![image](https://github.com/Hossein-Nzari/OS-FSCS-algorithm/assets/64418976/aae290fd-bd2a-4338-a921-209c26244020)
