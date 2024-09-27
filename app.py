#Automação FireHydrant

"""
Automação com Opsgenie & FireHydrant 


Inicio do projeto na data 25/09/2025 - Call com Chacon e Cesar



PROJETO - "A ideia é quando tiver um incidente é criar um canal canal/comunicação e pessoas envolvidas de forma automática" 

Chacon - "Opsgenie cria o incidente no JIRA de forma automática"


Firehydrant esta integrado com Jira, Zoom, Slack e Opsgenie | Opsgenie é o final de cada alerta, ele so faz o meio termo, o fireHydrant é um passo após o Opsgenie


O que o firehydrant faz de diferente ? --> 


Procurar se é possível criar um botão de integração no Slack onde faz a função de abrir call com o FireHydrant 


"OPsgenie Alerts" ele que é o runbook principal 



O ideal seria clonar um Runbook, colocar com Owner team o time de Infosec --> 


Olhar a parte de estrutura de decisão por palavras, o firehydrant esta integrado dentro do Slack! 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

É possível escolher palavras chave e criticidade para iniciar o alerta, também é possível enviar um webhook com POST ( API ) 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------



Enviar o dados do opsgenie para o Hydrant-> Depois gerenciar e escolher as tomadas de decisão -> Runbook contém as "funções" de decisão.



----------------------------------------------------------------------------------------------------------------------------------------------------------------------
				O BOTÃO NO OPSGENIE CONTENDO A FUNÇÃO É O FOCO
----------------------------------------------------------------------------------------------------------------------------------------------------------------------


Ler a documentação por completa com FireHydrant e olhar as opções para integração e funções.


"""