# Permit Radar — teste de saúde das cidades (2026-10-06)

Resumo por situação: address_only: 2, confirmed: 3, experimental: 11, login_required: 2, needs_adapter: 1, planning_only: 1, robots_blocked: 8, to_investigate: 9

| Cidade | Situação | Acesso | Páginas no ar | Plataforma detectada | Coleta de teste |
| --- | --- | --- | --- | --- | --- |
| Boston | confirmed | open_data_api | — | — | 346 permits |
| Cambridge | confirmed | open_data_api | — | — | 28 permits |
| Worcester | confirmed | open_data_api | — | — | 225 permits |
| Reading | experimental | file_report | 3/3 | CivicPlus, OpenGov/ViewpointCloud | 90 permits |
| Newton | robots_blocked | search_by_address_or_record | 1/2 | OpenGov/ViewpointCloud | — |
| Brookline | needs_adapter | search_by_address_or_record | 4/4 | Accela | — |
| North Reading | experimental | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | ERRO |
| Concord | experimental | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | ERRO |
| Mansfield | experimental | search_by_address_or_record | 1/2 | PermitEyes | ERRO |
| Pittsfield | experimental | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | ERRO |
| Great Barrington | experimental | search_by_address_or_record | 3/4 | CivicPlus, PermitEyes | ERRO |
| Danvers | address_only | address_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Sudbury | address_only | address_only | 3/3 | OpenGov/ViewpointCloud | — |
| Revere | login_required | login_required | 1/1 | — | — |
| Needham | login_required | login_required | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Northampton | planning_only | planning_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Watertown | robots_blocked | search_by_address_or_record | 4/4 | CivicPlus, OpenGov/ViewpointCloud | — |
| Hingham | experimental | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | 0 permits |
| Attleboro | experimental | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | ERRO |
| Springfield | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| New Bedford | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Haverhill | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Quincy | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Gloucester | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lexington | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lowell | to_investigate | search_by_address_or_record | 1/1 | CivicPlus | — |
| West Springfield | to_investigate | open_data_api | 1/1 | ArcGIS | — |
| Taunton | experimental | search_by_address_or_record | 4/4 | Accela, CivicPlus, PermitEyes | 0 permits |
| Falmouth | experimental | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | 0 permits |
| Stockbridge | experimental | search_by_address_or_record | 3/4 | PermitEyes | ERRO |
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
- Coleta de teste (14 dias): 28 permits. Exemplo: {'permit_number': '1192874', 'address': '16 Worcester St, Cambridge, MA 02139', 'permit_type': 'Building: New Construction', 'category': 'New Construction', 'estimated_value': 1290000.0, 'contractor': 'SAM C ZOU', 'issue_date': '2026-09-25'}
- Mensagens da coleta de teste:
    [info] Cambridge / New Construction: permit mais recente emitido em: [{'latest': '2026-09-25T00:00:00.000'}]
    [info] Cambridge / New Construction: 3 registros recentes encontrados
    [info] Cambridge / Addition/Alteration: permit mais recente emitido em: [{'latest': '2026-10-02T00:00:00.000'}]
    [info] Cambridge / Addition/Alteration: 25 registros recentes encontrados

### Worcester — confirmed
- Coleta de teste (14 dias): 225 permits. Exemplo: {'permit_number': 'B-26-4061', 'address': '577 Grove St Worcester MA 01605', 'permit_type': 'Building Permit (type not listed)', 'category': 'Unspecified', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-03'}
- Mensagens da coleta de teste:
    [info] Worcester: 25 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Worcester: permit mais recente emitido em: 2026-10-03

### Reading — experimental
- https://readingma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://www.readingma.gov/959/Monthly-Building-Permit-Report → HTTP 200 · título: Monthly Building Permit Report | Reading, MA · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: permitido
- https://readingma.viewpointcloud.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://readingma.viewpointcloud.com/
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places | https://readingma.viewpointcloud.com/ | https://www.readingma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste (14 dias): 90 permits. Exemplo: {'permit_number': 'B-26-696', 'address': '10 ARROW CIRCLE, Reading, MA 01867', 'permit_type': 'Re-roofing', 'category': 'Renovation', 'estimated_value': 13000.0, 'contractor': 'Michael Nugent', 'issue_date': '2026-09-17'}
- Mensagens da coleta de teste:
    [info] Reading: 2 arquivo(s) de relatório encontrado(s)
    [info] Reading: colunas do arquivo (WEBSITE-Building-Permits-Issued): ['record', 'record_type', 'document_title', 'type', 'full_address', 'owner_name', 'applicant_name', 'dba', 'applicant_phoneno', 'date_issued', 'permit_for', 'work_description', 'project_cost', 'total_paid', 'record_status']
    [info] Reading: 132 linhas em https://www.readingma.gov/DocumentCenter/View/24939/September---Building-Permits-Issued
    [info] Reading: colunas do arquivo (Building-Monthly-Report_2026_re): ['record', 'record_type', 'applicant_name', 'owner_name', 'full_address', 'applicant_email', 'date_submitted', 'permit_license_issued_date', 'project_cost_please_enter_a_whole_number_no_comma_or_decimals', 'total_paid', 'permit_for', 'work_description_please_provide_a_detailed_description_of_the_work_being_done', 'record_status']
    [info] Reading: 90 linhas em https://www.readingma.gov/DocumentCenter/View/24729/August-2026---Building-Permits-Issued
    [info] Reading: 105 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)

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

### North Reading — experimental
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.northreadingma.gov/210/Project-Updates → HTTP 200 · título: Project Updates | North Reading, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/northreading/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/northreading/controller/getvalues_controller.php | https://www.northreadingma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php', 'ajax/getbohpublichome.php', 'ajax/getplanningpublichome.php', 'ajax/getconcompublichome.php', 'ajax/getfirepublichome.php', 'ajax/getzbapublichome.php', 'ajax/getclerkpublichome.php', 'ajax/ge
- Sondagem do PermitEyes em https://permiteyes.us/northreading/publicview.php:
```
script-inline-3:37: //Start-Datatable JS
script-inline-3:41: var tableHome = $(tableId).DataTable({
script-inline-3:69: "serverSide":true,
script-inline-3:81: "ajax": {
script-inline-3:103: //DATE RANGE ISSUE DATE
script-inline-3:106: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:187: $.ajax
script-inline-3:189: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-3:220: var tableHome = $(tableId).DataTable({
script-inline-3:248: "serverSide":true,
script-inline-3:260: "ajax": {
script-inline-3:282: //DATE RANGE ISSUE DATE
script-inline-3:285: $('#BOHDisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:369: $.ajax
script-inline-3:371: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-3:403: var tableHome = $(tableId).DataTable({
script-inline-3:431: "serverSide":true,
script-inline-3:443: "ajax": {
script-inline-3:465: // //DATE RANGE ISSUE DATE
script-inline-3:468: //     $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:538: //     $.ajax
script-inline-3:540: //       url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-3:571: var tableHome = $(tableId).DataTable({
script-inline-3:599: "serverSide":true,
script-inline-3:611: "ajax": {
script-inline-3:633: // //DATE RANGE ISSUE DATE
script-inline-3:636: //     $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:705: //     $.ajax
script-inline-3:707: //       url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-3:739: var tableHome = $(tableId).DataTable({
script-inline-3:767: "serverSide":true,
script-inline-3:779: "ajax": {
script-inline-3:801: //DATE RANGE ISSUE DATE
script-inline-3:804: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:874: $.ajax
script-inline-3:876: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-3:907: var tableHome = $(tableId).DataTable({
script-inline-3:935: "serverSide":true,
script-inline-3:947: "ajax": {
script-inline-3:969: // //DATE RANGE ISSUE DATE
POST https://permiteyes.us/northreading/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 (sem JSON) :: 
POST https://permiteyes.us/northreading/ajax/getpublicview.php -> HTTP 200 text/html; charset=UTF-8 (sem JSON) :: <html lang="en"> <head> <meta charset="utf-8" /> <title>Permiteyes</title> <meta http-equiv="X-UA-Compatible" content="IE=edg
POST https://permiteyes.us/northreading/ajax/getbuildingpublichome.php -> HTTP 500 text/html; charset=UTF-8 (sem JSON) :: 
```

### Concord — experimental
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.concordma.gov/589/Building-Permit-Information → HTTP 200 · título: Building Permit Information&#160; &#160; --&#160; &#160; (Scroll down for Public View) | C · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/concord/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/concord/loginuser.php | https://permiteyes.us/concord/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/concord/controller/getvalues_controller.php | https://www.concordma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/concord/controller/userregistration_controller.php
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php', 'ajax/getfirepublichome.php'])

### Mansfield — experimental
- https://permiteyes.us/mansfield/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.mansfieldma.com/156/Building-Department → HTTP 403 · título: Just a moment... · robots.txt: n/d
- Endereços de dados candidatos: https://permiteyes.us/mansfield/controller/getvalues_controller.php
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php'])

### Pittsfield — experimental
- https://permiteyes.us/berkshire/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.pittsfieldma.gov/226/Public-View---Permit-Records → HTTP 200 · título: Public View - Permit Records | Pittsfield, MA · plataforma: PermitEyes, CivicPlus · robots.txt: NÃO permitido
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css | https://permiteyes.us/berkshire/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php | https://permiteyes.us/berkshire/publicviewmodal.php | https://residentagent-api-production.azurewebsites.net | https://www.pittsfieldma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php', 'ajax/getpublichome.php'])
- Sondagem do PermitEyes em https://permiteyes.us/berkshire/publicview.php:
```
script-inline-2:10: url: null,
script-inline-2:23: url: url,
script-inline-2:73: * @returns {object} an object with the parsed url with the following structure {url: URL, params:{ KEY: VALUE }}
script-inline-2:79: url: url,
script-inline-2:95: url: url,
script-inline-4:23: else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-4:52: if ( $.fn.DataTable.isDataTable(tableId) ) {
script-inline-4:53: $(tableId).DataTable().destroy();
script-inline-4:55: //Start-Datatable JS
script-inline-4:59: var tableHome = $(tableId).DataTable({
script-inline-4:89: "serverSide":true,
script-inline-4:101: "ajax": {
script-inline-4:126: //DATE RANGE ISSUE DATE
script-inline-4:129: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:224: $.ajax
script-inline-4:226: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:305: $.ajax
script-inline-4:307: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:486: var tableHome = $(tableId).DataTable({
script-inline-4:514: "serverSide":true,
script-inline-4:526: "ajax": {
script-inline-4:548: //DATE RANGE ISSUE DATE
script-inline-4:551: $('#BOHDisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:619: $.ajax
script-inline-4:621: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:653: var tableHome = $(tableId).DataTable({
script-inline-4:681: "serverSide":true,
script-inline-4:693: "ajax": {
script-inline-4:715: // //DATE RANGE ISSUE DATE
script-inline-4:718: //     $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:770: //     $.ajax
script-inline-4:772: //       url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:803: var tableHome = $(tableId).DataTable({
script-inline-4:831: "serverSide":true,
script-inline-4:843: "ajax": {
script-inline-4:865: // //DATE RANGE ISSUE DATE
script-inline-4:868: //     $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:920: //     $.ajax
script-inline-4:922: //       url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:954: var tableHome = $(tableId).DataTable({
script-inline-4:982: "serverSide":true,
script-inline-4:994: "ajax": {
script-inline-4:1016: //DATE RANGE ISSUE DATE
script-inline-4:1019: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:1072: $.ajax
POST https://permiteyes.us/berkshire/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 (sem JSON) :: 
POST https://permiteyes.us/berkshire/ajax/getpublicview.php -> HTTP 404 text/html; charset=iso-8859-1 (sem JSON) :: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> <html><head> <title>404 Not Found</title> </head><body> <h1
POST https://permiteyes.us/berkshire/ajax/getbuildingpublichome.php -> HTTP 404 text/html; charset=iso-8859-1 (sem JSON) :: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> <html><head> <title>404 Not Found</title> </head><body> <h1
```

### Great Barrington — experimental
- https://permiteyes.us/berkshire/greatbarringtonpublicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://greatbarringtonma.civicpluswebopen.com/building-department/pages/online-permitting → HTTP 403 · título: Just a moment... · plataforma: CivicPlus · robots.txt: n/d
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php', 'ajax/getgreatbarringtonpublichome.php'])
- Sondagem do PermitEyes em https://permiteyes.us/berkshire/greatbarringtonpublicview.php:
```
script-inline-2:10: url: null,
script-inline-2:23: url: url,
script-inline-2:73: * @returns {object} an object with the parsed url with the following structure {url: URL, params:{ KEY: VALUE }}
script-inline-2:79: url: url,
script-inline-2:95: url: url,
script-inline-4:23: else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-4:51: if ( $.fn.DataTable.isDataTable(tableId) ) {
script-inline-4:52: $(tableId).DataTable().destroy();
script-inline-4:54: //Start-Datatable JS
script-inline-4:58: var tableHome = $(tableId).DataTable({
script-inline-4:88: "serverSide":true,
script-inline-4:100: "ajax": {
script-inline-4:125: //DATE RANGE ISSUE DATE
script-inline-4:128: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:195: $.ajax
script-inline-4:197: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:276: $.ajax
script-inline-4:278: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:457: var tableHome = $(tableId).DataTable({
script-inline-4:485: "serverSide":true,
script-inline-4:497: "ajax": {
script-inline-4:519: //DATE RANGE ISSUE DATE
script-inline-4:522: $('#BOHDisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:590: $.ajax
script-inline-4:592: url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:624: var tableHome = $(tableId).DataTable({
script-inline-4:652: "serverSide":true,
script-inline-4:664: "ajax": {
script-inline-4:686: // //DATE RANGE ISSUE DATE
script-inline-4:689: //     $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:741: //     $.ajax
script-inline-4:743: //       url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:774: var tableHome = $(tableId).DataTable({
script-inline-4:802: "serverSide":true,
script-inline-4:814: "ajax": {
script-inline-4:836: // //DATE RANGE ISSUE DATE
script-inline-4:839: //     $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:891: //     $.ajax
script-inline-4:893: //       url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-4:925: var tableHome = $(tableId).DataTable({
script-inline-4:953: "serverSide":true,
script-inline-4:965: "ajax": {
script-inline-4:987: //DATE RANGE ISSUE DATE
script-inline-4:990: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-4:1043: $.ajax
POST https://permiteyes.us/berkshire/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 (sem JSON) :: 
POST https://permiteyes.us/berkshire/ajax/getpublicview.php -> HTTP 404 text/html; charset=iso-8859-1 (sem JSON) :: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> <html><head> <title>404 Not Found</title> </head><body> <h1
POST https://permiteyes.us/berkshire/ajax/getbuildingpublichome.php -> HTTP 404 text/html; charset=iso-8859-1 (sem JSON) :: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> <html><head> <title>404 Not Found</title> </head><body> <h1
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

### Hingham — experimental
- https://permiteyes.us/hingham/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.hingham-ma.gov/577/View → HTTP 200 · título: View | Hingham, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- http://www.permiteyes.net/hingham/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: http://www.permiteyes.net/hingham/building/homepage.asp
- Endereços de dados candidatos: https://permiteyes.us/hingham/publicattachments.php?application_id= | https://permiteyes.us/hingham/controller/getvalues_controller.php | https://permiteyes.us/hingham/ajax/getbuildingpublichome.php | https://www.hingham-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Coleta de teste (14 dias): 0 permits. Exemplo: None
- Mensagens da coleta de teste:
    [info] Hingham: endereço de dados getbuildingpublichome.php; colunas: ['Application', 'Permit', 'Inspection', 'App.', 'Permit', 'COC', 'Insp.', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Parcel No.', 'Street No.', 'Street Name', 'Applicant', 'Owner', 'Brief Description', 'Appl. Type', 'Permit Number', 'Appl. Status', 'Att.']
    [info] Hingham: 55096 registros; data no início=2023-01-03, no fim=2026-10-06; mais novos no end
    [info] Hingham: exemplo de linha: {'ap_no': '961', 'appl_date': '01/03/23', 'issue_date': '01/03/23', 'street_no': '2', 'street_name': 'aberdeen road', 'applicant': 'user', 'owner': 'vaughn john t & alexandra m', 'appl_type': 'RESI.', 'permit_number': 'R-23-0075', 'appl_status': 'Closed', 'site_address': '2 aberdeen road'}
    [info] Hingham: 200 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)

### Attleboro — experimental
- https://permiteyes.us/attleboro/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.cityofattleboro.us/167/Building-Inspection → HTTP 200 · título: Building Inspection | Attleboro, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.net/Attleboro/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/attleboro/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.net/Attleboro/building/homepage.asp | https://permiteyes.us/attleboro/loginuser.php
- Endereços de dados candidatos: https://permiteyes.us/attleboro/publicattachments.php?application_id= | https://permiteyes.us/attleboro/controller/getvalues_controller.php | https://www.cityofattleboro.us/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/attleboro/controller/userregistration_controller.php
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php', 'ajax/getpublichome.php'])

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

### Taunton — experimental
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.taunton-ma.gov/169/Online-Building-Permits → HTTP 200 · título: Online Building Permits | Taunton, MA · plataforma: Accela, PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/taunton/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/taunton/loginuser.php | https://permiteyes.us/taunton/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/taunton/controller/getvalues_controller.php | https://permiteyes.us/taunton/ajax/getpublicview.php | https://www.taunton-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/taunton/controller/userregistration_controller.php
- Coleta de teste (14 dias): 0 permits. Exemplo: None
- Mensagens da coleta de teste:
    [info] Taunton: endereço de dados getpublicview.php; colunas: ['App.', 'Permit', 'Insp.', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Site Address', 'Applicant', 'Owner', 'Contractor Name', 'Estimated Cost', 'Brief Description', 'Appl. Type', 'Permit Number', 'Appl. Status']
    [info] Taunton: 41191 registros; data no início=2021-12-20, no fim=2026-10-06; mais novos no end
    [info] Taunton: exemplo de linha: {'appl_date': '5990', 'issue_date': '12/20/21', 'site_address': '03/08/22', 'applicant': '141 oak street', 'owner': 'city of taunton', 'contractor_name': 'test', 'estimated_cost': '1000.00', 'brief_description': 'water heater replacement', 'appl_type': 'PLUMB.', 'permit_number': 'P-22-0001', 'appl_status': 'Closed'}
    [info] Taunton: 200 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)

### Falmouth — experimental
- https://permiteyes.us/falmouth/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.falmouthma.gov/313/Online-Permitting → HTTP 200 · título: Online Permitting | Falmouth, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/falmouth/userregistration.php → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/falmouth/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/falmouth/userregistration.php | https://permiteyes.us/falmouth/loginuser.php | https://permiteyes.us/falmouth/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/falmouth/publicattachments.php?application_id= | https://permiteyes.us/falmouth/controller/getvalues_controller.php | https://permiteyes.us/falmouth/ajax/getbuildingpublichome.php | https://www.falmouthma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/falmouth/controller/sitedetails_controller.php | https://permiteyes.us/falmouth/controller/userregistration_controller.php | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Email | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Username
- Coleta de teste (14 dias): 0 permits. Exemplo: None
- Mensagens da coleta de teste:
    [info] Falmouth: endereço de dados getbuildingpublichome.php; colunas: ['Application', 'Permit', 'Inspection', 'App.', 'Permit', 'COC', 'Insp.', 'Ap. No.', 'Appl. Date', 'Issue Date', 'Unit No.', 'Parcel No.', 'Street No.', 'Street Name', 'Applicant', 'Owner', 'Brief Description', 'Appl. Type', 'Permit Number', 'Appl. Status', 'Att.']
    [info] Falmouth: 218982 registros; data no início=2007-10-30, no fim=2026-10-06; mais novos no end
    [info] Falmouth: exemplo de linha: {'ap_no': '4857', 'appl_date': '10/30/07', 'parcel_no': '46 01 000 019', 'street_no': '4', 'street_name': 'shoreview ave', 'applicant': 'pratt trustee harold i', 'owner': 'pratt trustee harold i', 'appl_type': 'SFA', 'appl_status': 'CLOSED', 'site_address': '4 shoreview ave'}
    [info] Falmouth: 299 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)
    [info] Falmouth: data mais recente encontrada: 2026-09-18

### Stockbridge — experimental
- https://permiteyes.us/berkshire/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.stockbridge-ma.gov/building-inspector/page/permiteyes-how → HTTP 403 · título: Just a moment... · plataforma: PermitEyes · robots.txt: n/d
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php | https://permiteyes.us/berkshire/publicviewmodal.php
- Coleta de teste FALHOU: nenhum endereço de dados respondeu (tentados: ['ajax/getpublicview.php', 'ajax/getbuildingpublichome.php', 'ajax/getpublichome.php'])

### Arlington — to_investigate

### Weston — to_investigate

### Westford — to_investigate

### Milton — to_investigate

### Cohasset — to_investigate

### Holland — to_investigate

### Ludlow — to_investigate
