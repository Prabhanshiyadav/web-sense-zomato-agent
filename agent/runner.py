import json

class AgentRunner:
    def __init__(self, browser, reasoner, observer, insight):
        self.browser = browser
        self.reasoner = reasoner
        self.observer = observer
        self.insight = insight

    async def run(self):
        try:
            await self.browser.open("https://www.zomato.com")
            goal = "Explore UX"

            while True:
                state = await self.observer.observe()
                decision = await self.reasoner.decide(state, goal)
                action = json.loads(decision)
                print("🧠", action["thought"])

                if action["action"] == "fill":
                    await self.browser.smart_fill(action["value"])
                elif action["action"] == "press":
                    await self.browser.smart_press_enter()
                elif action["action"] == "click":
                    await self.browser.click_first_result()
                elif action["action"] == "observe":
                    report = await self.insight.generate(state)
                    print("\n📝 UX REPORT\n", report)
                    self.reasoner.history["success"].append(report)
                elif action["action"] == "finish":
                    break

        finally:
            self.reasoner.memory.save(self.reasoner.history)
            await self.browser.close()
            print("💾 Memory saved | Browser closed")
