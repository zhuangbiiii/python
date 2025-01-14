# ZBS utility 

# Quickly compare two Chinese strings, excluding spaces and symbols
def compareChineseString(str1, str2):
    # Using regular expressions to obtain Chinese substrings in a string
    return getChineseString(str1) == getChineseString(str2)

def getChineseString(str):
    import re
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    result = pattern.findall(str)
    return result

def getEnglishString(str):
    import re
    pattern = re.compile(r'[a-zA-Z]+')
    result = pattern.findall(str)
    return result