import random
secret = random.randint(1, 100)

guess_count = 0

while True:
  try:
    number_guessed = int(input("Guess a number between 1 and 100: "))
  except ValueError:
    print("Oops! Please enter a valid number")
    continue
  guess_count += 1

  if guess_count >= 5:
    print("Sorry you couldn't guess in 5 tries, try again?")
    break

  elif number_guessed > secret:
    print("Too high")
    continue
  elif number_guessed < secret:
    print("Too low")
    continue
  else:
    print(f"You got it right!!, you guessed {guess_count} times ")
    break