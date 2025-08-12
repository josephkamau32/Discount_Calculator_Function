# Discount Calculator - README

## Overview
This Python script provides a simple yet effective discount calculator that determines the final price of an item after applying a discount, but only if the discount meets a minimum threshold. The program is designed with clear functionality and user-friendly interaction.

## Features
- **Conditional Discount Application**: Only applies discounts of 20% or higher
- **User Input Handling**: Accepts both original price and discount percentage
- **Formatted Output**: Displays results with proper currency formatting (Kenyan Shillings)
- **Clear Feedback**: Informs user whether a discount was applied or not

## Function Documentation

### `calculate_discount(price, discount_percent)`
The core function that performs the discount calculation.

**Parameters:**
- `price` (float): The original price of the item
- `discount_percent` (float): The discount percentage to be applied (e.g., 25 for 25%)

**Returns:**
- float: The final price after discount (if applicable) or the original price

**Logic:**
1. Checks if the discount percentage is 20% or higher
2. If qualified:
   - Calculates discount amount: `price * (discount_percent / 100)`
   - Deducts discount from original price
3. If not qualified, returns original price unchanged

## Usage Instructions

1. **Run the Program**:
   ```bash
   python discount_calculator.py
   ```

2. **Input Prompts**:
   - You will be asked to enter:
     - The original price of the item (in Kshs)
     - The discount percentage (without the % sign)

3. **Output Examples**:
   - For qualified discount:
     ```
     Final price after 25.0% discount: Kshs750.00
     ```
   - For unqualified discount:
     ```
     No discount applied. Original price: Kshs500.00
     ```

## Example Scenarios

### Scenario 1: Qualified Discount
```
Enter the original price of the item: 1000
Enter the discount percentage: 30
Final price after 30.0% discount: Kshs700.00
```

### Scenario 2: Unqualified Discount
```
Enter the original price of the item: 500
Enter the discount percentage: 15
No discount applied. Original price: Kshs500.00
```

## Currency Note
The program formats all monetary values in Kenyan Shillings (Kshs) with two decimal places for consistency. This can be easily modified to support other currencies by changing the output strings.

## Error Handling
The current implementation assumes valid numeric input. For production use, consider adding:
- Input validation to ensure positive numbers
- Try-catch blocks for non-numeric input
- Range checking for discount percentages (0-100%)

## Modification Guide
To adapt this program:
1. Change currency symbol by modifying the print statements
2. Adjust the discount threshold by changing the `20` in the comparison
3. Extend functionality by adding multiple items or tiered discounts

## License
This code is provided as-is for educational and demonstration purposes. Feel free to modify and use in your projects.
