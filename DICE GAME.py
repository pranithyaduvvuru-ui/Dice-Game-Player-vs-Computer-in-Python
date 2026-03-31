import random

def roll_dice():
    return random.randint(1, 6)

def player_turn():
    input("Press Enter to roll dice...")
    roll = roll_dice()
    print(f"You rolled: {roll}")
    return roll

def computer_turn():
    roll = roll_dice()
    print(f"Computer rolled: {roll}")
    return roll

def game():
    player_score = 0
    computer_score = 0
    target = 30

    print("🎯 First to reach 30 wins!\n")

    while player_score < target and computer_score < target:
        print("\n--- Your Turn ---")
        player_score += player_turn()
        print(f"Your Total Score: {player_score}")

        if player_score >= target:
            break

        print("\n--- Computer Turn ---")
        computer_score += computer_turn()
        print(f"Computer Total Score: {computer_score}")

    print("\n🏁 Game Over!")

    if player_score > computer_score:
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")

# Start the game
game()
