import azure.functions as func
from playwright.async_api import async_playwright


async def main(req: func.HttpRequest) -> func.HttpResponse:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        title = await page.title()
        await browser.close()
        return func.HttpResponse(title)
