segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // (24*60*60)
segundos = segundos % (24*60*60)
horas = segundos // (60*60)
segundos = segundos % (60*60)
minutos = segundos // (60)
segundos = segundos // 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
