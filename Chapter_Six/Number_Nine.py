# (Dictionary Manipulations)

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

print('Canada' in tlds)
print('France' in tlds)

print(f'{"Country":<15}{"TLD"}')
for country, tld in tlds.items():
    print(f'{country:<15}{tld}')

tlds['Sweden'] = 'sw'
print("\nadd new Sweden:", tlds)

tlds['Sweden'] = 'se'
print("updated Sweden:", tlds)

reversed_tlds = {tld: country for country, tld in tlds.items()}
print("\nReversed:", reversed_tlds)

uppercase_reversed = {tld: country.upper() for tld, country in reversed_tlds.items()}
print("Uppercase Reversed:", uppercase_reversed)
