# Poker Chip Counter

This in-class/homework assignment covers several new concepts:

- it's very common in computer science to build short programs that manipulate files
- invisible ASCII characters like tabs are used in lots of files
- dealing with NULL or missing data
- converting words into numbers
- iterating through a file using wc.py as a starting point
- building up to the Dictionary object in Python
- eventually we'll accomplish this task with AWK and Shell utilities

A new poker data file has been created. And this one is a little bit easier. 

|Player  |chipcount-day-1  |chipcount-day-2  |
|--------|-----------------|-----------------|
|Josh P  |1000             |2080             |
|Marcus C|625              |0                |
|Daniel H|980              |870              |
|Trevon N|                 |0                |
|Beeman  |1200             |1095             |
|Nick U  |280              |975              |


The poker data file is located at this [gist](https://gist.github.com/scottstanfield/0b18719bf24ecd20745d)

On your smpanthers.com account, use these commands to download the file:

        $ cd ~/code
        $ curl https://gist.github.com/scottstanfield/0b18719bf24ecd20745d/raw > poker.tsv
        $ expand -20 poker.tsv

The extension "tsv" stands for tab-separated variables. csv is more common, but 
I like tabs.

The only problem with tabs are they are sometimes indistinguishable from spaces. 
In ASCII, they are stored as **0x09**. In the C language and Python, they are 
represented with two characters, the backtick and a lower-case t: `\t`

Type in these lines in ipython to see how \t is translated into a tab character

        print "michael\tjackson"
        print "michael" + "\t"*5 "jackson"


The `expand` unix program replaces the tabs with 20 spaces, making it easier (for humans) to read.
Think of `expand` like `cat` but one that simply replaces tabs. Very handy.

Your first goal is to find the chip leader for day 1. 

Start with a copy of your working `wc`.py file. It's a good place to start since it walks through, line-by-line whatever file is `cat`ted into it. Test it like this:

        $ cat poker.tsv | wc.py
        35 153 725

There are 34 poker players (35 lines since the first line is the "header" -- something you'll need to avoid).

## TEST YOUR PROGRAM
The output of chipleader.py when run should look like this:

		$ cat poker.tsv | chipleader.py
		Jose Jasso 2925



