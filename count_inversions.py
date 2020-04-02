from arguments import Arguments


class InversionCounter:
    def __init__(self, arg):
        print('--> Preprocessing the input!')
        self.array = self.preprocess(arg)
        self.n = len(self.array)

        self.temp = [0] * self.n

    def preprocess(self, arg):
        arg[0] = arg[0].replace('[', '')
        arg[-1] = arg[-1].replace(']', '')

        arg = list(map(lambda x: int(x), arg))
        return arg

    def run(self):
        print('--> Counting inversions in a length {} array'.format(self.n))

        inversion_count = self.count_inversions(self.array, self.temp, 0, self.n - 1)

        print('Found {} inversions!'.format(inversion_count))

    def count_inversions(self, array, temp, l, r):
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
        count += self.count_inversions(array, temp, l, mid)
        count += self.count_inversions(array, temp, mid + 1, r)

        # Merge sub-arrays while counting inversions
        count += self.merge_and_count(array, temp, l, r, mid)

        return count

    def merge_and_count(self, array, temp, l, r, mid):
        """
        Merges two sorted arrays while counting the number of inversions that
        will occur in the resulting array
        """

        i = l
        j = mid + 1
        k = l

        count = 0

        while i <= mid and j <= r:
            # No inversion found
            if array[i] < array[j]:
                # Sort original array and move the left pointer forward
                temp[k] = array[i]
                i += 1

            # Inversion found
            else:
                # Since both subarrays are sorted, if an element in the left subarray is larger
                # than one in the right subarray, we know the remainder of the elements in the left
                # subarray will also be larger than this element of the right subarray, resulting in
                # a number of inversions equal to the number of elements remaining in the left subarray
                count += (mid - i + 1)

                # Sort original array and move the right pointer forward
                temp[k] = array[j]
                j += 1

            # Move pointer for sorted array forward
            k += 1

        # Copy any remaining elements from either left or right subarrays to the original array
        while i <= mid:
            temp[k] = array[i]
            i += 1
            k += 1

        while j <= r:
            temp[k] = array[j]
            j += 1
            k += 1

        for i in range(l, r + 1):
            array[i] = temp[i]

        return count


if __name__ == '__main__':
    arguments = Arguments()

    args = arguments.parse()

    array = args.array

    inversion_counter = InversionCounter(array)
    inversion_counter.run()
