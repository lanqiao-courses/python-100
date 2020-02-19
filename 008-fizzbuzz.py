class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 1:
            raise ValueError('num cannot be less than one')
        results = []
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results