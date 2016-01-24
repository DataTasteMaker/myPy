"""
File Name           : MergeList.py
Designed by         : Viraj (vb.bviraj@gmail.com)
Created on          : 24-01-2016
Last Updated        : 24-01-2016
Current Version     : V0_24012016 (Version number + Last Updated Date)
                    : V0 - Initial setup
"""


def merge2list(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while True:
        if i == len(list1):
            return merged_list + list2[j:]
        if j == len(list2):
            return merged_list + list1[i:]
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

a = [1,7,8,9,12]
b = [2,4,5,6,18,22]

print("\n List 1 -- " + str(a))
print("\n List 2 -- " + str(b))

print("\n Merged list -- " + str(merge2list(a,b)))
    