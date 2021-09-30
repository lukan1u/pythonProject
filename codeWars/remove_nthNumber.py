def delete_nth(order, max_e):
    new_order = []
    for x in order:
        if x not in new_order or order.count(x) <= max_e:
            new_order.append(x)
    return new_order
