my_tuple=("jan","feb","mar","apr","jan","feb", "feb")
print(my_tuple)
b=set()
result=[element for element in my_tuple
    if not (tuple(element) in b
        or  b.add(tuple(element)))]
print(str(result))