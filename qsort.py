#!/usr/bin/python
# encoding:utf-8


def quick_sort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quick_sort(lst, lo, p)
        quick_sort(lst, p + 1, hi)
    return lst


def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    if pivot < lst[i]:
        lst[i], lst[hi-1] = pivot, lst[i]
    return i


if __name__ == '__main__':

    input_nums = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    print input_nums
    print quick_sort(input_nums, 0, len(input_nums))
