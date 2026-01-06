if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)
    
    # Remove all occurrences of the maximum score
    while max_score in arr:
        arr.remove(max_score)
    
    # Now the maximum of remaining list is runner-up
    print(max(arr))
