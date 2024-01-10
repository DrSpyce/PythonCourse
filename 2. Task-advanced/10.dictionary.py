from PyDictionary import PyDictionary


def get_word_info(word):
    dictionary = PyDictionary()

    try:
        definition = dictionary.meaning(word)
        synonyms = dictionary.synonym(word)

        if definition:
            print(f"Definition of '{word}':")
            for part_of_speech, meanings in definition.items():
                print(f"{part_of_speech.capitalize()}: {', '.join(meanings)}")

            if synonyms:
                print(f"\nSynonyms:")
                print(', '.join(synonyms))
            else:
                print("No synonyms found.")
        else:
            print(f"No definition found for '{word}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    user_input = input("Enter a word: ")
    get_word_info(user_input)