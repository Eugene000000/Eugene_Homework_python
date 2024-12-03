from Address import Address
from Mailing import Mailing

to_address = Address("452920", "Агидель", "Курчатова", "1", "1")
from_address = Address("172530", "Белый", "Тверская", "2", "2")
mailing = Mailing("3432342432", from_address, to_address, "3")

print(mailing)