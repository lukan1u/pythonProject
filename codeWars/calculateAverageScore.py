import statistics
def better_than_average(class_points, your_points):
    if your_points > statistics.mean(class_points):
        return True
    else:
        return False

print(better_than_average([2, 20], 5))


# one line solution: return your_points > sum(class_points) / len(class_points) 