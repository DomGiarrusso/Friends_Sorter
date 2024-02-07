# **Friends Sorter**

![Static Badge](https://img.shields.io/badge/Program-Python_CLI-blue?style=flat)

<details>
<summary> Table of Contents </summary>

-   [**Friends Sorter**](#friends-sorter)
    -   [Demo Video](#demo-video)
    -   [Description:](#description)
    -   [Motivations](#motiviations)
    -   [🚀 Quick Start](#-quick-start)
        -   [Clone the repo](#clone-the-repo)
        -   [Navigate to repo](#navigate-to-repo)
        -   [Once in the repo you can run](#once-in-the-repo-you-can-run)
        -   [Now to see the sorted output run](#now-to-see-the-sorted-output-run)
    -   [⚙️ Usage](#️-usage)
        -   [Reference Table for Role and Attributes](#reference-table-for-role-and-attributes)
        -   [Unit Test](#unit-test)
        -   [**Input CSV**](#input-csv)
        -   [**Output CSV**](#output-csv)
    -   [🤝 Contributing](#-contributing)
        -   [Clone the repo if you haven't already](#clone-the-repo-if-you-havent-already)
        -   [Add or change code](#add-or-change-code)
        -   [Fork repo and open a pull request](#fork-repo-and-open-a-pull-request)

</details>

## [Demo Video](https://youtu.be/Wx16Dh6HEWk)

## Description:

A Python CLI program that allows you to input a list of friends with an attribute and birthdate. It then outputs a new list with the friends' role in the friend group and their star sign.

## Motivations

The idea for this project came about after having a heated argument with my friends about what role we all play in our friend group. At the time I was taking Harvard's CS50P course and was about to start my final project. So I decided why not make a Python CLI program that allows you to be able to sort your friends and even yourself.

## 🚀 Quick Start

> [!IMPORTANT]
> You will need [Python](https://www.python.org/) 3.11+ to run this program
> <sub>_3.10 and bellow may work but is untested_</sub>
>
> <sub>will use bash to demonstrate commands but you can use other terminals as well</sub>

### Clone the repo

```bash
$ git clone https://github.com/DomGiarrusso/Friends_Sorter.git
```

### Navigate to repo

```bash
$ cd path/to/repo/...
```

### Once in the repo you can run

```bash
$ python project.py friends_input.csv friends_output.csv
```

### Now to see the sorted output run

```bash
$ cat friends_output.csv
```

**Tada! you just sorted a group of friends**

> [!NOTE]
> More info provided below on how you can sort create your own list of friends to sort them.

## ⚙️ Usage

This program sorts out a list of your friends. It takes in a CSV file that has three columns.
The first one is the name of the friend. The second column is the attribute of the friend.
The third column is the birthday of the friend. The attribute and birthday are then sorted through
the program and a new ouput CSV file is then given. In the output CSV you will find the same first column, name.
In the second column, you will find the role in the friend group they were sorted into based off of their attribute.
Then in the third column, you will find their zodiac sign based off of the birthday given.

There are 16 roles in the friend group. In each role, there are three attributes given.
The attributes of course relate to a trait of the role.

### Reference Table for Role and Attributes

**source:** [wikiHow](https://www.wikihow.com/Friend-Group-Roles)

| Role                | Attributes                           |
| ------------------- | ------------------------------------ |
| The Mom             | lawmaker, stickler, caring           |
| The Therapist       | listner, comforting, insightful      |
| The Connector       | bonder, glue, friendly               |
| The Planner         | controlling, rigid, organized        |
| The Joker           | funny, silly, witty                  |
| The Hipster         | different, special, quirky           |
| The Overachiever    | extra, bold, leader                  |
| The Flirt           | cute, beautiful, sweet               |
| The Party Animal    | crazy, entertaining, hilarious       |
| The Chill One       | calm, relaxed, compossed             |
| The Artistic One    | creative, talented, imagitive        |
| The Fastionable One | trendy, stunning, together           |
| The Smart One       | academic, know-it-all, problemsolver |
| The Hot Head        | opinionated, firey, figher           |
| The Pessimist       | judgy, negative, responsible         |
| The Absolute Mess   | unorganized, unlucky, lost           |

The zodiac is based off of the western zodiac calendar i.e. Aries, Taurus, etc.

**source:** [Britannica](https://www.britannica.com/topic/zodiac)

The input birthday needs to be formated as month day(as number).

**Example:**

```
march 12
```

**The full CSV for the input should look like this:**

```
name,attribute,birthday
Timmy,special,october 18
etc, ..., ...
```

To run the program you must give 4 arguments total.

Argument 1 = `python`

Argument 2 = `project.py`

Argument 3 = `input CSV file`

Argument 4 = `output CSV file`

**Terminal should look like:**

```bash
$ python project.py friends_input.csv friends_output.csv
```

<sub>\*_Note of course the last two arguments are whatever the csv file names are that you want to input and output_</sub>

### Unit Test

You will also find `test_project.py` inside the repo

This file is to run a wide range of unit test of each of the four custom functions that were made in the project

**To run the tests for yourself type this command into the terminal:**

```bash
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

<sub>\*_Note that you can add/change lines in this file to test the program out. Just follow the format as shown above earlier_</sub>

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

<sub>\*_Note that is is only a sample set of the various outputs that can be given from the program._</sub>

## 🤝 Contributing

### Clone the repo if you haven't already

```bash
$ git clone https://github.com/DomGiarrusso/Friends_Sorter.git
```

### Add or change code

### Fork repo and open a pull request

[Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

Also feel free to contact me at dev.domgiarrusso@gmail.com
