# Question 1 answer
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Question 2 answer
# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(original_price, discount_percentage)

if discount_percentage >= 20:
    print(f"Final price after {discount_percentage}% discount: Kshs{final_price:.2f}")
else:
    print(f"No discount applied. Original price: Kshs{original_price:.2f}")