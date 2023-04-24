#source : https://thispointer.com/replace-first-n-characters-from-a-string-in-python/
# this replacement is done using counting
account_number = input("Please enter a 10 digit account number : ")
# this will replace the first 6 characters in the string with "XXXXXX"
n = 6
hidden_account = "XXXXXX"
account_number = hidden_account + account_number[n:]

print("Your account number is {}".format(account_number))

''' online, I found out that this can also be achieved using "Regex"
  which is similar, albeit slightly more complex looking to a noob like me
import re
account_number = input("Please enter a 10 digit account number : ")
account_number = re.sub(r'^.{0,6}', 'xxxxxx' account_number)

print("Your account number is {}".format(account_number))
although I could not get this to work, I do appreciate how it might work'''
#why is this not on the repo?