from data.food import items

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = {}
    remaining_budget = budget

    for item_name, item_data in sorted_items:
        quantity = remaining_budget // item_data["cost"]
        if quantity > 0:
            selected_items[item_name] = quantity
            remaining_budget -= quantity * item_data["cost"]

    return selected_items


def dynamic_programming(items, budget):
    ratios = {food: items[food]["calories"] / items[food]["cost"] for food in items}

    sorted_items = sorted(items.keys(), key=lambda x: ratios[x], reverse=True)

    dp = [0] * (budget + 1)
    prev = [None] * (budget + 1)

    for food in sorted_items:
        cost = items[food]["cost"]
        calories = items[food]["calories"]

        for j in range(cost, budget + 1):
            if dp[j - cost] + calories > dp[j]:
                dp[j] = dp[j - cost] + calories
                prev[j] = food

    result = {}
    current_budget = budget
    while prev[current_budget] is not None:
        food = prev[current_budget]
        if food in result:
            result[food] += 1
        else:
            result[food] = 1
        current_budget -= items[food]["cost"]

    return result


if __name__ == "__main__":
    budget = 20

    greedy_result = greedy_algorithm(items, budget)
    used_budget = sum([items[item_name]["cost"] * quantity for item_name, quantity in greedy_result.items()])
    calories = sum([items[item_name]["calories"] * quantity for item_name, quantity in greedy_result.items()])
    print(f"Greedy Algorithm Result {used_budget}$, {calories} ccal: {greedy_result}")

    dp_result = dynamic_programming(items, budget)
    used_budget = sum([items[item_name]["cost"] * quantity for item_name, quantity in dp_result.items()])
    calories = sum([items[item_name]["calories"] * quantity for item_name, quantity in dp_result.items()])
    print(f"Dynamic Programming Result {used_budget}$, {calories} ccal: {dp_result}")
