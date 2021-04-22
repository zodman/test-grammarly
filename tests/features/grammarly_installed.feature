@not_installed
Feature: Check if grammarly is installed
	Scenario: open a chrome browser with grammarly installed
		Given a url like google.com
		When the browser wait for the webpage is fully loaded
		Then check if the body properties contains data-gr-ext-installed
