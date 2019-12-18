from dataclasses import dataclass, field
from itertools import chain
import random

import numpy as np
import pandas as pd

NUM_PEOPLE = 30
QUESTIONS = (
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


@dataclass(order=True)
class Student:
    name: str
    interest: str

    def _gen_rand_answers(self, questions):
        """Generator for creating answers.

        The generator uses ``random.uniform`` together with appropriate limits
        to yield random number (answer) to yes/no questions from ``questions``.
        Returning 0 means 'completely negative' and 1 'completely positive'
        answer. In case the question is related to ``Student.interest`` answers
        are favourable (this makes answering more realistic). Therefore, the
        limits of ``random.uniform`` for favourable questions are higher than
        the limits for other questions.
        """ 
        switch = {self.interest: True}
        for question_topic in questions:
            answer_limit = (0.65, 1.00) if switch.get(question_topic, False) else (0.00, 0.75)
            answer = random.uniform(*answer_limit)
            yield answer

    def give_answers(self, questions):
        fmt = "{:.2f}"
        try:
            if self.answer:
                pass
        except AttributeError:
            self.answers = tuple(fmt.format(answer) for answer in self._gen_rand_answers(questions))


@dataclass
class Group:
    participants: list = field(default_factory=list)

    def add_participant(self, item):
        self.participants.append(item)

    def make_survey(self, questions):
        for participant in self.participants:
            participant.give_answers(questions)

    def survey_results(self, questions, file_name="students.csv"):
        with open(file_name, "w") as f:
            _header_info = chain(("name", "interests"), questions)
            header = self._fmt(_header_info)
            f.write(header)
            for student in self.participants:
                row = self._fmt([student.name, student.interest, *student.answers])
                f.write(row)

    def _fmt(self, seq):
        fields = ", ".join(str(field) for field in seq)
        fmt_row = fields + "\n"
        return fmt_row
                

def clean_whitespace(name):
    return " ".join(name.split())


if __name__ == "__main__":
    questions = QUESTIONS
    with open("names.txt", "r") as name_list:
        names_list = [clean_whitespace(name) for name in name_list]
    names = random.sample(names_list, NUM_PEOPLE)

    group = Group()
    # exclude "rand", i.e., no studnet can have ``interest`` "rand"
    interests = list(set(questions)-set(["rand"]))
    for name in names:
        interest = random.choice(interests)
        group.add_participant(Student(name, interest))

    group.make_survey(questions)
    group.survey_results(questions)
