name = input("Enter name: ")
choice = ""
while choice != "Q":
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    elif choice != 'Q':
        print("Invalid choice")
print("Finished.")