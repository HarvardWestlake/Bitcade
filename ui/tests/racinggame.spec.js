// @ts-check
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('http://localhost:3000/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/WYRM/);
});

test('Horse Racing Game', async ({ page }) => {
  await page.goto('http://localhost:3000/');

  // Click the button to start the race.
  await page.click('text=Start Race');

  // Wait for the race to finish (adjust timeout as needed).
  await page.waitForSelector('text=Winner:', { timeout: 60000 });

  // Confirm that the winner is displayed.
  const winnerText = await page.textContent('text=Winner:');
  expect(winnerText).toBeTruthy();

  // Ensure UI elements are visible and functional.
  // Example: Check if the race track is visible.
  const raceTrack = await page.$('.race-track');
  expect(raceTrack).toBeTruthy();

  // Example: Check if the finish line is visible.
  const finishLine = await page.$('.finish-line');
  expect(finishLine).toBeTruthy();

  // Example: Check if the horse emojis are visible.
  const horseEmojis = await page.$$('.horse-emoji');
  expect(horseEmojis.length).toBeGreaterThan(0);
});
