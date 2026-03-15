import pandas as pd
import ai_summarizer
import numpy as np
from datetime import datetime


class NotesManager:

    def __init__(self):
        self.notes = {}

    # Add note
    def add_note(self):
        note_id = input("Enter Note ID: ")

        if note_id in self.notes:
            print("Note ID already exists!")
            return

        title = input("Enter title: ")
        category = input("Enter category (Personal/Work/Ideas): ")
        content = input("Enter note content: ")

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

        self.notes[note_id] = {
            "title": title,
            "category": category,
            "content": content,
            "timestamp": timestamp
        }

        print("Note added successfully!")

    # View all notes
    def view_notes(self):

        if not self.notes:
            print("No notes available")
            return

        for note_id, note in self.notes.items():
            print("\nID:", note_id)
            print("Title:", note["title"])
            print("Category:", note["category"])
            print("Content:", note["content"])

    # Update note
    def update_note(self):

        note_id = input("Enter note ID to update: ")

        if note_id in self.notes:
            new_content = input("Enter new content: ")
            self.notes[note_id]["content"] = new_content
            print("Note updated")
        else:
            print("Note not found")

    # Delete note
    def delete_note(self):

        note_id = input("Enter note ID to delete: ")

        if note_id in self.notes:
            del self.notes[note_id]
            print("Note deleted")
        else:
            print("Note not found")

    # Category summary using NumPy
    def category_summary(self):

        categories = np.array([note["category"] for note in self.notes.values()])

        unique = np.unique(categories)

        print("\nCategory count:")
        for cat in unique:
            count = np.sum(categories == cat)
            print(cat, ":", count)

    # Export to Excel
    def export_excel(self):

        if not self.notes:
            print("No notes to export")
            return

        df = pd.DataFrame.from_dict(self.notes, orient="index")
        df.to_excel("notes_data.xlsx")

        print("Notes exported to Excel")

        # AI Summarizer

    # AI Summarizer
    def ai_summarize(self):

        note_id = input("Enter note ID to summarize: ")

        if note_id not in self.notes:
            print("Note not found")
            return

        content = self.notes[note_id]["content"]

        summary = ai_summarizer.summarize_note(content)

        print("\nAI Summary:")
        print(summary)

# -------- MAIN PROGRAM --------

manager = NotesManager()

while True:

    print("\n----- NOTES MANAGER -----")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Category Summary")
    print("6. Export to Excel")
    print("7. AI Summarize Note")
    print("8. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        manager.add_note()

    elif choice == "2":
        manager.view_notes()

    elif choice == "3":
        manager.update_note()

    elif choice == "4":
        manager.delete_note()

    elif choice == "5":
        manager.category_summary()

    elif choice == "6":
        manager.export_excel()

    elif choice == "7":
        manager.ai_summarize()

    elif choice == "8":
        print("Exiting program")
        break

    else:
        print("Invalid choice")