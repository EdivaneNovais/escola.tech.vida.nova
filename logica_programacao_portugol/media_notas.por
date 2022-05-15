programa
{
	
	funcao inicio()
	{
	inteiro nota1, nota2, nota3, nota4, idade
	real notafinal
	cadeia nome, sobrenome 

	escreva("digite o nome:")
	leia(nome)

	escreva ("digitee o sobrenome:")
	leia(sobrenome)

	escreva("digite sua idade:")
	leia(idade)

	escreva ("digite sua primeira not")
	leia(nota1)

	escreva("digite sua segunada nota")
	leia(nota2)

	escreva ("digite sua terceira nota")
	leia(nota3)

	escreva("escreva sua quarta nota")
	leia(nota4)

     notafinal=(nota1 + nota2 + nota3 + nota4) /4

     escreva("\nseu nome é:",nome)
     escreva("\nseu sobrenome é:",sobrenome)
     escreva("\nsua idade é:", idade)

     escreva("\nsua nota primeira é:", nota1)
     escreva("\nsua nota segunda é:", nota2)
     escreva("\nsua nota terceira é:", nota3)
     escreva("\nsua nota quarta é:", nota4)

     escreva("\n\n sua nota é:", notafinal)

     se (notafinal>=5)
     {
     	escreva("\nAPROVADO\n")
     }

     senao
     {
     	escreva("\nREPROVADO\n")
     }

     
	
	
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 194; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */