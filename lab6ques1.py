def my_zip(names, ids, points, strct=True):
    if strct:
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            raise ValueError("All lists must have equal length when strct is True")
    else:
        min_length = min(len(names), len(ids), len(points))
        return list(zip(names[:min_length], ids[:min_length], points[:min_length]))


def my_sort(data, key):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if key == 0:
                if data[j][0] > data[j + 1][0]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif key == 1:
                if data[j][1] > data[j + 1][1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif key == 2:
                if data[j][2] > data[j + 1][2]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data


names = ["Sanskar", "Yuvraj", "Aunj"]
ids = [1, 2, 3]
points = [100, 150, 200]

customer_data = my_zip(names, ids, points, strct=False)

sorted_by_name = my_sort(customer_data, key=0)
sorted_by_id = my_sort(customer_data, key=1)
sorted_by_points = my_sort(customer_data, key=2)

print("Sorted by Name:", sorted_by_name)
print("Sorted by ID:", sorted_by_id)
print("Sorted by Points:", sorted_by_points)
