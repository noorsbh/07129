class Solution(object):
    def romanToInt(self, s):
        order = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        integer = 0
        prevchar = ""
        for char in s[::-1]:
            if prevchar == "":
                integer += order[char]
            elif order[prevchar] > order[char]:
                integer -= order[char]
            else:
                integer += order[char]
            prevchar = char
        return integer