// @ts-check
import { test, expect } from '@playwright/test';

test('renders List Games box with description button and dropdown', async ({ page }) => {
    // Navigate to the page where the ListGames component is rendered
    await page.goto('http://localhost:3000'); // Update the URL to match your application

    // Check if there is a List Games box
    const listGameBox = await page.$('.list-games');
    expect(listGameBox).not.toBeNull();

    // Check if the box has a description button
    // @ts-ignore
    const descriptionButton = await listGameBox.$('.description-button');
    expect(descriptionButton).not.toBeNull();

    // Click on the description button
    // @ts-ignore
    await descriptionButton.click();

    // Check if the description dropdown is visible
    // @ts-ignore
    const descriptionDropdown = await listGameBox.$('.description-dropdown');
    expect(descriptionDropdown).not.toBeNull();
});
