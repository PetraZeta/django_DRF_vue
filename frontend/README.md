# Vue 3 + TypeScript + Vite

This template should help get you started developing with Vue 3 and TypeScript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended Setup

- [VS Code](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (previously Volar) and disable Vetur

- Use [vue-tsc](https://github.com/vuejs/language-tools/tree/master/packages/tsc) for performing the same type checking from the command line, or for generating d.ts files for SFCs.



## Objetivo
Realizar la prueba técnica cumpliendo los requisitos de la definición técnica.

## Alcance
Se debe desarrollar un pequeño proyecto, cumpliendo con la definición
técnica, que conste de:
• Formulario de inicio de sesión.
• Vista de tipo lista.
• Detalle de cada registro.
• Operaciones CRUD de cada registro independiente

## Definición técnica
Base de datos relacional con, al menos, 2 tablas.
• Backend que comunique la base de datos con el capa Frontend. El
intercambio de información debe ser en formato JSON. La API debe
ser RESTFul y, preferiblemente, desarrollada con Django y DRF.
• Frontend desarrollado en Vue.js, que consuma los datos de la API

## Definición funcional
1.1. El proyecto debe comenzar con un formulario de inicio de sesión que
autentique si no están ya iniciada la sesión y dentro del tiempo de
preservación de las cookies.
1.2. Una vez iniciada la sesión, deberá mostrar el listado de, al menos, los
elementos de dos tablas y poder realizar las operaciones de CRUD sobre
la base de datos de, al menos, una de ellas,
1.3. Debe tener validaciones de campos obligatorios.