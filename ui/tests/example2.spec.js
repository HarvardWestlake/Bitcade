// @ts-check
import { test, expect } from '@playwright/test';

/*test('renders WYRM link', () => {
  render(<selectionScreen />);
  const linkElement = screen.getByText(/WYRM/i);
  expect(linkElement).toBeInTheDocument();
});*/

test('has title', async ({ page }) => {
    await page.goto('http://localhost:3000/'); //how do I get the link?
  
    // Expect a title "to contain" a substring.
    await expect(page).toHaveTitle(/WYRM/);
});