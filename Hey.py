def min_messages_to_remove(N, msgList):
    msgList.sort()  # Sort the list of message lengths in ascending order.
    min_messages_removed = N  # Initialize the minimum number of messages to remove with the maximum value.

    for i in range(N):
        # For each possible starting point, calculate the maximum length of a message in the selected sequence.
        max_length = msgList[i] * 2

        # Use binary search to find the index of the first message that exceeds the max_length.
        left, right = i, N - 1
        while left <= right:
            mid = (left + right) // 2
            if msgList[mid] <= max_length:
                left = mid + 1
            else:
                right = mid - 1

        # Calculate the number of messages to remove from both ends.
        messages_removed = i + (N - left)

        # Update the minimum number of messages to remove.
        min_messages_removed = min(min_messages_removed, messages_removed)

    return min_messages_removed

# Read input
N = int(input())
msgList = list(map(int, input().split()))

# Call the function and print the result
result = min_messages_to_remove(N, msgList)
print(result)
