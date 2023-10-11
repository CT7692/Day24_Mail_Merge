with open("Input\\Names\\invited_names.txt") as friends_file:
    friends_list = friends_file.readlines()

with open("Input\\Letters\\starting_letter.txt") as letter_file:
    letter = letter_file.read()

for friend_text in friends_list:
    friend = friend_text.strip()
    with open(f"Output\\ReadyToSend\\{friend}'s Letter.txt", mode="w") as file:
        new_letter = letter.replace("[name]", f"{friend}")
        file.write(new_letter)
