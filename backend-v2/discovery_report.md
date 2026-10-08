# Permit Radar — varredura de descoberta (2026-10-08)

## Resumo

| Estado | Cidades | PermitEyes | Validadas | OpenGov | Tyler | Novas no cadastro |
| --- | --- | --- | --- | --- | --- | --- |
| Massachusetts | 351 | 23 | 17 | 3 | 0 | 12 |
| New Hampshire | 235 | 6 | 4 | 0 | 0 | 3 |
| Rhode Island | 39 | 1 | 1 | 0 | 0 | 1 |
| Connecticut | 169 | 3 | 1 | 0 | 0 | 1 |

## Massachusetts

Cidades verificadas: 351 (fonte da lista: https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_gaz_cousubs_25.txt)

### PermitEyes (a coleta é permitida)

| Cidade | Endereço | Validação | Campos extras |
| --- | --- | --- | --- |
| Attleboro | https://permiteyes.us/attleboro/publicview.php | 79 permits em 14 dias | — |
| Bellingham | https://permiteyes.us/bellingham/publicview.php | 0 permits em 14 dias | — |
| Braintree | https://permiteyes.us/braintree/publicview.php | 67 permits em 14 dias | description |
| Chicopee | https://permiteyes.us/chicopee/publicview.php | 0 permits em 14 dias | — |
| Concord | https://permiteyes.us/concord/publicview.php | 42 permits em 14 dias | description |
| Easthampton | https://permiteyes.us/easthampton/publicview.php | 21 permits em 14 dias | description |
| Easton | https://permiteyes.us/easton/publicview.php | 0 permits em 14 dias | — |
| Fairhaven | https://permiteyes.us/fairhaven/publicview.php | 37 permits em 14 dias | — |
| Foxborough | https://permiteyes.us/foxborough/publicview.php | 39 permits em 14 dias | contractor, estimated_value |
| Hanson | https://permiteyes.us/hanson/publicview.php | 13 permits em 14 dias | description |
| Hingham | https://permiteyes.us/hingham/publicview.php | 22 permits em 14 dias | description |
| Hopedale | https://permiteyes.us/hopedale/publicview.php | 15 permits em 14 dias | — |
| Ipswich | https://permiteyes.us/ipswich/publicview.php | 27 permits em 14 dias | — |
| Lincoln | https://permiteyes.us/lincoln/publicview.php | 8 permits em 14 dias | — |
| Mansfield | https://permiteyes.us/mansfield/publicview.php | FALHOU: nenhum endereço de dados respondeu (4 tentativas; veja as mensagens) | |
| Mashpee | https://permiteyes.us/mashpee/publicview.php | 0 permits em 14 dias | — |
| Milton | https://permiteyes.us/milton/publicview.php | 64 permits em 14 dias | description |
| Otis | https://permiteyes.us/otis/publicview.php | 7 permits em 14 dias | description |
| Pittsfield | https://permiteyes.us/pittsfield/publicview.php | 0 permits em 14 dias | — |
| Rehoboth | https://permiteyes.us/rehoboth/publicview.php | 28 permits em 14 dias | — |
| Sandwich | https://permiteyes.us/sandwich/publicview.php | 52 permits em 14 dias | — |
| Taunton | https://permiteyes.us/taunton/publicview.php | 48 permits em 14 dias | contractor, description, estimated_value |
| West Bridgewater | https://permiteyes.us/westbridgewater/publicview.php | 16 permits em 14 dias | description |

### OpenGov / ViewpointCloud (existe, mas o robots.txt não permite coleta automática)

Adams (adamsma.portal.opengov.com), Florida (floridama.viewpointcloud.io), Ware (warema.viewpointcloud.io)

## New Hampshire

Cidades verificadas: 235 (fonte da lista: https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_gaz_cousubs_33.txt)

### PermitEyes (a coleta é permitida)

| Cidade | Endereço | Validação | Campos extras |
| --- | --- | --- | --- |
| Concord | https://permiteyes.us/concord/publicview.php | 42 permits em 14 dias | description |
| Easton | https://permiteyes.us/easton/publicview.php | 0 permits em 14 dias | — |
| Lincoln | https://permiteyes.us/lincoln/publicview.php | 8 permits em 14 dias | — |
| Milton | https://permiteyes.us/milton/publicview.php | 64 permits em 14 dias | description |
| Pittsfield | https://permiteyes.us/pittsfield/publicview.php | 0 permits em 14 dias | — |
| Sandwich | https://permiteyes.us/sandwich/publicview.php | 52 permits em 14 dias | — |

## Rhode Island

Cidades verificadas: 39 (fonte da lista: https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_gaz_cousubs_44.txt)

### PermitEyes (a coleta é permitida)

| Cidade | Endereço | Validação | Campos extras |
| --- | --- | --- | --- |
| Lincoln | https://permiteyes.us/lincoln/publicview.php | 8 permits em 14 dias | — |

## Connecticut

Cidades verificadas: 169 (fonte da lista: https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_gaz_cousubs_09.txt)

### PermitEyes (a coleta é permitida)

| Cidade | Endereço | Validação | Campos extras |
| --- | --- | --- | --- |
| East Hampton | https://permiteyes.us/easthampton/publicview.php | 21 permits em 14 dias | description |
| Easton | https://permiteyes.us/easton/publicview.php | 0 permits em 14 dias | — |
| Mansfield | https://permiteyes.us/mansfield/publicview.php | FALHOU: nenhum endereço de dados respondeu (4 tentativas; veja as mensagens) | |

## Endereços avaliados individualmente

| Item | HTTP | Observação |
| --- | --- | --- |
| Nashua NH - serviço da cidade (permits, MapServer) | 200 | {"currentVersion":10.81,"serviceDescription":"This service displays building permits for the last three years. |
| Dover NH - portal de permits | 200 | SelfService Public Site html, body, .esri-view { padding: 0; margin: 0; height: 100%; width: 100%; } /* When v |
| Concord NH - portal (Tyler CSS) | 200 | (function(w,d,s,l,i){w.GAMeasurementID='G-1ZKX01PB1R';w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime |
| Enfield CT - arquivo de permits mensais | 200 | (function(w,d,s,l,i){w.GAMeasurementID='G-MRL4PW2TCH';w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime |
| Milford CT - permits emitidos por mês | 404 | (function(w,d,s,l,i){w.GAMeasurementID='G-ZDBX92NQJW';w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime |
| Tolland CT - viewmypermitct | 200 | Regional Online Permit Center - Capitol Region Council of Governments CRCOG Regional Online Permit Center A Co |
| New Haven CT - portal | 403 | Access Denied Access Denied You don't have permission to access "http&#58;&#47;&#47;www&#46;newhavenct&#46;gov |
