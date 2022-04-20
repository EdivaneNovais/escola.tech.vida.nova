programa{
	
	funcao inicio()
	{
		inteiro idade =0, soma_idade =0, contador=0, grupo, genero
		cadeia nome
		cadeia resposta
		real valor_imc, peso, altura
		real quantidade_entrevistados = 0
		real soma_jovens=0, contagem_jovens=0, media_jovens=0
		real soma_adultos=0, contagem_adultos=0, media_adultos=0
		real soma_expert=0, contagem_expert=0, media_expert=0
		real soma_peso_jovem=0, cont_peso_jovem=0, media_peso_jovem=0
		real soma_peso_adulto=0, cont_peso_adulto=0, media_peso_adulto=0
		real soma_peso_expert=0, cont_peso_expert=0, media_peso_expert=0
		real soma_altura_jovem=0, cont_altura_jovem=0, media_altura_jovem=0
		real soma_altura_adulto=0, cont_altura_adulto=0, media_altura_adulto=0
		real soma_altura_expert=0, cont_altura_expert=0, media_altura_expert=0
		real soma_m_jovem=0, cont_m_jovem=0, media_m_jovem=0, soma_h_jovem=0, cont_h_jovem=0, media_h_jovem=0
		real soma_m_adultas=0, cont_m_adultas=0, media_m_adultas=0, soma_h_adultos=0, cont_h_adultos=0, media_h_adultos=0
		real soma_m_expert=0, cont_m_expert=0, media_m_expert=0, soma_h_expert=0, cont_h_expert=0, media_h_expert=0
		real soma_m_jovem_peso=0, cont_m_jovem_peso=0, media_m_jovem_peso=0
		real soma_m_adultas_peso=0, cont_m_adultas_peso=0, media_m_adultas_peso=0
		real soma_m_expert_peso=0, cont_m_expert_peso=0, media_m_expert_peso=0
		real soma_h_jovem_peso=0, cont_h_jovem_peso=0, media_h_jovem_peso=0
		real soma_h_adultos_peso=0, cont_h_adultos_peso=0, media_h_adultos_peso=0
		real soma_h_expert_peso=0, cont_h_expert_peso=0, media_h_expert_peso=0
		real soma_m_jovem_altura=0, cont_m_jovem_altura=0, media_m_jovem_altura=0
		real soma_m_adultas_altura=0, cont_m_adultas_altura=0, media_m_adultas_altura=0
		real soma_m_expert_altura=0, cont_m_expert_altura=0, media_m_expert_altura=0
		real soma_h_jovem_altura=0, cont_h_jovem_altura=0, media_h_jovem_altura=0
		real soma_h_adultos_altura=0, cont_h_adultos_altura=0, media_h_adultos_altura=0
		real soma_h_expert_altura=0, cont_h_expert_altura=0, media_h_expert_altura=0
		
		inteiro quantidade_idades=0
		
		
faca {
	faca {
			escreva ("\ndigite sua idade:")
			leia (idade)
			limpa()
			
				se (idade<18)
				{
					escreva("\nvocê precisa ser maior de 18")
				}
				
				}
	
	enquanto (idade<18)
	
	      	  se (idade >= 18 e idade <=32){
			    contagem_jovens = contagem_jovens + 1
    		         soma_jovens = soma_jovens + idade
			    media_jovens = soma_jovens / contagem_jovens
			}
			 
			senao se (idade >= 33 e idade <= 61){
				contagem_adultos = contagem_adultos + 1
				soma_adultos = soma_adultos + idade
				media_adultos =  soma_adultos / contagem_adultos 
			}

			senao {contagem_expert = contagem_expert + 1
				soma_expert = soma_expert + idade 
				media_expert = soma_expert / contagem_expert
			}

			escreva ("\n\nQual o seu genero? digite 1 para Feminino e 2 para Masculino: ")
			leia(genero)
			limpa()

			 se (idade >= 18 e idade <=32 e genero == 1){
			 	cont_m_jovem = cont_m_jovem + 1
			 	soma_m_jovem = soma_m_jovem + idade
			 	media_m_jovem = soma_m_jovem / cont_m_jovem
			 }
			 senao se (idade >= 33 e idade <= 61 e genero == 1){
			 	cont_m_adultas = cont_m_adultas + 1
			 	soma_m_adultas = soma_m_adultas + idade
			 	media_m_adultas = soma_m_adultas / cont_m_adultas
			 }
			 senao se (idade > 61 e genero == 1){
			 	cont_m_expert = cont_m_expert +1
			 	soma_m_expert = soma_m_expert + idade
			 	media_m_expert = soma_m_expert / cont_m_expert
			 }
			  senao se (idade >= 18 e idade <=32 e genero == 2){
			 	cont_h_jovem = cont_h_jovem + 1
			 	soma_h_jovem = soma_h_jovem + idade
			 	media_h_jovem = soma_h_jovem / cont_h_jovem
			 }
			 senao se (idade >= 33 e idade <= 61 e genero == 2){
			 	cont_h_adultos = cont_h_adultos + 1
			 	soma_h_adultos = soma_h_adultos + idade
			 	media_h_adultos = soma_h_adultos / cont_h_adultos
			 }
			 senao se (idade > 61 e genero == 2) {
			 	cont_h_expert = cont_h_expert +1
			 	soma_h_expert = soma_h_expert + idade
			 	media_h_expert = soma_h_expert / cont_h_expert
			 }
			
			escreva("\ndigite o seu nome:")
			leia (nome)
			limpa()
	
			escreva("\ndigite o seu peso:")
			leia (peso)
			limpa()


			se (idade >= 18 e idade <=32){
				cont_peso_jovem = cont_peso_jovem + 1
				soma_peso_jovem = soma_peso_jovem + peso
				media_peso_jovem = soma_peso_jovem / cont_peso_jovem 
			}
			senao se (idade >= 33 e idade <= 61){
				cont_peso_adulto = cont_peso_adulto + 1
				soma_peso_adulto = soma_peso_adulto + peso
				media_peso_adulto = soma_peso_adulto / cont_peso_adulto
			}	
			senao {cont_peso_expert = cont_peso_expert +1
				soma_peso_expert = soma_peso_expert + peso
				media_peso_expert =  soma_peso_expert / cont_peso_expert
			}


			
			 se (idade >= 18 e idade <=32 e genero == 1){
			 	cont_m_jovem_peso = cont_m_jovem_peso + 1
			 	soma_m_jovem_peso = soma_m_jovem_peso + peso
			 	media_m_jovem_peso = soma_m_jovem_peso / cont_m_jovem_peso
			 }
			 senao se (idade >= 33 e idade <= 61 e genero == 1){
			 	cont_m_adultas_peso = cont_m_adultas_peso + 1
			 	soma_m_adultas_peso = soma_m_adultas_peso + peso
			 	media_m_adultas_peso = soma_m_adultas_peso / cont_m_adultas_peso
			 }
			 senao se (idade > 61 e genero == 1){
			 	cont_m_expert_peso = cont_m_expert_peso +1
			 	soma_m_expert_peso = soma_m_expert_peso + peso
			 	media_m_expert_peso = soma_m_expert_peso / cont_m_expert_peso
			 }

			  senao se (idade >= 18 e idade <=32 e genero == 2){
			 	cont_h_jovem_peso = cont_h_jovem_peso + 1
			 	soma_h_jovem_peso = soma_h_jovem_peso + peso
			 	media_h_jovem_peso = soma_h_jovem_peso / cont_h_jovem_peso
			 }
			 senao se (idade >= 33 e idade <= 61 e genero == 2){
			 	cont_h_adultos_peso = cont_h_adultos_peso + 1
			 	soma_h_adultos_peso = soma_h_adultos_peso + peso
			 	media_h_adultos_peso = soma_h_adultos_peso / cont_h_adultos_peso
			 }
			 senao se (idade > 61 e genero == 2){
			 	cont_h_expert_peso = cont_h_expert_peso + 1
			 	soma_h_expert_peso = soma_h_expert_peso + peso
			 	media_h_expert_peso = soma_h_expert_peso / cont_h_expert_peso
			 }

			escreva("\ndigite sua altura em cm:")
			leia (altura)
			limpa()
			
			se (idade >= 18 e idade <=32){
				cont_altura_jovem = cont_altura_jovem + 1 
				soma_altura_jovem = soma_altura_jovem + altura 
				media_altura_jovem = soma_altura_jovem / cont_altura_jovem
			}
			senao se (idade >= 33 e idade <= 61){
				cont_altura_adulto = cont_altura_adulto + 1
				soma_altura_adulto = soma_altura_adulto + altura
				media_altura_adulto = soma_altura_adulto / cont_altura_adulto
			}
			senao {cont_altura_expert = cont_altura_expert + 1
			soma_altura_expert = soma_altura_expert + altura
			media_altura_expert = soma_altura_expert / cont_altura_expert
			}

	
			valor_imc = (peso/(altura*altura)) *10000
			escreva (valor_imc)
			
			se (valor_imc <= 18.5){
			escreva ("\nSeu IMC esta abaixo")
			}
	
	
			 senao se (valor_imc >= 24.9){ 
			 escreva ("\nVocê esta com sobrepeso")
			 }
		
	
			 senao {
			 escreva ("\nVocê esta com o peso adequado")
			 }

			  se (idade >= 18 e idade <=32 e genero == 1){
			 	cont_m_jovem_altura = cont_m_jovem_altura + 1
			 	soma_m_jovem_altura = soma_m_jovem_altura + altura
			 	media_m_jovem_altura = soma_m_jovem_altura / cont_m_jovem_altura
			 }
			 senao se (idade >= 33 e idade <= 61 e genero == 1){
			 	cont_m_adultas_altura = cont_m_adultas_altura + 1
			 	soma_m_adultas_altura = soma_m_adultas_altura + altura
			 	media_m_adultas_altura = soma_m_adultas_altura / cont_m_adultas_altura
			 }
			 senao se (idade > 61 e genero == 1){
			 	cont_m_expert_altura = cont_m_expert_altura +1
			 	soma_m_expert_altura = soma_m_expert_altura + altura
			 	media_m_expert_altura = soma_m_expert_altura / cont_m_expert_altura
			 }

			  senao se (idade >= 18 e idade <=32 e genero == 2){
			 	cont_h_jovem_altura = cont_h_jovem_altura + 1
			 	soma_h_jovem_altura = soma_h_jovem_altura + altura
			 	media_h_jovem_altura = soma_h_jovem_altura / cont_h_jovem_altura
			 }
			 senao se (idade >= 33 e idade <= 61 e genero == 2){
			 	cont_h_adultos_altura = cont_h_adultos_altura + 1
			 	soma_h_adultos_altura = soma_h_adultos_altura + altura
			 	media_h_adultos_altura = soma_h_adultos_altura / cont_h_adultos_altura
			 }
			 senao {
			 	cont_h_expert_altura = cont_h_expert_altura +1
			 	soma_h_expert_altura = soma_h_expert_altura + altura
			 	media_h_expert_altura = soma_h_expert_altura / cont_h_expert_altura
			 }


		escreva("\nvoce Deseja continuar a pesquisa? Digite: \n s -> para sim \n n -> para não:")
		leia(resposta)
	limpa()
	contador = contador + 1
	    
	
}
enquanto (resposta == "s")
    se (resposta == "n"){
    escreva("\nQuantidade de entrevistados é: ", contador)
    
    
    escreva("\n\nA média de idade entre os jovens é:", media_jovens)
    escreva("\nMédia de peso entre os jovens é:", media_peso_jovem)
    escreva("\nMédia de altura entre os jovens é:", media_altura_jovem)
    escreva("\nA média de idade das mulheres jovens foi:", media_m_jovem, ",a média de peso é:", media_m_jovem_peso, " e a média de altuta:", media_m_jovem_altura)
    escreva("\nA média de idade dos homens jovens foi:",media_h_jovem, ", a média de peso é:", media_h_jovem_peso, " e a média de altura:", media_h_jovem_altura)
    
    escreva("\n\nA média de idade entre adultos é:", media_adultos)
    escreva("\nMedia de peso entre os adultos é:", media_peso_adulto)
    escreva("\nMédia de altura entre os adultos é:", media_altura_adulto)
    escreva("\nA média de idade entre mulheres adultas é:", media_m_adultas, ",a média de peso é:", media_m_adultas_peso, " e a média de altura:", media_m_adultas_altura)
    escreva("\nA média de idade entre os homens adultos é:", media_h_adultos, ",a média de peso é:", media_h_adultos_peso, " e a média de altura:", media_h_adultos_altura)
    
    escreva("\n\nMédia de idade entre os expert é:", media_expert)
    escreva("\nMédia de peso entre os expert é:", media_peso_expert)
    escreva("\nMedia de altura entre os expert:", media_altura_expert)
    escreva("\nMédia de idade entre as mulheres expert é:", media_m_expert, ",a média de peso e:", media_m_expert_peso, " e a média de altura:", media_m_expert_altura)
    escreva("\nA média de idade entre os homens expert é:", media_h_expert, ",a média de peso e:", media_h_expert_peso, " e a média de altura:", media_h_expert_altura)
    
    
}
}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 9191; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */