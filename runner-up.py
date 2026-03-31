pts = [1,0]
max = -101
runner = -101
for i in pts:
    if max < i :
        runner = max
        max = i
    elif max>i>runner :
        runner = i

if runner == -101:
    print(f"Winner = {max} \nrunner up = {None}")
else :
    print(f"Winner = {max} \nrunner up = {runner}")