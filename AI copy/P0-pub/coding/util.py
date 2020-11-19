##### Filename: util.py
##### Author: David Chen
##### Date: 1/20/20
##### Email: dzc5ta@virginia.edu

import copy

class Util:

    ## Problem 1
    def matrix_multiply(self, x, y):
        ret = []
        for i in range(len(y)):
            ret.append([])
            for j in range(len(x[0])):
                temp = 0
                for k in range(len(x)):
                    temp += x[i][k] * y[k][j]
                ret[i].append(temp)
        return ret

    ## Problem 2, 3
    class MyQueue:
        def __init__(self):
            self.x = []
        def push(self, val):
            self.x.append(val)
        def pop(self):
            if self.x == []:
                return None
            return self.x.pop(0)
        def __eq__(self, other):
            return self.x == other.x
        def __ne__(self, other):
            return not (self.x == other.x)
        def __str__(self):
            return str(self.x)

    class MyStack:
        def __init__(self):
            self.x = []
        def push(self, val):
            self.x.append(val)
        def pop(self):
            if self.x == []:
                return None
            return self.x.pop()
        def __eq__(self, other):
            return self.x == other.x
        def __ne__(self, other):
            return not (self.x == other.x)
        def __str__(self):
            return str(self.x)

    ## Problem 4
    def add_position_iter(self, lst, number_from=0):
        ret = []
        for i in range(len(lst)):
            ret.append(lst[i] + i + number_from)
        return ret

    def add_position_recur(self, lst, number_from=0):
        return add_position_recur_helper(self, lst, number_from, [])
    def add_position_recur_helper(self, lst, number_from, ret):
        if len(ret) == len(lst):
            return ret
        return add_position_recur_helper(self, lst, number_from, ret.append(lst[len(ret)] + len(ret) + number_from))
    def add_position_map(self, lst, number_from=0):
        pass

    ## Problem 5
    def remove_course(self, roster, student, course):
        roster[student].remove(course)
        return roster

    ## Problem 6
    def copy_remove_course(self, roster, student, course):
        temp = copy.deepcopy(roster)
        temp[student].remove(course)
        return temp