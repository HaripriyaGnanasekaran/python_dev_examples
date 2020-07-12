import getpass
username = input('Please enter an username: \t')
passwd = getpass.getpass('Type your password: \t')
passwd_len = len(passwd)
passwd_hid = "*"*passwd_len
print(f'Hi {username}, your password {passwd_hid} has {passwd_len} characters')