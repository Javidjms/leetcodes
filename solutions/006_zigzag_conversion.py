class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        z_index = 2 * numRows - 2
        output = s[::z_index]
        for i in range(1, numRows-1):
            for j in range(math.ceil(len(s)/z_index)+1):
                if z_index*j-i > 0 and z_index*j-i < len(s):
                    output += s[z_index*j-i]
                if z_index*j+i > 0 and z_index*j+i < len(s):
                    output += s[z_index*j+i]   
        output += s[numRows-1::z_index]
        return output