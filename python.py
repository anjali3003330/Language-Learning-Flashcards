import tkinter as tk
from tkinter import messagebox
import random

# Define the lists
word1 = ['eloquent', 'adroit', 'affable', 'concur', 'ephemeral', 'revere', 'ubiquitous', 'meticulous', 'sagacious', 'pragmatic']
meaning1 = ['Fluent or persuasive in speaking or writing.', 'Skillful and adept in the use of hands or mind.', 'Friendly, good-natured, and easy to talk to.', 'To agree or express agreement.', 'Lasting for a very short time.', 'To feel deep respect or admiration for something.', 'Present, appearing, or found everywhere.', 'Showing great attention to detail; very careful and precise.', 'Having or showing keen mental discernment and good judgment.', 'Dealing with things sensibly and realistically, based on practical considerations.']

word2 = ['prolific', 'ubiquitous', 'voracious', 'ambiguous', 'cacophony', 'ephemeral', 'indolent', 'nefarious', 'quintessential', 'surreptitious']
meaning2 = ['Producing abundant works or results.', 'Present or found everywhere.', 'Having a very eager approach to an activity.', 'Open to more than one interpretation; unclear.', 'A harsh, discordant mixture of sounds.', 'Lasting for a very short time.', 'Wanting to avoid activity or exertion; lazy.', 'Wicked, villainous, or criminal in nature.', 'Representing the most perfect or typical example of a quality or class.', 'Kept secret, especially because it would not be approved of.']

word3 = ['equanimity', 'facetious', 'ineffable', 'obfuscate', 'reticent', 'serendipity', 'truculent', 'veracity', 'zeitgeist', 'querulous']
meaning3 = ['Mental calmness, composure, and evenness of temper, especially in difficult situations.', 'Treating serious issues with deliberately inappropriate humor.', 'Too great or extreme to be expressed or described in words.', 'To deliberately make something unclear or difficult to understand.', 'Not revealing one\'s thoughts or feelings readily.', 'The occurrence of events by chance in a happy or beneficial way.', 'Eager or quick to argue or fight; aggressively defiant.', 'Conformity to facts; accuracy.', 'The defining spirit or mood of a particular period of history as shown by the ideas and beliefs of the time.', 'Complaining in a petulant or whining manner.']

# Example sentences for each word 

examples1 = [
    'She delivered an eloquent speech at the conference.',
    'He is adroit at solving complex mathematical problems.',
    'She is known for her affable personality and kindness.',
    'They concurred on the need for further investigation.',
    'The beauty of the sunset was ephemeral, lasting only a few moments.',
    'People revere him for his contributions to science.',
    'Mobile phones have become ubiquitous in modern society.',
    'He is meticulous in his work, paying attention to every detail.',
    'Her sagacious advice helped us make the right decision.',
    'Being pragmatic, she focused on practical solutions to the problem.'
]

examples2 = [
    'He is a prolific writer, publishing several books each year.',
    'Smartphones are ubiquitous, found everywhere around the world.',
    'He has a voracious appetite for knowledge, always seeking to learn.',
    'The meaning of his words was ambiguous, leaving us confused.',
    'The cacophony of car horns filled the busy city streets.',
    'The beauty of the cherry blossoms is ephemeral, lasting only a few weeks.',
    'He led an indolent lifestyle, preferring to relax rather than work.',
    'The nefarious activities of the criminal organization were finally exposed.',
    'His latest work is considered quintessential in the genre.',
    'He made surreptitious glances at the classified documents.'
]

examples3 = [
    'She faced the challenge with equanimity, remaining calm under pressure.',
    'He often makes facetious remarks, lightening the mood with humor.',
    'The beauty of the landscape was ineffable, beyond description.',
    'The politician tried to obfuscate the issue by using complex language.',
    'He is reticent about discussing his personal life with others.',

    'Their meeting was a serendipity, leading to unexpected opportunities.',
    'He adopted a truculent attitude, ready to argue at any moment.',
    'His veracity was questioned after inconsistencies in his story emerged.',
    'The novel captured the zeitgeist of the 1920s.',
    'She is often querulous, complaining about trivial matters.'
]

# Create dictionaries for each level
dictionary1 = dict(zip(meaning1, zip(word1, examples1)))
dictionary2 = dict(zip(meaning2, zip(word2, examples2)))
dictionary3 = dict(zip(meaning3, zip(word3, examples3)))

# Function to learn words from a dictionary
def learn_words(dictionary):
    message = ""
    for meaning, (word, example) in dictionary.items():
        message += f"Word: {word}\n"
        message += f"Meaning: {meaning}\n"
        message += f"Example: {example}\n\n"
    return message

# Function to play a level of the game
def play_level(dictionary, examples, level_name, next_level_func):
    score = 0
    total_questions = len(dictionary)
    
    # Shuffle the questions for variety
    questions = list(dictionary.items())
    random.shuffle(questions)
    
    root = tk.Tk()
    root.title(f"{level_name} Level")
    root.geometry("400x300")
    
    tk.Label(root, text="Guess the Word:").pack(pady=5)
    user_input = tk.Entry(root, width=30)
    user_input.pack(pady=5)
    
    tk.Label(root, text="Meaning:").pack(pady=5)
    meaning_label = tk.Label(root, text=questions[0][0], wraplength=380)
    meaning_label.pack(pady=5)
    
    def submit():
        nonlocal score
        nonlocal total_questions
        nonlocal questions
        user_word = user_input.get().lower()
        if len(questions) == 0:
            root.destroy()
            score_percentage = (score / total_questions) * 100
            messagebox.showinfo("Score", f"Your score for this level is: {score_percentage:.2f}%")
            next_level_func()
        else:
            correct_meaning, (word, example) = questions.pop(0)
            if user_word == word.lower():
                messagebox.showinfo("Result", "Correct answer.")
                score += 1
            else:
                messagebox.showinfo("Result", f"Wrong answer. The correct answer is: {word}")
            user_input.delete(0, tk.END)
            if questions:
                meaning_label.config(text=questions[0][0])
    
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=5)
    
    root.mainloop()

# Function to start intermediate level
def start_intermediate():
    learn_msg = learn_words(dictionary2)
    messagebox.showinfo("Learning Phase", learn_msg)
    play_level(dictionary2, examples2, 'Intermediate', lambda: continue_to_advanced())

# Function to start advanced level
def start_advanced():
    learn_msg = learn_words(dictionary3)
    messagebox.showinfo("Learning Phase", learn_msg)
    play_level(dictionary3, examples3, 'Advanced', lambda: messagebox.showinfo("Game Over", "You have completed all levels!"))

# Function to start beginner level
def start_beginner():
    global score1
    learn_msg = learn_words(dictionary1)
    messagebox.showinfo("Learning Phase", learn_msg)
    play_level(dictionary1, examples1, 'Beginner', lambda: continue_to_intermediate())

# Function to continue to intermediate level
def continue_to_intermediate():
    answer = messagebox.askquestion("Continue", "Do you want to continue to the intermediate level?")
    if answer == 'yes':
        start_intermediate()
    else:
        messagebox.showinfo("Game Over", "Level completed!")

# Function to continue to advanced level
def continue_to_advanced():
    answer = messagebox.askquestion("Continue", "Do you want to continue to the advanced level?")
    if answer == 'yes':
        start_advanced()
    else:
        messagebox.showinfo("Game Over", "Level completed!")

# Function to add a new flashcard
def add_flashcard():
    def save_flashcard():
        new_word = entry_word.get()
        new_meaning = entry_meaning.get()
        new_example = entry_example.get()
        
        if new_word and new_meaning and new_example:
            messagebox.showinfo("Success", "New flashcard added successfully!")
            dictionary1[new_meaning] = (new_word, new_example)
            entry_word.delete(0, tk.END)
            entry_meaning.delete(0, tk.END)
            entry_example.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    root = tk.Tk()
    root.title("Add Flashcard")
    root.geometry("400x200")
    
    tk.Label(root, text="Word:").pack(pady=5)
    entry_word = tk.Entry(root, width=30)
    entry_word.pack(pady=5)
    
    tk.Label(root, text="Meaning:").pack(pady=5)
    entry_meaning = tk.Entry(root, width=30)
    entry_meaning.pack(pady=5)
    
    tk.Label(root, text="Example:").pack(pady=5)
    entry_example = tk.Entry(root, width=30)
    entry_example.pack(pady=5)
    
    btn_submit = tk.Button(root, text="Submit", command=save_flashcard)
    btn_submit.pack(pady=10)
    
    root.mainloop()

# Main tkinter window
root = tk.Tk()
root.title("Vocabulary Game")
root.geometry("400x300")

# Welcome message
tk.Label(root, text="Welcome to the Vocabulary Game!", font=("Helvetica", 14, "bold")).pack(pady=10)
tk.Label(root, text="You will learn some words and their meanings with examples. Then, you will be tested on them.", font=("Helvetica", 10)).pack(pady=5)

# Button to start
btn_start = tk.Button(root, text="Start", font=("Helvetica", 15), command=start_beginner)
btn_start.pack(pady=10)

# Create flashcards button
flashcards_button = tk.Button(root, text="Create Flashcards", font=("Helvetica", 15), command=add_flashcard)
flashcards_button.pack(pady=10)

# Global variables to store scores
score1 = 0
score2 = 0
score3 = 0

root.mainloop()
