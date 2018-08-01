class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        l = len(primes)
        p = [0 for _ in range(l)]
        for i in range(n-1):
            min_n = min([res[p[j]] * primes[j] for j in range(l)])
            for k in range(l):
                if min_n == res[p[k]] * primes[k]: p[k] += 1
            res.append(min_n)
        return res[-1]
