# return without duplicates


def remove_duplicates(string):
    table = []
    for item in string:
        if item in table:
            pass
        else:
            table.append(item)
    report = ''.join(table)
    print(report)


remove_duplicates('GHIIIKKKL')
