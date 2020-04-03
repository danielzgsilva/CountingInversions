import sys
import re


# from timeit import default_timer as timer
# import psutil
# import os


class InversionCounter:
    def __init__(self, arg):
        self.array = self.preprocess(arg)
        self.n = len(self.array)

        self.temp = [None] * self.n

    def preprocess(self, input):
        # Build input array from stdin
        array = []
        for line in input:
            for ele in line.split():
                re.sub('\D', '', ele)
                if type(ele) is str:
                    ele = int(ele.replace('[', '').replace(']', ''))

                array.append(ele)

        return array

    def run(self):
        # start = timer()
        inversion_count = self.count_inversions(0, self.n - 1)

        print(inversion_count)

        # end = timer()
        # print('Execution time: {} seconds'.format(round(end-start, 5)))

        # process = psutil.Process(os.getpid())
        # print('Memory usage: {} mb'.format(process.memory_info().rss * 0.000001))
        return inversion_count

    def count_inversions(self, l, r):
        """
        Counts the number of inversions found in the given array
        """

        # Base case
        if l >= r:
            return 0

        count = 0

        # Split array
        mid = (r + l) // 2

        # Recursively split sub-arrays
        count += self.count_inversions(l, mid)
        count += self.count_inversions(mid + 1, r)

        # Merge sub-arrays while counting inversions
        count += self.merge_and_count(l, r, mid)

        return count

    def merge_and_count(self, l, r, mid):
        """
        Merges two sorted arrays while counting the number of inversions that
        will occur in the resulting array
        """

        i = l
        j = mid + 1
        cur = l

        count = 0

        while i <= mid and j <= r:
            # No inversion found
            if self.array[i] < self.array[j]:
                # Place element in correct position in temporary array and move left pointer forward
                self.temp[cur] = self.array[i]
                i += 1

            # Inversion found
            else:
                # Since both subarrays are sorted, if an element in the left subarray is larger
                # than one in the right subarray, we know the remainder of the elements in the left
                # subarray will also be larger than this element of the right subarray, resulting in
                # a number of inversions equal to the number of elements remaining in the left subarray
                count += (mid - i + 1)

                # Place element in correct position in temporary array and move right pointer forward
                self.temp[cur] = self.array[j]
                j += 1

            # Move pointer for sorted array forward
            cur += 1

        # Copy any remaining elements from either left or right subarrays to the original array
        while i <= mid:
            self.temp[cur] = self.array[i]
            i += 1
            cur += 1

        while j <= r:
            self.temp[cur] = self.array[j]
            j += 1
            cur += 1

        self.array[l:r + 1] = self.temp[l:r + 1]

        return count


if __name__ == '__main__':
    inversion_counter = InversionCounter(sys.stdin)
    inversion_counter.run()
