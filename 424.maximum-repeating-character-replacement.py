from collections import defaultdict
def maxRep(s: str, k: int) -> int:
    count = defaultdict(int)
    max_count = 0
    left = right = 0
    while right < len(s):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        right += 1
        if right - left - max_count > k:
            count[s[left]] -= 1
            left += 1
    return right - left

