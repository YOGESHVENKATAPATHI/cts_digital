purchase_amounts = [5200, 8900, 1500, 7200, 2800]

print("--- Initial Purchase Data ---")
print(purchase_amounts)

# Implementation of Bubble Sort
bubble_data = purchase_amounts.copy()
for i in range(len(bubble_data)):
    for j in range(len(bubble_data) - 1):
        if bubble_data[j] > bubble_data[j + 1]:
            bubble_data[j], bubble_data[j + 1] = bubble_data[j + 1], bubble_data[j]

print("\\n--- After Bubble Sort ---")
print(bubble_data)


# Implementation of Quick Sort
def execute_quick_sort(dataset):
    if len(dataset) <= 1:
        return dataset
    
    pivot_val = dataset[-1]
    left_partition = []
    right_partition = []
    
    for value in dataset[:-1]:
        if value < pivot_val:
            left_partition.append(value)
        else:
            right_partition.append(value)
            
    return execute_quick_sort(left_partition) + [pivot_val] + execute_quick_sort(right_partition)

print("\\n--- After Quick Sort ---")
print(execute_quick_sort(purchase_amounts))