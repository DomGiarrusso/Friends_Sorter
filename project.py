import sys
import csv

# Friends Sorter

def main():
    arg_checker()

    # A list that gathers the information inputed from csv file
    data_list = []

    # Opens the first csv file and gathers the data and adds it to the data list
    try:
        with open(sys.argv[1], "r") as csv_file:
            file_read = csv.DictReader(csv_file)
            for row in file_read:
                data_list.append(row)
    except FileNotFoundError:
        sys.exit("File could not be read")

    # New data set
    output_data = []

    # Use a loop through data list
    for row in data_list:
        role = role_selector(row["attribute"])
        zodiac = zodiac_selector(row["birthday"])
        output_data.append({"name": row["name"], "role": role, "zodiac": zodiac})

    with open(sys.argv[2], "w") as output_file:
        write = csv.DictWriter(output_file, fieldnames=["name", "role", "zodiac"])
        write.writerow({"name": "name", "role": "role", "zodiac": "zodiac"})
        # Loop through adding the new data
        for row in output_data:
            write.writerow(
                {"name": row["name"], "role": row["role"], "zodiac": row["zodiac"]}
            )


# Checks if the input argument is good or not
def arg_checker():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


# Looks at a person's arributes and gives the friend group role
def role_selector(attribute):
    # 1
    if attribute in ["lawmaker", "stickler", "caring"]:
        return "The Mom"
    # 2
    elif attribute in ["listner", "comforting", "insightful"]:
        return "The Therapist"
    # 3
    elif attribute in ["bonder", "glue", "friendly"]:
        return "The Connector"
    # 4
    elif attribute in ["controlling", "rigid", "organized"]:
        return "The Planner"
    # 5
    elif attribute in ["funny", "silly", "witty"]:
        return "The Joker"
    # 6
    elif attribute in ["different", "special", "quirky"]:
        return "The Hipster"
    # 7
    elif attribute in ["extra", "bold", "leader"]:
        return "The Overachiever"
    # 8
    elif attribute in ["cute", "beautiful", "sweet"]:
        return "The Flirt"
    # 9
    elif attribute in ["crazy", "entertaining", "hilarious"]:
        return "The Party Animal"
    # 10
    elif attribute in ["calm", "relaxed", "compossed"]:
        return "The Chill One"
    # 11
    elif attribute in ["creative", "talented", "imagitive"]:
        return "The Artistic One"
    # 12
    elif attribute in ["trendy", "stunning", "together"]:
        return "The Fastionable One"
    # 13
    elif attribute in ["academic", "know-it-all", "problemsolver"]:
        return "The Smart One"
    # 14
    elif attribute in ["opinionated", "firey", "figher"]:
        return "The Hot Head"
    # 15
    elif attribute in ["judgy", "negative", "responsible"]:
        return "The Pessimist"
    # 16
    elif attribute in ["unorganized", "unlucky", "lost"]:
        return "The Absolute Mess"
    else:
        return "No role"


def zodiac_loop(range1, range2, month1, month2, zodiac, birthday):
    for num in range1:
        combo = month1 + str(num)
        if birthday == combo:
            return zodiac
    for num in range2:
        combo = month2 + str(num)
        if birthday == combo:
            return zodiac


# Looks at a person's birthday and assigns them their zodiac sign
def zodiac_selector(birthday):
    # Month Variables
    march = "march "
    april = "april "
    may = "may "
    june = "june "
    july = "july "
    august = "august "
    september = "september "
    october = "october "
    november = "november "
    december = "december "
    january = "january "
    february = "february "

    # Zodica Variables
    aries = "Aries"
    taurus = "Taurus"
    gemini = "Gemini"
    cancer = "Cancer"
    leo = "Leo"
    virgo = "Virgo"
    libra = "Libra"
    scorpius = "Scorpius"
    sagittarius = "Sagittarius"
    capricornus = "Capricornus"
    aquarius = "Aquarius"
    pisces = "Pisces"

    # Ranges Variables
    # Range variables formated as first letter of month, zodiac, range i.e. mar = march aries range
    # if month both start with same letter then short form of month will be use i.e. juncr and julcr

    # Aries Ranges
    mar = range(21, 32)
    aar = range(1, 20)
    # Taurus Ranges
    atr = range(20, 31)
    mtr = range(1, 21)
    # Gemini Ranges
    mgr = range(21, 32)
    jgr = range(1, 22)
    # Cancer Ranges
    juncr = range(22, 31)
    julcr = range(1, 23)
    # Leo Ranges
    jlr = range(23, 32)
    alr = range(1, 23)
    # Virgo Ranges
    avr = range(23, 31)
    svr = range(1, 23)
    # Libra Ranges
    slr = range(23, 32)
    olr = range(1, 24)
    # Scorpius Ranges
    osr = range(24, 31)
    nscr = range(1, 22)
    # Sagittarius Ranges
    nsar = range(22, 32)
    dsr = range(1, 22)
    # Capricornus Ranges
    dcr = range(22, 31)
    jancr = range(1, 20)
    # Aquarius Ranges
    jar = range(20, 32)
    far = range(1, 19)
    # Pisces Ranges
    fpr = range(19, 29)
    mpr = range(1, 21)

    # Aries Check March 21–April 19
    aries_check = zodiac_loop(mar, aar, march, april, aries, birthday)
    if aries_check is not None:
        return aries_check

    # Taurus Check April 20–May 20
    taurus_check = zodiac_loop(atr, mtr, april, may, taurus, birthday)
    if taurus_check is not None:
        return taurus_check

    # Gemini Check  May 21–June 21
    gemini_check = zodiac_loop(mgr, jgr, may, june, gemini, birthday)
    if gemini_check is not None:
        return gemini_check

    # Cancer Check June 22–July 22
    cancer_check = zodiac_loop(juncr, julcr, june, july, cancer, birthday)
    if cancer_check is not None:
        return cancer_check
    # Leo Check July 23–August 22
    leo_check = zodiac_loop(jlr, alr, july, august, leo, birthday)
    if leo_check is not None:
        return leo_check
    # Virgo Check August 23–September 22
    virgo_check = zodiac_loop(avr, svr, august, september, virgo, birthday)
    if virgo_check is not None:
        return virgo_check
    # Libra Check September 23–October 23
    libra_check = zodiac_loop(slr, olr, september, october, libra, birthday)
    if libra_check is not None:
        return libra_check
    # Scorpius Check October 24–November 21
    scorpius_check = zodiac_loop(osr, nscr, october, november, scorpius, birthday)
    if scorpius_check is not None:
        return scorpius_check
    # Sagittarius Check November 22–December 21
    sagittarius_check = zodiac_loop(
        nsar, dsr, november, december, sagittarius, birthday
    )
    if sagittarius_check is not None:
        return sagittarius_check
    # Capricornus Check December 22–January 19
    capricornus_check = zodiac_loop(
        dcr, jancr, december, january, capricornus, birthday
    )
    if capricornus_check is not None:
        return capricornus_check
    # Aquarius Check January 20–February 18
    aquarius_check = zodiac_loop(jar, far, january, february, aquarius, birthday)
    if aquarius_check is not None:
        return aquarius_check
    # Pisces Check February 19–March 20
    pisces_check = zodiac_loop(fpr, mpr, february, march, pisces, birthday)
    if pisces_check is not None:
        return pisces_check
    else:
        return "No zodiac"


if __name__ == "__main__":
    main()
