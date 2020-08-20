'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        nums = [str(i) for i in range(10)]
        signs = ['+', '-']
        flag_e = -1
        flag_sign = False
        flag_num = False
        flag_dot = False
        for idx, x in enumerate(s):
            if x in nums:
                flag_num = True
            elif x in signs:
                if idx == 0:
                    flag_sign = True
                elif flag_e > 0 and idx == flag_e + 1 and idx < len(s) - 1:
                    flag_sign = True
                else:
                    return False
            elif x == 'e':
                if idx == 0:
                    return False
                elif flag_num == False:
                    return False
                        
                elif flag_e == -1:
                    flag_e = idx
                else:
                    return False
            elif x == '.':
                if flag_e != -1:
                    return False
                elif flag_num == True and flag_dot == False:
                    flag_dot = True
                elif idx == 0 or (idx == 1 and flag_sign == True):
                    flag_dot = True
                else:
                    return False
            else:
                return False
        if flag_e == (len(s) - 1):
            return False
        return flag_num
