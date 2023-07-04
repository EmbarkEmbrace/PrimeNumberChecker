# Defining function "prime_checker."
def prime_checker(number):
  #Populate answer.
  answer = ""
  # Assign all numbers within the range of 2 - chosen number.
  for i in range(2, number):
    # If "chosen number" divisble by "i" (numbers in range of 2 - chosen number), with no            remainder:
    if number % i == 0:
      # Make "answer" equal to "The 'chosen number' is not a Prime Number."
      answer = f"{number} is not a Prime Number."
      # Break "for" loop if "chosen number" was divisble by the first integer in our specified           range.
      break
    # If "chosen number" is divisible by "i" with remainders:
    else:
      # Make "answer" equal to "The 'chosen number' is a Prime Number."
      answer = f"{number} is a Prime Number."
  # Print "answer."
  print(answer)

# Ask user to input a number (integer), and assign it the "n."
n = int(input("Enter a number to find it's a Prime number or not: "))
# Take "n," and assign it to "number," and specified function.
prime_checker(number = n)