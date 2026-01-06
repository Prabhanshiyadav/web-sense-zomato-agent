import unittest
import asyncio
from agent.insight import InsightEngine

class TestInsightEngine(unittest.TestCase):
    def test_generate_insights(self):
        engine = InsightEngine()

        async def run_test():
            html_with_login = "<html><body>Please login to continue</body></html>"
            report = await engine.generate(html_with_login)
            self.assertIn("Login wall may interrupt browsing", report)

            html_clean = "<html><body>Welcome to food delivery</body></html>"
            report = await engine.generate(html_clean)
            self.assertIn("No major UX issues detected", report)

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
