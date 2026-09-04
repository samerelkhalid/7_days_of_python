import re 

# Search for a phone number in a string
text = 'My phone number is 555-7777'
match = re.search(r'\d{3}-\d{4}', text)

if match:
    print(match.group(0))

# Extract email addresses from a string
text = 'My email address is example@devops.com, but I also use other@cloud.com.'
matches = re.findall(r'\S+@\S+', text)
print(matches)