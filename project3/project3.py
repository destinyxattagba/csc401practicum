def lcs_algorithm(string1, string2):
    m = len(string1)
    n = len(string2)
    memo = [["" for tracker in range(n + 1)] for tracker2 in range(m+1)]
    result = lcsRec(string1,string2,m,n,memo)
    print("\nLCS: ", result)
    return result


def lcsRec(s1,s2,m,n, memo):

    print(f" Entering LCS finder with m={m}, n={n}")

    if m == 0 or n == 0:
        print(f"   Base case reached --> return ''")
        return ""

    if memo [m][n] != "":
        print(f"   Memo hit for (m={m}, n={n} --> '{memo[m][n]}'")
        return memo[m][n]

    if s1[m-1] == s2[n-1]:
        print(f"   Match: '{s1[m-1]}' == '{s2[n-1]}'")
        result = lcsRec(s1, s2, m-1, n-1, memo) + s1[m-1]
        memo[m][n] = result
        print(f"    Set memo[{m}][{n}] = '{result}' (match case)")
        return result

    print(f"    No match: '{s1[m - 1]}' != '{s2[n - 1]}'")

    left = lcsRec(s1, s2, m, n - 1, memo)
    up = lcsRec(s1, s2, m - 1, n, memo)

    if(len(left) > len(up)):
        memo[m][n] = left
        print(f"    Set memo[{m}][{n}] = '{left}' (left branch)")

    else:
        memo[m][n] = up
        print(f"    Set memo[{m}][{n}] = '{up}' (up branch)")
    return memo[m][n]

