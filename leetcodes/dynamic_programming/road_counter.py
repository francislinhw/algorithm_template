# Optiver Interview Question


def count_paths(m: int, n: int) -> int:
    """
    Count paths from (0,0) to (m-1,n-1) without 3 consecutive right moves.

    Args:
        m (int): Number of rows
        n (int): Number of columns

    Returns:
        int: Number of valid paths
    """
    MOD = 10**9 + 7

    # dp[i][j][k] represents number of paths to cell (i,j)
    # where k is number of consecutive right moves ending at this cell
    dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(m)]

    # Initialize starting point
    dp[0][0][0] = 1

    # Fill the dp table
    for i in range(m):
        for j in range(n):
            for k in range(3):
                if dp[i][j][k] == 0:
                    continue

                # Can move down (resets consecutive right moves to 0)
                if i + 1 < m:
                    dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) % MOD

                # Can move right if we haven't made 2 consecutive right moves yet
                if j + 1 < n and k < 2:
                    dp[i][j + 1][k + 1] = (dp[i][j + 1][k + 1] + dp[i][j][k]) % MOD

    # Sum all possible ending states (with 0, 1, or 2 consecutive right moves)
    result = sum(dp[m - 1][n - 1]) % MOD
    return result


# Test the function
def test_path_counter():
    test_cases = [
        (3, 3),  # Small square grid
        (2, 3),  # Rectangle grid
        (1, 5),  # Single row
        (5, 1),  # Single column
        (5, 5),  # 5x5 grid
    ]

    for m, n in test_cases:
        paths = count_paths(m, n)
        print(f"Grid {m}x{n}: {paths} valid paths")


if __name__ == "__main__":
    test_path_counter()
