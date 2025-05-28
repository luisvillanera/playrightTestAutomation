import { Before, After, setWorldConstructor } from '@cucumber/cucumber';
import { chromium, Page, Browser } from '@playwright/test';

let browser: Browser;
let page: Page;

Before(async () => {
  browser = await chromium.launch({ headless: false });
  page = await browser.newPage();
});

After(async () => {
  await browser.close();
});

export async function getPage(): Promise<Page> {
  return page;
}

// Configuración del World de Cucumber
class CustomWorld {
  constructor() {
    // Puedes agregar propiedades personalizadas aquí
  }
}

setWorldConstructor(CustomWorld); 