from dataclasses import dataclass, field
import random

import numpy as np
import pandas as pd

NUMPEOPLE = 30
QUESTION_TOPICS = (
    "sport",
    "art",
    "science",
    "science",
    "sport",
    "rand",
    "art",
    "sport",
    "rand",
    "science",
    "science",
    "art",
    "rand",
    "rand",
)


@dataclass
class Student:
    name: str
    interest: str

    def _rand_answers(self, questions):
        switch = {self.interest: True}
        for topic in questions:
            limits = (0.65, 1.00) if switch.get(topic, False) else (0.00, 0.75)
            yield random.uniform(*limits)

    def do_survay(self, questions):
        if not hasattr(self, "answer"):
            self.answers = tuple("{:.3f}".format(answer) for answer in
                self._rand_answers(questions))
        return None


@dataclass
class Group:
    participants: list = field(default_factory=list)

    def add_participant(self, participant):
        self.participants.append(participant)

    def make_survay(self, questions):
        for participant in self.participants:
            participant.do_survay(questions)

    def export_results(self, questions, to_file="students.csv"):
        with open(to_file, "w") as f:
            f.write(self._format_output(questions))
            for student in self.participants:
                output = self._format_output((student.name, student.interest, *student.answers))
                f.write(output)

    def _format_output(self, iterator):
        csv_fields = ", ".join(str(field) for field in iterator)
        output_line = csv_fields + "\n"
        return output_line
                

def clean_whitespace(name):
    return " ".join(name.split())


if __name__ == "__main__":
    questions = QUESTION_TOPICS
    with open("names.txt", "r") as _names:
        names_list = [clean_whitespace(name) for name in _names]
    names = random.sample(names_list, NUMPEOPLE)

    group = Group()
    for name in names:
        interest = random.choice(list(set(questions)-set(["rand"])))
        group.add_participant(Student(name, interest))

    group.make_survay(questions)
    group.export_results(questions)
