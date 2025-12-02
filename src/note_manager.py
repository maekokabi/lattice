from datetime import datetime
import json

class NoteManager:
    def __init__(self):
        self.notes = []

    def save_to_file(self, filename="notes.json"):
        pass

    def load_from_file(self, filename="notes.json"):
        pass
    
    def display_all_notes(self):
        if self.notes == []:
            print("No note entries yet.")
        else:
            for note in self.notes:
                print(note)

    def add_note(self, note_object):
        pass

    def delete_note(self, note_object):
        pass

    def delete_note_by_id(self, note_id):
        pass

    


class Note:
    def __init__(self, id:int, topic, note, category, date):
        self.id = id
        self.topic = topic
        self.note = note
        self.category = category
        self.date = date

    def __repr__(self):
        return f"ID: {self.id}, Topic: {self.topic}, Note: {self.note}, Category: {self.category}, Date: {self.date}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "note": self.note,
            "category": self.category,
            "date": self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["topic"],
            data["note"],
            data["category"],
            data["date"]
        )