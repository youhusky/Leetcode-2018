def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
    elif common_divisor == 1:
        return "%d/%d is already at its most simplified state" % (numer, denom)
    else:
        return "%d/%d is simplified to %d/%d" % (numer, denom, reduced_num, reduced_den)
def divide(s1, s2):
	# 1/2, 2/3 -> 7/6
	if not s1[1] or not s2[1]:
		return "Error"
	res = [0,0]
	res[0] = s1[0] * s2[1] + s2[0] * s1[1]
	res[1] = s1[1] * s2[1]
	return res

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

print simplify_fraction(4,2)
	
print divide([1,2],[2,3])