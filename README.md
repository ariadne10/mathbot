# mathbot

Say you are an online casino & there are winners and losers every week that need to be paid out on mondays. The casino generates a data sheet with the winners & their winnings, & losers & their losses.

Every Monday you need to figure out what losers need to pay what winners.

You need to use the data given to you to figure out what losers need to pay the winners & how much they need to pay...with python. 

## Losers:

mike = (4)

jake = (6)

sarah = (12)

rob = (13)

## Winners:

alex = (21)

john = (14)

## Variables:

(a) = winners number

(b) = sum of loser's losses before exceeding (a)

(c) = last number that exceeds (a) when added to satisfy (a)

(d) = a - b

(e) = c - d

## Steps:

1. Find first winners number that you want to satisfy (a):

   a = 21

2. Starting from the top of the losers list you need to sum the loser's losses together & stop before exceeding (a):

   b = 4 + 6
   
   b = 10
  
3. Find the number that exeeds (a) when added to satisfy (a):

   c = 12
   
4. Find the number that is needed to satisfy (a) when added to (b):

   d = a - b
   
   d = 21 - 10
   
   d = 11
   
5. Add (d) to (b) to satisfy the (a):

   a = b + d
   
   21 = 10 + 11
   
6. Mark (a) as satisfied & start to satisfy the next winner with (e)

   e = 1
  
7. Go back to step 1:

## Final Product looks something like this

### Winner (alex = 21)

  mike = 4
  
  jake = 6
  
  sarah = 11
  
### Winner (john = 14)

  sarah = 1
  
  rob = 13
   
   






