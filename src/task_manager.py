from datetime import datetime
import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def save_to_file(self, filename="tasks.json"):
        pass

    def load_from_file(self, filename="tasks.json"):
        pass

class Task:
    def __init__(self, id:int, task, description="", deadline="No Deadline", done=False):
        self.id = id
        self.task = task
        self.description = description
        self.deadline = deadline
        self.done = done

    def __repr__(self):
        return f"ID: {self.id}, Task: {self.task}, Description: {self.description}, Deadline: {self.deadline}, Status: {self.done}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "description": self.description,
            "deadline": self.deadline,
            "done": self.done
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["task"],
            data["description"],
            data["deadline"],
            data["done"]
        )