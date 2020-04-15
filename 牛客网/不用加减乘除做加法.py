MAX_BIT = 2 ** 32
MAX_BIT_COMPLIMENT = -2 ** 32
class Solution:
    @classmethod
    def Add(self, num1, num2):
        print(hex(num1),hex(num2),hex(MAX_BIT),hex(MAX_BIT_COMPLIMENT))
        while num2:
            if num2 == MAX_BIT:
                return num1 ^ MAX_BIT_COMPLIMENT
            carry = num1 & num2
            num1 = num1 ^ num2
            num2 = carry << 1
            print(hex(num1),hex(num2),carry)

        return num1

if __name__=='__main__':
    print(Solution.Add(-1,200000))