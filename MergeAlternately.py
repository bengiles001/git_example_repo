import itertools as it
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        out = word1 + word2
        list1 = [i for i in word1]
        list2 = [i for i in word2]
        test = it.zip_longest(list1, list2)
        result = []
        for i,z in test:
            if i is not None:
                result.append(i)
            if z is not None:
                result.append(z)   
        out = "".join(result)
        """
        loop through first word letter by letter 

        print(zip)
        """
        return out



test = Solution

Solution.mergeAlternately(test, word1 = "abc",word2 = "pqr" )
Solution.mergeAlternately(test, word1 = "ab",word2 = "pqrs" )
Solution.mergeAlternately(test, word1 = "abcd", word2 = "pq")
teststr = "sdf"

list1 = [i for i in teststr]
list1
teststr

print("this is in an example print statement")

z = 2 
y = 3

print(z*y)

print(z+y)