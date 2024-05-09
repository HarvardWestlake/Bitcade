const { chromium } = require('playwright');

class HorseRacingGameComponentTest {
  constructor(url) {
    this.url = url;
  }

  async runTests() {
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();

    await page.goto(this.url);

    // Test 1: Verify Join Game button is present
    await page.waitForSelector('button');
    const joinButton = await page.$('button');
    expect(joinButton).toBeTruthy();

    // Test 2: Click Join Game button
    await joinButton.click();

    // Test 3: Verify if race track is displayed after joining game
    await page.waitForSelector('.race-track');
    const raceTrack = await page.$('.race-track');
    expect(raceTrack).toBeTruthy();

    // Test 4: Verify racers are displayed after joining game
    const racers = await page.$$('.racer');
    expect(racers.length).toBeGreaterThan(0);

    await browser.close();
  }
}

// Example usage:
const test = new HorseRacingGameComponentTest('http://localhost:3000'); // Replace URL with your application URL
test.runTests().then(() => console.log('Tests completed.'));
