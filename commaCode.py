def listParse(spam):
    result = ''
    for i in spam:
        if spam.index(i) == len(spam) - 2:
            i = str(i)
            i += ' and '
            result += i
        elif spam.index(i) == len(spam) - 1:
            i = str(i)
            i += '.'
            result += i
        else:
            i = str(i)
            i += ', '
            result += i
    print(result)


listParse([1,2,'tofu','cats'])