from rehive import Rehive, APIException
from secret import REHIVE_API

rehive =  Rehive(REHIVE_API)

rehive.auth.login(user="helghardt@rehive.com", company="hackmission", password="Belfius123")
accounts = rehive.admin.users.get()

transaction = rehive.admin.transactions.create_credit(user='helghardt@gmail.com', amount=10000, confirm_on_create=True)

print(accounts)