function Sum_Solution(n)
{
    var res = n
    n && (res = res+Sum_Solution(n-1))
    return res
}