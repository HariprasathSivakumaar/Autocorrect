from collections import Counter
import re
import nltk

# nltk.download('words')

# def process_data():
def process_data(file_name):
    with open(file_name, "r") as file:
        text = file.read()
    text = text.lower()
    words = re.findall(r'\w+', text)
    return words
    # words = nltk.corpus.words.words()

    # return words

def get_count(word_l):
    word_count_dict = {}
    for word in word_l:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

def get_probs(word_count_dict):
    probs = {}
    total_count = sum(word_count_dict.values())
    for word, ct in word_count_dict.items():
        probs[word] = ct / total_count
    return probs

def get_corrections(word, probs, vocab, n=2, verbose=False):
    suggestions = []
    n_best = []

    def get_suggestions(word):
        suggestions = set()
        edit_one = edit_one_letter(word)
        edit_two = edit_two_letters(word)
        suggestions = list()
        if word in vocab:
            suggestions.append(word)
        elif edit_one.intersection(vocab):
            suggestions.extend(edit_one.intersection(vocab))
        elif edit_two.intersection(vocab):
            suggestions.extend(edit_two.intersection(vocab))
        return suggestions

    suggestions = get_suggestions(word)
    word_probs = {word: probs.get(word, 0) for word in suggestions}
    n_best = Counter(word_probs).most_common(n)
    
    if verbose:
        print("entered word = ", word)
        print("suggestions = ", suggestions)
    
    return n_best

def edit_one_letter(word):
    delete_l = [word[:i] + word[i + 1:] for i in range(len(word))]
    switch_l = [word[:i] + word[i + 1] + word[i] + word[i + 2:] for i in range(len(word)-1)]
    replace_l = [word[:i] + letter + word[i + 1:] for i in range(len(word)) for letter in 'abcdefghijklmnopqrstuvwxyz']
    insert_l = [word[:i] + letter + word[i:] for i in range(len(word) + 1) for letter in 'abcdefghijklmnopqrstuvwxyz']
    return set(delete_l + switch_l + replace_l + insert_l)

def edit_two_letters(word):
    edit_two_set = set()
    first_edit = edit_one_letter(word)
    for w in first_edit:
        second_edit = edit_one_letter(w)
        edit_two_set.update(second_edit)
    return edit_two_set

# Get the input word from the user
user_input = input("Enter a word: ")

# Load and process the data
word_l = process_data(r"C:\Users\Hariprasath\Downloads\Coursera\Natural Language Processing Specialization\2 - Natural Language Processing with Probabilistic Models\Week - 1\data\shakespeare.txt")
# word_l = process_data()
vocab = set(word_l)
word_count_dict = get_count(word_l)
probs = get_probs(word_count_dict)

# Get autocorrected word and print it
autocorrected_word = get_corrections(user_input, probs, vocab, 1)
print(f"The autocorrected word is: {autocorrected_word[0][0]}")

# MAIN FINAL CODE for SENTENCE
a = []

a = [item for item in input("Enter the list items : ").split()]

for i in a:
    word_l = process_data(r"C:\Users\Hariprasath\Downloads\Coursera\Natural Language Processing Specialization\2 - Natural Language Processing with Probabilistic Models\Week - 1\data\shakespeare.txt")
    vocab = set(word_l)
    word_count_dict = get_count(word_l)
    probs = get_probs(word_count_dict)

    # Get autocorrected word and print it
    autocorrected_word = get_corrections(i, probs, vocab, 1)    
    # print(''.join(autocorrected_word[0][0]))
    print(f"The autocorrected word is: {autocorrected_word[0][0]}")