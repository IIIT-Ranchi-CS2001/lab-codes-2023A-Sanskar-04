def my_zip(names, ids, points, strct=True):
    if strct:
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            raise ValueError("All lists must have equal length when strct is True")
    else:
        min_length = min(len(names), len(ids), len(points))
        return list(zip(names[:min_length], ids[:min_length], points[:min_length]))


names = ["Anuj", "yuvraj", "sanskar"]
ids = [1, 2, 3]
points = [100, 150, 200]

try:
    print(my_zip(names, ids, points, strct=True))
except ValueError as e:
    print(e)


print(my_zip(names, ids, points, strct=False))
