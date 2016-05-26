# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def digits_sum(non_neg_int):
    if non_neg_int <= 10:
        return non_neg_int
    else:
        return non_neg_int % 10 + digits_sum(non_neg_int // 10)

print(digits_sum(245))
