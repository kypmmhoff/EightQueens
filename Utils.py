def mergeDictionaries(x, y):
    z = x.copy()
    z.update(y)
    return z

def formatArray(arrayValues):
    result =''
    for value in arrayValues:
        result+= '(%s,%s),' % (value[0], value[1])
    return result[:-1]