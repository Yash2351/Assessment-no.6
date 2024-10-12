def lcs(str1, str2, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Building DP table from bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def min_operations(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Finding the length
    lcs_length = lcs(str1, str2, m, n)
    
    # Minimum deletions
    min_deletions = m - lcs_length
    
    # Minimum insertions
    min_insertions = n - lcs_length
    
    return min_deletions, min_insertions

# Input
str1 = "heap"
str2 = "pea"
deletions, insertions = min_operations(str1, str2)

# Output
print(f"Minimum Deletion = {deletions} and Minimum Insertion = {insertions}")
