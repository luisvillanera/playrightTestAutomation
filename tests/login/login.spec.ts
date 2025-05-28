import { test, expect } from '@playwright/test';
import { LoginPage } from '../../src/pages/LoginPage';

test.describe('Login Tests', () => {
  let loginPage: LoginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.navigate();
  });

  test('debería permitir login con credenciales válidas', async () => {
    await loginPage.login('student', 'Password123');
    expect(await loginPage.isSuccessMessageVisible(), 
      'El mensaje de éxito no está visible').toBeTruthy();
  });

  test('debería mostrar error con contraseña inválida', async () => {
    await loginPage.login('student', 'password_incorrecta');
    expect(await loginPage.isSuccessMessageVisible(),
      'No debería mostrarse el mensaje de éxito').toBeFalsy();
  });

  test('debería mostrar error con usuario inválido', async () => {
    await loginPage.login('usuario_invalido', 'Password123');
    expect(await loginPage.isSuccessMessageVisible(),
      'No debería mostrarse el mensaje de éxito').toBeFalsy();
  });
}); 