class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            ('M',),
            ('C', 'D', 'M'),
            ('X', 'L', 'C'),
            ('I', 'V', 'X'),
        ]

        output = ""
        curr = num
        for i in range(4):
            count, curr = divmod(curr, int(10**(3-i)))

            if count <= 3:
                output += symbols[i][0]*count
            elif count == 4:
                output += symbols[i][0]+symbols[i][1]
            elif count == 5:
                output += symbols[i][1]
            elif count > 5 and count < 9:
                output += symbols[i][1]+symbols[i][0]*(count-5)
            elif count == 9:
                output += symbols[i][0]+symbols[i][2]
        return output