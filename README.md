# **Friends Sorter**
#### **Video Demo:**  <https://youtu.be/Wx16Dh6HEWk>
#### **Description:**

### **Main Program**
This program sorts out a list of your friends. It takes in a CSV file that has three columns.
First one being the name of the friend. The second column is the attribute of the friend.
The third column is the birthday of the friend. The attribute and birthday are then sorted through
the program and a new ouput CSV file is then given. In the output CSV you will find the same first column, name.
In the second column, you will find the role in the friend group they were sorted into based off of their attribute.
Then in the third column, you will find their zodiac sign based off of the birthday given.

There are 16 roles in the friend group. In each role there are three attributes given.
The attributes of course relate to a trait of the role.

<sub>*_Here is reference table made up for each role and their attributes_</sub>

**source:** <https://www.wikihow.com/Friend-Group-Roles>

### Role, Attributes

1. The Mom = lawmaker, stickler, caring
2. The Therapist = listner, comforting, insightful
3. The Connector = bonder, glue, friendly
4. The Planner = controlling, rigid, organized
5. The Joker = funny, silly, witty
6. The Hipster = different, special, quirky
7. The Overachiever = extra, bold, leader
8. The Flirt = cute, beautiful, sweet
9. The Party Animal = crazy, entertaining, hilarious
10. The Chill One = calm, relaxed, compossed
11. The Artistic One = creative, talented, imagitive
12. The Fastionable One = trendy, stunning, together
13. The Smart One = academic, know-it-all, problemsolver
14. The Hot Head = opinionated, firey, figher
15. The Pessimist = judgy, negative, responsible
16. The Absolute Mess = unorganized, unlucky, lost

<sub>*_This data can also be found in `fraars.txt` file_</sub>

The zodiac is based off of the western zodiac calendar i.e. Aries, Taurus, etc.

**source:** <https://www.britannica.com/topic/zodiac>

The input birthday needs to be formated as month day(as number).

**Example:**
```
march 12
```

**The full CSV for the input should look like this:**
```
name,attribute,birthday
Timmy,special,october 18
```

To run the program you must give 4 arguments total.

Argument 1 = **python**

Argument 2 = **project.py**

Argument 3 = **input CSV file**

Argument 4 = **output CSV file**

**Terminal should look like:**
```
$ python project.py friends_input.csv friends_output.csv
```
<sub>*_Note of course the last two arguments are whatever the csv file names are that you want to input_</sub>

### **Unit Test**

You will also find `test_project.py`

This file is to run a wide range of unit test of each of the four custom functions that were made in the project

**To run the tests for yourself type this command into the terminal:**
```
$ pytest test_project.py
```

### **Input CSV**

The next file you will find in the project folder is `friends_input.csv`

In this CSV file is the input data that will get pulled into the program.

**It should have a data set already inside it looking like this:**
```
name,attribute,birthday
Dominic,stickler,april 13
Paul,leader,july 27
George,quirky,december 24
Matt,unlucky,july 3
Josh,negative,october 19
Anakin,firey,april 5
Obi-Wan,compossed,july 4
Ahsoka,bonder,january 25
Frodo,imagative,september 22
Sam,glue,april 6
Merry,entertaining,november 24
Pippin,funny,may 28
```
<sub>*_Note that you can add/change lines in this file to test the program out. Just follow the format as shown above earlier_</sub>

### **Output CSV**

The last file you will find is called `friends_output.csv`

When you first open it up it maybe empty. Once you run the program it should get filled out with the sorted data

The output should look like this when program is ran using same input data from earlier above:
```
name,role,zodiac
Dominic,The Mom,Aries
Paul,The Overachiever,Leo
George,The Hipster,Capricornus
Matt,The Absolute Mess,Cancer
Josh,The Pessimist,Libra
Anakin,The Hot Head,Aries
Obi-Wan,The Chill One,Cancer
Ahsoka,The Connector,Aquarius
Frodo,No role,Virgo
Sam,The Connector,Aries
Merry,The Party Animal,Sagittarius
Pippin,The Joker,Gemini
```
<sub>*_Note that is is only a sample set of the various outputs that can be given from the program._</sub>
