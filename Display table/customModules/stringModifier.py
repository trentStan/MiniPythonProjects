import camelcase
def capitalise(string):
    c = camelcase.CamelCase()
    return c.hump(string)