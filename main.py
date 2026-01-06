import asyncio
from tools.browser import Browser
from agent.reasoner import LLMReasoner
from agent.observer import Observer
from agent.insight import InsightEngine
from agent.runner import AgentRunner


async def main():
    # Updated to pass headless=False
    browser = Browser(headless=False)
    # LLMReasoner now defaults to "default" scenario
    reasoner = LLMReasoner()
    observer = Observer(browser)
    insight = InsightEngine()

    agent = AgentRunner(browser, reasoner, observer, insight)
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
