


sheets = ["s1", "s2"]

views = ["1", "2", "3", "4"]


for s in sheets:
    for v in views:
        if v in s:
            print("Sheet created")
            break