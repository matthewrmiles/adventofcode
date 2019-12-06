def main():
	with open('input.txt') as f:
		d = f.read().splitlines()
	print(str(sum([repeatadd(int(i)) for i in d])))

def repeatadd(x):
	if (x//3-2) <= 0:
		return 0;
	return (x//3 - 2) + repeatadd(x//3 - 2)

main()
