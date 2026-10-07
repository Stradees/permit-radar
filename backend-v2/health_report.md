# Permit Radar — teste de saúde das cidades (2026-10-07)

Resumo por situação: address_only: 2, confirmed: 9, experimental: 5, login_required: 2, needs_adapter: 1, planning_only: 1, robots_blocked: 8, to_investigate: 9

| Cidade | Situação | Acesso | Páginas no ar | Plataforma detectada | Coleta de teste |
| --- | --- | --- | --- | --- | --- |
| Boston | confirmed | open_data_api | — | — | 346 permits |
| Cambridge | confirmed | open_data_api | — | — | 26 permits |
| Worcester | confirmed | open_data_api | — | — | 195 permits |
| Reading | confirmed | file_report | 3/3 | CivicPlus, OpenGov/ViewpointCloud | 110 permits |
| Newton | robots_blocked | search_by_address_or_record | 1/2 | OpenGov/ViewpointCloud | — |
| Brookline | needs_adapter | search_by_address_or_record | 4/4 | Accela | — |
| North Reading | confirmed | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | 29 permits |
| Concord | experimental | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | 44 permits |
| Mansfield | experimental | search_by_address_or_record | 1/2 | PermitEyes | ERRO |
| Pittsfield | experimental | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | 68 permits |
| Great Barrington | experimental | search_by_address_or_record | 3/4 | CivicPlus, PermitEyes | 0 permits |
| Danvers | address_only | address_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Sudbury | address_only | address_only | 3/3 | OpenGov/ViewpointCloud | — |
| Revere | login_required | login_required | 1/1 | — | — |
| Needham | login_required | login_required | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Northampton | planning_only | planning_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Watertown | robots_blocked | search_by_address_or_record | 4/4 | CivicPlus, OpenGov/ViewpointCloud | — |
| Hingham | confirmed | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | 26 permits |
| Attleboro | confirmed | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | 75 permits |
| Springfield | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| New Bedford | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Haverhill | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Quincy | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Gloucester | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lexington | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lowell | to_investigate | search_by_address_or_record | 1/1 | CivicPlus | — |
| West Springfield | to_investigate | open_data_api | 1/1 | ArcGIS | — |
| Taunton | confirmed | search_by_address_or_record | 4/4 | Accela, CivicPlus, PermitEyes | 48 permits |
| Falmouth | confirmed | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | 73 permits |
| Stockbridge | experimental | search_by_address_or_record | 3/4 | PermitEyes | 10 permits |
| Arlington | to_investigate | search_by_address_or_record | — | — | — |
| Weston | to_investigate | search_by_address_or_record | — | — | — |
| Westford | to_investigate | search_by_address_or_record | — | — | — |
| Milton | to_investigate | search_by_address_or_record | — | — | — |
| Cohasset | to_investigate | file_report | — | — | — |
| Holland | to_investigate | file_report | — | — | — |
| Ludlow | to_investigate | file_report | — | — | — |

## Detalhes por cidade

### Boston — confirmed
- Coleta de teste (14 dias): 346 permits. Exemplo: {'permit_number': 'SF1904734', 'address': '75 Clarendon ST', 'permit_type': 'Short Form Bldg Permit', 'category': 'Renovation', 'estimated_value': 48500.0, 'contractor': 'Mohamad Habboub', 'issue_date': '2026-10-05'}
- Mensagens da coleta de teste:
    [info] Boston: 650 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)

### Cambridge — confirmed
- Coleta de teste (14 dias): 26 permits. Exemplo: {'permit_number': '1203958', 'address': '202 Garden St, Cambridge, MA 02138', 'permit_type': 'Building: New Construction', 'category': 'New Construction', 'estimated_value': 1898000.0, 'contractor': 'JEFFREY KEACH', 'issue_date': '2026-10-05'}
- Mensagens da coleta de teste:
    [info] Cambridge / New Construction: permit mais recente emitido em: [{'latest': '2026-10-05T00:00:00.000'}]
    [info] Cambridge / New Construction: 4 registros recentes encontrados
    [info] Cambridge / Addition/Alteration: permit mais recente emitido em: [{'latest': '2026-10-06T00:00:00.000'}]
    [info] Cambridge / Addition/Alteration: 22 registros recentes encontrados

### Worcester — confirmed
- Coleta de teste (14 dias): 195 permits. Exemplo: {'permit_number': 'B-26-4061', 'address': '577 Grove St Worcester MA 01605', 'permit_type': 'Building Permit (type not listed)', 'category': 'Unspecified', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-03'}
- Mensagens da coleta de teste:
    [info] Worcester: 25 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Worcester: permit mais recente emitido em: 2026-10-03

### Reading — confirmed
- https://readingma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://www.readingma.gov/959/Monthly-Building-Permit-Report → HTTP 200 · título: Monthly Building Permit Report | Reading, MA · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: permitido
- https://readingma.viewpointcloud.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://readingma.viewpointcloud.com/
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places | https://readingma.viewpointcloud.com/ | https://www.readingma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste (14 dias): 110 permits. Exemplo: {'permit_number': 'B-26-696', 'address': '10 ARROW CIRCLE, Reading, MA 01867', 'permit_type': 'Re-roofing', 'category': 'Renovation', 'estimated_value': 13000.0, 'contractor': 'Michael Nugent', 'issue_date': '2026-09-17'}
- Mensagens da coleta de teste:
    [info] Reading: 2 arquivo(s) de relatório encontrado(s)
    [info] Reading: colunas do arquivo (WEBSITE-Building-Permits-Issued): ['record', 'record_type', 'document_title', 'type', 'full_address', 'owner_name', 'applicant_name', 'dba', 'applicant_phoneno', 'date_issued', 'permit_for', 'work_description', 'project_cost', 'total_paid', 'record_status']
    [info] Reading: 132 linhas em https://www.readingma.gov/DocumentCenter/View/24939/September---Building-Permits-Issued
    [info] Reading: colunas do arquivo (Building-Monthly-Report_2026_re): ['record', 'record_type', 'applicant_name', 'owner_name', 'full_address', 'applicant_email', 'date_submitted', 'permit_license_issued_date', 'project_cost_please_enter_a_whole_number_no_comma_or_decimals', 'total_paid', 'permit_for', 'work_description_please_provide_a_detailed_description_of_the_work_being_done', 'record_status']
    [info] Reading: 90 linhas em https://www.readingma.gov/DocumentCenter/View/24729/August-2026---Building-Permits-Issued
    [info] Reading: 74 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)

### Newton — robots_blocked
- https://newtonma.viewpointcloud.com/search → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://www.newtonma.gov/government/inspectional-services → HTTP 403 · título: Access Denied · robots.txt: n/d
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Brookline — needs_adapter
- https://aca-prod.accela.com/BROOKLINE/Welcome.aspx?TabName=Home → HTTP 200 · título: Accela Citizen Access · plataforma: Accela · robots.txt: permitido
- https://brooklinema.teamdynamix.com/TDClient/101/Portal/KB/Article/17096/ACCELA-Searching-for-Records → HTTP 200 · título: Article - ACCELA: Searching for Records · plataforma: Accela · robots.txt: permitido
- https://api-prod.accela.com → HTTP 200 · plataforma: Accela · robots.txt: permitido
- https://aca-prod.accela.com/BROOKLINE/Accela-Favicon.svg → HTTP 200 · plataforma: Accela · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://api-prod.accela.com | https://aca-prod.accela.com/BROOKLINE/Accela-Favicon.svg | https://brookline-prod-av.accela.com | https://brooklinema.teamdynamix.com/TDClient/101/Portal/Login.aspx?ReturnUrl=%2fTDClient%2f101%2fPortal%2fKB%2fArticle%2f17096%2fACCELA-Searching-for-Records | https://brooklinema.teamdynamix.com/TDClient/101/Portal/KB/Search?SearchText=%2523Accela
- Endereços de dados candidatos: https://api-prod.accela.com/profile

### North Reading — confirmed
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.northreadingma.gov/210/Project-Updates → HTTP 200 · título: Project Updates | North Reading, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/northreading/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/northreading/controller/getvalues_controller.php | https://www.northreadingma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste (14 dias): 29 permits. Exemplo: {'permit_number': 'FND-26-0028', 'address': '12 gillis dr', 'permit_type': 'FND', 'category': 'Unspecified', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-06'}
- Mensagens da coleta de teste:
    [info] North Reading: endereço de dados getbuildingpublichome.php (pedido completo); colunas: ['Application', 'Permit', 'Inspection', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Site Address', 'Applicant', 'Owner', 'Appl. Type', 'Permit Number', 'Appl. Status', '']
    [info] North Reading: 13 cabeçalhos para 12 células; cabeçalhos sem dado: ['applicant']
    [info] North Reading: ordenação por Issue Date (decrescente) confirmada; mais novos no início
    [info] North Reading: exemplo de linha: {'ap_no': '1', 'appl_date': '08/20/19', 'issue_date': '08/20/19', 'site_address': '32 winter st', 'owner': 'soriya danny pen', 'appl_type': 'SHT MTL', 'permit_number': 'SH-19-0001', 'appl_status': 'Closed'}
    [info] North Reading: tipos nas 100 linhas lidas: [('ELECT.', 28), ('RESI.', 25), ('PLUMB.', 16), ('GAS', 12), ('MECH', 7), ('CI', 3), ('FND', 3), ('COMM.', 3), ('SHT MTL', 2), ('SHED', 1)]
    [info] North Reading: 69 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] North Reading: data mais recente encontrada: 2026-10-06
- Sondagem do PermitEyes em https://permiteyes.us/northreading/publicview.php:
```
script-inline-3:4: // if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapp
script-inline-3:9: // } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("buildingpublichome.php") > 0) {
script-inline-3:31: var url = $(e.target).data('url');
script-inline-3:34: var tableId = $(target).attr('id');
script-inline-3:35: tableId = '#'+tableId;
script-inline-3:81: "ajax": {
script-inline-3:82: "url": url,
script-inline-3:83: "type":'post'
script-inline-3:84: },
script-inline-3:85: "rowCallback": function( row, data, index ) {
script-inline-3:86: 
script-inline-3:87: }
script-inline-3:88: });
script-inline-3:89: 
script-inline-3:90: //DATE RANGE APPL DATE
script-inline-3:168: var DeptName = $(this).data("folderpath");
script-inline-3:260: "ajax": {
script-inline-3:261: "url": url,
script-inline-3:262: "type":'post'
script-inline-3:263: },
script-inline-3:264: "rowCallback": function( row, data, index ) {
script-inline-3:265: 
script-inline-3:266: }
script-inline-3:267: });
script-inline-3:268: 
script-inline-3:269: //DATE RANGE APPL DATE
script-inline-3:350: var DeptName = $(this).data("folderpath");
script-inline-3:443: "ajax": {
script-inline-3:444: "url": url,
script-inline-3:445: "type":'post'
script-inline-3:446: },
script-inline-3:447: "rowCallback": function( row, data, index ) {
script-inline-3:448: 
script-inline-3:449: }
script-inline-3:450: });
script-inline-3:451: 
script-inline-3:452: //DATE RANGE APPL DATE
script-inline-3:519: //     var DeptName = $(this).data("folderpath");
script-inline-3:611: "ajax": {
script-inline-3:612: "url": url,
script-inline-3:613: "type":'post'
script-inline-3:614: },
script-inline-3:615: "rowCallback": function( row, data, index ) {
script-inline-3:616: 
script-inline-3:617: }
script-inline-3:618: });
script-inline-3:619: 
script-inline-3:620: //DATE RANGE APPL DATE
script-inline-3:686: //     var DeptName = $(this).data("folderpath");
script-inline-3:779: "ajax": {
script-inline-3:780: "url": url,
script-inline-3:781: "type":'post'
script-inline-3:782: },
script-inline-3:783: "rowCallback": function( row, data, index ) {
script-inline-3:784: 
script-inline-3:785: }
script-inline-3:786: });
script-inline-3:787: 
script-inline-3:788: //DATE RANGE APPL DATE
script-inline-3:855: var DeptName = $(this).data("folderpath");
```

### Concord — experimental
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.concordma.gov/589/Building-Permit-Information → HTTP 200 · título: Building Permit Information&#160; &#160; --&#160; &#160; (Scroll down for Public View) | C · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/concord/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/concord/loginuser.php | https://permiteyes.us/concord/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/concord/controller/getvalues_controller.php | https://www.concordma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/concord/controller/userregistration_controller.php
- Coleta de teste (14 dias): 44 permits. Exemplo: {'permit_number': 'R-26-0783', 'address': '243 heaths bridge rd', 'permit_type': 'RESI.', 'category': 'Renovation', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-07'}
- Mensagens da coleta de teste:
    [info] Concord: endereço de dados getbuildingpublichome.php (pedido completo); colunas: ['Application', 'Description of Work', 'Fees Paid', 'Permit', 'Inspection', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Site Address', 'Applicant', 'Owner', 'Appl. Type', 'Permit Number', 'Appl. Status', '']
    [info] Concord: 15 cabeçalhos para 12 células; cabeçalhos sem dado: ['application', 'applicant', 'col14']
    [info] Concord: ordenação por Issue Date (decrescente) confirmada; mais novos no início
    [info] Concord: exemplo de linha: {'description_of_work': 'replacement of a cook stov...', 'fees_paid': 'Fee: $60.00', 'ap_no': '37153', 'appl_date': '01/30/23', 'issue_date': '01/31/23', 'site_address': '363 main st', 'owner': 'ronald b pontes', 'appl_type': 'GAS', 'permit_number': 'G-23-0029', 'appl_status': 'Final Inspection'}
    [info] Concord: tipos nas 200 linhas lidas: [('ELECT.', 66), ('RESI.', 49), ('PLUMB.', 38), ('GAS', 23), ('COMM.', 11), ('SHT MTL', 9), ('TENT', 2), ('SIGN', 2)]
    [info] Concord: 140 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Concord: data mais recente encontrada: 2026-10-07
- Sondagem do PermitEyes em https://permiteyes.us/concord/publicview.php:
```
script-inline-3:4: // if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapp
script-inline-3:9: // } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("buildingpublichome.php") > 0) {
script-inline-3:31: var url = $(e.target).data('url');
script-inline-3:34: var tableId = $(target).attr('id');
script-inline-3:35: tableId = '#'+tableId;
script-inline-3:82: "ajax": {
script-inline-3:83: "url": url,
script-inline-3:84: "type":'post'
script-inline-3:85: },
script-inline-3:86: "rowCallback": function( row, data, index ) {
script-inline-3:87: // $(row).children().eq(0).removeAttr('style');
script-inline-3:88: // $(row).children().eq(0).css({'width' : '171 px;'});
script-inline-3:89: // $(".BriefDesc").removeAttr('style');
script-inline-3:90: // $(".BriefDesc").css({'width' : '171 px;'});
script-inline-3:91: },
script-inline-3:177: var DeptName = $(this).data("folderpath");
script-inline-3:269: "ajax": {
script-inline-3:270: "url": url,
script-inline-3:271: "type":'post'
script-inline-3:272: },
script-inline-3:273: "rowCallback": function( row, data, index ) {
script-inline-3:274: 
script-inline-3:275: }
script-inline-3:276: });
script-inline-3:277: 
script-inline-3:278: //DATE RANGE APPL DATE
script-inline-3:362: var DeptName = $(this).data("folderpath");
script-inline-3:455: "ajax": {
script-inline-3:456: "url": url,
script-inline-3:457: "type":'post'
script-inline-3:458: },
script-inline-3:459: "rowCallback": function( row, data, index ) {
script-inline-3:460: 
script-inline-3:461: }
script-inline-3:462: });
script-inline-3:463: 
script-inline-3:464: //DATE RANGE APPL DATE
script-inline-3:530: //     var DeptName = $(this).data("folderpath");
script-inline-3:622: "ajax": {
script-inline-3:623: "url": url,
script-inline-3:624: "type":'post'
script-inline-3:625: },
script-inline-3:626: "rowCallback": function( row, data, index ) {
script-inline-3:627: 
script-inline-3:628: }
script-inline-3:629: });
script-inline-3:630: 
script-inline-3:631: //DATE RANGE APPL DATE
script-inline-3:696: //     var DeptName = $(this).data("folderpath");
script-inline-3:792: "ajax": {
script-inline-3:793: "url": url,
script-inline-3:794: "type":'post'
script-inline-3:795: },
script-inline-3:796: "rowCallback": function( row, data, index ) {
script-inline-3:797: 
script-inline-3:798: }
script-inline-3:799: });
script-inline-3:800: 
script-inline-3:801: //DATE RANGE APPL DATE
script-inline-3:869: var DeptName = $(this).data("folderpath");
```

### Mansfield — experimental
- https://permiteyes.us/mansfield/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.mansfieldma.com/156/Building-Department → HTTP 403 · título: Just a moment... · robots.txt: n/d
- Endereços de dados candidatos: https://permiteyes.us/mansfield/controller/getvalues_controller.php
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (4 tentativas; veja as mensagens)
- Mensagens da coleta de teste:
    [info] Mansfield: tentativa ajax/getpublicview.php (simples) -> redirecionou para https://permiteyes.us/mansfield/login.php (exige sessão/login)
    [info] Mansfield: tentativa ajax/getpublicview.php (completo) -> redirecionou para https://permiteyes.us/mansfield/login.php (exige sessão/login)
    [info] Mansfield: tentativa ajax/getbuildingpublichome.php (simples) -> HTTP 500 :: 
    [info] Mansfield: tentativa ajax/getbuildingpublichome.php (completo) -> HTTP 500 :: 
- Sondagem do PermitEyes em https://permiteyes.us/mansfield/publicview.php:
```
script-inline-3:4: // if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapp
script-inline-3:9: // } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("buildingpublichome.php") > 0) {
script-inline-3:31: var url = $(e.target).data('url');
script-inline-3:34: var tableId = $(target).attr('id');
script-inline-3:35: tableId = '#'+tableId;
script-inline-3:82: "ajax": {
script-inline-3:83: "url": url,
script-inline-3:84: "type":'post'
script-inline-3:85: },
script-inline-3:86: "rowCallback": function( row, data, index ) {
script-inline-3:87: // $(row).children().eq(0).removeAttr('style');
script-inline-3:88: // $(row).children().eq(0).css({'width' : '171 px;'});
script-inline-3:89: // $(".BriefDesc").removeAttr('style');
script-inline-3:90: // $(".BriefDesc").css({'width' : '171 px;'});
script-inline-3:91: },
script-inline-3:142: var DeptName = $(this).data("folderpath");
script-inline-3:234: "ajax": {
script-inline-3:235: "url": url,
script-inline-3:236: "type":'post'
script-inline-3:237: },
script-inline-3:238: "rowCallback": function( row, data, index ) {
script-inline-3:239: 
script-inline-3:240: }
script-inline-3:241: });
script-inline-3:242: 
script-inline-3:243: //DATE RANGE APPL DATE
script-inline-3:308: var DeptName = $(this).data("folderpath");
script-inline-3:401: "ajax": {
script-inline-3:402: "url": url,
script-inline-3:403: "type":'post'
script-inline-3:404: },
script-inline-3:405: "rowCallback": function( row, data, index ) {
script-inline-3:406: 
script-inline-3:407: }
script-inline-3:408: });
script-inline-3:409: 
script-inline-3:410: //DATE RANGE APPL DATE
script-inline-3:459: //     var DeptName = $(this).data("folderpath");
script-inline-3:551: "ajax": {
script-inline-3:552: "url": url,
script-inline-3:553: "type":'post'
script-inline-3:554: },
script-inline-3:555: "rowCallback": function( row, data, index ) {
script-inline-3:556: 
script-inline-3:557: }
script-inline-3:558: });
script-inline-3:559: 
script-inline-3:560: //DATE RANGE APPL DATE
script-inline-3:609: //     var DeptName = $(this).data("folderpath");
script-inline-3:702: "ajax": {
script-inline-3:703: "url": url,
script-inline-3:704: "type":'post'
script-inline-3:705: },
script-inline-3:706: "rowCallback": function( row, data, index ) {
script-inline-3:707: 
script-inline-3:708: }
script-inline-3:709: });
script-inline-3:710: 
script-inline-3:711: //DATE RANGE APPL DATE
script-inline-3:761: var DeptName = $(this).data("folderpath");
```

### Pittsfield — experimental
- https://permiteyes.us/berkshire/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.pittsfieldma.gov/226/Public-View---Permit-Records → HTTP 200 · título: Public View - Permit Records | Pittsfield, MA · plataforma: PermitEyes, CivicPlus · robots.txt: NÃO permitido
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css | https://permiteyes.us/berkshire/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php | https://permiteyes.us/berkshire/publicviewmodal.php | https://residentagent-api-production.azurewebsites.net | https://www.pittsfieldma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste (14 dias): 68 permits. Exemplo: {'permit_number': 'C-26-0219', 'address': '5', 'permit_type': 'COMM', 'category': 'Renovation', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-06'}
- Mensagens da coleta de teste:
    [info] Pittsfield: abas de cidades encontradas: [('0fb1f327-10de-11ee-9520-00e04c68c964', '', 'ajax/getpublichome.php')]
    [info] Pittsfield: usando town_id=0fb1f327-10de-11ee-9520-00e04c68c964 ()
    [info] Pittsfield: endereço de dados getpublichome.php (pedido completo); colunas: ['Application', 'Permit', 'CO', 'COC', 'Inspection', 'Sign Off', 'Ap. No.', 'Parcel Id', 'Appl. Date', 'Issue Date', 'Street No', 'Street Name', 'Applicant', 'Owner', 'Appl. Type', 'Permit Number', 'Appl. Status', '']
    [info] Pittsfield: 18 cabeçalhos para 17 células; cabeçalhos sem dado: ['street_name']
    [info] Pittsfield: ordenação por Issue Date (decrescente) confirmada; mais novos no início
    [info] Pittsfield: exemplo de linha: {'ap_no': '24316', 'parcel_id': 'H060005116', 'appl_date': '10/17/17', 'issue_date': '01/17/18', 'street_no': '450', 'applicant': 'south st', 'owner': 'gable electric inc', 'appl_type': 'ELECT', 'permit_number': 'E-18-0042', 'appl_status': 'Permit Issued', 'site_address': '450'}
    [info] Pittsfield: tipos nas 300 linhas lidas: [('RESI', 99), ('ELECT', 78), ('GAS', 47), ('PLUMB', 33), ('COMM', 17), ('CI', 13), ('FENCE', 5), ('SIGN', 3), ('SHT MTL', 2), ('SFA', 2), ('TENT', 1)]
    [info] Pittsfield: 182 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Pittsfield: data mais recente encontrada: 2026-10-06
- Sondagem do PermitEyes em https://permiteyes.us/berkshire/publicview.php:
```
aba de cidade: <a class="tab-header" href="#buildingpublichometab"data-toggle="tab" data-url='ajax/getpublichome.php' data-town-id="0fb1f327-10de-11ee-9520-00e04c68c964"><img src="images/departments/BLDG_sm.gif" val
script-inline-2:42: url = url.split("#");
script-inline-2:44: url = url[0];
script-inline-2:48: url = obj.url;
script-inline-2:86: url = parts[0];
script-inline-2:154: $.redirect('./../gis/map.php', {'TownId': id});
script-inline-4:3: var CurrDeptName='';
script-inline-4:4: // if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapp
script-inline-4:9: // } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("buildingpublichome.php") > 0) {
script-inline-4:20: if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapplic
script-inline-4:23: else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-4:31: var SelectedTownId;
script-inline-4:44: var url = $(e.target).data('url');
script-inline-4:46: var SelectedTownId = $(e.target).data('town-id');
script-inline-4:47: // alert(SelectedTownId);
script-inline-4:49: var tableId = $(target).data('table-id');
script-inline-4:50: tableId = '#'+tableId;
script-inline-4:101: "ajax": {
script-inline-4:102: "url": url,
script-inline-4:103: "type":'post',
script-inline-4:104: "data": {
script-inline-4:105: "town_id": SelectedTownId
script-inline-4:106: }
script-inline-4:107: },
script-inline-4:108: "rowCallback": function( row, data, index ) {
script-inline-4:109: 
script-inline-4:110: }
script-inline-4:201: var DeptName = $(this).data("folderpath");
script-inline-4:206: var TownId = $(this).data("town-id");
script-inline-4:240: var loadUrl = DeptName+"/"+TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&per
script-inline-4:283: var DeptName = $(this).data("folderpath");
script-inline-4:288: var TownId = $(this).data("town-id");
script-inline-4:321: var loadUrl = DeptName+"/"+TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&per
script-inline-4:360: var DeptName = $(this).data("folderpath");
script-inline-4:432: var DeptName = $(this).data("folderpath");
script-inline-4:460: var loadUrl =TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&permit_editfile="
script-inline-4:526: "ajax": {
script-inline-4:527: "url": url,
script-inline-4:528: "type":'post'
script-inline-4:529: },
script-inline-4:530: "rowCallback": function( row, data, index ) {
script-inline-4:531: 
script-inline-4:532: }
script-inline-4:533: });
script-inline-4:534: 
script-inline-4:535: //DATE RANGE APPL DATE
script-inline-4:600: var DeptName = $(this).data("folderpath");
script-inline-4:693: "ajax": {
script-inline-4:694: "url": url,
script-inline-4:695: "type":'post'
script-inline-4:696: },
script-inline-4:697: "rowCallback": function( row, data, index ) {
script-inline-4:698: 
script-inline-4:699: }
script-inline-4:700: });
script-inline-4:701: 
script-inline-4:702: //DATE RANGE APPL DATE
script-inline-4:751: //     var DeptName = $(this).data("folderpath");
script-inline-4:843: "ajax": {
script-inline-4:844: "url": url,
```

### Great Barrington — experimental
- https://permiteyes.us/berkshire/greatbarringtonpublicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://greatbarringtonma.civicpluswebopen.com/building-department/pages/online-permitting → HTTP 403 · título: Just a moment... · plataforma: CivicPlus · robots.txt: n/d
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php
- Coleta de teste (14 dias): 0 permits. Exemplo: None
- Mensagens da coleta de teste:
    [info] Great Barrington: abas de cidades encontradas: [('6da083b6-26d9-11ee-9520-00e04c68c964', '', 'ajax/getgreatbarringtonpublichome.php')]
    [info] Great Barrington: usando town_id=6da083b6-26d9-11ee-9520-00e04c68c964 ()
    [info] Great Barrington: endereço de dados getgreatbarringtonpublichome.php (pedido completo); colunas: ['Application', 'Permit', 'CO', 'COC', 'Inspection', 'Sign Off', 'Ap. No.', 'Parcel Id', 'Appl. Date', 'Issue Date', 'Street No', 'Street Name', 'Applicant', 'Owner', 'Appl. Type', 'Permit Number', 'Appl. Status', '']
    [info] Great Barrington: 18 cabeçalhos para 17 células; cabeçalhos sem dado: ['permit_number']
    [info] Great Barrington: ordenação por Issue Date (decrescente) confirmada; mais novos no início
    [info] Great Barrington: exemplo de linha: {'ap_no': '143537', 'parcel_id': '1130150000000260', 'appl_date': '08/22/05', 'issue_date': '08/22/05', 'street_no': '8', 'street_name': 'locust st', 'applicant': 'callas peter j', 'owner': 'RESI', 'appl_type': '2005-00171', 'appl_status': 'Permit Issued', 'site_address': '8 locust st'}
    [info] Great Barrington: tipos nas 100 linhas lidas: [('G-26-0100', 1), ('G-26-0099', 1), ('P-26-0085', 1), ('G-26-0098', 1), ('P-26-0086', 1), ('E-26-0221', 1), ('P-26-0084', 1), ('P-26-0083', 1), ('E-26-0220', 1), ('E-26-0217', 1), ('R-26-0266', 1), ('P-26-0082', 1), ('R-26-0264', 1), ('R-26-0268', 1)]
    [info] Great Barrington: 100 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
- Sondagem do PermitEyes em https://permiteyes.us/berkshire/greatbarringtonpublicview.php:
```
aba de cidade: <a class="tab-header" href="#buildingpublichometab"data-toggle="tab" data-url='ajax/getgreatbarringtonpublichome.php' data-town-id="6da083b6-26d9-11ee-9520-00e04c68c964"><img src="images/departments/B
script-inline-2:42: url = url.split("#");
script-inline-2:44: url = url[0];
script-inline-2:48: url = obj.url;
script-inline-2:86: url = parts[0];
script-inline-2:154: $.redirect('./../gis/map.php', {'TownId': id});
script-inline-4:3: var CurrDeptName='';
script-inline-4:4: // if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapp
script-inline-4:9: // } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("buildingpublichome.php") > 0) {
script-inline-4:20: if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapplic
script-inline-4:23: else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-4:31: var SelectedTownId;
script-inline-4:43: var url = $(e.target).data('url');
script-inline-4:45: var SelectedTownId = $(e.target).data('town-id');
script-inline-4:46: // alert(SelectedTownId);
script-inline-4:48: var tableId = $(target).data('table-id');
script-inline-4:49: tableId = '#'+tableId;
script-inline-4:100: "ajax": {
script-inline-4:101: "url": url,
script-inline-4:102: "type":'post',
script-inline-4:103: "data": {
script-inline-4:104: "town_id": SelectedTownId
script-inline-4:105: }
script-inline-4:106: },
script-inline-4:107: "rowCallback": function( row, data, index ) {
script-inline-4:108: 
script-inline-4:109: }
script-inline-4:172: var DeptName = $(this).data("folderpath");
script-inline-4:177: var TownId = $(this).data("town-id");
script-inline-4:211: var loadUrl = DeptName+"/"+TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&per
script-inline-4:254: var DeptName = $(this).data("folderpath");
script-inline-4:259: var TownId = $(this).data("town-id");
script-inline-4:292: var loadUrl = DeptName+"/"+TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&per
script-inline-4:331: var DeptName = $(this).data("folderpath");
script-inline-4:403: var DeptName = $(this).data("folderpath");
script-inline-4:431: var loadUrl =TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&permit_editfile="
script-inline-4:497: "ajax": {
script-inline-4:498: "url": url,
script-inline-4:499: "type":'post'
script-inline-4:500: },
script-inline-4:501: "rowCallback": function( row, data, index ) {
script-inline-4:502: 
script-inline-4:503: }
script-inline-4:504: });
script-inline-4:505: 
script-inline-4:506: //DATE RANGE APPL DATE
script-inline-4:571: var DeptName = $(this).data("folderpath");
script-inline-4:664: "ajax": {
script-inline-4:665: "url": url,
script-inline-4:666: "type":'post'
script-inline-4:667: },
script-inline-4:668: "rowCallback": function( row, data, index ) {
script-inline-4:669: 
script-inline-4:670: }
script-inline-4:671: });
script-inline-4:672: 
script-inline-4:673: //DATE RANGE APPL DATE
script-inline-4:722: //     var DeptName = $(this).data("folderpath");
script-inline-4:814: "ajax": {
script-inline-4:815: "url": url,
```

### Danvers — address_only
- https://www.danversma.gov/651/View-Issued-Permits → HTTP 200 · título: View Issued Permits | Danvers, MA · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: NÃO permitido
- https://danversma.viewpointcloud.com/search → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://danversma.viewpointcloud.com/categories/1071 → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://danversma.viewpointcloud.com/search | https://danversma.viewpointcloud.com/categories/1071
- Endereços de dados candidatos: https://danversma.viewpointcloud.com/search | https://danversma.viewpointcloud.com/categories/1071 | https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Sudbury — address_only
- https://sudbury.ma.us/building/2020/08/26/search-building-department-permits-by-address/ → HTTP 200 · título: Search Building Department Permits By Address &raquo; Building Department · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://sudburyma.viewpointcloud.com/categories/1080 → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://sudburyma.portal.opengov.com/search → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://sudburyma.viewpointcloud.com/categories/1080 | https://sudburyma.portal.opengov.com/search
- Endereços de dados candidatos: https://api.w.org/ | https://sudburyma.viewpointcloud.com/categories/1080 | https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Revere — login_required
- https://www.revere.org/departments/building-division → HTTP 200 · título: Building Division - City of Revere, Massachusetts · robots.txt: permitido

### Needham — login_required
- https://www.needhamma.gov/227/Building → HTTP 200 · título: Building | Needham, MA · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: permitido
- https://needhamma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://needhamma.portal.opengov.com/search → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://needhamma.portal.opengov.com/ | https://needhamma.portal.opengov.com/search
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Northampton — planning_only
- https://northamptonma.gov/938/Permits-Codes → HTTP 200 · título: Permits, Code &amp; Regulations | Northampton, MA - Official Website · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: permitido
- https://northamptonma.portal.opengov.com/search → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://northamptonma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://northamptonma.portal.opengov.com/search | https://northamptonma.portal.opengov.com/ | https://northamptonma.portal.opengov.com/categories/1071/record-types/1006582
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Watertown — robots_blocked
- https://watertownma.viewpointcloud.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://www.watertown-ma.gov/code-enforcement-zoning-and-planning-search → HTTP 200 · título: Code enforcement, Zoning and Planning Search | Watertown, MA - Official Website · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: permitido
- https://watertownma.viewpointcloud.com/categories/1071 → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://watertownma.viewpointcloud.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://watertownma.viewpointcloud.com/categories/1071 | https://watertownma.viewpointcloud.com/ | https://watertownma.viewpointcloud.com/\\
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places | https://content.civicplus.com/api/assets/9a094458-af4c-4fcd-bc9b-3e8d34d23966?height=150 | https://content.civicplus.com/api/assets/7468d5ea-1026-4b52-b101-4a477b8be65f?height=150 | https://content.civicplus.com/api/assets/efcb4763-bfa7-48b8-b634-2a5c7b1cf114?width=180&amp;height=180&amp;mode=crop | https://content.civicplus.com/api/assets/efcb4763-bfa7-48b8-b634-2a5c7b1cf114?width=32&amp;height=32&amp;mode=crop | https://content.civicplus.com/api/assets/efcb4763-bfa7-48b8-b634-2a5c7b1cf114?width=16&amp;height=16&amp;mode=crop | https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&amp;family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&amp;display=fallback | https://content.civicplus.com/api/assets/e3e0dfb8-75ce-4bfe-8987-27b0ff4ea994?cache=1800&amp;width=300&amp;mode=min 300w,https://content.civicplus.com/api/assets/e3e0dfb8-75ce-4bfe-8987-27b0ff4ea994?cache=1800&amp;width=687&amp;mode=min 687w | https://content.civicplus.com/api/assets/e3e0dfb8-75ce-4bfe-8987-27b0ff4ea994?cache=1800 | https://watertownma.viewpointcloud.com/categories/1071 | https://watertownma.viewpointcloud.com/ | https://content.civicplus.com/api/assets/ma-watertown/{{id}}

### Hingham — confirmed
- https://permiteyes.us/hingham/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.hingham-ma.gov/577/View → HTTP 200 · título: View | Hingham, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- http://www.permiteyes.net/hingham/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: http://www.permiteyes.net/hingham/building/homepage.asp
- Endereços de dados candidatos: https://permiteyes.us/hingham/publicattachments.php?application_id= | https://permiteyes.us/hingham/controller/getvalues_controller.php | https://permiteyes.us/hingham/ajax/getbuildingpublichome.php | https://www.hingham-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste (14 dias): 26 permits. Exemplo: {'permit_number': 'R-26-0929', 'address': '27 pioneer road', 'permit_type': 'RESI.', 'category': 'Renovation', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-09-23'}
- Mensagens da coleta de teste:
    [info] Hingham: endereço de dados getbuildingpublichome.php (pedido simples); colunas: ['Application', 'Permit', 'Inspection', 'App.', 'Permit', 'COC', 'Insp.', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Parcel No.', 'Street No.', 'Street Name', 'Applicant', 'Owner', 'Brief Description', 'Appl. Type', 'Permit Number', 'Appl. Status', 'Att.']
    [info] Hingham: 20 cabeçalhos para 17 células; cabeçalhos sem dado: ['application', 'inspection']
    [info] Hingham: 55101 registros; data no início=2023-01-03, no fim=2026-10-07; mais novos no end
    [info] Hingham: exemplo de linha: {'ap_no': '961', 'appl_date': '01/03/23', 'issue_date': '01/03/23', 'street_no': '2', 'street_name': 'aberdeen road', 'applicant': 'user', 'owner': 'vaughn john t & alexandra m', 'appl_type': 'RESI.', 'permit_number': 'R-23-0075', 'appl_status': 'Closed', 'site_address': '2 aberdeen road'}
    [info] Hingham: tipos nas 100 linhas lidas: [('ELECT.', 29), ('RESI.', 19), ('PLUMB.', 19), ('GAS', 18), ('COMM.', 8), ('SHTMTL', 6), ('Sprinkler', 1)]
    [info] Hingham: 73 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Hingham: data mais recente encontrada: 2026-10-07

### Attleboro — confirmed
- https://permiteyes.us/attleboro/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.cityofattleboro.us/167/Building-Inspection → HTTP 200 · título: Building Inspection | Attleboro, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.net/Attleboro/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/attleboro/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.net/Attleboro/building/homepage.asp | https://permiteyes.us/attleboro/loginuser.php
- Endereços de dados candidatos: https://permiteyes.us/attleboro/publicattachments.php?application_id= | https://permiteyes.us/attleboro/controller/getvalues_controller.php | https://www.cityofattleboro.us/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/attleboro/controller/userregistration_controller.php
- Coleta de teste (14 dias): 75 permits. Exemplo: {'permit_number': 'R-26-1657', 'address': '37 bambury ln', 'permit_type': 'RESI.', 'category': 'Renovation', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-07'}
- Mensagens da coleta de teste:
    [info] Attleboro: endereço de dados getpublichome.php (pedido completo); colunas: ['App.', 'Permit', 'COC', 'Insp.', 'Fee', 'Sign Off', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Site Address', 'Applicant', 'Owner', 'Appl. Type', 'Permit Number', 'Appl. Status', 'Att.']
    [info] Attleboro: ordenação por Issue Date (decrescente) confirmada; mais novos no início
    [info] Attleboro: exemplo de linha: {'ap_no': '1', 'appl_date': '08/01/17', 'issue_date': '08/01/17', 'site_address': '10 dewey ave', 'applicant': 'ronald menard', 'owner': 'menard ronald w and carol a', 'appl_type': 'RESI.', 'permit_number': 'R-17-0001', 'appl_status': 'PCO Issued'}
    [info] Attleboro: tipos nas 300 linhas lidas: [('RESI.', 92), ('ELECT.', 63), ('PLUMB.', 39), ('GAS', 28), ('CI', 16), ('MECH', 16), ('COMM.', 14), ('FENCE', 10), ('TRENCH', 9), ('SFA', 4), ('SHT MTL', 3), ('AGAS', 3), ('SIGN', 2), ('TENT', 1)]
    [info] Attleboro: 190 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Attleboro: data mais recente encontrada: 2026-10-07
- Sondagem do PermitEyes em https://permiteyes.us/attleboro/publicview.php:
```
script-inline-3:4: if (pageURL.indexOf("applications.php") > 0 || pageURL.indexOf("buildinghome.php") > 0 ||  pageURL.indexOf("deletedapplications.php") > 0 ||  pageURL.indexOf("printapplic
script-inline-3:9: } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-3:66: "ajax": {
script-inline-3:67: "url":'ajax/getpublichome.php',
script-inline-3:68: "type":'post'
script-inline-3:69: },
script-inline-3:70: 
script-inline-3:71: });
script-inline-3:72: 
script-inline-3:73: 
script-inline-3:74: $("#PublicHome_wrapper").find('.pull-left').addClass('col-md-7');
script-inline-3:75: $("#PublicHome_wrapper").find('.pull-left').prepend('<div class="col-md-8" >&nbsp;</div><div class="col-md-2" style="display:none;cursor:pointer;" id="BuildingHomePointer
script-inline-3:187: var DeptName = $(this).data("folderpath");
script-inline-3:242: var DeptName = $(this).data("folderpath");
script-inline-3:300: var DeptName = $(this).data("folderpath");
script-inline-3:357: var DeptName = $(this).data("folderpath");
script-inline-3:385: var loadUrl =TransFile+"?application_id="+ApplicationId+"&permit_id="+PermitId+"&data_id="+DataId+"&transname="+transnameid+"&permit_file="+Permitfile+"&permit_editfile="
script-inline-3:433: var DeptName = $(this).data("folderpath");
script-inline-3:437: var TransFile="publicinspection.php";
script-inline-3:500: url:"controller/getvalues_controller.php",
POST https://permiteyes.us/attleboro/controller/getvalues_controller.php -> HTTP 200 (sem JSON) texto da página: 
POST https://permiteyes.us/attleboro/ajax/getpublicview.php -> erro HTTPConnectionPool(host='34.236.239.89', port=80): Max retries exceeded with url: /attleboro/login.p
POST https://permiteyes.us/attleboro/ajax/getbuildingpublichome.php -> erro HTTPConnectionPool(host='34.236.239.89', port=80): Max retries exceeded with url: /attleboro/login.p
```

### Springfield — robots_blocked
- https://springfieldma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### New Bedford — robots_blocked
- https://newbedfordma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Haverhill — robots_blocked
- https://haverhillma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Quincy — robots_blocked
- https://quincyma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Gloucester — robots_blocked
- https://gloucesterma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Lexington — robots_blocked
- https://lexingtonma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Lowell — to_investigate
- https://www.lowellma.gov/1631/Online-Permitting → HTTP 200 · título: Online Permitting | Lowell, MA · plataforma: CivicPlus · robots.txt: permitido

### West Springfield — to_investigate
- https://opendata-westspringfield.hub.arcgis.com/ → HTTP 200 · título: West Springfield Open Data · plataforma: ArcGIS · robots.txt: permitido

### Taunton — confirmed
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.taunton-ma.gov/169/Online-Building-Permits → HTTP 200 · título: Online Building Permits | Taunton, MA · plataforma: Accela, PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/taunton/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/taunton/loginuser.php | https://permiteyes.us/taunton/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/taunton/controller/getvalues_controller.php | https://permiteyes.us/taunton/ajax/getpublicview.php | https://www.taunton-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/taunton/controller/userregistration_controller.php
- Coleta de teste (14 dias): 48 permits. Exemplo: {'permit_number': 'BP-2027-0508', 'address': '95 joanne drive', 'permit_type': 'RESI.', 'category': 'Renovation', 'estimated_value': 88775.0, 'contractor': 'joseph oliveira jr', 'issue_date': '2026-10-02'}
- Mensagens da coleta de teste:
    [info] Taunton: endereço de dados getpublicview.php (pedido simples); colunas: ['App.', 'Permit', 'Insp.', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Site Address', 'Applicant', 'Owner', 'Contractor Name', 'Estimated Cost', 'Brief Description', 'Appl. Type', 'Permit Number', 'Appl. Status']
    [info] Taunton: 15 cabeçalhos para 14 células; cabeçalhos sem dado: ['applicant']
    [info] Taunton: 41200 registros; data no início=2022-05-10, no fim=2026-10-07; mais novos no end
    [info] Taunton: exemplo de linha: {'ap_no': '5990', 'appl_date': '12/20/21', 'issue_date': '03/08/22', 'site_address': '141 oak street', 'owner': 'city of taunton', 'contractor_name': 'test', 'estimated_cost': '1000.00', 'brief_description': 'water heater replacement', 'appl_type': 'PLUMB.', 'permit_number': 'P-22-0001', 'appl_status': 'Closed'}
    [info] Taunton: tipos nas 200 linhas lidas: [('RESI.', 53), ('PLUMB.', 53), ('ELECT.', 46), ('GAS', 38), ('COMM.', 5), ('SHT MTL', 3), ('CO (Res)', 1), ('CO (Comm)', 1)]
    [info] Taunton: 142 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Taunton: data mais recente encontrada: 2026-10-07

### Falmouth — confirmed
- https://permiteyes.us/falmouth/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.falmouthma.gov/313/Online-Permitting → HTTP 200 · título: Online Permitting | Falmouth, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/falmouth/userregistration.php → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/falmouth/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/falmouth/userregistration.php | https://permiteyes.us/falmouth/loginuser.php | https://permiteyes.us/falmouth/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/falmouth/publicattachments.php?application_id= | https://permiteyes.us/falmouth/controller/getvalues_controller.php | https://permiteyes.us/falmouth/ajax/getbuildingpublichome.php | https://www.falmouthma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/falmouth/controller/sitedetails_controller.php | https://permiteyes.us/falmouth/controller/userregistration_controller.php | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Email | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Username
- Coleta de teste (14 dias): 73 permits. Exemplo: {'permit_number': 'R-26-2329', 'address': '6 teneycke hill rd', 'permit_type': 'RESI.', 'category': 'Renovation', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-02'}
- Mensagens da coleta de teste:
    [info] Falmouth: endereço de dados getbuildingpublichome.php (pedido simples); colunas: ['Application', 'Permit', 'Inspection', 'App.', 'Permit', 'COC', 'Insp.', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Unit No.', 'Parcel No.', 'Street No.', 'Street Name', 'Applicant', 'Owner', 'Brief Description', 'Appl. Type', 'Permit Number', 'Appl. Status', 'Att.']
    [info] Falmouth: 21 cabeçalhos para 18 células; cabeçalhos sem dado: ['application', 'inspection']
    [info] Falmouth: 218996 registros; data no início=2007-11-06, no fim=2026-10-07; mais novos no end
    [info] Falmouth: exemplo de linha: {'ap_no': '4857', 'appl_date': '10/30/07', 'parcel_no': '46 01 000 019', 'street_no': '4', 'street_name': 'shoreview ave', 'applicant': 'pratt trustee harold i', 'owner': 'pratt trustee harold i', 'appl_type': 'SFA', 'appl_status': 'CLOSED', 'site_address': '4 shoreview ave'}
    [info] Falmouth: tipos nas 300 linhas lidas: [('ELECT.', 88), ('GAS', 59), ('REP', 54), ('PLUMB.', 39), ('RESI.', 34), ('SHT MTL', 11), ('SIGN', 4), ('TENT', 4), ('FIREALARM', 1), ('COMM.', 1), ('CEP', 1), ('SFA', 1), ('COU', 1), ('ADU', 1)]
    [info] Falmouth: 221 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Falmouth: data mais recente encontrada: 2026-10-07

### Stockbridge — experimental
- https://permiteyes.us/berkshire/stockbridgepublicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.stockbridge-ma.gov/building-inspector/page/permiteyes-how → HTTP 403 · título: Just a moment... · plataforma: PermitEyes · robots.txt: n/d
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php
- Coleta de teste (14 dias): 10 permits. Exemplo: {'permit_number': 'R-26-0139', 'address': '14', 'permit_type': 'RESI', 'category': 'Renovation', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-05'}
- Mensagens da coleta de teste:
    [info] Stockbridge: abas de cidades encontradas: [('2c98fd5f-8460-11ee-bcdc-00e04c68c964', '', 'ajax/getstockbridgepublichome.php')]
    [info] Stockbridge: usando town_id=2c98fd5f-8460-11ee-bcdc-00e04c68c964 ()
    [info] Stockbridge: endereço de dados getstockbridgepublichome.php (pedido completo); colunas: ['Application', 'Permit', 'CO', 'COC', 'Inspection', 'Sign Off', 'Ap. No.', 'Parcel Id', 'Appl. Date', 'Issue Date', 'Street No', 'Street Name', 'Applicant', 'Owner', 'Appl. Type', 'Permit Number', 'Appl. Status', '']
    [info] Stockbridge: 18 cabeçalhos para 17 células; cabeçalhos sem dado: ['street_name']
    [info] Stockbridge: ordenação por Issue Date (decrescente) confirmada; mais novos no início
    [info] Stockbridge: exemplo de linha: {'ap_no': '203805', 'parcel_id': '107', 'appl_date': '09/25/15', 'issue_date': '09/30/15', 'street_no': '11', 'applicant': 'elm st', 'owner': 'allan mclain', 'appl_type': 'ELECT', 'permit_number': 'E-15-0001', 'appl_status': 'Permit Issued', 'site_address': '11'}
    [info] Stockbridge: tipos nas 100 linhas lidas: [('RESI', 24), ('ELECT', 22), ('GAS', 18), ('COMM', 11), ('CI', 10), ('PLUMB', 8), ('TENT', 3), ('Co (comm)', 1), ('SHT MTL', 1), ('TRENCH', 1), ('SFA', 1)]
    [info] Stockbridge: 64 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Stockbridge: data mais recente encontrada: 2026-10-05

### Arlington — to_investigate

### Weston — to_investigate

### Westford — to_investigate

### Milton — to_investigate

### Cohasset — to_investigate

### Holland — to_investigate

### Ludlow — to_investigate
