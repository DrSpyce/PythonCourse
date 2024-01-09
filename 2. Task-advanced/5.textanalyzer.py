import string
from collections import Counter


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def get_word_count(text):
    words = text.split()
    return len(words)


def get_sentence_count(text):
    sentences = []
    for sentence in text.split('.'):
        if sentence.strip():
            sentences.append(sentence.strip())
    return len(sentences)


def get_most_common_words(text, num_words=5):
    words = []
    for word in text.split():
        words.append(word.strip(string.punctuation))
    word_counter = Counter(words)
    most_common_words = word_counter.most_common(num_words)
    return most_common_words


def get_average_word_length(text):
    words = [word.strip(string.punctuation) for word in text.split()]
    total_word_length = sum(len(word) for word in words)
    return total_word_length / len(words) if len(words) > 0 else 0


def main():
    file_path = input("Enter the path to the text file: ")

    try:
        text = read_file(file_path)

        word_count = get_word_count(text)
        sentence_count = get_sentence_count(text)
        most_common_words = get_most_common_words(text)
        average_word_length = get_average_word_length(text)

        print("\nStatistics:")
        print(f"Word Count: {word_count}")
        print(f"Sentence Count: {sentence_count}")
        print(f"Most Common Words: {most_common_words}")
        print(f"Average Word Length: {average_word_length:.2f} characters")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
