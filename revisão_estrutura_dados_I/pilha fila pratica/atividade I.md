//Na linha a seguir estamos carregando a biblioteca Standart Input Output
// para usarmos os comandos de entrada (scanf) e saida (printf) de dados
#include <stdio.h>
#include <locale.h>

/*Escreva um algoritmo que solicite nome, Sexo, idade e tres notas de N alunos
em uma turma e ao final apresente: 

1 - total de alunos cadastrados------------------------------------------------------ ok

2- a media das idades dos alunos da turma-------------------------------------------- ok

3- quantidade de alunos aprovados---------------------------------------------------- ok

3.1 - quantidade de alunos reprovados------------------------------------------------ ok

4- percentual de aprovação por sexo (masculinos e femininos) (dever de casa p/ 11/03)

5- Relatorio de alunos aprovados 

6 - permitir ao usuario configurar quantidade de provas e media de aprovacao--------- ok
*/

//a seguir estamos definindo uma estrutura de dados na memoria do pc
struct Aluno {
	char Nome[30];
	char Sexo;
	int Idade;
	float Notas[10];
	bool Aprovado;
};

//a seguir temos a funcao principal do programa
int main (){
	setlocale(LC_ALL, "");
	int QtdAlunos; //variavel que controlara o total de alunos da turma
	int QtdProvas; //variavel que controlara o total de alunos da turma
	int SomaIdades = 0; //variavel que controlara o total das idades da turma (para o calculo da media das idades)
	int QtdAprovados = 0; //variavel que lista os aprovados
	float media = 0, soma = 0, MediaAprove; 
	struct Aluno Alunos[100]; //vetor chamado alunos, com cem posicoes do tipo struct de aluno
	//configurando a quantidade de alunos da turma
	printf("Informe a quantidade de alunos da turma: ");
	scanf("%i", &QtdAlunos);
	//configurando a quantidade de provas
	printf("Informe a quantidade de provas: ");
	scanf("%i", &QtdProvas);
	//configurando a media
	printf("Informe a média das provas: ");
	scanf("%f", &MediaAprove);
	//vamos percorrer os N alunos para solicitar seus dados
	for (int i=1; i<=QtdAlunos; i++){
		printf("informe o nome do %i. aluno: ", i);
		scanf("%s", &Alunos[i].Nome);
		printf("informe o idade de %s ", Alunos[i].Nome);
		scanf("%i", &Alunos[i].Idade);
		SomaIdades = SomaIdades + Alunos[i].Idade; //SomaIdades+=Alunos[i].idade
		printf("informe o sexo de %s: [M/F] ", Alunos[i].Nome);
		scanf("%s", &Alunos[i].Sexo);
		
		soma = 0;
		for (int n=1; n<=QtdProvas; n++) { //antes era HARD CODED
			printf("   informe a %i nota: ", n);
			scanf("%f", &Alunos[i].Notas[n]);
			soma = soma + Alunos[i].Notas[n];
		  // Calculo da aprovacao/reprovacao do aluno
		media = soma / QtdProvas;
		  // Alimentar a clausula Aprovado (do tipo Booleano)
	    if (media >= MediaAprove) { // antes era HARD CODED
	        Alunos[i].Aprovado = true;
	        QtdAprovados=QtdAprovados+1; //QtdAprovados++; ou QtdAprovados+=1;
	    }
	    	else
	        	Alunos[i].Aprovado = false;
	    printf("Média de %s: %.2f\n", Alunos[1].Nome, media);
	    }
	}
	printf("\n Total de alunos cadastrados na turma: %i ", QtdAlunos);
	float MediaIdades = SomaIdades/QtdAlunos;
	printf("\n A media das idades dos alunos da turma: %0.2f ", MediaIdades);
	printf("\n A quantidade de alunos aprovados: %d", QtdAprovados);
	printf("\n A quantidade de alunos reprovados: %d", QtdAlunos-QtdAprovados);
}
