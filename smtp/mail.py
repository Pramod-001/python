import smtplib as smp
mail = "pramod123.knr@gmail.com"

con = smp.SMTP()
con.starttls()
con.login(user= mail, password = "Pramodkumar@2005")
con.sendmail(from_addr=mail,to_addrs="teja.kasimsetti@gmail.com",msg="Hello")
con.close()

#create a new email and try again