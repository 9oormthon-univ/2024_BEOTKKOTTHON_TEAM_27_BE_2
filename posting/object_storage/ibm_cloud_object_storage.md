## IBM Cloud Object Storage ☁️
### IBM Cloud Object Storage S3 API 정보
- 오브젝트를 읽고 쓰기 위한 REST기반 API이다.
- 오브젝트 오퍼레이션
  - DELETE: 버킷에서 오브젝트를 삭제한다.
  - GET: 버킷에서 오브젝트를 검색한다.
  - PUT: 버킷에 오브젝트를 추가한다.
- IBM Cloud Object Storage HMAC 신임 정보 사용 의 인스턴스에 인증할 때 HMAC 서명 구성 인 경우 다음의 정보가 필요하다.
  - HMAC 인증 정보 사용
    - 인증이 필요한 S3-compatible 도구 및 라이브러리와 함게 사용하기 위해 쌍을 이루는 **액세스 키 및 비밀 키**로 구성된다.
    - Include HMAC Credential 를 On 로 전환하여 서비스 신임 정보 의 일부로 HMAC 신임 정보 세트를 작성할 수 있습니다.
    - ![img.png](image/img.png)
    - 서비스 인증 정보가 작성되고 나면 HMAC 키가 `cos_hmac_keys` 필드에 포함된다.
    - 이 HMAC 키는 서비스 ID와 연관되며, 서비스 ID의 역할에서 허용되는 리소스 또는 오퍼레이션에 액세스 하는데 사용될 수 있다.
        ```
        cos_hmac_keys:
            access_key_id:      
            secret_access_key:  
        ```
    - 다음과 같이 이를 환경 변수로 설정한다.
        ```
        export COS_HMAC_ACCESS_KEY_ID=
        export COS_HMAC_SECRET_ACCESS_KEY=
        ```
    - Create a new policy for a user - cloud object storage
      - ![img_2.png](image/img_2.png)
    - Where is resouce ID?
      - b41c048334ae::d26a651b-47d7-4a0d-b5b3-b41c048334ae
      - ![img_1.png](image/img_1.png)
      - resouce_id : d26a651b-47d7-4a0d-b5b3-b41c048334ae
    - 서비스 아이디 생성 완료 및 액세스 부여 완료
      - ![img_3.png](image/img_3.png)
    - How can I get IAM Token?
      - 서비스 ID의 API 키를 이용하여 받을 수 있다.
      - service id - api key : juggN_XeJO__ruAcSfbdRcQ259fwCBffDntPBcgy1Ama
      - user - api key : 6CZdm_q1wQMqvsb7VS0sR4WV81hDtNjXbXqzVhTC-x8S
      - curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=juggN_XeJO__ruAcSfbdRcQ259fwCBffDntPBcgy1Ama'
      - 오 받아땅 대박
      - service id - access token : eyJraWQiOiIyMDI0MDMwNjA4MzgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTUxMThkNDJjLWEyMzItNDU3My1iMTg2LTdiN2M2ZTVlNWMwZCIsImlkIjoiaWFtLVNlcnZpY2VJZC01MTE4ZDQyYy1hMjMyLTQ1NzMtYjE4Ni03YjdjNmU1ZTVjMGQiLCJyZWFsbWlkIjoiaWFtIiwianRpIjoiMTczYjFlM2YtYmJhZS00Y2UyLWIzOTItY2JmN2I5NDM1ODI3IiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC01MTE4ZDQyYy1hMjMyLTQ1NzMtYjE4Ni03YjdjNmU1ZTVjMGQiLCJuYW1lIjoic29kb25nLXNlcnZpY2UtaWQiLCJzdWIiOiJTZXJ2aWNlSWQtNTExOGQ0MmMtYTIzMi00NTczLWIxODYtN2I3YzZlNWU1YzBkIiwic3ViX3R5cGUiOiJTZXJ2aWNlSWQiLCJhdXRobiI6eyJzdWIiOiJTZXJ2aWNlSWQtNTExOGQ0MmMtYTIzMi00NTczLWIxODYtN2I3YzZlNWU1YzBkIiwiaWFtX2lkIjoiaWFtLVNlcnZpY2VJZC01MTE4ZDQyYy1hMjMyLTQ1NzMtYjE4Ni03YjdjNmU1ZTVjMGQiLCJzdWJfdHlwZSI6IlNlcnZpY2VJZCIsIm5hbWUiOiJzb2Rvbmctc2VydmljZS1pZCJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiIyMzFiZmQ0OWEzMGQ0N2E3YjdjMjYxYjdmMjUxMWU5YSIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTcxMDU2OTc0MiwiZXhwIjoxNzEwNTczMzQyLCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.qaLx_4G3fuSQBIpa3O9nc1Uw-MAmP5czEpKW66mPQ6pMVPitwALiSMAp7uiSwQk1KJr31U6XBnxb2LLBWSIpp3MqjWIx1gLku7dexi1qCEDYVoOawFQMMMOfsqFniqeE_u1tLEiOXOlKwGs5F0cE1hQEHCX5CLXkOPUOWIOkXDCZXsScOD-QM4H4Y_f2r8YQ208Gc8bkkOXhoke9V6zeZJTumFUcGurlD2rz-j0Qg0e16uGqFDoi-AZGER4vCsifOhq_7VCHP3QO5Uvnu7hZcwqz0qD6k3pCmMoc041vCZIyt3I_wD9HSEgMOr0uH1IhUo66Kk6pttWNCYRhnUheug
      - user - access token : eyJraWQiOiIyMDI0MDMwNjA4MzgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTEwMDBCRThLIiwiaWQiOiJJQk1pZC02OTEwMDBCRThLIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNDdmMjYxNTItOTkwNS00ZGIwLWEwMjUtMjViMDM1ZGQyZDdlIiwiaWRlbnRpZmllciI6IjY5MTAwMEJFOEsiLCJnaXZlbl9uYW1lIjoi7LGE66awIiwiZmFtaWx5X25hbWUiOiLslpEiLCJuYW1lIjoi7LGE66awIOyWkSIsImVtYWlsIjoia2V1a2tldTQ2NEBnbWFpbC5jb20iLCJzdWIiOiJrZXVra2V1NDY0QGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6ImtldWtrZXU0NjRAZ21haWwuY29tIiwiaWFtX2lkIjoiSUJNaWQtNjkxMDAwQkU4SyIsIm5hbWUiOiLssYTrprAg7JaRIiwiZ2l2ZW5fbmFtZSI6IuyxhOumsCIsImZhbWlseV9uYW1lIjoi7JaRIiwiZW1haWwiOiJrZXVra2V1NDY0QGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiIyMzFiZmQ0OWEzMGQ0N2E3YjdjMjYxYjdmMjUxMWU5YSIsImltc191c2VyX2lkIjoiMTE4NDk0MzgiLCJmcm96ZW4iOnRydWUsImltcyI6IjI3OTE0MDgifSwiaWF0IjoxNzEwNTcwOTc0LCJleHAiOjE3MTA1NzQ1NzQsImlzcyI6Imh0dHBzOi8vaWFtLmNsb3VkLmlibS5jb20vaWRlbnRpdHkiLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.i03fxrUbbvDHXOpjdCmiVMh9lSodC1Yxk1xaYZO5V96fBQ8vKVsv6KXYrR4c3RbJhmCo9EcrpNocMqE1weprU3-0pn8Id9eZhhVD_nTNVdKaLLChtb1t-YCgrJYSZwxMMZR4447MhgsW24Jvgb_mzqre6MtNghHzJlCI26YSVz2k1JTpH6vk7JUgrIkRzAcPquXeNmbT_21EhJGR3L8uVbsV7Yi26emPCoITGddACxphl-1XniMSWWZajdO0kD9Qzwtf2BqW5JVB7UABuikJ3XehG1ot-R6EkJrYiKYBEqwL7EFHMClsw2asofvHhUzXE0Qh6Lo9kTgcl06o5ltxTQ
      - 버킷의 객체 나열
        - curl -X "GET" "https://s3.$REGION.cloud-object-storage.appdomain.cloud/$BUCKET" -H "Authorization: Bearer $IAM_TOKEN" 

### Access Denied Error...
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Error><Code>AccessDenied</Code><Message>Access Denied</Message><Resource>/image-with-copywriter/</Resource><RequestId>b920c480-79c8-4622-84f3-dfc074a04cb7</RequestId><httpStatusCode>403</httpStatusCode></Error>% 
```
왜일까... 일단 그 service id의 권한을 살펴보자.  
`cloud-object-storage.bucket.get` 권한이 있어야 한다고 한다.  
![img_4.png](image/img_4.png)
있는데...

### 시도 1
모든 권한을 주었던 것에서 일부 권한만 제공하는 것으로 변경하였다. 
**실패**

### 시도 2
user의 api key로 받은 토큰으로 하니까 성공했다.
```
curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=fBnt1SrMjlDdgkZD6qexf1KaiNJsRHg7Ay9a0miwGtH4'
```

**버킷의 객체 나열 API**
```
curl -X "GET" "https://s3.us-south.cloud-object-storage.appdomain.cloud/image-with-copywriter" -H "Authorization: Bearer eyJraWQiOiIyMDI0MDMwNjA4MzgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTEwMDBCRThLIiwiaWQiOiJJQk1pZC02OTEwMDBCRThLIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNTg5YzhjNzktOWM1OS00NmFiLWJkNDEtNjZjYzljNjAzNzIzIiwiaWRlbnRpZmllciI6IjY5MTAwMEJFOEsiLCJnaXZlbl9uYW1lIjoi7LGE66awIiwiZmFtaWx5X25hbWUiOiLslpEiLCJuYW1lIjoi7LGE66awIOyWkSIsImVtYWlsIjoia2V1a2tldTQ2NEBnbWFpbC5jb20iLCJzdWIiOiJrZXVra2V1NDY0QGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6ImtldWtrZXU0NjRAZ21haWwuY29tIiwiaWFtX2lkIjoiSUJNaWQtNjkxMDAwQkU4SyIsIm5hbWUiOiLssYTrprAg7JaRIiwiZ2l2ZW5fbmFtZSI6IuyxhOumsCIsImZhbWlseV9uYW1lIjoi7JaRIiwiZW1haWwiOiJrZXVra2V1NDY0QGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiIyMzFiZmQ0OWEzMGQ0N2E3YjdjMjYxYjdmMjUxMWU5YSIsImltc191c2VyX2lkIjoiMTE4NDk0MzgiLCJmcm96ZW4iOnRydWUsImltcyI6IjI3OTE0MDgifSwiaWF0IjoxNzEwNjEwMjY2LCJleHAiOjE3MTA2MTM4NjYsImlzcyI6Imh0dHBzOi8vaWFtLmNsb3VkLmlibS5jb20vaWRlbnRpdHkiLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.3rVpguXEuQLve16UD1xODhwNybROl50kwUAU5I4cvwmxZzrZNuZU_wqx3bJF5GN7ZnzhIELrYi5ATU_cfGJ-_JgUW7mKeBqbuDXv58_PNZ0Qe5aCJlI-f_R0D_bpV9fR0dnVM0kzeN92pOAc2qgqHipXiSSv9Z0bR5L2VpVqdRZ6bw4twAwW2vYoS8jMzA1xR95cU4aOWishSWa2-ZNn7ErIM7A2-yA2lSdjP9GbfygYfaEZRx_mcWh9bT4JGFoWMJ7GlLe39tjcYmcwlRrWS_rNYYDuwlZbNRBfpl3sQDAIMlk7czQ5yYL2bznHzw19FnzbFVsGu9S5r2mnbGj3dw"
```

**결과**
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>image-with-copywriter</Name><Prefix></Prefix><Marker></Marker><MaxKeys>1000</MaxKeys><Delimiter></Delimiter><IsTruncated>false</IsTruncated><Contents><Key>스크린샷 2024-03-13 오전 2.35.25.png</Key><LastModified>2024-03-15T18:02:50.719Z</LastModified><ETag>&quot;cfa36ae6b901fa23aee4e75ec530fe9b&quot;</ETag><Size>501453</Size><Owner><ID>d26a651b-47d7-4a0d-b5b3-b41c048334ae</ID><DisplayName>d26a651b-47d7-4a0d-b5b3-b41c048334ae</DisplayName></Owner><StorageClass>STANDARD</StorageClass></Contents></ListBucketResult>%
```

### TOKEN은 만료되었을 때 그때그때 발급받아야 한다.
- 만료되었는가?
- 새로 발급

### python-sdk-core
https://github.com/IBM/python-sdk-core/blob/main/Authentication.md 