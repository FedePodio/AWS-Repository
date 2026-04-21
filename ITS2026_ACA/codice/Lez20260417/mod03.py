from datetime import date, datetime, timedelta

oggi = date.today()
print(oggi)
print(oggi.year)
print(oggi.month)
print(oggi.day)

adesso = datetime.now()
print(adesso)
print(adesso.year, adesso.month, adesso.day)
print(adesso.hour, adesso.minute, adesso.second)

fra_20_minuti = adesso + timedelta(minutes=20)

print(f"Intervallo finisce tra: {fra_20_minuti}")

print(adesso.strftime("%d/%m/&Y"))