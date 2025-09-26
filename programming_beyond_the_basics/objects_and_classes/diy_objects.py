def vec(x, y):
    def make_vector(x, y):
        return [x, y]

    container = {'vector': make_vector(x,y)}

    def add_vector(b):
        vector = container['vector']
        container['vector'] = make_vector(vector[0]+b[0], vector[1]+b[1])

    def print_vector():
        vector = container['vector']
        print(f'Vec({vector[0]}, {vector[1]})')

    def is_equal(y):
        vector = container['vector']
        return vector[0] == y[0] and vector[1] == y[1]

    def multiply_scalar(n):
        vector = container['vector']
        container['vector'] = [n*vector[0], n*vector[1]]

    def get_magnitude(x):
        return (vector[0]**2 + vector[1]**2)**0.5
    
    def get():
        return container['vector']

    return {"get": get, "multiply_scalar": multiply_scalar, "add": add_vector}


vec_object = vec(4, 5)
print(vec_object['get']())
print(vec_object['add'](vec(2, 5)['get']()))
print(vec_object['get']())
