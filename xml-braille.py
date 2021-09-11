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
                "B,8": "⠾", #-----
                }

octave_dict = { 1: "⠈",
                2: "⠘",
                3: "⠸",
                4: "",
                5: "", 
                6: "",
                7: ""}

accidental_dict = {1: "⠩",
                   0: "",
                   -1: "⠣"}


out_file = open("final.brf", "w+")
brailleText = pitch_length_dict["B,4"]
encodedBraille = brailleText.encode("utf8")
out_file.write(encodedBraille)

out_file.close()