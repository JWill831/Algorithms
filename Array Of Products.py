def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
            temp = 1
            for j in range(len(array)):
                if j != i:
                    temp *= array[j]
            products[i] = temp

    return products


print(arrayOfProducts([5, 1, 4, 2]))
