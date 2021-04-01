l = list("abcdefghijklmnoprstquwxyz")
abc = list("dksfjmojsmnfafgkopmasLOKMDFIOJKPNSsdfdsfsdfKIPJAMNFOKPMDSsgfsfdsfPLOFMLODSAMADOPLKFMDSOPLKgfhfdhgfdsgwsfMFOKMSDAKPOJFNMKPOJASDMNF")
while True:
	print("1-добавить букву в список.")
	print("2-склеить списки.")
	print("3-Вставить элемент (i, element).")
	print("4-удалить элемент.")
	print("5-удалить элемент по индексу.")
	print("6-узнать индекс элемента.")
	print("7-перевернуть список")
	ans = int(input())
	if ans == 1:
		l.append(input().lower())
		print(l)
	elif ans == 2:
		l.extend(abc)
		print(l)
	elif ans == 3:
		i = int(input("I	==>	"))
		
		element = input("element	==>	").upper() # меняем регистр на большой, чтобы искать только такие
		l.insert(i,element)
		print(l)
	elif ans==4: # удалить элементы
		el = input("Element		==>	").lower() # чтобы исключить возможных ошибок, мы меняем регистр символов на маленький
		for i in range(l.count(el)):
			l.remove(el)
	elif ans == 5: 
		pos = int(input("index	==>	"))
		n = len(l)
		if pos < n:
			if l.pop(pos).isascii():
				print("Это ASCII")
			print(l)
	elif ans == 6:
		try:
			print(l.index(input("element	==>	"),0,len(l)-1))

		except:
			print("нет такого в списке")
	elif ans == 7:
		print("Переворачиваем и сортируем списки...")
		l.reverse()
		print(l)
		l.sort()
		print(l)
