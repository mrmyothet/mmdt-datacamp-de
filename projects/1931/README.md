# Debugging a Sales Data Workflow

### Project Instructions
- Run the load_and_check() function first. 

Look for any error messages in the output - these will point you to what needs fixing. 
You should aim for exactly two success messages: "Data loaded successfully" and "Data integrity check was successful!"

- Review the load_and_check() function code, paying special attention to the two integrity checks:
1. The first check validates the column count.
2. The second check validates data integrity based on Condition_1 (Total values) and Condition_2 (Tax calculations at 5%)

Your task is to identify and fix issues within the load_and_check() function itself, not by modifying the raw sales.csv dataset. 
You are permitted and expected to correct any columns within the function. 
Ensure the function only returns two success messages when completed.