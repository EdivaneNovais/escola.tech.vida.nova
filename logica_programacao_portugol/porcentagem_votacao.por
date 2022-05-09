programa
{
	
	funcao inicio()
	{
		inteiro candidato_a = 0, candidato_b=0
		real branco =0, nulos =0, total_votos=0
		real porcentagem_candidato_a, porcentagem_candidato_b
		real porcentagem_brancos, porcentagem_nulos
		inteiro voto
		
		
		faca
		{

		limpa()
		escreva("\nEscolha seu candidato ou tecle zero para encerrar\n")

		escreva("1 -> candidato A\n") 
		escreva("2 -> candidato B\n")
		escreva ("3 -> Branco\n")

		escreva ("\nQualquer número diferente de 0, 1, 2 e 3 anulara seu voto!\n")

		escreva ("Digite seu voto:")

		leia (voto)

		limpa()

		escolha (voto)
		{ 
			caso 0:

	     		escreva("\nVotacao encerrada!\n")

	         pare

	      	caso 1:  
	   			candidato_a = candidato_a + 1 // soma um voto para o candidato A

	       pare
	       
	       	caso 2: 
	      	 	candidato_b=candidato_b + 1 

	       pare
	       
	       	caso 3:
	       		branco=branco + 1 //soma um voto em branco 

	       pare
	       
	       	caso contrario:
	       		nulos=nulos + 1 // opcao invalida, soma um voto nulo
		}
	}
	enquanto(total_votos <=10)
	
	
	     
	total_votos = candidato_a + candidato_b + branco + nulos
		
	porcentagem_candidato_a= (100 * candidato_a) / total_votos

	porcentagem_candidato_b= (100 * candidato_b) / total_votos
		
	porcentagem_brancos = (100 * branco) / total_votos
	
	porcentagem_nulos=(100 * nulos) / total_votos
		
		escreva ("\nPorcentagem candidato A:", porcentagem_candidato_a, "%")
	     escreva ("\nPorcentagem candidato B:", porcentagem_candidato_b, "%")

	     escreva ("\nPorcentagem brancos:" , porcentagem_brancos, "%")
	     escreva ("\nPorcentagem nulos:" , porcentagem_nulos, "%")

	     se (candidato_a > candidato_b)
	     escreva("\nCandidato A ganhou a eleicao")
	     se (candidato_b > candidato_a)
	     escreva("\nCandidato B ganhou a eleicao")
	     se (candidato_a == candidato_b)
	     escreva ("\nNinguem ganhou")

	     escreva ("\nTotal de votos:", total_votos)

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 222; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */