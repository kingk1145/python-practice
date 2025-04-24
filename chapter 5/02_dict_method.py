# method of dict

# 1. items()
marks={
    "Harry": 90,
    "kritesh": 95,
    "Ayan":94,
}
print(marks.items())

# 2. key()
marks={
    "Harry": 90,
    "kritesh": 95,
    "Ayan":94,
}
print(marks.keys())

# 3.values()
marks={
    "Harry": 90,
    "kritesh": 95,
    "Ayan":94,
}
print(marks.values())

# 4.update()
marks={
    "Harry": 90,
    "kritesh": 95,
    "Ayan":94,
}
marks.update({"kritesh":98,"Anant":88})
print(marks)
