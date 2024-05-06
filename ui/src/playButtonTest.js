const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.goto('http://localhost:8000');

    // Click the "Play Game" button
    await page.click('.play-game-button');

    // Wait for navigation
    await page.waitForNavigation();

    // Output the current URL
    console.log('Current URL:', page.url());

    await browser.close();
})();
