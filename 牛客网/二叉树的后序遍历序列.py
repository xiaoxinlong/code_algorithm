class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return True
        if len(sequence) == 1:
            return True

        temp = sequence[-1]
        i = 0
        while sequence[i] < temp:
            i += 1
        for j in range(i, len(sequence)-1):
            if sequence[j] < temp:
                return False
        left, right = True, True
        if i>0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i<len(sequence):
            right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
        return left or right