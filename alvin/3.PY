import random
generated_password=""
print("!     PASSWORD GENERATOR     !")
password_length=int(input("Enter the length of the password:").strip())

for i in range(password_length):
    capital_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabet="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    symbol="!@#$%^&*()-_/"
    character_choice=random.choice([capital_alphabet,small_alphabet,numbers,symbol])
    character=random.choice(character_choice)
    generated_password+=character
print("---------------------------------------------------------------")
print("THE PASSWORD GENERATED IS :",generated_password)
print("---------------------------------------------------------------")