
import unittest


class VotingSystem:
    def __init__(self):
        self.voted_students = set()

    def vote(self, student_id):
        if student_id in self.voted_students:
            return False

        self.voted_students.add(student_id)
        return True


class TestVoting(unittest.TestCase):
    def test_first_vote(self):
        system = VotingSystem()
        self.assertTrue(system.vote("student_1"))

    def test_duplicate_vote(self):
        system = VotingSystem()
        system.vote("student_1")
        self.assertFalse(system.vote("student_1"))

    def test_different_students(self):
        system = VotingSystem()
        self.assertTrue(system.vote("student_1"))
        self.assertTrue(system.vote("student_2"))


if __name__ == "__main__":
    unittest.main()
