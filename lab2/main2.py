connect = True
>>> 
>>> while connect == True:
	number = input('Число: ')
	percent = input('Процент: ')
	while type(number) != int:
		try:
			number = int(number)
			percent = int(percent)

		except ValueError:
			print('Введи цифры!')
			number = input('Введи число: ')
			print()
	                percent = input('Введи процент: ')
                        print()
                        
	while type(number) != float:
                 try:
                        number = float(number)
			percent = float(percent)
			
	         except ValueError:
			print('Введи цифры!')
			number = input('Введи число: ')
			print()
            percent = input('Введи процент: ')
	                print()

	finish = number / 100 * percent

	print('Ваш ответ:', float(finish))