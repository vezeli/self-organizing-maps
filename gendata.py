from dataclasses import dataclass, field
from itertools import chain
from pathlib import Path
import random

import numpy as np
import pandas as pd

CWD = Path.cwd()
OUTPUT_CSV = CWD / "data" / "students.csv"
NAMES_FILE = CWD / "data" / "names.txt"
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
            answer_limit = (
                (0.65, 1.00) if switch.get(question_topic, False) else (0.00, 0.75)
            )
            answer = random.uniform(*answer_limit)
            yield answer

    def give_answers(self, questions):
        fmt = "{:.2f}"
        try:
            if self.answer:
                pass
        except AttributeError:
            self.answers = tuple(
                fmt.format(answer) for answer in self._gen_rand_answers(questions)
            )


@dataclass
class Group:
    participants: list = field(default_factory=list)

    def add_participant(self, item):
        self.participants.append(item)

    def make_survey(self, questions):
        for participant in self.participants:
            participant.give_answers(questions)

    def survey_results(self, questions, file_name=OUTPUT_CSV):
        with open(file_name, "w") as f:
            header_msg = (
                "# This file is automatically generated with gendata.py file.\n"
                "# The content is pseudo-random with logical patterns to make it look real.\n"
            )
            f.write(header_msg)

            columns = chain(("name", "interests"), questions)
            f.write(self._fmt_row(columns))
            for student in self.participants:
                row = self._fmt_row([student.name, student.interest, *student.answers])
                f.write(row)

    def _fmt_row(self, seq):
        fields = ",".join(str(field) for field in seq)
        fmt_row = fields + "\n"
        return fmt_row


def clean_whitespace(name):
    return " ".join(name.split())


if __name__ == "__main__":
    questions = QUESTIONS

    with open(NAMES_FILE, "r") as name_list:
        names = []
        for name in name_list:
            comment = name.startswith("#")
            if not comment:
                names.append(clean_whitespace(name))
    names = random.sample(names, NUM_PEOPLE)

    group = Group()
    # exclude "rand", i.e., no studnet can have ``interest`` "rand"
    interests = list(set(questions) - set(["rand"]))
    for name in names:
        interest = random.choice(interests)
        group.add_participant(Student(name, interest))
    group.make_survey(questions)
    group.survey_results(questions)
