def main():
    import random
    lowest_num = 1
    highest_num = 100
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True

    while is_running:
        guess = input(f"Enter Your Guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print(f"Please select a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too Low! Try Again")
            elif guess > answer:
                print("Too High! Try Again")
            else:
                print()
                print(f"CORRECT! The Answer Was {answer}")
                print(f"Number of Guesses: {guesses}")
                is_running = False
        else:
            print("Invalid Guess")
            print(f"Please select a number between {lowest_num} and {highest_num}")

if __name__ == '__main__':
    main()
