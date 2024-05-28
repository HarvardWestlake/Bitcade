// @ts-check
import { test, expect } from '@playwright/test';

test('Verify Bet button exists', async ({ page }) => {
    await page.goto('http://localhost:3000/'); // Replace with your application URL

    // Check if the Bet button exists
    const betButton = await page.$('button:has-text("Bet")');
    expect(betButton).not.toBeNull();
});

test('Verify Hit button exists', async ({ page }) => {
    await page.goto('http://localhost:3000/'); // Replace with your application URL

    // Check if the Hit button exists
    const hitButton = await page.$('button:has-text("Hit")');
    expect(hitButton).not.toBeNull();
});

test('User cards and sum update when Hit button is clicked', async ({ page }) => {
    await page.goto('http://localhost:3000/'); // Replace with your application URL

    // Ensure initial state of user cards and sum
    const initialUserCards = await page.textContent('p:has-text("Your Hand:")');
    const initialCardSum = await page.textContent('p:has-text("Sum:")');
    expect(initialUserCards).toContain('1,2');
    expect(initialCardSum).toContain('3');

    // Click on the Hit button
    await page.click('button:has-text("Hit")');

    // Wait for a brief moment to ensure the click event is processed
    await page.waitForTimeout(100);

    // Check if the user cards and sum are updated
    const updatedUserCards = await page.textContent('p:has-text("Your Hand:")');
    const updatedCardSum = await page.textContent('p:has-text("Sum:")');
    expect(updatedUserCards).toContain('1,2,3');
    expect(updatedCardSum).toContain('6');
});
