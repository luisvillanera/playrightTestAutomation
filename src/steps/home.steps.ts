import { Given, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';
import { HomePage } from '@/pages/HomePage';
import { getPage } from '../hooks/world';

let homePage: HomePage;

Given('que estoy en la página principal', async function() {
  const page = await getPage();
  homePage = new HomePage(page);
  await homePage.navigate();
});

Then('el título de la página debe ser {string}', async function(titulo: string) {
  await expect(homePage.getTitle()).resolves.toContain(titulo);
}); 