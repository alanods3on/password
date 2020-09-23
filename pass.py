#密碼重試程式
n = 3
while True:
	n = n-1
	password = input('請輸入密碼： ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		if n == 2:
			print('密碼錯誤,還有2次機會')
		elif n == 1:
			print('密碼錯誤,還有1次機會')
		else:
			print('密碼錯誤,還有0次機會')
			break

			
