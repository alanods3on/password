#密碼重試程式
#另一種寫法 在首行先提出password = 'a123456'
#迴圈變數就請改變不然密碼並不會變
#或改變while True --> while n > 0: (則最後一段if就無需要)
n = 3
while n > 0:
	n = n-1
	password = input('請輸入密碼： ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if n > 0:
			print('還有',n,'次機會')
		else:
			print('沒機會嘗試了,帳號已鎖定')	