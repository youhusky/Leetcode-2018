inputfile = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
def minimumTotal(triangle):
    if not triangle:
        return 
    res = [[x,str(x)] for x in triangle[-1]]
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
        	if res[j][0] < res[j+1][0]:
        		res[j][0] = res[j][0] + triangle[i][j]
        		res[j][1] = res[j][1] +'->'+ str(triangle[i][j])
        	else:
        		res[j][0] = res[j+1][0] + triangle[i][j]
        		res[j][1] = res[j+1][1] +'->'+ str(triangle[i][j])
    print res[0]
    return res[0]

def minimumTotal2(triangle):
    if not triangle:
        return 
    res = triangle[-1]
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    print res[0]
    return res[0]
minimumTotal(inputfile)
minimumTotal2(inputfile)
