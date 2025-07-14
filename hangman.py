import random

def print_header():
    print("\n" + "="*40)
    print("        🎮 Hangman Game 🎮")
    print("="*40)

def display_status(guessed, attempts, used_letters):
    print("\nWord     :", " ".join(guessed))
    print("Attempts :", attempts)
    print("Used     :", ", ".join(used_letters))

def play_game():
    words = ["apple", "banana", "mango", "grape", "orange"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print_header()

    while attempts > 0 and "_" in guessed:
        display_status(guessed, attempts, used_letters)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabet only.")
            continue

        if guess in used_letters:
            print("⚠️ You already guessed that letter.")
            continue

        used_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    print("\n" + "-"*40)
    if "_" not in guessed:
        print(f"🎉 You won! The word was: {word}")
    else:
        print(f"😢 You lost! The word was: {word}")
    print("-"*40)

if __name__ == "__main__":
    play_game()
