const { test, expect } = require('@playwright/test');

test('Test Play Game Button', async ({ page, browser }) => {
  // Navigate to the page
  await page.goto('http://localhost:3000');

  // Stub window.ethereum
  await page.evaluate(() => {
    window.ethereum = {
      request: async function () {
        return ['0xUserAddress'];
      }
    };
  });

  // Stub prompt to provide contract address
  await page.evaluate(() => {
    window.prompt = function () {
      return '0xContractAddress';
    };
  });

  // Stub contract interaction
  await page.evaluate(() => {
    window.exampleGameContract = {
      example_game_address: async function () {
        return 'http://examplegame.com';
      }
    };
  });

  // Click the "Play Game" button
  await page.click('.play-game-button');

  // Wait for navigation to the example game URL
  await page.waitForURL('http://examplegame.com');

  // Verify that the user is redirected to the correct game URL
  expect(page.url()).toBe('http://examplegame.com');
});
