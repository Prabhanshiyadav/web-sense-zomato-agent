class Observer:
    def __init__(self, browser):
        self.browser = browser

    async def observe(self):
        return await self.browser.page.content()
