import { render, screen } from '@testing-library/react';
import selectionScreen from './selectionScreen.js';
// @ts-check
const { test, expect } = require('@playwright/test');

/*test('renders WYRM link', () => {
  render(<selectionScreen />);
  const linkElement = screen.getByText(/WYRM/i);
  expect(linkElement).toBeInTheDocument();
});*/

test('has title', async ({ page }) => {
    await page.goto('https://selectionScreen.dev/'); //how do I get the link?
  
    // Expect a title "to contain" a substring.
    await expect(page).toHaveTitle(/WYRM/);
});