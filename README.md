# python-challenge
Bootcamp Data Analytics week 3 homework assignment

## Introduction
This homework assignment puts into action the introdutory Python content we've covered in Module 3 which include topics such as:

- importing modules
- conditional statements
- creating lists and dictionaries
- creating functions

This homework assignment is has two tasks Pybank and Pypoll. Each task has it's own directory with a `main.py` script to run. Each directory has it's own resources sub-directory which contains the dataset.

## Task 1: PyBank
Create a Python script to analyse the financial records of a company from  a csv file. The csv file contatins two columns: "Date" and "Profit/Losses". The script will
output the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

The analysis ouputs the following results to file and terminal:
```
Financial Analysis
-----------------------------------
Total Months: 86
Total: $22564198
Average change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```


## Task 2: PyPoll
Automate a vote counting process from a csv file. 

The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

The analysis ouputs the following results to file and terminal:
```
Election Results

----------------------------
Total Votes: 369711
----------------------------

Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)

----------------------------
Winner: Diana DeGette
----------------------------
```


