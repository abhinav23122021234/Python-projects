# 🔠 NATO Phonetic Alphabet Converter

This folder contains a Python script that converts user-inputted words into their NATO phonetic alphabet representation using a CSV file.

## 📖 What is the NATO Phonetic Alphabet?

The **NATO Phonetic Alphabet** is a standardized set of code words used to represent letters in spoken communication. It was developed by NATO to improve clarity and avoid misinterpretation, especially in noisy environments like military and aviation communications. Each letter of the English alphabet is assigned a distinct word to ensure accurate transmission of information.

## 📂 Files in this Folder

- 📜 **`nato_phonetic.py`**: The main Python script that reads the CSV file and converts words into phonetic code.
- 📄 **`nato_phonetic_alphabet.csv`**: A CSV file containing the NATO phonetic alphabet with letters and corresponding code words.

## ⚙️ How It Works

1. 📥 The script reads `nato_phonetic_alphabet.csv` using pandas.
2. 🗂️ It creates a dictionary where each letter maps to its phonetic code.
3. 📝 The user is prompted to enter a word.
4. 🔊 The script converts the word into phonetic code and displays the result.

## 🚀 Usage

1. ✅ Ensure you have Python installed.
2. 📦 Install pandas if not already installed:
   ```bash
   pip install pandas
   ```
3. ▶️ Run the script:
   ```bash
   python nato_phonetic.py
   ```
4. ⌨️ Enter a word when prompted.

## 🖥️ Example Output
```
Enter a word: Chat
['Charlie', 'Hotel', 'Alfa', 'Tango']
```

## ℹ️ Notes
- 🔠 The input is converted to uppercase automatically.
- 📂 Ensure `nato_phonetic_alphabet.csv` is in the same folder as the script.

---

📚 This simple tool helps users learn and utilize the NATO phonetic alphabet effectively! ✨
