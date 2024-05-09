const { test, expect } = require('@playwright/test');
const { ExampleGameComponent } = require('../../src/games/ExampleGameComponent');

test('Test Play Game Button', async ({ page, browser }) => {
  // Navigate to the local hosting URL
  await page.goto('http://localhost:3000/');

  // Stub window.ethereum
  await page.evaluate(() => {
    window.ethereum = {
      request: async function () {
        return ['0xUserAddress'];
      }
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

  // Stub prompt to provide contract address
  page.on('dialog', async dialog => {
    await dialog.accept('0xContractAddress');
  });

  // Click the "Play Game" button
  await page.click('.play-game-button');

  // Wait for navigation to the example game URL
  await page.waitForURL('http://examplegame.com');

  // Verify that the user is redirected to the correct game URL
  expect(page.url()).toBe('http://examplegame.com');
});
