'''
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
s consists of digits only.

'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        self.final = []
        self.backtrace([], s, 4)
        return self.final
    
    def backtrace(self, cur_s, remain_s, num):
        if num == 0 and len(remain_s) == 0:
            tmp = ''
            for x in cur_s:
                tmp += x + '.'
            tmp = tmp[:-1]
            self.final.append(tmp)
            return 
        if (num == 0 and len(remain_s) > 0) or (num >0 and len(remain_s) <= 0):
            return
        for i in range(3):
            if i + 1 > len(remain_s):
                return 
            elif i > 0 and int(remain_s[0]) == 0:
                continue
            elif i == 2 and int(remain_s[:i+1]) > 255:
                continue
            else:
                self.backtrace(cur_s + [remain_s[:i+1]], remain_s[i+1:],num - 1)
            
        return 
        
