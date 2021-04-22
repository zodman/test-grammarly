Feature: Grammarly not working like expect
	Scenario: Write a phrase without comas
		Given grammarly activated
		When user type a phrase without comas
		Then grammarly not showing error
