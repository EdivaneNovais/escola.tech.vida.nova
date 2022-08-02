
*** Settings *** 
Library  RequestsLibrary
Variables  config.py


*** test cases ***
Testar API Marvel Chars
    configurar Sessão
    Realizar a requisicao no catalogo
    validar os campos obrigatorios

*** Keywords ***
Configurar Sessão
    Create Session  requisicao_catalogo  https://servicespub.prod.api.aws.grupokabum.com.br  headers=${HEADERS}  verify=true

Realizar a requisicao no catalogo
    ${resposta_catalog}=  Get On Session  requisicao_catalogo  /catalog/v2/releases
    Log To Console  ${resposta_catalog}
    Set Test Variable  ${resposta_catalog}

validar os campos obrigatorios
    Request Should Be Successful  ${resposta_catalog}
    Should Not Be Empty  ${resposta_catalog.json()}[data]