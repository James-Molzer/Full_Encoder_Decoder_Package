import encoder
import decoder
def menu(choice):
    if choice == "e":
        print(encoder.encode(input("Type what you want encrypted: ")))
        return menu(input("would you like to Encrypt (e) or Translate (t): "))
    elif choice == "t":
        print(decoder.decode(input("Enter your code: ")))
        return menu(input("would you like to Encrypt (e) or Translate (t): "))
    else:
        print("invalid selection please enter e or t")
        return menu(input("would you like to Encrypt (e) or Translate (t): "))

