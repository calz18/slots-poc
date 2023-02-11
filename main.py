from fastapi import FastAPI
from slotmachine import SlotMachine

app = FastAPI()


@app.get("/")
def read_root():
    slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})
    return slot1.spin()


@app.get("/simulation")
def simulation():
    slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})

    return slot1.simulation(100000, 20000, 2)


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# Sample simulations
# slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})
# slot2 = SlotMachine(4, {
#     '7': 1,
#     '77': 10,
#     '777': 150,
#     '7777': 1000
# })

# print(slot1.simulation(100000, 20000, 2))
# print(slot2.simulation(1000000, 20000, 2))
