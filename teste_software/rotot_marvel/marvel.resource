*** Settings ***
Library  RequestsLibrary
Variables  config.py

*** Variables ***
${URL}

*** keywords ***
Configurar Sessao
    ${URL}  Set Variable  ${URL_COMIC}?apikey=${API_KEY}

Realizar requisicao para API 
    Create Session  requisicao_comics  ${BASE_URL}  headers=${HEADERS}
    ${response_comics}=  Get On Session  requisicao_comics  url=${URL_COMIC}?apikey=${API_KEY}
    Log To Console  ${response_comics}
    Set Test Variable  ${response_comics}

Validar se a chave "code" esta preenchida
    ${StatusCodeInt}=  Convert To Integer  200
    Should Be Equal  ${response_comics.json()}[code]  ${StatusCodeInt}