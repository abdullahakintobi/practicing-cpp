def display_salary_ranking(employee_salaries: dict) -> None:
    """
    Displays a ranked, formatted table of employees sorted by salary in descending order.

    Args:
        employee_salaries (dict): Dictionary with employee full names as keys and salaries as integer values.
    """
    # Capitalize only the first name in a full name
    def uppercase_first_name(full_name):
        parts = full_name.split(" ")
        if parts:
            parts[0] = parts[0].upper()
        return " ".join(parts)

    # Sort employees by salary (descending) and apply first-name capitalization
    sorted_employees = {
        uppercase_first_name(k): v
        for k, v in sorted(employee_salaries.items(), key=lambda item: item[1], reverse=True)
    }

    # Output formatting
    separator = "=" * 59
    columns = ["No.", "Employee Name", "Annual Salary ($)"]
    print(separator)
    print(f"| {columns[0]:<5}| {columns[1]:<28}| {columns[2]:<18} |")
    print(separator)

    # Display ranked employee salary list with formatted numbers
    for rank, (name, salary) in enumerate(sorted_employees.items(), start=1):
        no_column = f"{rank}.".ljust(5)
        name_column = name.ljust(28)
        salary_column = f"$ {salary:,.2f}".rjust(18)
        print(f"| {no_column}| {name_column}| {salary_column} |")

    print(separator)


# Test case
employees = {
    "Adewale Olawale": 85000,
    "Bamidele Adeniyi": 72000,
    "Chidinma Okoro": 91000,
    "Damilola Bakare": 68000,
    "Emeka Nwachukwu": 79000,
    "Funke Ajayi": 94000,
    "Ganiyu Idris": 66000,
    "Hauwa Usman": 88000,
    "Ifeanyi Okeke": 75000,
    "Jumoke Akinyemi": 97000,
    "Kolawole Adekunle": 70000,
    "Latifat Abdullahi": 82000,
    "Mustapha Bello": 69000,
    "Ngozi Okafor": 90000,
    "Olumide Adeyemi": 77000,
    "Pelumi Fashola": 83000,
    "Quadri Ayodele": 71000,
    "Risikat Ojo": 95000,
    "Segun Davies": 74000,
    "Tunde Lawal": 86000
}

display_salary_ranking(employees)



'''
Output:
===========================================================
| No.  | Employee Name               | Annual Salary ($)  |
===========================================================
| 1.   | JUMOKE Akinyemi             |        $ 97,000.00 |
| 2.   | RISIKAT Ojo                 |        $ 95,000.00 |
| 3.   | FUNKE Ajayi                 |        $ 94,000.00 |
| 4.   | CHIDINMA Okoro              |        $ 91,000.00 |
| 5.   | NGOZI Okafor                |        $ 90,000.00 |
| 6.   | HAUWA Usman                 |        $ 88,000.00 |
| 7.   | TUNDE Lawal                 |        $ 86,000.00 |
| 8.   | ADEWALE Olawale             |        $ 85,000.00 |
| 9.   | PELUMI Fashola              |        $ 83,000.00 |
| 10.  | LATIFAT Abdullahi           |        $ 82,000.00 |
| 11.  | EMEKA Nwachukwu             |        $ 79,000.00 |
| 12.  | OLUMIDE Adeyemi             |        $ 77,000.00 |
| 13.  | IFEANYI Okeke               |        $ 75,000.00 |
| 14.  | SEGUN Davies                |        $ 74,000.00 |
| 15.  | BAMIDELE Adeniyi            |        $ 72,000.00 |
| 16.  | QUADRI Ayodele              |        $ 71,000.00 |
| 17.  | KOLAWOLE Adekunle           |        $ 70,000.00 |
| 18.  | MUSTAPHA Bello              |        $ 69,000.00 |
| 19.  | DAMILOLA Bakare             |        $ 68,000.00 |
| 20.  | GANIYU Idris                |        $ 66,000.00 |
===========================================================
'''