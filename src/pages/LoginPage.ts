import { Locator } from '@playwright/test';
import { BasePage } from './BasePage';
import { LoginLocators } from '../locators/login.locators';
import { ILoginPage } from '../types/page.types';
import { Page } from '@playwright/test';

export class LoginPage extends BasePage implements ILoginPage {
  private readonly usernameInput: Locator;
  private readonly passwordInput: Locator;
  private readonly submitButton: Locator;
  private readonly successMessage: Locator;
  private readonly errorMessage: Locator;

  constructor(page: Page) {
    super(page);
    this.usernameInput = page.locator(LoginLocators.inputs.username);
    this.passwordInput = page.locator(LoginLocators.inputs.password);
    this.submitButton = page.locator(LoginLocators.buttons.submit);
    this.successMessage = page.locator(LoginLocators.messages.success);
    this.errorMessage = page.locator(LoginLocators.messages.error);
  }

  async navigate(): Promise<void> {
    await this.page.goto('/practice-test-login');
    await this.waitForPageLoad();
  }

  async login(username: string, password: string): Promise<void> {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async isSuccessMessageVisible(): Promise<boolean> {
    return this.successMessage.isVisible();
  }

  async isErrorMessageVisible(): Promise<boolean> {
    return this.errorMessage.isVisible();
  }

  async getErrorMessage(): Promise<string> {
    return await this.errorMessage.isVisible() ? 
      (await this.errorMessage.textContent()) || '' : 
      '';
  }
} 