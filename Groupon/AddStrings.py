def addStrings(nums1, nums2,base):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # 123 + 
    #  45
    res = ""
    i,j = len(nums1)-1, len(nums2)-1
    carry =  0
    while i >= 0 or j >= 0 :
        if i >= 0:
            carry += int(nums1[i])
            i -= 1
        if j >= 0:
            carry += int(nums2[j])
            j -= 1
        res = str(carry%base) + res
        carry /= base
    return res if not carry else '1' + res
print 'base=10:   '+addStrings('11','1',10)

def addString2(nums1, nums2):
    dic = {'A':10, 'B':11,'C':12,'D':13,'E':14,'F':15}
    for num in range(10):
        dic[str(num)] = num
    dic2 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    i,j = len(nums1)-1, len(nums2)-1
    carry =  0
    res = ""
    while i >= 0 or j >= 0 :
        if i >= 0:
            carry += dic[nums1[i]]
            i -= 1
        if j >= 0:
            carry += dic[nums2[j]]
            j -= 1
        
        res = str(dic2[carry%16]) + res
        carry /= 16
    return res if not carry else '1' + res

print addString2('A','1')

def toHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

numbers = [0, 11, 16, 32, 33, 41, 45, 678, 574893]
print [toHex(x) for x in numbers]
print [hex(x) for x in numbers]