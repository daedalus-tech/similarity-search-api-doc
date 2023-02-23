# Similarity Search API Documentation
A interface do sistema foi divida em duas APIs:
- Process Request API: responsável por receber a imagem e realizar o processamento.
- Get Results API: responsável por acessar os resultados no banco de dados.

A utilização de cada API será detalhada a seguir.

<br>

------------------

<br>

## <div align="center">Process Request</div>
- Nome: Process Request
- API URL: https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/process_request
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

## <div align="center">Get Results</div>

- Nome: Get Results
- API URL: https://184s7zt2xi.execute-api.sa-east-1.amazonaws.com/get_results
- Método: GET
- Autenticação: JWT token
- Descrição: Dado o ID único utilizado em Process Request, esta API acessa o banco de dados e retorna os resultados do processamento.

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

<br>

------------------

<br>


### Um exemplo completo em python pode ser encontrado [aqui](./similarity_search_demo.py).

<br>

------------------

<br>

## <div align="center">Create Gallery</div>

- Nome: Create Gallery
- API URL: https://vgpdf3oowa.execute-api.sa-east-1.amazonaws.com/create-gallery
- Método: GET
- Autenticação: JWT token
- Descrição: Retorna um link para fazer o upload da galeria. Para criar a galeria, a única coisa que precisa ser feita é o upload do arquivo .ZIP utilizando o link. Isso acionará outro serviço para processar as imagens.


## curl

<details open>
<summary>Como chamar a API</summary>

```bash
export GET_UPLOAD_DETAILS_URL=https://vgpdf3oowa.execute-api.sa-east-1.amazonaws.com/create-gallery
export GET_UPLOAD_DETAILS_TOKEN= # add your token here

curl $GET_UPLOAD_DETAILS_URL -H "Authorization: Bearer $GET_UPLOAD_DETAILS_TOKEN"
```

</details>

<details open>
<summary>Retorno esperado</summary>

```
{
    "upload_details": {
        "url": "https://daedalus-similarity-search.s3.amazonaws.com/",
        "fields": {
            "key": "gallery.zip",
            "AWSAccessKeyId": "ASIAQ3P7ZJ2NZL3X4P5S",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEFwaCXNhLWVhc3QtMSJHMEUCIDxcKRZnJmu5Vci9S7W16T4el3j5RNil6++dBQvOomGmAiEAtnbgKjDW9Zub5Bi5PGOhaqrGaAcMHSyVbE3iALDyIqEqpAMI9f//////////ARACGgwwNTkwNTUzNjE2OTEiDBXPerm/P7PHptbwBCr4An8vbS9LoOhJPofwALitf4CXn+9DDn/oZez2rq1Omba59FjFInCGk1tPn4FQ1ERlP3jjVBkOKjUIkf9zDZWSg+oSobvq/2bEACr4LqBD9a+O7nhT61Z4hkR3X/k3ApYeu2V0MpllccHioDC0X02jXtmV/1UmpA6hga7YGzoX3vW/4Hp94d7JjylhnEB86DfDBaKZr9zvNTWt4miN4bhhHJ+eirxp4BnYRG5VplyTeaqYVR1VchQpWyRgVNSPXIJUQKAZYa9W1siXyW7xtckXwTz9hdjcxWSGJj5U2ltnMaoAQiPTf9AsxrRXK5/pH2hMzKNGLdzQIliV4OByZ2SFsFtnxh1240X+ODMreQ1lytraHiJlGDDf/2/EOkX1VQ4e2klH2og/PmAJy0/wbX3BJ8MyaUCL2NNBrzbvVfqr99n7gDzvJ93ZXA+fr8yz2r9vLwNCkfLAm3Jd+y+MRlTC0z/2IievuBjF29/rMgG1s7aEiua3uO8EjAkwroPfnwY6nQGU2gK+RFKGHN7wU4WKdYkaQEsWPiaZMs66x3UovVl23q9kKxAVawzTof03p+vAduM89WraQ67oSv1YycyDrDsxI/rXkSF5ouP6aqDxLp6kE8uFbNh6QNIdnMeA8kFW9oqnOkSixzILcwP4KPapBLxfSFLwaEjSGXltfd360F+Mr89JfavwqWUOt4P8bkVndLCE5JDmOnYz7Eajkx90",
            "policy": "eyJleHBpcmF0aW9uIjogIjIwMjMtMDItMjNUMTk6NTM6MDNaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiZGFlZGFsdXMtc2ltaWxhcml0eS1zZWFyY2gifSwgeyJrZXkiOiAiZ2FsbGVyeS56aXAifSwgeyJ4LWFtei1zZWN1cml0eS10b2tlbiI6ICJJUW9KYjNKcFoybHVYMlZqRUZ3YUNYTmhMV1ZoYzNRdE1TSkhNRVVDSUR4Y0tSWm5KbXU1VmNpOVM3VzE2VDRlbDNqNVJOaWw2KytkQlF2T29tR21BaUVBdG5iZ0tqRFc5WnViNUJpNVBHT2hhcXJHYUFjTUhTeVZiRTNpQUxEeUlxRXFwQU1JOWYvLy8vLy8vLy8vQVJBQ0dnd3dOVGt3TlRVek5qRTJPVEVpREJYUGVybS9QN1BIcHRid0JDcjRBbjh2YlM5TG9PaEpQb2Z3QUxpdGY0Q1huKzlERG4vb1plejJycTFPbWJhNTlGakZJbkNHazF0UG40RlExRVJsUDNqalZCa09LalVJa2Y5ekRaV1NnK29Tb2J2cS8yYkVBQ3I0THFCRDlhK083bmhUNjFaNGhrUjNYL2szQXBZZXUyVjBNcGxsY2NIaW9EQzBYMDJqWHRtVi8xVW1wQTZoZ2E3WUd6b1gzdlcvNEhwOTRkN0pqeWxobkVCODZEZkRCYUtacjl6dk5UV3Q0bWlONGJoaEhKK2VpcnhwNEJuWVJHNVZwbHlUZWFxWVZSMVZjaFFwV3lSZ1ZOU1BYSUpVUUtBWllhOVcxc2lYeVc3eHRja1h3VHo5aGRqY3hXU0dKajVVMmx0bk1hb0FRaVBUZjlBc3hyUlhLNS9wSDJoTXpLTkdMZHpRSWxpVjRPQnlaMlNGc0Z0bnhoMTI0MFgrT0RNcmVRMWx5dHJhSGlKbEdERGYvMi9FT2tYMVZRNGUya2xIMm9nL1BtQUp5MC93YlgzQko4TXlhVUNMMk5OQnJ6YnZWZnFyOTluN2dEenZKOTNaWEErZnI4eXoycjl2THdOQ2tmTEFtM0pkK3krTVJsVEMwei8ySWlldnVCakYyOS9yTWdHMXM3YUVpdWEzdU84RWpBa3dyb1BmbndZNm5RR1UyZ0srUkZLR0hON3dVNFdLZFlrYVFFc1dQaWFaTXM2NngzVW92VmwyM3E5a0t4QVZhd3pUb2YwM3ArdkFkdU04OVdyYVE2N29TdjFZeWN5RHJEc3hJL3JYa1NGNW91UDZhcUR4THA2a0U4dUZiTmg2UU5JZG5NZUE4a0ZXOW9xbk9rU2l4eklMY3dQNEtQYXBCTHhmU0ZMd2FFalNHWGx0ZmQzNjBGK01yODlKZmF2d3FXVU90NFA4YmtWbmRMQ0U1SkRtT25ZejdFYWpreDkwIn1dfQ==",
            "signature": "UBRG1EGSP8kaasyw2wSuwsvuGYY="
        }
    }
}
```

</details>

<details open>
<summary>Upload do arquivo</summary>

```
export ZIP_PATH=gallery.zip
curl -v --request POST -H "Content-Type: multipart/form-data" \
     -F key=gallery.zip \
     -F AWSAccessKeyId=ASIAQ3P7ZJ2NZL3X4P5S \
     -F x-amz-security-token=IQoJb3JpZ2luX2VjEFwaCXNhLWVhc3QtMSJHMEUCIDxcKRZnJmu5Vci9S7W16T4el3j5RNil6++dBQvOomGmAiEAtnbgKjDW9Zub5Bi5PGOhaqrGaAcMHSyVbE3iALDyIqEqpAMI9f//////////ARACGgwwNTkwNTUzNjE2OTEiDBXPerm/P7PHptbwBCr4An8vbS9LoOhJPofwALitf4CXn+9DDn/oZez2rq1Omba59FjFInCGk1tPn4FQ1ERlP3jjVBkOKjUIkf9zDZWSg+oSobvq/2bEACr4LqBD9a+O7nhT61Z4hkR3X/k3ApYeu2V0MpllccHioDC0X02jXtmV/1UmpA6hga7YGzoX3vW/4Hp94d7JjylhnEB86DfDBaKZr9zvNTWt4miN4bhhHJ+eirxp4BnYRG5VplyTeaqYVR1VchQpWyRgVNSPXIJUQKAZYa9W1siXyW7xtckXwTz9hdjcxWSGJj5U2ltnMaoAQiPTf9AsxrRXK5/pH2hMzKNGLdzQIliV4OByZ2SFsFtnxh1240X+ODMreQ1lytraHiJlGDDf/2/EOkX1VQ4e2klH2og/PmAJy0/wbX3BJ8MyaUCL2NNBrzbvVfqr99n7gDzvJ93ZXA+fr8yz2r9vLwNCkfLAm3Jd+y+MRlTC0z/2IievuBjF29/rMgG1s7aEiua3uO8EjAkwroPfnwY6nQGU2gK+RFKGHN7wU4WKdYkaQEsWPiaZMs66x3UovVl23q9kKxAVawzTof03p+vAduM89WraQ67oSv1YycyDrDsxI/rXkSF5ouP6aqDxLp6kE8uFbNh6QNIdnMeA8kFW9oqnOkSixzILcwP4KPapBLxfSFLwaEjSGXltfd360F+Mr89JfavwqWUOt4P8bkVndLCE5JDmOnYz7Eajkx90 \
     -F policy=eyJleHBpcmF0aW9uIjogIjIwMjMtMDItMjNUMTk6NTM6MDNaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiZGFlZGFsdXMtc2ltaWxhcml0eS1zZWFyY2gifSwgeyJrZXkiOiAiZ2FsbGVyeS56aXAifSwgeyJ4LWFtei1zZWN1cml0eS10b2tlbiI6ICJJUW9KYjNKcFoybHVYMlZqRUZ3YUNYTmhMV1ZoYzNRdE1TSkhNRVVDSUR4Y0tSWm5KbXU1VmNpOVM3VzE2VDRlbDNqNVJOaWw2KytkQlF2T29tR21BaUVBdG5iZ0tqRFc5WnViNUJpNVBHT2hhcXJHYUFjTUhTeVZiRTNpQUxEeUlxRXFwQU1JOWYvLy8vLy8vLy8vQVJBQ0dnd3dOVGt3TlRVek5qRTJPVEVpREJYUGVybS9QN1BIcHRid0JDcjRBbjh2YlM5TG9PaEpQb2Z3QUxpdGY0Q1huKzlERG4vb1plejJycTFPbWJhNTlGakZJbkNHazF0UG40RlExRVJsUDNqalZCa09LalVJa2Y5ekRaV1NnK29Tb2J2cS8yYkVBQ3I0THFCRDlhK083bmhUNjFaNGhrUjNYL2szQXBZZXUyVjBNcGxsY2NIaW9EQzBYMDJqWHRtVi8xVW1wQTZoZ2E3WUd6b1gzdlcvNEhwOTRkN0pqeWxobkVCODZEZkRCYUtacjl6dk5UV3Q0bWlONGJoaEhKK2VpcnhwNEJuWVJHNVZwbHlUZWFxWVZSMVZjaFFwV3lSZ1ZOU1BYSUpVUUtBWllhOVcxc2lYeVc3eHRja1h3VHo5aGRqY3hXU0dKajVVMmx0bk1hb0FRaVBUZjlBc3hyUlhLNS9wSDJoTXpLTkdMZHpRSWxpVjRPQnlaMlNGc0Z0bnhoMTI0MFgrT0RNcmVRMWx5dHJhSGlKbEdERGYvMi9FT2tYMVZRNGUya2xIMm9nL1BtQUp5MC93YlgzQko4TXlhVUNMMk5OQnJ6YnZWZnFyOTluN2dEenZKOTNaWEErZnI4eXoycjl2THdOQ2tmTEFtM0pkK3krTVJsVEMwei8ySWlldnVCakYyOS9yTWdHMXM3YUVpdWEzdU84RWpBa3dyb1BmbndZNm5RR1UyZ0srUkZLR0hON3dVNFdLZFlrYVFFc1dQaWFaTXM2NngzVW92VmwyM3E5a0t4QVZhd3pUb2YwM3ArdkFkdU04OVdyYVE2N29TdjFZeWN5RHJEc3hJL3JYa1NGNW91UDZhcUR4THA2a0U4dUZiTmg2UU5JZG5NZUE4a0ZXOW9xbk9rU2l4eklMY3dQNEtQYXBCTHhmU0ZMd2FFalNHWGx0ZmQzNjBGK01yODlKZmF2d3FXVU90NFA4YmtWbmRMQ0U1SkRtT25ZejdFYWpreDkwIn1dfQ== \
     -F signature=UBRG1EGSP8kaasyw2wSuwsvuGYY= \
     -F file=@$ZIP_PATH https://daedalus-similarity-search.s3.amazonaws.com/
```

</details>

<details open>
<summary>Retorno esperado</summary>

```
*   Trying 52.217.130.57:443...
* TCP_NODELAY set
* Connected to daedalus-similarity-search.s3.amazonaws.com (52.217.130.57) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: CN=*.s3.amazonaws.com
*  start date: Sep 21 00:00:00 2022 GMT
*  expire date: Aug 26 23:59:59 2023 GMT
*  subjectAltName: host "daedalus-similarity-search.s3.amazonaws.com" matched cert's "*.s3.amazonaws.com"
*  issuer: C=US; O=Amazon; OU=Server CA 1B; CN=Amazon
*  SSL certificate verify ok.
> POST / HTTP/1.1
> Host: daedalus-similarity-search.s3.amazonaws.com
> User-Agent: curl/7.68.0
> Accept: */*
> Content-Length: 49327
> Content-Type: multipart/form-data; boundary=------------------------49c3dcadf6ba24ea
> Expect: 100-continue
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 100 Continue
* We are completely uploaded and fine
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< x-amz-id-2: hRB64Tn4XM2sGxvsEtCHyeMKa0ahMk0x0CJIxeFCkTMXE51gGYnX2glvJY/SEOW/sx9KWoiZgIE=
< x-amz-request-id: 9MWE1EHMPK4ZF8J2
< Date: Thu, 23 Feb 2023 19:48:38 GMT
< x-amz-server-side-encryption: AES256
< ETag: "90e664c0b2d0f4d47fd8ae44d6fceefe"
< Location: https://daedalus-similarity-search.s3.amazonaws.com/gallery.zip
< Server: AmazonS3
< 
* Connection #0 to host daedalus-similarity-search.s3.amazonaws.com left intact

```

</details>



Um exemplo completo em python pode ser encontrado [aqui](./create_gallery.py).
