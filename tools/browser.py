from playwright.async_api import async_playwright

class Browser:

    async def start(self):
        self.pw = await async_playwright().start()
        self.browser = await self.pw.chromium.launch(headless=False)
        self.page = await self.browser.new_page()

        # 🔥 Disable Playwright global timeout
        self.page.set_default_timeout(0)

    async def open(self, url):
        await self.start()
        await self.page.goto(url)
        await self.page.wait_for_timeout(5000)

    async def smart_find(self, keywords):
        for word in keywords:
            el = await self.page.query_selector(f"input[placeholder*='{word}']")
            if el:
                return el

        inputs = await self.page.query_selector_all("input")
        if inputs:
            return inputs[0]
        return None

    async def smart_fill(self, value):
        el = await self.smart_find(["Search", "restaurant", "dishes", "food"])
        if el:
            await el.fill(value)

    async def smart_press_enter(self):
        el = await self.smart_find(["Search", "restaurant", "dishes", "food"])
        if el:
            await el.press("Enter")

    async def click_first_result(self):
        await self.page.wait_for_timeout(5000)
        links = await self.page.query_selector_all("a[href*='order']")
        if links:
            await links[0].click()

    async def close(self):
        await self.browser.close()
        await self.pw.stop()
