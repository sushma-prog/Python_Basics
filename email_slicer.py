#get user's email address

email = input("what is your email address?: ").strip()#will strip off any space as email doesnt contain space

#slice out user name

user = email[:email.index("@")]

#slice out domain name

domain = email[email.index("@") + 1 :]#will start from letter after @ till end

#format output message

output = "Your user name is {} and Your domain name is {} ".format(user,domain)

#display output message

print(output)
