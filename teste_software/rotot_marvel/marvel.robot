*** Settings ***

Resource  marvel.resource
Suite Setup  Configurar Sessao


*** Test Cases ***
Testar API Comics da Marvel 
    Configurar Sessao
    Realizar requisicao para API 
    Validar se a chave "code" esta preenchida






