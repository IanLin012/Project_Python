import json

orders = {
    "order1": {
        "customer": {"name": "Alice", "email": "alice@example.com"},
        "items": [
            {"product_name": "Item A", "quantity": 2, "price": 30},
            {"product_name": "Item B", "quantity": 1, "price": 20}
        ]
    },
    "order2": {
        "customer": {"name": "Bob", "email": "bob@example.com"},
        "items": [
            {"product_name": "Item A", "quantity": 1, "price": 30},
            {"product_name": "Item C", "quantity": 3, "price": 25}
        ]
    },
}

res = {"order_price":[], "item_sales":{}} # initial print form
for order_id, order_data in orders.items(): # order_id: order number, order_data: customer & items data
    order_total = 0
    for item in order_data["items"]:
        order_total += item["quantity"] * item["price"]
        product_name = item["product_name"]
        if product_name in res["item_sales"]:
            res["item_sales"][product_name] += item["quantity"]
        else:
            res["item_sales"][product_name] = item["quantity"]
    res["order_price"].append({order_id:order_total})
print("result = " + json.dumps(res, ensure_ascii=False, indent=4, separators=(',', ':')))
# json.dumps(): change dict or list to JSON string form
# ensure_ascii=False: ensure none ASCII char display
# indent=4: let print be readability, display in TAB form
# separators=(',', ':'): let , & : remove blank