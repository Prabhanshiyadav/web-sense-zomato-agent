from playwright.async_api import async_playwright

class Browser:
    def __init__(self, headless=False, slow_mo=500):
        self.headless = headless
        self.slow_mo = slow_mo
        self.pw = None
        self.browser = None
        self.page = None

    async def start(self):
        if not self.pw:
            self.pw = await async_playwright().start()
            self.browser = await self.pw.chromium.launch(
                headless=self.headless,
                slow_mo=self.slow_mo
            )
            self.page = await self.browser.new_page()
            # 🔥 Disable Playwright global timeout
            self.page.set_default_timeout(0)

    async def open(self, url):
        if not self.page:
            await self.start()
        await self.page.goto(url)
        # We rely on smart_find to wait for elements now

    async def smart_find(self, keywords):
        # Using locator strategies with waiting
        for word in keywords:
            try:
                # Create a locator for the input
                loc = self.page.locator(f"input[placeholder*='{word}']").first
                # Wait for it to be visible with a short timeout (2s) so we don't hang too long on wrong guesses
                await loc.wait_for(state="visible", timeout=2000)
                return loc
            except Exception:
                continue

        # Fallback to any visible input
        try:
            loc = self.page.locator("input").first
            await loc.wait_for(state="visible", timeout=2000)
            return loc
        except Exception:
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
        try:
            # Wait for the element to be visible
            link = self.page.locator("a[href*='order']").first
            await link.wait_for(state="visible", timeout=5000)
            await link.click()
        except Exception as e:
            print(f"Error clicking first result: {e}")

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.pw:
            await self.pw.stop()
        self.browser = None
        self.pw = None
        self.page = None
