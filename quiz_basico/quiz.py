print("Bem vindo ao quiz de TI!")
answer_user= input("Quer testar o seus conhecimentos de TI? (S/N) ")

if answer_user != "s":# (!=) significa diferente de...
    quit()

score = 0#sistema de pontuação

print("Starting...")
print("Unidade lógica é... \n (a)um disco velho\n (b)um disco vazio\n (c)um disco rígido\n (d)nda")
answer_1 = input("Resposta: ")

if answer_1 == "c":#(==)significa igualdade
    print("Correto! \n")
    score = score + 1#sistema de pontuação
else:
    print("Incorreto! \n")
     

print("HD, ou simplesmente...\n (a)Winchester\n (b)Hardcore\n (c)Disco Fabulous\n (d)Hard Disk")
answer_2= input("Resposta: ")

if answer_2 == "d":
    print("Correto! \n")
    score = score + 1
else:
    print("Incorreto \n!")
    
    
print("MySQL refere-se a: \n (a)tipo de linguagem\n (b)tipo de insão cibernético\n (c)tipo de banco de dados\n (d)sistema de engrenagem")
answer_3= input("Resposta: ")

if answer_3 == "c":
    print("Correto! \n")
    score = score + 1
else:
    print("Incorreto! \n") 
    

print(f"Fim! Pontuação: {score}/3")