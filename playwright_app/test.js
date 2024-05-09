const { test, expect } = require('@playwright/test');

test('should increment the counter on button click', async ({ page }) => {
    // Start the server and open the app page
    await page.goto('http://localhost:3000'); // Adjust URL based on where your app is served

    // Expect the initial count to be 0
    await expect(page.locator('text=Current count: 0')).toBeVisible();

    // Click the increment button
    await page.click('#increment-button');

    // Expect the count to be 1 after click
    await expect(page.locator('text=Current count: 1')).toBeVisible();
});
