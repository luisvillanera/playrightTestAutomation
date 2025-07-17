import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';
import { HomePage } from '../pages/HomePage';
import { getPage } from '../hooks/world';
import { DataTable } from '@cucumber/cucumber';

let homePage: HomePage;

Given('que estoy en la página principal', async function() {
  const page = await getPage();
  homePage = new HomePage(page);
  await homePage.navigate();
});

When('ingreso las credenciales', async function(dataTable: DataTable) {
  // Este paso es un placeholder, ya que normalmente no se ingresan credenciales en la home
  const credentials = dataTable.hashes()[0];
  console.log('Credenciales recibidas en home:', credentials);
});

Then('el título de la página debe ser {string}', async function(titulo: string) {
  await expect(homePage.getTitle()).resolves.toContain(titulo);
}); 