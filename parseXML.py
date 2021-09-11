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

if len(accidentalNotes) == 0:
    print("(None found)")
else:
    for note in accidentalNotes:
        notesArr.append(get_step(note))
        alterArr.append(get_accidental(note))

if len(nonAccidentalsNotes) == 0:
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

