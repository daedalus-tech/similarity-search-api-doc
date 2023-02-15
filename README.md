# Similarity Search API Documentation
A interface do sistema foi divida em duas APIs:
- [Process Request API](#process_request_api): responsável por receber a imagem e realizar o processamento.
- [Get Results API](#get_results_api): responsável por acessar os resultados no banco de dados.

<br>

------------------

<br>

## [<div align="center">Process Request</div>](#process_request_api)
- Nome: Process Request
- API URL: https://8wvaarvrsc.execute-api.sa-east-1.amazonaws.com/default/fullstack_exam_get_presigned_url
- Método: POST
- Autenticação: JWT token
- Descrição: Esta API recebe uma requisição HTTP via POST contendo a imagem codificada em base64 e um ID da requisição. Este ID deverá ser usado posteriormente para consultar os resultados do processamento.

<br>

## <div align="center">Exemplo</div>

</details>

## curl

<details open>
<summary>Como chamar a API</summary>

```bash
export PROCESS_REQUEST_URL=https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/process_request
export PROCESS_REQUEST_AUTH_TOKEN= # add your token here
export REQUEST_UUID=$( uuidgen ) # generates an unique id for your request
export IMAGE_PATH=demo_data.jpg

curl -X POST $PROCESS_REQUEST_URL -H "Authorization: Bearer $PROCESS_REQUEST_AUTH_TOKEN" --header 'Content-Type: application/json' --data-raw '{"encoded_image" : "'"$( base64 -w 0 $IMAGE_PATH)"'", "request_uuid": "'$REQUEST_UUID'"}'
```

Note que a flag **-w 0** é utilizada para desabilitar a quebra de linha no encoding da imagem.

</details>

<br>

------------------

<br>

## [<div align="center">Get Results</div>](#get_results_api)

- Nome: Get Results
- API URL: https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/get_results
- Método: GET
- Autenticação: JWT token
- Descrição: Dado o ID único utilizado em [Process Request](#process_request_api), esta API acessa o banco de dados e retorna os resultados do processamento.

<br>

## <div align="center">Exemplo</div>

</details>

## curl

<details open>
<summary>Como chamar a API</summary>

```bash
export GET_RESULTS_URL=https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/get_results
export GET_RESULTS_AUTH_TOKEN= # add your token here

curl $GET_RESULTS_URL?request_uuid=$REQUEST_UUID -H "Authorization: Bearer $GET_RESULTS_AUTH_TOKEN"
```

</details>