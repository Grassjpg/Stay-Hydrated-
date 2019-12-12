n = input("How  Many Cups Of Water Have You Had Today? \n")
n = int(n)
if n >= 11 and n <= 17:
    print(
        "You Are Probably Hydrated. Good Job!"
    )
elif n < 11:
    print(
        "You Should Drink More Water! The Average Adult Male Needs 15.5 Cups A Day! The Average Adult Women Needs At Least 11.5!"
    )
elif n >= 18:
    print("Be Careful! Water Is Great, But You Can Get Over-Hydrated!")
else:
  print("Please enter a numeral!")