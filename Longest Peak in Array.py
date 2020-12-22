def longestPeak(array):
    longestPeakLength = 0
    i = 1

    while i < len(array)-1:
        peak = array[i-1] < array[i] and array[i] > array[i+1]
        if not peak:
            i += 1
            continue

        lIdx = i - 2
        while lIdx >= 0 and array[lIdx] < array[lIdx+1]:
            lIdx -= 1

        rIdx = i+2
        while rIdx < len(array) and array[rIdx] < array[rIdx-1]:
            rIdx +=1

        currentPeakLength = rIdx - lIdx-1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rIdx
    return longestPeakLength

print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))