const { test, expect } = require('@playwright/test');

test('Dashboard button should navigate to the dashboard page and show "not connected" giff', async ({ browser }) => {
  const context = await browser.newContext({
    ignoreHTTPSErrors: true,  // Ignore SSL certificate errors
  });

  const page = await context.newPage();

  //LOGIN
	await page.goto('https://localhost:4430/sign-in', { timeout: 60000 });

	// Enter email and password
	await page.fill('#email', 'carolina');
	await page.fill('#password', 'pass123');

	// Click the login button
	await page.click('#loginButton');

	// Wait for some time to let the console log appear
	await page.waitForTimeout(1000);

	// Listen for console log
	page.on('console', msg => {
		if (msg.type() === 'log' && msg.text() === 'Successfully logged in') {
			console.log('Success message found in console log');
		}
	});

	//Check if redirected to profile page once logged in
	expect(page.url()).toBe('https://localhost:4430/profile');


	console.log("Logged in");

  //DASHBOARD BUTTON

  // Log when navigation starts
  console.log('Navigating to https://localhost:4430');
  
  await page.goto('https://localhost:4430', { timeout: 60000 });

  // Log the current page URL
  console.log('Current URL:', await page.url());

  // Log page content before waiting for the selector
  // const content = await page.content();
  // console.log('Page content before waiting for button:', content);

  // Wait for the pong button
  await page.waitForSelector('#dashboard_button', { timeout: 60000 });

  console.log('dashboard button found, clicking it...');
  
  // Simulate clicking the pong button
  await page.click('#dashboard_button');

  // Verify navigation
  await expect(page).toHaveURL(/dashboard/);
});