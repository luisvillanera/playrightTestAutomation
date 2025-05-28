import { Given, When, Then, DataTable } from '@cucumber/cucumber';
import { expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { getPage } from '../hooks/world';

let loginPage: LoginPage;

Given('que estoy en la página de login', async function() {
  const page = await getPage();
  loginPage = new LoginPage(page);
  await loginPage.navigate();
});

When('ingreso las credenciales', async function(dataTable: DataTable) {
  const credentials = dataTable.hashes()[0];
  await loginPage.login(credentials.usuario, credentials.contraseña);
});

When('hago clic en el botón de login', async function() {
  // Este paso está implícito en el método login, pero lo mantenemos por claridad en el Gherkin
});

Then('debería ver un mensaje de éxito', async function() {
  expect(await loginPage.isSuccessMessageVisible(),
    'El mensaje de éxito no está visible').toBeTruthy();
});

Then('no debería ver un mensaje de éxito', async function() {
  expect(await loginPage.isSuccessMessageVisible(),
    'No debería mostrarse el mensaje de éxito').toBeFalsy();
}); 