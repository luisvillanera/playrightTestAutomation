# Proyecto de Automatización con Playwright y TypeScript

Este proyecto utiliza [Playwright](https://playwright.dev/) y TypeScript para la automatización de pruebas end-to-end en aplicaciones web. Incluye integración con Cucumber para pruebas BDD.

## Requisitos Previos
- Node.js >= 16.x
- npm >= 8.x

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd playwright-typescript-tests
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Instala los navegadores necesarios para Playwright:
   ```bash
   npx playwright install
   ```

## Estructura del Proyecto

- `tests/` — Pruebas automatizadas en TypeScript.
- `src/pages/` — Page Objects para estructurar la automatización.
- `src/features/` — Features de Cucumber (BDD).
- `src/steps/` — Definiciones de pasos para Cucumber.
- `playwright.config.ts` — Configuración de Playwright.
- `package.json` — Scripts y dependencias del proyecto.

## Ejecución de Pruebas

Todas las pruebas ahora se ejecutan usando Cucumber (BDD).

### Ejecutar todas las pruebas BDD

```bash
npm run test:cucumber
```

Esto ejecutará todos los escenarios definidos en los archivos `.feature` dentro de la carpeta `src/features/`.

### Ejecutar un feature específico

```bash
npx cucumber-js src/features/home.feature
```

O para login:

```bash
npx cucumber-js src/features/login.feature
```

### Agregar nuevas pruebas
1. Crea un nuevo archivo `.feature` en `src/features/`.
2. Crea o edita el archivo de steps correspondiente en `src/steps/`.
3. Si es necesario, crea o actualiza el Page Object en `src/pages/` y los locators en `src/locators/`.

---

**Nota:** Ya no se usan archivos `.spec.ts` en la carpeta `tests/`. Todo el flujo de pruebas está basado en Cucumber y Gherkin.

## Ejemplo de Prueba

A continuación, un ejemplo de prueba para verificar el título de la página principal:

```typescript
import { test, expect } from '@playwright/test';

test('La página principal debe tener el título correcto', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Practice Test Automation/i);
});
```

Guarda este ejemplo en `tests/home.spec.ts`.

## Agregar Nuevas Pruebas
1. Crea un nuevo archivo `.spec.ts` en la carpeta `tests/`.
2. Utiliza los Page Objects de `src/pages/` para estructurar tus pruebas.
3. Ejecuta las pruebas para validar que todo funcione correctamente.

## Recursos
- [Documentación de Playwright](https://playwright.dev/docs/intro)
- [Documentación de Cucumber](https://cucumber.io/docs/guides/10-minute-tutorial/)

---

¡Contribuciones y sugerencias son bienvenidas! 

## Reporte de ejecución en la web

Puedes generar y abrir un reporte HTML interactivo de tus pruebas de Cucumber siguiendo estos pasos:

1. Ejecuta los tests para generar el reporte en formato JSON:
   ```bash
   npm run test:cucumber
   ```

2. Genera y abre el reporte HTML en tu navegador:
   ```bash
   npm run report:cucumber
   ```

Esto abrirá automáticamente el reporte en tu navegador, donde podrás ver el detalle de cada escenario y step ejecutado.

> El reporte se genera en la carpeta `reports/cucumber_report.html`. 