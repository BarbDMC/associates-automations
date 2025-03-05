import { test, expect } from '@playwright/test';
// import { fs } from 'fs';
// import { csv } from 'csv-parser';


test.use({ storageState: 'auth.json' });

test.beforeEach(async ({ page }) => {
  await page.goto('https://platzi.com/home/');
});


test('has title', async ({ page }) => {
  await page.goto('https://platzi.com/clases/examen/8cb75463-1adc-4d0a-9867-ff0e147ee17c/examen_usuario/');
  await expect(page).toHaveTitle(/Curso de TailwindCSS/);
});

test('get started link', async ({ page }) => {
  await page.goto('https://platzi.com/clases/examen/8cb75463-1adc-4d0a-9867-ff0e147ee17c/examen_usuario/');

  await page.getByRole('button', { name: 'Por examen' }).click();
  await page.waitForTimeout(1000);
});

// test('answer questions', async ({ page }) => {
//   await page.goto('https://platzi.com/clases/examen/8cb75463-1adc-4d0a-9867-ff0e147ee17c/examen_usuario/');
//   await page.getByRole('button', { name: 'Por examen' }).click();
//   await page.waitForTimeout(1000);
//   const results = [];
//   fs.createReadStream('./exam-csv/exam.csv')
//     .pipe(csv())
//     .on('data', (data) => results.push(data))
//     .on('end', () => {
//       console.log(results);
//       for (let i = 0; i < results.length; i++) {
//         const question = results[i].question;
//         const answer = results[i].answer;
//         await page.waitForTimeout(1000);
//         await page.waitForSelector('text=' + question);
//         await page.click('text=' + answer);
//         await page.waitForTimeout(1000);
//         await page.click('text=Siguiente');
//         await page.waitForTimeout(1000);
//       }
//     });
//   await page.waitForSelector('text=Terminar');
//   await page.click('text=Terminar');
//   await page.waitForTimeout(1000);
// });




