def main():
	showNewl = input ("Show newlines? y/n : ").strip(',./1234567890').lower()
	showNewl = True if (showNewl == 'y' or showNewl == 'yes') else False
	print("Input yer kappas. END to stop.")
	lines = []
	while (True):
		line = input()
		if ( line != "END" and line != "end" ):
			line = line.split("\n")[0]
			lines.append(line)
		else:
			break
	if ( showNewl ):
		print("\\n".join(lines))
	else:
		print("".join(lines))

if (__name__ == "__main__"):
	main()
