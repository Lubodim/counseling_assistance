
import re

sample_text = """
Имейл адресите могат да бъдат в различни формати, 
като например example@email.com или пък user1234@example.co.uk. 
Друг валиден имейл адрес може да е some.address@email.bg. 
несъществуващ имейл gosho123@gosho.gosho.com, gosho123@gosho.gosho.c3om
"""

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails_found = re.findall(pattern, sample_text)

for email in emails_found:
    print(email)
