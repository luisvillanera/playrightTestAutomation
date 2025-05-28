import { Page } from '@playwright/test';
import { IBasePage } from '../types/page.types';

export abstract class BasePage implements IBasePage {
  protected constructor(protected readonly page: Page) {}

  abstract navigate(): Promise<void>;

  protected async waitForPageLoad(): Promise<void> {
    await this.page.waitForLoadState('networkidle');
  }
} 