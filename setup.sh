#!/bin/bash

# Instalar dependencias
npm install

# Instalar navegadores de Playwright
npx playwright install chromium

# Crear directorios si no existen
mkdir -p tests
mkdir -p pages/login

echo "¡Configuración completada! Para ejecutar los tests:"
echo "npm test          # Ejecutar todos los tests"
echo "npm run test:ui   # Ejecutar tests en modo UI"
echo "npm run test:headed # Ejecutar tests con navegador visible" 