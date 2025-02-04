def lcs3(first_sequence, second_sequence, third_sequence):
    n = len(first_sequence)
    m = len(second_sequence)
    t = len(third_sequence)
    
    dp = [[[0] * (t + 1) for _ in range(m + 1)] for _ in range( n + 1)]
          
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, t + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                   dp[i][j][k] = dp[i-1][j-1][k - 1] + 1
                else:
                   dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k], dp[i][j][k - 1])
          
    return dp[n][m][t]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))