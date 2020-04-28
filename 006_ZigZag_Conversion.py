'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        if numRows <= 1:
            return s
        out_string = [""] * numRows
        for i in range(0, len(s), 2 * numRows - 2):
            
            for j in range(i, i + numRows):
                if j >= len(s):
                    break
                out_string[j - i] += s[j]
            for k in range(i + numRows, i + 2 * numRows -2):
                if k >= len(s):
                    break
                out_string[i + 2 * numRows -2 - k] += s[k]
        out_string = "".join(out_string)
        return out_string
