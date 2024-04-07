N = int(input())

def add_stars(star_output):
	for x in range(len(star_output)):
		star_output[x].insert(0, " ")
		star_output[x].insert(0, "*") 
		star_output[x].append(" ")
		star_output[x].append("*")
	star_output.insert(0, ["*"] + [" "] * (len(star_output[0]) - 1))
	star_output.insert(0, ["*"] * len(star_output[0]))
	star_output.append(["*"] + [" "] * (len(star_output[0]) - 2) + ["*"])
	star_output.append(["*"] * len(star_output[0]))
	return star_output

def starprint(cur_N):
	if cur_N == 1:
		return [["*"]]
	elif cur_N == 2:
		return [ ["*", "*", "*", "*", "*"], ["*", " ", " ", " ", " "], ["*", " ", "*", "*", "*"], ["*", " ", "*", " ", "*"], ["*", " ", "*", " ", "*"], ["*", " ", " ", " ", "*"], ["*", "*", "*", "*", "*"], ]
	recur_output = starprint(cur_N - 1)
	recur_output = add_stars(recur_output)
	recur_output[2][-2] = "*"
	return recur_output

for line in map("".join, starprint(N)):
	print(line.rstrip())