#!/usr/bin/env python3

# Dependencies
import math

# Check num:
def check_num(n: str) -> (int | bool):
    try:
        n_list = n.split(',')
        nums = []
        for i in n_list:
            n = int(i)
            nums.append(n)
        return nums
    except ValueError:
        return False
    
# Calc Average of Num List
def calc_average(n: list) -> float:
    try:
        sum_n = 0
        len_list = len(n)
        for i in n:
            sum_n += i

        average = sum_n / len_list
        return average, len_list
    
    except Exception as e:
        print(f"ERROR while calculating average of numbers: {e}")
        exit()

# Calc Standar deviation
def calc_standar_deviation(average, len_list, n_list):

    try:
        top = 0
        for i in n_list:
            top += (i - average) ** 2
        
        s = math.sqrt(
            (top / (len_list-1)
        ))

        return s
    
    except Exception as e:
        print(f"ERROR while calculating standar deviation of numbers: {e}")
        exit()

# Main function
def main():
    nums = input("Introduce a list of numbers (separated by commas): ").strip().replace(' ', '')
    nums = check_num(nums)
    if nums:
        average_results = calc_average(nums)
        average = average_results[0]
        len_list = average_results[1]

        standar_deviation = calc_standar_deviation(average, len_list, nums)
        
        print(f"\n- Average = {average}")
        print(f"- Standar Deviation = {standar_deviation}")
        
    else:
        print("ERROR: You haven't introduced the numbers in the correct format.")

# Main function
if __name__ == '__main__':
    main()