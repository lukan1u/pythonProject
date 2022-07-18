def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    if average < your_points:
        return True
    else:
        return False
