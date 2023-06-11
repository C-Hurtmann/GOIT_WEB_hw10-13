import connection
import os
import django
from models import Quotes, Authors
from pprint import pprint

all_authors = Authors.objects.all()
all_quotes = Quotes.objects.all()

for obj in all_authors:
    pprint(obj)

print('-' * 50)
for obj in all_quotes:
    pprint(obj)

