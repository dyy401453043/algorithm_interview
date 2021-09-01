class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 递归
        # def my_pow(x, n): # require n > 0
        #     if n == 0:
        #         return 1
        #     elif n == 1:
        #         return x
        #     elif n % 2 == 0:
        #         y = my_pow(x, n//2)
        #         return y * y
        #     else:
        #         y = my_pow(x, int(n//2))
        #         return y * y * x
        # return my_pow(x, n) if n > 0 else 1 / my_pow(x, -n)

        # 迭代
        # k = (I_n-1...I_0)_2
        # k = 2 ** 0 * I_0 + 2 ** 1 * I_1 + ... + 2 ** (n-1) * I_(n-1)
        # x ** k = (x ** 2 ** 0) ** I_0 * (x ** 2 ** 1) ** I_1 *...* (x ** 2 ** (n-1)) ** I_(n-1)
        # 其中
        # x ** 2 ** (j+1) =  x ** (2 **j * 2) = (x ** 2 ** j) ** 2, 故可迭代
        def my_pow_it(x, n):
            str_gin = bin(n)[2:][::-1]
            value = x
            result = 1
            for i in range(len(str_gin)):
                value = value * value if i > 0 else value
                if int(str_gin[i]):
                    result *= value
            return result
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return my_pow_it(x, n) if n > 0 else 1 / my_pow_it(x, -n)
