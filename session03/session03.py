# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:02:27 2019

@author: JungWoo
"""

#1.Write a program that reads an integer number and prints its previous and next numbers. See the example below.
#
#- Example input: 179
#- Example output:
# The next number for the number 179 is 180
# The previous number for the number 179 is 178
#
#x = int(input())
#print("The next number for the number", x, "is", x+1)
#print("The previous number for the number", x, "is", x-1)


#2. N students take K apples and distribute them among each other evenly. The remaining (the indivisible) part remains in the basket. 
#How many apples will each single student get? How many apples will remain in the basket?
#The program reads the numbers N and K. It should print the two answers for the questions above.
#
#- Example input: 6 
#		  50
#- Example output: 8
#		   2
#
#x, y = input().split()
#x, y = int(x), int(y)
#print(y // x, y % x)


#3.(If/else) Given an integer, print "odd" if it's odd and print "even" otherwise.
#
#- Example input: 5 
#- Example output: add 
#
#x = int(input())
#if x % 2 == 1:
#    print("odd")
#else:
#    print("even")


#4. Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), 
#print a single integer root if it exists and print "no solution" or "many solutions" otherwise.
#
#- Example input 1: 1 -2 Example output 1:  -2
#- Example input 2: 2 -1 Example output 2: no solution
#
#a, b = input().split()
#a, b = int(a), int(b)
#p = "many solutions" if (a, b) == (0, 0) else "no solution" if a == 0 else int(b / a) if b % a == 0 else "no solution"
#print(p)


#5.(For) Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
#
#- Example input: 1 10 
#- Example output: 1 2 3 4 5 6 7 8 9 10
#
#x, y = input().split()
#x, y = int(x), int(y)
#for i in range(x, y+1):
#    print(i, end=" ")


#6. For the given integer N calculate the following sum:
#1³ + 2³ + ... + N³
#
#- Example input: 3 Example output: 36
#
#x = int(input())
#y = 0
#for i in range(1, x+1):
#    y += i**3
#print(y)


#7. There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
#Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.
#
#- Example input: 5 3 5 2 1  
#- Example output: 4
#
#x = input().split()
#n = int(x[0])
#l1 = {str(i) for i in range(1, n+1)}
#l2 = {i for i in x[1:]}
#print(l1 - l2)


#8.(String) Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.
#
#- Example input: Hello World 
#- Example output: 2
#
#print(len(input().split()))


#9. Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.
#
#- Example input: In the hole in the ground there lived a hobbit
#- Example output: In tobbit
#
#x = input().split()
#print(x[0], x[-1])


#10. Given a string that may contain a letter f. Print the index of the first and last occurrence of f. If the letter f occurs only once, then output its index once. If the letter f does not occur, print -1.
#
#- Example input1: comfort
#- Example output1: 3
#- Example input2:  office
#- Example output2: 1 2
#
#- Example input3: hello
#- Example output3: -1
#
#x = str(input())
#y = ""
#if x.count("f") > 1:
#    y += str(x.rfind("f"))
#y = str(x.find("f")) + " " + y
#print(y)


#11.(While) Fibonacci numbers
#Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:
#
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
#Given a positive integer n, print the nth Fibonacci number.
#
#- Example input: 6
#- Example output: 8
#
#x, y, z = int(input()), 0, 1
#while x > 1:
#    y, z, x = z, (y+z), x-1
#print(z)


#12. Fibonacci index 
#Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:
#
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
#Given a positive integer, determine if it's the nth Fibonacci number for some n. If it is, print such n, otherwise print -1.
#
#- Example input: 8
#- Example output: 6
#
#x, y, z, c  = int(input()), 0, 1, 1
#while z != x:
#    y, z, c = z, (y+z), c+1
#print(c)


#13.(Lists) Given a list of numbers, find and print the elements that appear in it only once. Such elements should be printed in the order in which they occur in the original list.
#
#- Example input: 4 3 5 2 5 1 3 5
#- Example output: 4 2 1
#
#x = input().split()
#s = sorted(set(x), reverse=True)
#for i in s:
#    if 1 == x.count(i):
#        print(i, end=" ")


#14. Given a list of numbers, count a number of pairs of equal elements. Any two elements that are equal to each other should be counted exactly once.
#
#- Example input1: 1 2 3 2 3
#- Example output1: 2
#- Example input2: 1 1 1 1 1
#- Example output2: 10
#
#count, x = 0, [int(i) for i in input().split()]
#while len(x) > 0:
#    y = x.pop()
#    for i in x:
#        count = count+1 if y == i else count
#print(count)


#15. (Dicts) The text is given in a single line. For each word of the text count the number of its occurrences before it.
#
#- Example input : one two one two three two four three
#- Example output: 0 0 1 1 0 2 0 1
#
x, y = input().split(), {}
for i in x:
    y[i] = y[i] + 1 if i in y.keys() else 0
    print(y[i], end = " ")
