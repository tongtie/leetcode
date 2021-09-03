# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

 

# Example 1:

# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
# Example 2:

# Input: n = 1
# Output: [0,1]
 

# Constraints:

# 1 <= n <= 16

class Solution:
    #def grayCode(self, n: int) -> List[int]:
    # 笨方法
    def grayCode(self, n):
        import copy
        from collections import defaultdict
        from functools import reduce
        if n == 1:
            return [0, 1]
        biggest = (1 << n) - 1
        record = defaultdict(set)
        # 先计算出每个数与2n的gray code
        for i in range(0, biggest):
            j = 0
            m = 1 << j
            while m + i <= biggest:
                if m & i == 0:
                    record[i].add(m+i)
                    record[m+i].add(i)
                j += 1
                m = 1 << j
        record[0].add(1)
        record[1].add(0)

        def help(current, adjacent, result):
            not_match_number = []
            if len(result) == biggest + 1:
                return result
            for i in adjacent:
                # 可以回到0（是0的gray code）
                if i == 0:
                    if len(current) > len(result):
                        result = copy.copy(current)
                elif i not in current:
                    current.insert(1, i)
                    result = help(current, record[i], result)
                    current.pop(1)
            return result
        # 从0开始，依次输入，当前gray code列表，当前值的gray code数组
        result = help([0], record[0], [])
        return result

    # https://wenku.baidu.com/view/340671ef69dc5022abea005e.html
    # 数学方法
    # o(N)
    def grayCode2(self, n):
        result = []
        for i in range(1 << n):
            result.append(i ^ (i >> 1))
        return result
    # https://www.cnblogs.com/grandyang/p/4315649.html
    # n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的方式快速的得到.(回溯法)
    # n=2: 2
    # n=3: 2 + 4
    # n=4: 2 + 4 + 8
    # o(N)
    def grayCode3(self, n):
        if n == 0:
            return [0]
        result = [0, 1]
        for i in range(1, n):
            result += [x + 2 ** i for x in result[::-1]]
        return result
    # 递归
    # 解释器做了优化，占用内存更小
    def grayCode4(self, n):
        if n == 0:
            return [0]
        result = self.grayCode(n - 1)
        result += [x + 2 ** (n - 1) for x in result[::-1]]
        return result
    # 笨方法
    # 时间最慢
    # 2: 3 * 2
    # 3: 7 * 3
    # 4: 15 * 4
    # 5: 31 * 5
    # 6: 63 * 6
    # 7: 127 * 7
    # 8: 255 * 8
    # 9: 511 * 9
    # 10: 1023 * 10
    # 11: 2047 * 11
    # 12: 4095 * 12
    # 13: 8191 * 13
    # 14: 16383 * 14
    # 15: 32767 * 15
    # 16: 65535 * 16
    # o(N2)
    def grayCode5(self, n):
        unique_set, result = {0}, [0]
        if n == 0:
            return result
        for i in range(1, 1 << n):
            c = result[-1]
            for j in range(n):
                if c & (1 << j) == 0:
                    gray_code = c | (1 << j)
                else:
                    gray_code = c & ~(1 << j)
                if gray_code not in unique_set:
                    result.append(gray_code)
                    unique_set.add(gray_code)
                    break
        return result


if __name__ == '__main__':
    for i in range(2, 6):
        print(i)
        print('grayCode1')
        print(Solution().grayCode(i))
        print('grayCode2')
        print(Solution().grayCode2(i))

