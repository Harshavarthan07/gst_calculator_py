cp = float(input('Enter the cost of product: '))
CGST = float(input('Enter tax % imposed by centre, i.e. CGST: '))
SGST = float(input('Enter tax % imposed by state, i.e. SGST: '))
total = 0
Amount_CGST = ((CGST/100) * cp)
Amount_SGST = ((SGST/100) * cp)
total = cp + Amount_CGST + Amount_SGST
print(f'Total cost of product = Rs.{total}')
