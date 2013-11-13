Final Exam
==========

Email me at sstanfield@smpanthers.org

All programs must be saved to your ~/final folder on smpanthers.com.

All programs' second line should look like this:

		# Scott Stanfield

If you're in a pair, do it like this:

		# Scott Stanfield and Michael Jackson

Implement 4 programs from the following list.

1. collatz.py	
Find the longest sequence under 1000. This is nearly identical to
problem number 14 on Project Euler (https://projecteuler.net/problem=14)
except that I want the number under 1000, not 1 million.

		$ ./collatz.py 
		collatz(481) has the longest length of 39 elements

2. squareroot.py 
Implement the square root algorithm (without using math.sqrt)

		$ ./squareroot.py 100
		10
		$ ./squareroot.py 101
		10.0498756211

3. deck.py		Deal a deck of shuffled cards

"Shuffle" with random a deck of cards and print the results, grouped by
hands of five. Each subsequent run of the program emits a different
result.

		$ ./deck.py
		3s  5c  Tc  7d  Jd
		3d  Kh  Th  Kd  Js
		7s  4d  9s  3c  5s
		5d  2d  Ah  8c  8d
		Qs  9c  4s  7h  5h
		Jh  4c  Qc  6c  Td
		8s  Qh  8h  9d  2h
		4h  3h  7c  Ts  Jc
		Kc  9h  6s  6h  Ad
		2c  As  Ac  Ks  Qd
		2s  6d

4. fold.py		Fold alphabet encryption
5. vowel.py		Disemvowel
6. dupes.py		Remove duplicate words from a file (lexical illusions)
7. tip.py		Tip Calculator
8. quiz.py		State Capital Quiz builder (worth two)

