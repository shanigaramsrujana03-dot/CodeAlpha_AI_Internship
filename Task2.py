import tkinter as tk
from tkinter import messagebox
from difflib import SequenceMatcher

faqs = {
    "what is your name": "I am an AI FAQ Chatbot.",
    "what is artificial intelligence": "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn from data.",
    "what courses are available": "We offer courses in AI, Machine Learning, Python and Data Science.",
    "how can i contact you": "You can contact us through the official college contact details.",
    "what are the college timings": "College timings are from 9:00 AM to 4:00 PM.",
    "where is the college located": "The college is located in Hyderabad, Telangana."
}

def get_answer():
    question = entry.get().lower().strip()

    if not question:
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    best_question = None
    best_score = 0

    for faq_question in faqs:
        score = SequenceMatcher(None, question, faq_question).ratio()

        if score > best_score:
            best_score = score
            best_question = faq_question

    if best_score >= 0.45:
        answer = faqs[best_question]
    else:
        answer = "Sorry, I don't know the answer to that question."

    chat.insert(tk.END, "You: " + question + "\n")
    chat.insert(tk.END, "Bot: " + answer + "\n\n")
    entry.delete(0, tk.END)


window = tk.Tk()
window.title("AI FAQ Chatbot")
window.geometry("600x500")

title = tk.Label(
    window,
    text="AI FAQ Chatbot",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

chat = tk.Text(window, height=18, width=65)
chat.pack(pady=10)

entry = tk.Entry(window, width=50, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Ask",
    command=get_answer,
    font=("Arial", 12, "bold")
)
button.pack()

window.mainloop()