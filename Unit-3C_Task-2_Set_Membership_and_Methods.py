set_data = {10, 20, 30}
print("Set:", set_data)

print("20 in set?", set_data )
print("40 not in set?", set_data )

set_data.add(40)  # add 40
print("After add:", set_data)

set_data.remove(10)  # remove 10
print("After remove:", set_data)

set_data.discard(99)  # discard 99 (safe even if missing)
print("After discard:", set_data)