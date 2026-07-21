catalog_items = ["Tablet", "Headphones", "Webcam", "Microphone", "Router"]
search_query = "Webcam"

print(f"Searching for: {search_query}\\n")

# Linear Search Approach
is_item_located = False
for index in range(len(catalog_items)):
    if catalog_items[index] == search_query:
        print(f"[Linear Search] Item discovered at index: {index}")
        is_item_located = True
        break

if not is_item_located:
    print("[Linear Search] Item is unavailable.")

# Binary Search Approach
catalog_items.sort()
print(f"\\nSorted Catalog: {catalog_items}")

bottom = 0
top = len(catalog_items) - 1

while bottom <= top:
    middle = (bottom + top) // 2
    if catalog_items[middle] == search_query:
        print(f"[Binary Search] Item discovered at index: {middle}")
        break
    elif search_query > catalog_items[middle]:
        bottom = middle + 1
    else:
        top = middle - 1