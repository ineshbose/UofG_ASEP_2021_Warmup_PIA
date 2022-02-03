def count_change(s, n, m=len(S)):
    
    if (n == 0):
        return 1
 
    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;
 
    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        return 0
 
    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count_change(s, n, m - 1 ) + count_change(s, m, n-S[m-1] );