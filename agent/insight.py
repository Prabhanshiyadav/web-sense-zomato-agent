class InsightEngine:
    async def generate(self, html):
        issues = []

        if "login" in html.lower():
            issues.append("Login wall may interrupt browsing")

        if "error" in html.lower():
            issues.append("Possible error text visible")

        if "delivery" not in html.lower():
            issues.append("Delivery option not clearly visible")

        if len(html) > 400000:
            issues.append("Page is very heavy – may impact load time")

        if not issues:
            issues.append("No major UX issues detected")

        return "\n".join([f"• {i}" for i in issues])
