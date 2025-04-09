# Installation

```console
docker build -t andmete-kaart .
docker run -p 8000:8000 andmete-kaart:latest
```

Find JSONs available at:

http://127.0.0.1:8000/index.json

http://127.0.0.1:8000/YS001.json

# Lahenduse kirjeldus
Olen tutvunud näidetega ja spefikatsiooniga, ning otsustasin et kasutan Flask JSONide serveerimiseks ning Pandas XLSX parsimiseks. xlsx_parser.py teeb viimast, eemaldab NaN ja teisi ebavajalikke asju, ning pärast seda täidab "data" andmevälja. 

Juurutamiseks kasutasin Docker-it.