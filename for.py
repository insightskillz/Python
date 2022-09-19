
def main():
	fh = open('lines.txt')
	for index, line in enumerate(fh.readlines()):
		print(index, line, end=' ')



if __name__ == '__main__':
	main()