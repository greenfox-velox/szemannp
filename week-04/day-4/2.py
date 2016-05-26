# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def summarize(n):
    if n <= 0:
        return 0
    else:
        return summarize(n - 1) + n

print(summarize(10))
