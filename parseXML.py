from xml.dom.minidom import parse, parseString

def get_step(note):
    stepNode = note.getElementsByTagName("step")[0]
    #get the text from the Text Node within the <step>,
    #and convert it from unicode to ascii
    return str(stepNode.childNodes[0].nodeValue)

def get_interval(note):
    stepNode = note.getElementsByTagName("octave")[0]
    return str(stepNode.childNodes[0].nodeValue)

def get_alter(note):
    alters = note.getElementsByTagName("alter")
    if len(alters) == 0:
        return None
    return alters[0]

def get_accidental(note):
    alter = get_alter(note)
    return str(alter.childNodes[0].nodeValue)

def is_rest(note):
    return len(note.getElementsByTagName("rest")) > 0

def is_accidental(note):
    return get_alter(note) != None

def get_duration(note):
    stepNode = note.getElementsByTagName("duration")[0]
    return str(stepNode.childNodes[0].nodeValue)

dom = parse("New.musicxml")

notes = dom.getElementsByTagName("note")

notes = filter(lambda note: not is_rest(note), notes)

accidentals = filter(lambda note: is_accidental(note), notes)

accidentalNotes = filter(lambda note: get_step(note) in ["C", "D", "E", "F", "G", "A", "B"], accidentals)

non_accidentals = filter(lambda note: not is_accidental(note), notes)

nonAccidentalsNotes = filter(lambda note: get_step(note) in ["C", "D", "E", "F", "G", "A", "B"], non_accidentals)

intervals = filter(lambda note: get_interval(note), notes)

durations = filter(lambda note: get_duration(note), notes)

intervalsArr = []
notesArr = []
alterArr = []
durationArr = []

for note in intervals:
    intervalsArr.append(get_interval(note))

for note in durations:
    durationArr.append(get_duration(note))

if False:
    print("(None found)")
else:
    for note in accidentalNotes:
        notesArr.append(get_step(note))
        alterArr.append(get_accidental(note))

if False:
    print("(None found)")
else:
    for note in nonAccidentalsNotes:
        notesArr.append(get_step(note))
        alterArr.append('0')

totalNotesArr = []

for i in range(len(notesArr)):
    totalNotesArr.append([notesArr[i], intervalsArr[i], alterArr[i], durationArr[i]])

for note in totalNotesArr:
    print(note)


# ----------------------------------------------------------

pitch_length_dict = {"C,1": "⠙",
                    "D,1": "⠑",
                    "E,1": "⠋",
                    "F,1": "⠛",
                    "G,1": "⠓",
                    "A,1": "⠊",
                    "B,1": "⠚", #-----
                    "C,2": "⠹",
                    "D,2": "⠱",
                    "E,2": "⠫",
                    "F,2": "⠻",
                    "G,2": "⠳",
                    "A,2": "⠪",
                    "B,2": "⠺", #-----
                    "C,4": "⠝",
                    "D,4": "⠱",
                    "E,4": "⠏",
                    "F,4": "⠟",
                    "G,4": "⠗",
                    "A,4": "⠎",
                    "B,4": "⠞", #-----
                    "C,8": "⠽",
                    "D,8": "⠵",
                    "E,8": "⠯",
                    "F,8": "⠿",
                    "G,8": "⠷",
                    "A,8": "⠮",
                    "B,8": "⠾"}

octave_dict = { 1: "⠈",
                2: "⠘",
                3: "⠸",
                4: "⠐",
                5: "⠨",
                6: "⠰",
                7: "⠠"}

accidental_dict = { 1: "⠩",
                    0: "",
                    -1: "⠣"}

for i in range(len(notesArr)-1):
    note_i = str(totalNotesArr[i][0])
    interval_i = str(totalNotesArr[i][1])
    alter_i = str(totalNotesArr[i][2])
    duration_i = str(totalNotesArr[i][3])
    pitch_length_i = note_i + "," + duration_i      # gets pitch + rhythm braille
    print(pitch_length_dict[pitch_length_i])
    octave_i = octave_dict[alter_i]                 # gets octave braille
    print(octave_i)
    accidental_i = accidental_dict[alter_i]         # gets accidental braille
    print(accidental_i)
