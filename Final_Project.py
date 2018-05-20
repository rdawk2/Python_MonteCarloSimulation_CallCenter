"""
>>> disney = object_creation(7)
>>> print(disney)
[CallCenter('1', '4', '15'), CallCenter('2', '6', '14'), CallCenter('3', '7', '8'), CallCenter('4', '5', '9'), CallCenter('5', '4', '13'), CallCenter('6', '4', '5'), CallCenter('7', '5', '17')]

>>> popup_on_number_of_representative(2, 7, 0, disney)
([CallCenter('3', '7', '8'), CallCenter('4', '5', '9'), CallCenter('5', '4', '13'), CallCenter('6', '4', '5'), CallCenter('7', '5', '17')], [4, 6], 2)

>>> disney = object_creation(7)
>>> print(disney)
[CallCenter('1', '4', '15'), CallCenter('2', '6', '14'), CallCenter('3', '7', '8'), CallCenter('4', '5', '9'), CallCenter('5', '4', '13'), CallCenter('6', '4', '5'), CallCenter('7', '5', '17')]

>>> popup_on_number_of_representative(3, 7, 0, disney)
([CallCenter('4', '5', '9'), CallCenter('5', '4', '13'), CallCenter('6', '4', '5'), CallCenter('7', '5', '17')], [4, 6, 7], 3)

>>> count_zero_occurence_list([0,3,5], disney, 1, 1, 4)
(2, 4, [CallCenter('5', '4', '13'), CallCenter('6', '4', '5'), CallCenter('7', '5', '17')], [3, 5, 5])

>>> count_zero_occurence_list([0,0,5], disney, 2, 1, 4)
(3, 4, [CallCenter('7', '5', '17')], [5, 4, 4])

>>> disney = object_creation(7)
>>> print(disney)
[CallCenter('1', '4', '15'), CallCenter('2', '6', '14'), CallCenter('3', '7', '8'), CallCenter('4', '5', '9'), CallCenter('5', '4', '13'), CallCenter('6', '4', '5'), CallCenter('7', '5', '17')]

>>> call_center_metrics(1,1,[1],7,1,1,1,2,1,2,1,2)
(15.285714285714285, 1, 1, 4.0, 2, 2)

>>> call_center_metrics(2,1,[2,2],7,1,1,1,2,1,2,1,2)
(1, 15.285714285714285, 1, 2, 5.0, 2)

>>> call_center_metrics_for_1000_simulations(1, [], [], 1, 2, 3, 1, 2, 3)
([0.001], [0.001])

>>> call_center_metrics_for_1000_simulations(2, [1], [1], 1, 2, 3, 1, 2, 3)
([1, 0.002], [1, 0.002])

>>> call_center_metrics_for_1000_simulations(3, [1,2], [1,2], 1, 2, 3, 1, 2, 3)
([1, 2, 0.003], [1, 2, 0.003])
"""

import random
import matplotlib.pyplot as plt

class CallCenter(object):

    def __init__(self, num, call_duration, hold_time):
        self.num = num
        self.call_duration = call_duration
        self.hold_time = hold_time

    def __repr__(self):
        return "CallCenter('{}', '{}', '{}')".format(self.num, self.call_duration, self.hold_time)

def object_creation(n):
    """
    function that creates list of object depending on number of callers
    :param n: number of callers:
    :return: list of objects
    """
    d = []
    random.seed(0)
    for i in range(n):
        num = i + 1
        call_duration = int(random.normalvariate(5, 1.5))
        while call_duration <= 0:
            call_duration = int(random.normalvariate(5, 1.5))
        if not call_duration:
            print("I am zero")
        hold_time = int(random.normalvariate(15, 4.5))
        while hold_time <= 0:
            hold_time = int(random.normalvariate(5, 1.5))
        if not hold_time:
            print("I am zero hold")
        disney = CallCenter(num, call_duration, hold_time)
        disney.attr = n
        d.append(disney)
    return d

def popup_on_number_of_representative(rep, n, normal_pop_count, d):
    """
    1 st popup of callers depending on number of representatives
    :param rep: number of representatives
    :param n: number of callers
    :param normal_pop_count: count number of normal pop from list
    :param d: list of objects
    :return: list d of objects, list e to find min wait time and updated count of normal popups
    """
    e = []
    if len(d) == n:
        if rep == 3:
            e.append(d[0].call_duration)
            #print("Normal popup", d[0])
            d.pop(0)
            normal_pop_count += 1
            e.append(d[0].call_duration)
            #print("Normal popup", d[0])
            d.pop(0)
            normal_pop_count += 1
            e.append(d[0].call_duration)
            #print("Normal popup", d[0])
            d.pop(0)
            normal_pop_count += 1
            #print('list of callers assigned for 3 reps', e)
        if rep == 2:
            e.append(d[0].call_duration)
            #print("Normal popup", d[0])
            d.pop(0)
            normal_pop_count += 1
            e.append(d[0].call_duration)
            #print("Normal popup", d[0])
            d.pop(0)
            normal_pop_count += 1
            #print('list of callers assigned 2 reps', e)
        if rep == 1:
            e.append(d[0].call_duration)
            #print("Normal popup", d[0])
            d.pop(0)
            normal_pop_count += 1
            #print('list of callers assigned 1 rep', e)
    return d, e, normal_pop_count

def count_zero_occurence_list(e, d, cnt, normal_pop_count, total_wait_time):
    """
    Function finds out number of o's found in list e(means call is over and remove those callers from list d and append next wait time values in list e
    :param e: list containing wait time depending on number of representatives
    :param d: list of objects
    :param cnt: number of 0's found in list e
    :param normal_pop_count: count number of normal pop from list 
    :param total_wait_time: contains total wait time callers have to wait
    :return:
    """
    if 0 in e:
        if len(d) != 0:
            if cnt == 1:
                e.remove(0)
                e.append(d[0].call_duration)
                d.pop(0)
                normal_pop_count += 1
            if cnt == 2:
                if len(d) > 1:
                    e.remove(0)
                    e.remove(0)
                    e.append(d[0].call_duration)
                    e.append(d[1].call_duration)
                    d.pop(0)
                    normal_pop_count += 1
                    d.pop(0)
                    normal_pop_count += 1
                elif len(d) == 1:
                    e.remove(0)
                    e.append(d[0].call_duration)
                    d.pop(0)

            if cnt == 3:
                if len(d) > 2:
                    e.remove(0)
                    e.remove(0)
                    e.remove(0)
                    e.append(d[0].call_duration)
                    e.append(d[1].call_duration)
                    e.append(d[2].call_duration)
                    d.pop(0)
                    normal_pop_count += 1
                    d.pop(0)
                    normal_pop_count += 1
                    d.pop(0)
                    normal_pop_count += 1
                    total_wait_time += min(e)
                elif len(d) == 2:
                    e.remove(0)
                    e.remove(0)
                    e.append(d[0].call_duration)
                    e.append(d[1].call_duration)
                    d.pop(0)
                    normal_pop_count += 1
                    d.pop(0)
                    normal_pop_count += 1
                    total_wait_time += min(e)
                elif len(d) == 1:
                    e.remove(0)
                    e.append(d[0].call_duration)
                    d.pop(0)
                    normal_pop_count += 1
                    total_wait_time += min(e)
        elif len(d) == 0:
            total_wait_time += min(e)

    return normal_pop_count, total_wait_time, d , e

def call_center_metrics(rep, drop_count, e, n, normal_pop_count, total_wait_time, drop_avg1, average_speed_answer1_1, drop_avg2, average_speed_answer2_2, drop_avg3, average_speed_answer3_3):
    """
    Function to calculate call center metrics of droprate and average speed of answer
    :param rep: number of representatives
    :param drop_count: number of calls dropped
    :param e: list containing wait time depending on number of representatives 
    :param n: number of callers
    :param normal_pop_count: count number of normal pop from list
    :param total_wait_time: contains total wait time callers have to wait
    :param drop_avg1: addition of drop percetage in every iteration for representative = 1
    :param average_speed_answer1_1: addition of average speed of answer in every iteration for representative = 1
    :param drop_avg2: addition of drop percetage in every iteration for representative = 2
    :param average_speed_answer2_2: addition of average speed of answer in every iteration for representative = 2
    :param drop_avg3: addition of drop percetage in every iteration for representative = 3
    :param average_speed_answer3_3: addition of average speed of answer in every iteration for representative = 1
    :return: addition of average speed of answer and drop percentage in every iteration for representative = 1,2,3
    """
    if rep == 1:
        drop1 = (drop_count / n) * 100
        drop_avg1 += drop1
        total_wait_time += min(e)
        average_speed_answer1 = total_wait_time / normal_pop_count
        average_speed_answer1_1 += average_speed_answer1

    if rep == 2:
        drop2 = (drop_count / n) * 100
        drop_avg2 += drop2
        total_wait_time += min(e)
        average_speed_answer2 = total_wait_time / normal_pop_count
        average_speed_answer2_2 += average_speed_answer2

    if rep == 3:
        drop3 = (drop_count / n) * 100
        drop_avg3 += drop3
        total_wait_time += min(e)
        average_speed_answer3 = total_wait_time / normal_pop_count
        average_speed_answer3_3 += average_speed_answer3

    return drop_avg1, drop_avg2, drop_avg3, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3

def call_center_metrics_for_1000_simulations(rep, rep1, rep2, drop_avg1, drop_avg2, drop_avg3, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3):
    """
    Program to calculate call center metrics of droprate and average speed of answer for 1000 simulations
    :param rep:
    :param rep1: list containing average drop rate for representatives 1,2,3 for 1000 simulations
    :param rep2: list containing average speed of answer for representatives 1,2,3 for 1000 simulations
    :param drop_avg1: addition of drop percetage in every iteration for representative = 1
    :param drop_avg2: addition of drop percetage in every iteration for representative = 2
    :param drop_avg3: addition of drop percetage in every iteration for representative = 3
    :param average_speed_answer1_1: addition of average speed of answer in every iteration for representative = 1
    :param average_speed_answer2_2: addition of average speed of answer in every iteration for representative = 2
    :param average_speed_answer3_3: addition of average speed of answer in every iteration for representative = 3
    :return: rep1, rep2
    """
    if rep == 1:
        rep1.append(drop_avg1 / 1000)
        rep2.append(average_speed_answer1_1 / 1000)
    elif rep == 2:
        rep1.append(drop_avg2 / 1000)
        rep2.append(average_speed_answer2_2 / 1000)
    elif rep == 3:
        rep1.append(drop_avg3 / 1000)
        rep2.append(average_speed_answer3_3 / 1000)

    return rep1, rep2

def counter(wait_time, drop_count, d, e, count):
    """
    Function works as a counter to check if wait time is over
    :param wait_time: wait time callers have to wait 
    :param drop_count: number of calls dropped
    :param d: list of objects
    :param e: list containing wait time depending on number of representatives
    :param count: timer count
    :return: wait time, number of calls dropped, list of objects, list e, and timer count
    """
    for member in d:
        if member.hold_time <= wait_time:
            drop_count += 1
            d.remove(member)

    while True:  # starting first loop
        count += 1

        if wait_time == count:
            for member in d:
                member.hold_time = member.hold_time - wait_time
                if member.hold_time <= 0:
                    #print("Droupout counter", member)
                    drop_count += 1
                    d.remove(member)
            e = [x - wait_time for x in e]
            break

    return wait_time, drop_count, d, e, count

if __name__ == '__main__':
    random.seed(0)
    rep2 = []
    rep1 = []
    d = []
    total_wait_time = 0
    for rep in range(1, 4): #Loop for representatives 1,2,3
        drop_avg1 = 0
        drop_avg2 = 0
        drop_avg3 = 0
        average_speed_answer1_1 = 0
        average_speed_answer2_2 = 0
        average_speed_answer3_3 = 0
        for k in range(1000):   # loop for 1000 simulations
            d = []
            e = []
            drop_count = 0
            normal_pop_count = 0
            n = int(random.triangular(4, 20, 50))   #randomly generate number of callers - triangular distribution
            #n = 7
            #print('number of callers', n)
            d = object_creation(n)
            d, e, normal_pop_count = popup_on_number_of_representative(rep, n, normal_pop_count, d)

            drop1 = 0
            drop2 = 0
            drop3 = 0
            average_speed_answer1 = 0
            average_speed_answer2 = 0
            average_speed_answer3 = 0
            total_wait_time = 0

            for i in range(len(d)):
                if len(d) != 0:
                    count = 0
                    wait_time = min(e)
                    total_wait_time = total_wait_time + wait_time
                    wait_time, drop_count, d, e, count = counter(wait_time, drop_count, d, e, count)
                    cnt = e.count(0)
                    normal_pop_count, total_wait_time, d, e = count_zero_occurence_list(e, d, cnt, normal_pop_count,
                                                                                        total_wait_time)
            #print('drop count..', drop_count)
            drop_avg1, drop_avg2, drop_avg3, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3 = call_center_metrics(rep, drop_count, e, n, normal_pop_count,  total_wait_time, drop_avg1, average_speed_answer1_1, drop_avg2, average_speed_answer2_2, drop_avg3, average_speed_answer3_3)

        rep1, rep2 = call_center_metrics_for_1000_simulations(rep, rep1, rep2, drop_avg1, drop_avg2, drop_avg3, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3)

    rep4 = [1, 2, 3]
    fig = plt.figure()

    # To plot Avg dropout Percentage vs No of Reprenstatives
    ax1= plt.subplot(2, 2, 1)
    ax1.scatter(rep4, rep1)
    ax1.set_xlabel('No of Representatives')
    ax1.set_ylabel('Avg. dropout %')
    ax1.set_title('Avg dropout Percentage vs No of Reprenstatives')

    # To plot Avg speed of answer vs No of Reprenstative
    ax2 = plt.subplot(2, 2, 3)
    ax2.scatter(rep4, rep2)
    ax2.set_xlabel('No of Representatives')
    ax2.set_ylabel('Avg. speed of answer')
    ax2.set_title('Avg speed of answer (min) vs No of Reprenstatives')
    plt.tight_layout()
    plt.show()

    print("Program to run Monte Carlo simulation for a Call Center")
    print("\nHypothesis - True: As number of representatives increase Dropout Percentage and Avg wait time decrease")
    print("The lower your Avg speed of answer(ASA) time, the shorter amount of time that your customers are waiting in the queue.")
    # Zip rep4 with rep1, rep2 respectively to display result in tabulur form
    print("\nTable : Number of Representatives and the Avg dropout percentage")
    z = zip(rep4,rep1)
    for k in z:
        print(*k, sep='\t')

    print("\nTable : Number of Representatives and the Avg speed of answer ")
    z = zip(rep4,rep2)
    for x in z:
        print(*x, sep='\t')