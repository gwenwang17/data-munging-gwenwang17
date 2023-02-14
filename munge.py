# Place code below to do the munging part of this assignment.
all_text = []
x = 0


f = open("data/nasa_data.txt", "r")
all_text = f.readlines()


f = open("clean_data.csv", "w")

# make sure to subtract 1 from line_number as starts from 0
for line_number, line_text in enumerate(all_text):
    # remove notes
    if line_number <= 6 or line_number >= 166:
        continue
    else:
        # remove all but the first line of column headings
        if "Year" in line_text and line_number > 7:
            continue
        # remove all blank lines
        if not line_text.strip():
            continue
        else:
            # convert to fahrenheit
            # avoid headings
            if line_number >= 8:
                cel = line_text.split()
                fah = []
                for i, val in enumerate(cel):
                    # avoids years (first and last element)
                    if i == 0:
                        fah.append(val)
                    elif i == 19:
                        fah.append(val+"\n")
                    else:
                        if "*" not in val:
                            fah.append("{:.1f}".format(int(val)/100.0*1.8))
                        # handles missing values, we skip the line
                        else:
                            fah = []
                            break
                print(fah)
                string_text = " ".join(fah)
                f.write(string_text)
            # handle header
            else:
                string_list = line_text.split()
                string_text = " ".join(string_list)
                string_text += "\n"
                f.write(string_text)


f.close()
