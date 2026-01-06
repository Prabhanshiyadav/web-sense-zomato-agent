import unittest
import json
import asyncio
from agent.reasoner import LLMReasoner

class TestLLMReasoner(unittest.TestCase):
    def test_load_scenarios(self):
        reasoner = LLMReasoner()
        self.assertIsNotNone(reasoner.scenarios)
        self.assertIn("default", reasoner.scenarios)
        self.assertTrue(len(reasoner.scenarios["default"]) > 0)

    def test_steps_execution(self):
        reasoner = LLMReasoner()
        steps = reasoner.scenarios["default"]

        async def run_decisions():
            for expected_step in steps:
                decision = await reasoner.decide("state", "goal")
                data = json.loads(decision)
                self.assertEqual(data["action"], expected_step["action"])
                if "value" in expected_step:
                    self.assertEqual(data["value"], expected_step["value"])

            # After steps are done, it should return finish
            decision = await reasoner.decide("state", "goal")
            data = json.loads(decision)
            self.assertEqual(data["action"], "finish")

        asyncio.run(run_decisions())

if __name__ == '__main__':
    unittest.main()
