from typing import DefaultDict, List
def topKFrequent(nums: List[int], k:int) -> List[int]:
    """
    d = DefaultDict(int)
    for item in nums:
        d[item] += 1
    l = list(sorted(d.items(), key = lambda x: x[1],reverse=True))
    return [x[0] for x in l[:k]]
    """
    # O(nlogn), dominated by the sorting
    # O(n)

    ################################### ###################################
    # O(n) solution via bucket sort:
    # 1. count frequencies O(n)
    frequencies = DefaultDict(int) # lookup failures will be populated with a default int of 0
    for item in nums:
        frequencies[item] += 1

    n = len(nums)

    # 2. create buckets (index = frequency) O(n)
    buckets = [[] for _ in range(n+1)]
    for num, frequency in frequencies.items():
        buckets[frequency].append(num)

    # 3. collect k most frequent items O(n)
    result = []
    while n > -1 and k > 0:
        if buckets[n]:
            result.append(buckets[n].pop())
            k -= 1
        else:
            n -= 1
    return result




print(topKFrequent([1,1,2,2,3],2))
    
