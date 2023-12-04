class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        has_read_whitespace = False
        sign_str = ""
        current_number_str = ""
        while True:
            if i >= len(s):
                break

            if not has_read_whitespace and s[i] == " ":
                i +=1
                continue

            if not has_read_whitespace and s[i] != " ":
                has_read_whitespace = True

            if not sign_str and s[i] in ["+", "-"]:
                sign_str = s[i]
                i +=1
                continue

            if not sign_str and s[i].isdigit():
                sign_str = "+"

            if s[i].isdigit():
                current_number_str += s[i]
                i +=1
                continue
            else:
                break

        if not current_number_str:
            return 0
        parsed_int = int(current_number_str) * (-1 if sign_str == "-" else 1)
        if parsed_int < -2**31:
            return -2**31
        if parsed_int > 2**31-1:
            return 2**31-1
        return parsed_int
