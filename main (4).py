def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Test the function
products = ["Laptop", "Keyboard", "Mouse", "Laptop", "Monitor", "Laptop"]
target_product = "Laptop"

result = linear_search_product(products, target_product)

if result:
    print(f"The product '{target_product}' is found at indices: {result}")
else:
    print(f"The product '{target_product}' is not found in the list.")