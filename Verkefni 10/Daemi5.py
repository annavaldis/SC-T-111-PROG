def input_vector(size):
    vec = []
    for i in range(1, size + 1):
        ele = float(input("Element no " + str(i) + ": "))
        vec.append(ele)
    return vec


def dot_product(vec1, vec2):
    dot_prod = 0
    for j in range(0, len(vec1)):
        dot_prod += vec1[j] * vec2[j]
    return dot_prod


# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))
