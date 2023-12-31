import tkinter as tk
from tkinter import Label, Entry, Button, Text, Scrollbar, Toplevel
from autocorrect import process_data, count, get_probs, get_corrections

class AutocorrectApp:
    def __init__(self, master):
        self.master = master
        master.title("Autocorrect App")

        self.label = Label(master, text="Enter a word or sentence:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.button = Button(master, text="Autocorrect", command=self.autocorrect)
        self.button.pack()

        self.result_label = Text(master, wrap=tk.WORD, height=10, width=40)
        self.result_label.pack()

    def autocorrect(self):
        user_input = self.entry.get()

        if ' ' in user_input:
            words = user_input.split()
            autocorrected_words = []

            for word in words:
                word_l = process_data("shakespeare.txt")
                vocab = set(word_l)
                word_count_dict = count(word_l)
                probs = get_probs(word_count_dict)

                autocorrected_word = get_corrections(word, probs, vocab, 1)
                autocorrected_words.append(autocorrected_word[0][0])

            autocorrected_sentence = ' '.join(autocorrected_words)
            self.result_label.delete(1.0, tk.END)
            self.result_label.insert(tk.END, "The autocorrected sentence is: ")
            self.result_label.insert(tk.END, autocorrected_sentence, "red")

        else:
            word_l = process_data("shakespeare.txt")
            vocab = set(word_l)
            word_count_dict = count(word_l)
            probs = get_probs(word_count_dict)

            autocorrected_word = get_corrections(user_input, probs, vocab, 1)
            self.result_label.delete(1.0, tk.END)

            self.result_label.insert(tk.END, "The autocorrected word is: ")
            self.result_label.insert(tk.END, autocorrected_word[0][0], "blue")
        
        self.result_label.tag_configure("blue", foreground="blue")
        self.result_label.tag_configure("red", foreground="red")

root = tk.Tk()

app = AutocorrectApp(root)

root.mainloop()