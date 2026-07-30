'''
understand:
- input: numbers (array of ints, sorted in ascending order)
         target: int
- output: lst of 2 1- indexed indices where the vals add up to target

- limitations: index1 != index2, o(1) memory, o(n) time

plan:
- slow pointer: starts at position 0
- fast pointer: starts at position 1
- length = len(numbers) - 1
- if numbers[slow] + numbers[fast] = target return [slow + 1, fast + 1]
- elif fast < length fast +=1
- else slow +=1, fast = slow + 1
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers) - 1

        while True:

            if numbers[beg] + numbers[end] > target:
                end -= 1
            elif numbers[beg] + numbers[end] < target:
                beg +=1
                end = len(numbers)-1
            else:
                return [beg + 1, end + 1]
        