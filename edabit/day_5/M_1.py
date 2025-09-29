"""Medium"""

"""https://edabit.com/challenge/YfoKQWNeYETb9PYpw"""
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796

# profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }) ➞ 32411

# profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }) ➞ 44030


def profit(info):
    sell_price = info["inventory"] * info["sell_price"]
    make_price = info["inventory"] * info["cost_price"]
    return round(sell_price - make_price)
    # return round(
    #     (info["inventory"] * info["sell_price"])
    #     - (info["inventory"] * info["cost_price"])
    # )


print(profit({"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}))
print(profit({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}))
print(profit({"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}))
