my_tuple=("12","13","12","14","15","16", "15")
print(my_tuple)
b=set()
result=[element for element in my_tuple
    if not (tuple(element) in b
        or  b.add(tuple(element)))]
print(str(result))
