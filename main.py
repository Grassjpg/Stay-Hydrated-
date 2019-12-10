n = input("How  Many Cups Of Water Have You Had Today? ")
n = int(n)
if n > 10 and n < 20:
    print(
        "You May Be Hydrated, But You Should Drink Some More! The Average Adult Male Needs 15.5 Cups A Day! The Average Adult Women Needs At Least 11.5!"
    )
elif n < 10:
    print(
        "You Should Drink More Water! The Average Adult Male Needs 15.5 Cups A Day! The Average Adult Women Needs At Least 11.5!"
    )
elif n == 10:
    print(
        "You May Be Hydrated, But You Should Drink Some More! The Average Adult Male Needs 15.5 Cups A Day! The Average Adult Women Needs At Least 11.5!"
    )
elif n > 20:
    print("Be Careful! Water Is Great, But You Can Get Over-Hydrated!")
else:
    print('Please Enter A Numeral!')
