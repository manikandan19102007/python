from itertools import combinations:
list[1,-2,3,4,-7]
print("positive combinations")
for r in range(len(llist)+1):
  for combo in combinations(list,7):
    if all(num>0 for num in combo):
      print(combo)
