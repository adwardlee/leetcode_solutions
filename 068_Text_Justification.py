'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = ''
        self.final = []
        self.maxWidth = maxWidth
        for idx, x in enumerate(words):
            if idx == 0:
                line = x
            elif len(line) + len(x) >= maxWidth:
                self.padWords(line, False)
                line = ''
                line += x
            else:
                if line == '':
                    line += x
                else:
                    line += ' ' + x
        if line != '':
            self.padWords(line, True)
        return self.final
        
            
            
    def padWords(self, line, last):
        length = 0
        output = ''
        split_line = line.split(' ')
        for x in split_line:
            length += len(x)
        num = len(split_line)
        if num == 1:
            output = split_line[0] + ' ' * (self.maxWidth - len(line))
        elif last == True:
            output = line + ' ' * (self.maxWidth - len(line))
        else:
            avg_spaces = [' ' * ((self.maxWidth - length) // (num - 1))] * (num - 1)
            extra = self.maxWidth - length - (self.maxWidth - length) // (num - 1) * (num - 1)
            for i in range(extra):
                avg_spaces[i] += ' '
            output = split_line[0]
            for idx, x in enumerate(avg_spaces):
                output += x + split_line[idx + 1]
        self.final.append(output)
