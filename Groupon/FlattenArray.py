inputfile = [1, 2, [3, 4], [4, [5]]]
output = [1,2,3,4,4,5]

result = []
# def flatten(array, [])
def flatten(array):
     for i in array:
        if type(i) == type([]):
          flatten(i)
        else:
          result.append(i)
     return result

print flatten(inputfile)