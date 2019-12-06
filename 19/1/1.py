with open('input.txt') as f:
	d = f.read().splitlines()
print(str(sum([int(i)//3 - 2 for i in d])))
