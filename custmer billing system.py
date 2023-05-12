import datetime

def generate_invoice(invoice_number, customer_name, items, tax_rate):
    invoice_date = datetime.date.today()
    tax_amount = sum([item['price'] * item['quantity'] for item in items]) * tax_rate
    subtotal = sum([item['price'] * item['quantity'] for item in items])
    total = subtotal + tax_amount

    
    print('INVOICE')
    print('Invoice Number: ', invoice_number)
    print('Date: ', invoice_date)
    print('Customer Name: ', customer_name)
    print('')

    
    print('ITEMS')
    for item in items:
        print(item['name'], '\t', item['quantity'], '\t', item['price'])

    
    print('')
    print('Subtotal: $', format(subtotal, '.2f'))

    # Print the tax amount
    print('Tax Amount: $', format(tax_amount, '.2f'))

    # Print the total
    print('Total: $', format(total, '.2f'))


invoice_number = 'INV-001'
customer_name = 'Anil Sahu'
items = [{'name': 'Roti', 'quantity': 10, 'price': 15.00},
         {'name': 'Pizza', 'quantity': 2, 'price': 150.00},
         {'name': 'Burger', 'quantity': 2, 'price': 60.00}]
tax_rate = 12

generate_invoice(invoice_number, customer_name, items, tax_rate)
