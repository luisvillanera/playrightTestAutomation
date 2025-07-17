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

Puedes ejecutar los tests de diferentes maneras según tus necesidades. A continuación se detallan los comandos más importantes:

### 1. Ejecutar todas las pruebas automatizadas

Este comando ejecuta todos los tests definidos en la carpeta `tests/` usando Playwright:
```bash
npm test
```

### 2. Ejecutar pruebas en modo interactivo (UI)

Abre la interfaz visual de Playwright Test Runner, donde puedes seleccionar y depurar tests:
```bash
npm run test:ui
```

### 3. Ejecutar pruebas con navegador visible (headed)

Ejecuta los tests mostrando el navegador (útil para depuración visual):
```bash
npm run test:headed
```

### 4. Ejecutar pruebas BDD con Cucumber

Ejecuta los tests definidos en archivos `.feature` usando Cucumber:
```bash
npm run test:cucumber
```

### 5. Ver el reporte de pruebas

Abre un reporte HTML interactivo con los resultados de la última ejecución:
```bash
npm run report
```

---

**Nota:**
- Puedes personalizar los comandos en el archivo `package.json`.
- Si es la primera vez que ejecutas los tests, asegúrate de haber instalado los navegadores con `npx playwright install`.

## Ejecutar tests específicos

Además de los comandos generales con `npm`, puedes ejecutar archivos o pruebas individuales usando `npx playwright test`. Esto te da mayor flexibilidad para correr solo los tests que te interesan.

### Ejecutar solo el test de login

```bash
npx playwright test tests/login/login.spec.ts
```

### Ejecutar solo el test de home

```bash
npx playwright test tests/home/home.spec.ts
```

### Ejecutar un test específico dentro de un archivo

Puedes ejecutar un test puntual usando el flag `-g` seguido del nombre (o parte del nombre) del test:

```bash
npx playwright test -g "título correcto"
```

O para un test específico de login:

```bash
npx playwright test -g "credenciales válidas"
```

---

**¿Cuál es la diferencia entre npm y npx aquí?**
- Los comandos `npm test` o `npm run ...` ejecutan scripts predefinidos en el archivo `package.json` y suelen correr todos los tests.
- Usar `npx playwright test` te permite ejecutar archivos o pruebas individuales de forma directa y flexible.

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