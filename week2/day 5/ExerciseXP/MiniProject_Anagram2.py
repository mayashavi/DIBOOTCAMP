
from MiniProject_Anagram import AnagramChecker

def main():
    checker = AnagramChecker("sowpods.txt")

    while True:
        print("\n==== ANAGRAM MENU ====")
        print("1. Enter a word")
        print("2. Exit")

        choice = input("Choose (1 or 2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        elif choice == "1":
            user_input = input("Enter a single word: ").strip()

            # Validate input
            parts = user_input.split()
            if len(parts) != 1:
                print("Error: Please enter ONE word only.")
                continue

            word = parts[0]

            if not word.isalpha():
                print("Error: Only letters allowed. No numbers or symbols.")
                continue

            # Check if valid English word
            if not checker.is_valid_word(word):
                print(f"'{word}' is NOT a valid English word.")
                continue

            # Get anagrams
            anagrams = checker.get_anagrams(word)

            print("\n=== RESULT ===")
            print(f"WORD: {word.upper()}")
            print("This is a valid English word.")

            if anagrams:
                print("Anagrams found:")
                print(", ".join(anagrams))
            else:
                print("No anagrams found for this word.")

        else:
            print("Invalid choice. Please pick 1 or 2.")

if __name__ == "__main__":
    main()
