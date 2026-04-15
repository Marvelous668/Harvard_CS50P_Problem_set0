def main():
    get_input = input("Enter something with :) or :( ? ")
    get_input = convert(get_input)
    print(get_input)

def convert(emoji):
    emoji = emoji.replace(":)", "😊")
    emoji = emoji.replace(":(", "😒")
    return emoji
main()    