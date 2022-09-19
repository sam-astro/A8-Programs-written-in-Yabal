
from curses.ascii import isalpha
import sys

print()

base36 = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
defaultOctave = 4

def NoteToFreq(note):
	freq = 0
	if note=="C0":
		freq = 16
	if note=="C#0" or note == "Db0":
		freq = 17
	if note=="D0":
		freq = 18
	if note=="D#0" or note == "Eb0":
		freq = 19
	if note=="E0":
		freq = 20
	if note=="F0":
		freq = 21
	if note=="F#0" or note == "Gb0":
		freq = 23
	if note=="G0":
		freq = 24
	if note=="G#0" or note == "Ab0":
		freq = 26
	if note=="A0":
		freq = 27
	if note=="A#0" or note == "Bb0":
		freq = 29
	if note=="B0":
		freq = 30

	if note=="C1":
		freq = 32
	if note=="C#1" or note == "Db1":
		freq = 34
	if note=="D1":
		freq = 36
	if note=="D#1" or note == "Eb1":
		freq = 38
	if note=="E1":
		freq = 41
	if note=="F1":
		freq = 43
	if note=="F#1" or note == "Gb1":
		freq = 46
	if note=="G1":
		freq = 49
	if note=="G#1" or note == "Ab1":
		freq = 52
	if note=="A1":
		freq = 55
	if note=="A#1" or note == "Bb1":
		freq = 58
	if note=="B1":
		freq = 61

	if note=="C2":
		freq = 65
	if note=="C#2" or note == "Db2":
		freq = 69
	if note=="D2":
		freq = 73
	if note=="D#2" or note == "Eb2":
		freq = 77
	if note=="E2":
		freq = 82
	if note=="F2":
		freq = 87
	if note=="F#2" or note == "Gb2":
		freq = 92
	if note=="G2":
		freq = 98
	if note=="G#2" or note == "Ab2":
		freq = 104
	if note=="A2":
		freq = 110
	if note=="A#2" or note == "Bb2":
		freq = 116
	if note=="B2":
		freq = 123

	if note=="C3":
		freq = 130
	if note=="C#3" or note == "Db3":
		freq = 138
	if note=="D3":
		freq = 146
	if note=="D#3" or note == "Eb3":
		freq = 155
	if note=="E3":
		freq = 164
	if note=="F3":
		freq = 174
	if note=="F#3" or note == "Gb3":
		freq = 185
	if note=="G3":
		freq = 196
	if note=="G#3" or note == "Ab3":
		freq = 207
	if note=="A3":
		freq = 220
	if note=="A#3" or note == "Bb3":
		freq = 233
	if note=="B3":
		freq = 246

	if note=="C4":
		freq = 261
	if note=="C#4" or note == "Db4":
		freq = 277
	if note=="D4":
		freq = 293
	if note=="D#4" or note == "Eb4":
		freq = 311
	if note=="E4":
		freq = 329
	if note=="F4":
		freq = 349
	if note=="F#4" or note == "Gb4":
		freq = 370
	if note=="G4":
		freq = 392
	if note=="G#4" or note == "Ab4":
		freq = 415
	if note=="A4":
		freq = 440
	if note=="A#4" or note == "Bb4":
		freq = 466
	if note=="B4":
		freq = 493

	if note=="C5":
		freq = 523
	if note=="C#5" or note == "Db5":
		freq = 554
	if note=="D5":
		freq = 587
	if note=="D#5" or note == "Eb5":
		freq = 622
	if note=="E5":
		freq = 659
	if note=="F5":
		freq = 698
	if note=="F#5" or note == "Gb5":
		freq = 740
	if note=="G5":
		freq = 783
	if note=="G#5" or note == "Ab5":
		freq = 830
	if note=="A5":
		freq = 880
	if note=="A#5" or note == "Bb5":
		freq = 932
	if note=="B5":
		freq = 987

	if note=="C6":
		freq = 1046
	if note=="C#6" or note == "Db6":
		freq = 1108
	if note=="D6":
		freq = 1174
	if note=="D#6" or note == "Eb6":
		freq = 1244
	if note=="E6":
		freq = 1318
	if note=="F6":
		freq = 1396
	if note=="F#6" or note == "Gb6":
		freq = 1480
	if note=="G6":
		freq = 1567
	if note=="G#6" or note == "Ab6":
		freq = 1661
	if note=="A6":
		freq = 1760
	if note=="A#6" or note == "Bb6":
		freq = 1864
	if note=="B6":
		freq = 1975
	if note=="-":
		freq = 0

	return freq

def FreqToBase36(f):
	return base36[max(0, min(round((f / 400) / 2 * 31), 31))]
	# return base36[max(0, min(round(((f / 400) / (1.1+(2.5+(0.84*f)/100)/10)*31) - f/100), 31))]

def CompressLines(section):
	secCopy = []
	lines = section.split("\n")
	diffs = []
	for i, l in enumerate(lines):
		if len(l.strip()) > 0:
			oc = int(lines[i][0])

			if (oc in diffs) == False:
				diffs.append(oc)
				secCopy.append(str(oc)+"==========================")
				# print("oc: " + str(oc))

			ind = diffs.index(oc)
			# print("i:" + str(ind))
			sC = list(secCopy[ind])
			for c in range(0, 27):
				if lines[i][c] != '=' and (sC[c] == " " or sC[c] == "="):
					sC[c] = lines[i][c]
			secCopy[ind] = ''.join(sC)
			# print(secCopy[ind])

	out = '\n'.join(secCopy)
	print("processed: \n" + out)
	print()
	return out

argoffset = 0
octaveOffset = 0
octaveSpecificChannels = [-1] * 10

nlist = False
plnlist = False

filepath = ""

# Iterate all arguments
for aC in range(1, len(sys.argv)):
	if sys.argv[aC] == "-o": # Set default octave
		defaultOctave = int(sys.argv[aC+1])
		octaveOffset = defaultOctave
		aC += 1

	elif sys.argv[aC] == "-cO": # specify channels for octave (ex. -cO 23  will make anything on octave 2 only be played in channel 3) 
		while sys.argv[1+aC][0] != "-":
			octaveSpecificChannels[int(sys.argv[1+aC][0])] = int(sys.argv[1+aC][1])
			aC += 1

	elif sys.argv[aC] == "-nlist":
		nlist = True

	elif sys.argv[aC] == "-plnlist":
		plnlist = True

	else:
		filepath = sys.argv[aC]

if nlist:
	f = open(filepath, "r")
	contents = f.read().replace("\n", "|").replace(" ", "=")
	print(contents)
	print()
	output = ""
	last = ""
	length = 6
	for i, ch in enumerate(contents):
		if ch == '|': # If delay character
			output += "....."
			last = ch
			continue
		
		if ch.isalpha() and ch.upper() == ch: # If note character AND uppercase
			if last.isalpha():
				output += "..."

			octave = defaultOctave
			mod = ""

			if i < len(contents)-1:
				if contents[i+1] == '|': # Make note longer if it is followed by a pause
					length = 9
				elif contents[i+1] == 'b': # Flat modifier
					mod = "b"
				elif contents[i+1] == '#': # Sharp modifier
					mod = "#"
				elif contents[i+1] == '=': # Make note longer if extended
					for x in range(i+1, len(contents)-1):
						if contents[x] == '=':
							length += 0.5
						else:
							break
			if i > 0:
				if contents[i-1] == '_' or contents[i-1] == '^' or contents[i-1] == '°':  # Lower octave modifier
					octave += 1
				elif contents[i-1] == '*':  # Higher octave modifier
					octave += 2

			for x in range(0, int(length)):
				output += str(FreqToBase36(NoteToFreq(ch + mod + str(octave))))

			length = 6

			last = ch
			continue

	print(output)

# If using notes in the format found at pianoletternotes.com
if plnlist:
	f = open(filepath, "r")
	contents = f.read().replace(" ", "").replace("-", "=").replace("RH:", "").replace("LH:", "").replace("|", "").replace("\n\n", "\n~\n")
	print(contents)
	print()
	channels = ["const var channelA = \"", "const var channelB = \"", "const var channelC = \"", "const var channelD = \"", ]
	octaveTracks = [""] * 10
	contentSections = contents.split("~")

	# Place lines in contents variable into designated octaveTracks track
	for x, s in enumerate(contentSections):
		sec = CompressLines(s)
		lines = sec.split("\n")
		for l in lines:
			if len(l.strip()) > 0:
				index = int(l[0])
				octaveTracks[index] += l[1:]
		
		# Add blank lines in unused octaves
		targetLen = len("--------------------------") * (x+1)
		for i, o in enumerate(octaveTracks):
			if len(o) < targetLen:
				octaveTracks[i] += "=========================="

	for x, o in enumerate(octaveTracks):
		print(str(9-x) + " " + octaveTracks[9-x])

	n = -1
	while n < len(octaveTracks[0])-1:
		n += 1
		octave = 10
		usedChannels = 0
		length = 6

		# Check if there are any notes in column, and add delay if so.
		noteFound = False
		for o in octaveTracks:
			if o[n] != "=":
				noteFound = True
				break
		if noteFound == False:
			channels[0] += "."
			channels[1] += "."
			channels[2] += "."
			channels[3] += "."
			continue

		editedChannels = [0] * 4

		while octave >= 0:
			octave -= 1
			length = 6

			ch = octaveTracks[octave][n]

			# Only use the A and B squarewave channels
			if usedChannels >= 2 and octaveSpecificChannels[octave] == -1:
				continue
			
			if ch.isalpha():
				mod = ""

				if n < len(octaveTracks[octave])-1:
					if ch.upper() == ch: # Sharp modifier
						mod = "#"
					elif octaveTracks[octave][n+1] == '=': # Make note longer if extended
						for x in range(n+1, len(octaveTracks[octave])-1):
							allBlank = True
							for o in octaveTracks:
								if o[x] != '=':
									allBlank = False
									break

							if allBlank:
								length += 0.6
							else:
								break

				channelToUse = octaveSpecificChannels[octave]
				if channelToUse == -1:
					channelToUse = usedChannels
					usedChannels += 1
				
				for x in range(0, int(length)):
					channels[channelToUse] += str(FreqToBase36(NoteToFreq(ch.upper() + mod + str(octave+octaveOffset))))
					# if channelToUse != 0:
					# 	channels[0] += "."
					# if channelToUse != 1:
					# 	channels[1] += "."
					# if channelToUse != 2:
					# 	channels[2] += "."
					# if channelToUse != 3:
					# 	channels[3] += "."
				channels[channelToUse] += ".."

				continue
		
		highestLength = 0
		for i, e in enumerate(channels): # Find longest channel
			if len(e) > highestLength:
				highestLength = len(e)
		for i, e in enumerate(channels): # Add highest length to all unedited channels
			while len(channels[i]) < highestLength:
				channels[i] += "."
		# channels[0] += ".."
		# channels[1] += ".."
		# channels[2] += ".."
		# channels[3] += ".."

	print(channels[0]+".\"")
	print(channels[1]+".\"")
	print(channels[2]+".\"")
	print(channels[3]+".\"")
print()

exit()
