import requests
Search_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'


def Meaning(word):
    response = requests.get(Search_URL + word)
    response.raise_for_status()
    j = response.json()
    means = j[0]["meanings"][0]["definitions"][0]["definition"].capitalize()
    head = j[0]["word"].title()
    print('Word: ', head)
    return means


def check_Word():
    word = input("Enter the word: ")
    try:
        print('>>', Meaning(word))
    except Exception:
        print(f">> Word \"{word}\" not found!")
    print()


def process():
    check_Word()
    choice = input("Do you want to try again? (Y/N) ").lower()
    if choice == 'y' or choice == 'yes':
        process()


def main():
    process()


if __name__ == "__main__":
    main()
