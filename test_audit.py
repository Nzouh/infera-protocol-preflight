import unittest
from audit import audit
class TestAudit(unittest.TestCase):
    def test_ready(self):
        r={"run_id":"x","available_instruments":["a"],"inventory":{"b":2},"steps":[{"id":"1","instrument":"a","consumes":{"b":1}}]}
        self.assertEqual(audit(r)["status"],"ready")
    def test_flags_constraints(self):
        r={"run_id":"x","available_instruments":[],"inventory":{},"steps":[{"id":"1","instrument":"a","temperature_c":5,"instrument_max_c":4}]}
        self.assertEqual(len(audit(r)["issues"]),2)
if __name__=="__main__": unittest.main()
