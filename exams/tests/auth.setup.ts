import { test as setup } from '@playwright/test';
import path from 'path';
import dotenv from 'dotenv';

dotenv.config();

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

setup('authenticate', async ({ page }) => {

    await page.goto('https://platzi.com/login/');

    await page.fill('input[name="email"]', process.env.USERNAME || '');
    await page.getByRole('button', { name: 'Continuar' }).click();

    await page.waitForSelector('#password');

    await page.fill('#password', process.env.PASSWORD || '');
    await page.getByRole('button', { name: 'Iniciar sesión' }).click();

    await page.waitForURL('https://platzi.com/home/');

    await page.context().storageState({ path: authFile });

    console.log('Authentication state saved.');
});