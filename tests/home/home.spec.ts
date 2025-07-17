import { test, expect } from '@playwright/test';

test('La página principal debe tener el título correcto', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Practice Test Automation/i);
}); 