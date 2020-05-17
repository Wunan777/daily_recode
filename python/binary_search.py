import bisect
BISECT_UNFIND_RET = -1

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return BISECT_UNFIND_RET

# Usage:
if __name__ == "__main__":
    arr = [1,3,5]
    print index(arr, 2)
    print index(arr, 3)