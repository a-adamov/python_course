values = [1, 2 , 3]

transformation = lambda x: x

transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')