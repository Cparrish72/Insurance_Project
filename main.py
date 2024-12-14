"""

Gather user info
Driver Name (string)
Driver Age (integer)
Coverage Level (string (SM, L, F))

Store this information in a dictionary
Driver Age

State Minimum

Liability Coverage

Full Coverage

16

2593

2957

6930

25

608

691

1745

35

552

627

1564

45

525

596

1469

55

494

560

1363

65+

515

585

1402

Abbreviated table taken from https://www.carinsurance.com/average-rates-by-age.aspxLinks to an external site.

Add the customer’s coverage cost to the dictionary according to their age and coverage desired using the table above
Ask the user if they've had any accidents
If the user has had any accidents, their coverage rate increases by 41%
Update the customer’s coverage cost in the dictionary
Ask the user if they want to pay up front for a 10% discount
If paying up front update the dictionary with the new rate
Output the annual insurance cost for the customer

"""





def get_coverage_cost(age, coverage):
    """
    Returns the coverage cost based on age and coverage type.

    Parameters:
    - age (int): The age of the driver.
    - coverage (str): The type of coverage ('SM', 'L', or 'F').
    """
    rates = {
        16: {'SM': 2593, 'L': 2957, 'F': 6930},
        25: {'SM': 608, 'L': 691, 'F': 1745},
        35: {'SM': 552, 'L': 627, 'F': 1564},
        45: {'SM': 525, 'L': 596, 'F': 1469},
        55: {'SM': 494, 'L': 560, 'F': 1363},
        65: {'SM': 515, 'L': 585, 'F': 1402},
    }
    if age < 25:
        return rates[16][coverage]
    elif age < 35:
        return rates[25][coverage]
    elif age < 45:
        return rates[35][coverage]
    elif age < 55:
        return rates[45][coverage]
    elif age < 65:
        return rates[55][coverage]
    else:
        return rates[65][coverage]


def main():

    try:
        driver_name = input("Enter Driver Name: ")
        driver_age = int(input("Enter Driver Age: "))
        coverage_level = input("Enter Coverage Level (SM, L, F): ").upper()

        if coverage_level not in ['SM', 'L', 'F']:
            raise ValueError("Invalid input.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    insurance_cost = get_coverage_cost(driver_age, coverage_level)

    customer_info = {
        'Name': driver_name,
        'Age': driver_age,
        'Coverage Level': coverage_level,
        'Coverage_cost': insurance_cost
    }

    accidents = input("Have you had any accidents? (yes/no): ").lower()
    if accidents == 'yes':
        customer_info['Coverage_cost'] *= 1.41
    upfront = input("Do you want to pay upfront for a 10% discount? (yes/no): ").lower()
    if upfront == 'yes':
        customer_info['Coverage_cost'] *= 0.9

    print(f"\nAnnual insurance cost for {customer_info['Name']} is ${customer_info['Coverage_cost']:.2f}")


if __name__ == "__main__":
    main()