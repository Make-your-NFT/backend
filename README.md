# 🪙 Make Your NFT

### Platforms
![SpringBoot: Version](https://img.shields.io/badge/SpringBoot-2.6.6-6DB33F.svg?logo=SpringBoot&logoColor=white)
![MariaDB: Version](https://img.shields.io/badge/MariaDB-10.6.7-003545.svg?logo=MariaDB&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJIDEA-3.1.3-000000.svg?style=flat-square&logo=intellij-idea&logoColor=white)

### Tools
[![Notion](https://img.shields.io/badge/Notion-000000.svg?style=flat-square&logo=notion&logoColor=white)](https://www.notion.so/Backend-3e5c6c7e856e4014a6eedf50bce790a1)

***

## ✔️ Getting Started

### Spring Boot 프로젝트 생성
- [Spring Initializr](https://start.spring.io/)에서 압축 프로젝트 파일을 다운로드 한다.
- 필요한 의존성 항목을 선택한 뒤 'Generate' 버튼을 통해 원하는 폴더에 다운로드 후 압축을 풀어서 사용한다.

  <img width="1280" alt="image" src="https://user-images.githubusercontent.com/66625672/161768847-c383dccd-055d-447e-9e3f-06d4243a2497.png">

---

### Intellij IDEA 실행
- 압축 파일을 다운로드한 위치에서 `git pull` 명령으로 본 프로젝트의 내용을 본인의 저장소에 반영한다.
  - Spring Initializr을 통해 생성한 Spring Boot의 파일과 GitHub의 파일이 충돌될 수 있음에 유의해야 한다.

- 프로젝트의 폴더를 Intellij IDEA를 통해 Open한다.
  - src/main/resources/application.properties 파일의 경우 .gitignore 되어 있으므로 [application.properties 설정](https://github.com/yeseong31/Study_SpringBoot_Project/wiki/application.properties-%ED%8C%8C%EC%9D%BC)을 참고하여 파일을 수정한다.
  - 프로젝트에 포함된 코드 중 일부는 **프로젝트를 실행해야만 동작하는 경우**도 있으므로([Q도메인](https://github.com/yeseong31/Study_SpringBoot_Project/wiki/%EB%8F%99%EC%A0%81-%EC%BF%BC%EB%A6%AC-%EC%B2%98%EB%A6%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-Querydsl) 등) 설정이 완료되면 프로젝트를 한 번 실행해 본다.

---

### MariaDB 설정
- 본 프로젝트에서는 MariaDB라는 데이터베이스를 사용한다.
- [MariaDB Download](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.6.7&os=windows&cpu=x86_64&pkg=msi&m=yongbok)로 이동하여 DB 설치 후 HeidiSQL을 이용하여 데이터베이스에 접근하는 것으로 진행한다.

---

## 💾 DATABASES
[ERDCloud](https://www.erdcloud.com/d/pKAjCG9Pq5T3HzXDj)
