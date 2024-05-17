// @ts-check
import { test, expect } from '@playwright/test';

test('Verify Get Description button exists', async ({ page }) => {
    await page.goto('http://localhost:3000'); // Replace with your application URL

    // Check if the Get Description button exists
    const getDescriptionButton = await page.$('button:has-text("Get Description")');
    expect(getDescriptionButton).not.toBeNull();
});

test('User can click on the Get Description button', async ({ page }) => {
    await page.goto('http://localhost:3000'); // Replace with your application URL

    // Click on the Get Description button
    await page.click('button:has-text("Get Description")');

    // Wait for a brief moment to ensure the click event is processed
    await page.waitForTimeout(100);

    // Check if the description dropdown is visible
    const descriptionDropdown = await page.$('.more-description');
    expect(descriptionDropdown).not.toBeNull();
});

test('Description shows up when the user clicks on the button', async ({ page }) => {
    await page.goto('http://localhost:3000'); // Replace with your application URL

    // Ensure the description dropdown is initially hidden
    const descriptionDropdownBefore = await page.$('.more-description');
    expect(descriptionDropdownBefore).toBeNull();

    // Click on the Get Description button
    await page.click('button:has-text("Get Description")');

    // Wait for a brief moment to ensure the click event is processed
    await page.waitForTimeout(100);

    // Check if the description dropdown is visible after clicking the button
    const descriptionDropdownAfter = await page.$('.more-description');
    expect(descriptionDropdownAfter).not.toBeNull();
});
