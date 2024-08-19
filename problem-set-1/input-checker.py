def main():
  # TODO: Your goal is to implement a conditional that checks if a user correctly enters a number. If not, **loop indefinitely** until the user does.
  # TODO: Then, print out the user's number with accompanying text.

  while True:
    try:

      ui = input("Enter a number: ")
      num = float(ui)
      break
    except ValueError:
      print("not a valid num. please enter a valid num.")

  print(f"you have entered: {num}."



if __name__ == "__main__":
  main()
