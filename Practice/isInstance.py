# Understanding isInstance()
# to use as a way to determine whether a list is
# single or multidimensional

oneDimList = [1, 2, 3]
twoDimList = [[1,2,3],[1,2,3],[1,2,3]]
print('oneDimList = [1, 2, 3]\n' + 
      'twoDimList = [[1,2,3],[1,2,3],[1,2,3]]')
print ('isinstance(oneDimList,list)')
print (isinstance(oneDimList,list))
print('isinstance(oneDimList[0],list)')
print (isinstance(oneDimList[0],list))
print('isinstance(twoDimList,list)')
print (isinstance(twoDimList,list))
print('isinstance(twoDimList[0],list)')
print (isinstance(twoDimList[0],list))