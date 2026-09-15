import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es"
}

def translate_text():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = languages[source_language.get()]
    target = languages[target_language.get()]

    try:
        result = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror(
            "Error",
            "Translation failed. Please check your internet connection."
        )

def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# Main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("650x550")

# Title
title = tk.Label(
    root,
    text="Language Translator",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

# Input label
tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 13, "bold")
).pack()

# Input box
input_box = tk.Text(
    root,
    height=7,
    width=65,
    font=("Arial", 12)
)
input_box.pack(pady=10)

# Language selection
language_frame = tk.Frame(root)
language_frame.pack(pady=10)

tk.Label(
    language_frame,
    text="From:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=5)

source_language = ttk.Combobox(
    language_frame,
    values=list(languages.keys()),
    state="readonly",
    width=15
)
source_language.set("English")
source_language.grid(row=0, column=1, padx=10)

tk.Label(
    language_frame,
    text="To:",
    font=("Arial", 12)
).grid(row=0, column=2, padx=5)

target_language = ttk.Combobox(
    language_frame,
    values=list(languages.keys()),
    state="readonly",
    width=15
)
target_language.set("Telugu")
target_language.grid(row=0, column=3, padx=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    width=15
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=15
).grid(row=0, column=1, padx=10)

# Output label
tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 13, "bold")
).pack()

# Output box
output_box = tk.Text(
    root,
    height=7,
    width=65,
    font=("Arial", 12)
)
output_box.pack(pady=10)

# Start application
root.mainloop()