# Python_MonteCarloSimulation_CallCenter

# Title: MONTE CARLO SIMULATION FOR CUSTOMER CARE SERVICE

## Team Member(s):
Aditi Alankrita - aditia3

Rujuta Dawkhar - rdawk2

# Monte Carlo Simulation Scenario & Purpose:
The monte carlo scenario which we are planning to simulate is of a customer care service center. Everytime we have any complaint regarding any service we use, we tend to call the customer care service available for the product. During the calls we are always placed on hold till our turn arrives. 

In this simulation we are randomly trying to generate customers in queue with a certain wait time(time for which the customer is willing to wait in queue - patience time) and call duration assigned  to them. Our aim is to test if the dropout rate and wait time reduce if the number of call center representatives increase.

## Simulation's variables of uncertainty
The random variable we are considering are:
(i) call duration of the customer/ service time - Normal Distribution
(ii) time for which the customer is willing to wait - Normal Distribution
(iii) Number of callers - Triangular distribution

There will be call drops because people will lose patience and cut calls.
The simulation will help us prove that increase in number of representatives is needed to reduce the call drops and wait time.

## Hypothesis or hypotheses before running the simulation:
We are assuming as the number of representatives increase, there would be less wait time and less call drops.
We are calculating 2 factors here,
1. Percentage drop = No. of call drops / Total number of customers
   where call drop is the number of calls that do not reach the customer care representative.
2. ASA(Average Speed of Answer) = Total Waiting Time for Answered Calls/Total Number of Answered Calls
   The lower your ASA time, the shorter amount of time that your customers are waiting in the queue.

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

Assumptions made:
All representatives have the same efficiency.
There is no rest time for the representatives.
Every customer will have atleast 1min of time for which they will be willing to wait.
The customer will be served on first come first serve basis.
There is only one single queue for customers.
Every list of callers generated will have atleast 4 callers.

## Instructions on how to use the program:
The program has been written for 1000 simulations for number of representatives = 1/2/3
We are then finidng out call center metrics and displaying it in the form of a table and plot.
The calculation shows that as the number of representatives increase (from 1 to 3) the avergae dropout rate and wait time will be decreased.

Output of code which supports hypothesis:
Table : Number of Representatives and the Avg dropout percentage

1 	 -  78.18452380952391

2	 -  62.11309523809534

3	 -  50.05952380952353

Table : Number of Representatives and the Avg speed of answer 

1	-   4.916666666666667

2	-   2.674999999999975

3	-   1.7211538461538372


## All Sources Used:

(i) https://link.springer.com/article/10.1057%2Fdddmp.2011.25

