# Permit Radar — teste de saúde das cidades (2026-10-06)

Resumo por situação: address_only: 2, confirmed: 3, experimental: 1, login_required: 2, needs_adapter: 11, planning_only: 1, robots_blocked: 8, to_investigate: 9

| Cidade | Situação | Acesso | Páginas no ar | Plataforma detectada | Coleta de teste |
| --- | --- | --- | --- | --- | --- |
| Boston | confirmed | open_data_api | — | — | 346 permits |
| Cambridge | confirmed | open_data_api | — | — | 28 permits |
| Worcester | confirmed | open_data_api | — | — | 225 permits |
| Reading | experimental | file_report | 3/3 | CivicPlus, OpenGov/ViewpointCloud | 0 permits |
| Newton | robots_blocked | search_by_address_or_record | 1/2 | OpenGov/ViewpointCloud | — |
| Brookline | needs_adapter | search_by_address_or_record | 4/4 | Accela | — |
| North Reading | needs_adapter | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | — |
| Concord | needs_adapter | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | — |
| Mansfield | needs_adapter | search_by_address_or_record | 1/2 | PermitEyes | — |
| Pittsfield | needs_adapter | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | — |
| Great Barrington | needs_adapter | search_by_address_or_record | 3/4 | CivicPlus, PermitEyes | — |
| Danvers | address_only | address_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Sudbury | address_only | address_only | 3/3 | OpenGov/ViewpointCloud | — |
| Revere | login_required | login_required | 1/1 | — | — |
| Needham | login_required | login_required | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Northampton | planning_only | planning_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Watertown | robots_blocked | search_by_address_or_record | 4/4 | CivicPlus, OpenGov/ViewpointCloud | — |
| Hingham | needs_adapter | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | — |
| Attleboro | needs_adapter | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | — |
| Springfield | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| New Bedford | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Haverhill | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Quincy | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Gloucester | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lexington | robots_blocked | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lowell | to_investigate | search_by_address_or_record | 1/1 | CivicPlus | — |
| West Springfield | to_investigate | open_data_api | 1/1 | ArcGIS | — |
| Taunton | needs_adapter | search_by_address_or_record | 4/4 | Accela, CivicPlus, PermitEyes | — |
| Falmouth | needs_adapter | search_by_address_or_record | 4/4 | CivicPlus, PermitEyes | — |
| Stockbridge | needs_adapter | search_by_address_or_record | 3/4 | PermitEyes | — |
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

### Cambridge — confirmed
- Coleta de teste (14 dias): 28 permits. Exemplo: {'permit_number': '1192874', 'address': '16 Worcester St, Cambridge, MA 02139', 'permit_type': 'Building: New Construction', 'category': 'New Construction', 'estimated_value': 1290000.0, 'contractor': 'SAM C ZOU', 'issue_date': '2026-09-25'}
- Mensagens da coleta de teste:
    [info] Boston: 650 permits de especialidade/administrativos ignorados (elétrico, hidráulico, gás, alarme, certificados...)

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
- Coleta de teste (14 dias): 0 permits. Exemplo: None
- Mensagens da coleta de teste:
    [info] Cambridge / New Construction: permit mais recente emitido em: [{'latest': '2026-09-25T00:00:00.000'}]
    [info] Cambridge / New Construction: 3 registros recentes encontrados
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

### North Reading — needs_adapter
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.northreadingma.gov/210/Project-Updates → HTTP 200 · título: Project Updates | North Reading, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/northreading/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/northreading/controller/getvalues_controller.php | https://www.northreadingma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
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
datatable.js:2: Wrapper/Helper Class for datagrid based on jQuery Datatable Plugin
datatable.js:4: var Datatable = function() {
datatable.js:7: var dataTable; // datatable object
datatable.js:12: var ajaxParams = {}; // set filter mode
datatable.js:17: var text = tableOptions.dataTable.language.metronicGroupActions;
datatable.js:30: if (!$().dataTable) {
datatable.js:43: dataTable: {
datatable.js:44: "dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r><'table-responsive't><'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>", // datatable layout
datatable.js:49: "metronicAjaxRequestGeneralError": "Could not complete request. Please check your internet connection",
datatable.js:76: "serverSide": true, // enable/disable server side ajax loading
datatable.js:78: "ajax": { // define ajax settings
datatable.js:79: "url": "", // ajax URL
datatable.js:83: $.each(ajaxParams, function(key, value) {
datatable.js:132: message: tableOptions.dataTable.language.metronicAjaxRequestGeneralError,
datatable.js:149: // callback for ajax data load
datatable.js:163: // apply the special class that used to restyle the default datatable
datatable.js:164: var tmp = $.fn.dataTableExt.oStdClasses;
datatable.js:166: $.fn.dataTableExt.oStdClasses.sWrapper = $.fn.dataTableExt.oStdClasses.sWrapper + " dataTables_extended_wrapper";
datatable.js:167: $.fn.dataTableExt.oStdClasses.sFilterInput = "form-control input-xs input-sm input-inline";
datatable.js:168: $.fn.dataTableExt.oStdClasses.sLengthSelect = "form-control input-xs input-sm input-inline";
datatable.js:170: // initialize a datatable
datatable.js:171: dataTable = table.DataTable(options.dataTable);
datatable.js:174: $.fn.dataTableExt.oStdClasses.sWrapper = tmp.sWrapper;
datatable.js:175: $.fn.dataTableExt.oStdClasses.sFilterInput = tmp.sFilterInput;
datatable.js:176: $.fn.dataTableExt.oStdClasses.sLengthSelect = tmp.sLengthSelect;
datatable.js:179: tableWrapper = table.parents('.dataTables_wrapper');
datatable.js:216: the.setAjaxParam("action", tableOptions.filterApplyAction);
datatable.js:220: the.setAjaxParam($(this).attr("name"), $(this).val());
datatable.js:225: the.addAjaxParam($(this).attr("name"), $(this).val());
datatable.js:230: the.setAjaxParam($(this).attr("name"), $(this).val());
datatable.js:233: dataTable.ajax.reload();
datatable.js:243: the.clearAjaxParams();
datatable.js:244: the.addAjaxParam("action", tableOptions.filterCancelAction);
datatable.js:245: dataTable.ajax.reload();
datatable.js:261: setAjaxParam: function(name, value) {
datatable.js:262: ajaxParams[name] = value;
datatable.js:265: addAjaxParam: function(name, value) {
datatable.js:266: if (!ajaxParams[name]) {
datatable.js:267: ajaxParams[name] = [];
datatable.js:271: for (var i = 0; i < (ajaxParams[name]).length; i++) { // check for duplicates
POST https://permiteyes.us/northreading/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 :: 
GET https://permiteyes.us/northreading/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 :: 
```

### Concord — needs_adapter
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.concordma.gov/589/Building-Permit-Information → HTTP 200 · título: Building Permit Information&#160; &#160; --&#160; &#160; (Scroll down for Public View) | C · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/concord/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/concord/loginuser.php | https://permiteyes.us/concord/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/concord/controller/getvalues_controller.php | https://www.concordma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/concord/controller/userregistration_controller.php

### Mansfield — needs_adapter
- https://permiteyes.us/mansfield/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.mansfieldma.com/156/Building-Department → HTTP 403 · título: Just a moment... · robots.txt: n/d
- Endereços de dados candidatos: https://permiteyes.us/mansfield/controller/getvalues_controller.php

### Pittsfield — needs_adapter
- https://permiteyes.us/berkshire/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.pittsfieldma.gov/226/Public-View---Permit-Records → HTTP 200 · título: Public View - Permit Records | Pittsfield, MA · plataforma: PermitEyes, CivicPlus · robots.txt: NÃO permitido
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css | https://permiteyes.us/berkshire/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php | https://permiteyes.us/berkshire/publicviewmodal.php | https://residentagent-api-production.azurewebsites.net | https://www.pittsfieldma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=

### Great Barrington — needs_adapter
- https://permiteyes.us/berkshire/greatbarringtonpublicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://greatbarringtonma.civicpluswebopen.com/building-department/pages/online-permitting → HTTP 403 · título: Just a moment... · plataforma: CivicPlus · robots.txt: n/d
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php

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

### Hingham — needs_adapter
- https://permiteyes.us/hingham/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.hingham-ma.gov/577/View → HTTP 200 · título: View | Hingham, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- http://www.permiteyes.net/hingham/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: http://www.permiteyes.net/hingham/building/homepage.asp
- Endereços de dados candidatos: https://permiteyes.us/hingham/publicattachments.php?application_id= | https://permiteyes.us/hingham/controller/getvalues_controller.php | https://permiteyes.us/hingham/ajax/getbuildingpublichome.php | https://www.hingham-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback=
- Sondagem do PermitEyes em https://permiteyes.us/hingham/publicview.php:
```
script-inline-3:9: // } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-3:55: var tableHome = $(tableId).DataTable({
script-inline-3:68: "serverSide":true,
script-inline-3:94: "ajax": {
script-inline-3:132: //DATE RANGE ISSUE DATE
script-inline-3:135: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:220: $.ajax
script-inline-3:222: url:DeptName+"/"+$(this).data("permit-file")+"?application_id="+$(this).data("application-id")+"&permit_file="+$(this).parent().find(".view_app").data("permit-file")+"&permit_id=" + $(this).data("perm
script-inline-3:276: // $.ajax
script-inline-3:278: //    url:DeptName+"/"+Permitfile+"?application_id="+ApplicationId+"&permit_file="+$(this).parent().find(".view_app").data("permit-file"),
script-inline-3:371: var tableHome = $(tableId).DataTable({
script-inline-3:392: "serverSide":true,
script-inline-3:404: "ajax": {
script-inline-3:426: //DATE RANGE ISSUE DATE
script-inline-3:429: $('#BOHDisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:487: $.ajax
script-inline-3:489: url:DeptName+"/"+$(this).data("permit-file")+"?application_id="+$(this).data("application-id")+"&permit_file="+$(this).parent().find(".view_app").data("permit-file")+"&permit_id=" + $(this).data("perm
script-inline-3:805: $.ajax({
script-inline-3:807: url:"controller/getvalues_controller.php",
script-inline-3:890: $.ajax({
script-inline-3:891: url:"ajax/getbuildingpublichome.php",
script-inline-3:922: frameDoc.document.write('<thead><tr><th>Sq. No.</th><th>Ap. No.</th><th>Appl. Date</th><th>Issue Date</th><th>Site Address</th><th>Street No.</th><th>Street Name</th><th>Applicant</th><th>Owner</th><t
script-inline-3:953: var table = $('#BuildingPublicHome').DataTable();
script-inline-3:972: frameDoc.document.write('<thead><tr><th>Ap. No.</th><th>Appl. Date</th><th>Issue Date</th><th>Site Address</th><th>Street No.</th><th>Street Name</th><th>Applicant</th><th>Owner</th><th>Brief Descript
script-inline-3:1045: $.ajax({
script-inline-3:1046: url:"ajax/getbuildingpublichome.php",
script-inline-3:1060: table1 += '<thead><tr><th>Sq. No.</th><th>Ap. No.</th><th>Appl. Date</th><th>Issue Date</th><th>Site Address</th><th>Street No.</th><th>Street Name</th><th>Applicant</th><th>Owner</th><th>Brief Descri
script-inline-3:1118: $.ajax({
script-inline-3:1119: url:"ajax/getbuildingpublichome.php",
script-inline-3:1133: table1 += '<thead><tr><th>Sq. No.</th><th>Ap. No.</th><th>Appl. Date</th><th>Issue Date</th><th>Site Address</th><th>Street No.</th><th>Street Name</th><th>Applicant</th><th>Owner</th><th>Brief Descri
script-inline-3:1170: var table = $('#BuildingPublicHome').DataTable();
datatable.js:2: Wrapper/Helper Class for datagrid based on jQuery Datatable Plugin
datatable.js:4: var Datatable = function() {
datatable.js:7: var dataTable; // datatable object
datatable.js:12: var ajaxParams = {}; // set filter mode
datatable.js:17: var text = tableOptions.dataTable.language.metronicGroupActions;
datatable.js:30: if (!$().dataTable) {
datatable.js:43: dataTable: {
datatable.js:44: "dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r><'table-responsive't><'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>", // datatable layout
datatable.js:49: "metronicAjaxRequestGeneralError": "Could not complete request. Please check your internet connection",
datatable.js:76: "serverSide": true, // enable/disable server side ajax loading
datatable.js:78: "ajax": { // define ajax settings
datatable.js:79: "url": "", // ajax URL
datatable.js:83: $.each(ajaxParams, function(key, value) {
datatable.js:132: message: tableOptions.dataTable.language.metronicAjaxRequestGeneralError,
datatable.js:149: // callback for ajax data load
datatable.js:163: // apply the special class that used to restyle the default datatable
datatable.js:164: var tmp = $.fn.dataTableExt.oStdClasses;
datatable.js:166: $.fn.dataTableExt.oStdClasses.sWrapper = $.fn.dataTableExt.oStdClasses.sWrapper + " dataTables_extended_wrapper";
datatable.js:167: $.fn.dataTableExt.oStdClasses.sFilterInput = "form-control input-xs input-sm input-inline";
datatable.js:168: $.fn.dataTableExt.oStdClasses.sLengthSelect = "form-control input-xs input-sm input-inline";
datatable.js:170: // initialize a datatable
datatable.js:171: dataTable = table.DataTable(options.dataTable);
datatable.js:174: $.fn.dataTableExt.oStdClasses.sWrapper = tmp.sWrapper;
datatable.js:175: $.fn.dataTableExt.oStdClasses.sFilterInput = tmp.sFilterInput;
datatable.js:176: $.fn.dataTableExt.oStdClasses.sLengthSelect = tmp.sLengthSelect;
datatable.js:179: tableWrapper = table.parents('.dataTables_wrapper');
datatable.js:216: the.setAjaxParam("action", tableOptions.filterApplyAction);
datatable.js:220: the.setAjaxParam($(this).attr("name"), $(this).val());
datatable.js:225: the.addAjaxParam($(this).attr("name"), $(this).val());
datatable.js:230: the.setAjaxParam($(this).attr("name"), $(this).val());
datatable.js:233: dataTable.ajax.reload();
datatable.js:243: the.clearAjaxParams();
datatable.js:244: the.addAjaxParam("action", tableOptions.filterCancelAction);
datatable.js:245: dataTable.ajax.reload();
datatable.js:261: setAjaxParam: function(name, value) {
datatable.js:262: ajaxParams[name] = value;
datatable.js:265: addAjaxParam: function(name, value) {
datatable.js:266: if (!ajaxParams[name]) {
datatable.js:267: ajaxParams[name] = [];
datatable.js:271: for (var i = 0; i < (ajaxParams[name]).length; i++) { // check for duplicates
POST https://permiteyes.us/hingham/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 :: 
GET https://permiteyes.us/hingham/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 :: 
POST https://permiteyes.us/hingham/ajax/getbuildingpublichome.php -> HTTP 200 text/html; charset=UTF-8 :: {"data":[["<center><a class=\"app_data view_app\" data-permit-id=\"a404b5a6-1869-11e7-8252-00e04c500937\" data-permit-file=\"residentialview.php\" data-permit-editfile=\"residential.php\" data-application-id=\"4fa153f7-8bb2-11ed-a7ca-12716692ccab\" data-id=\"961\" data-folderpath=\"building\"><i class=\"fa fa-eye\" aria-hidden=\"true\" style=\"
GET https://permiteyes.us/hingham/ajax/getbuildingpublichome.php -> HTTP 200 text/html; charset=UTF-8 :: {"data":[["<center><a class=\"app_data view_app\" data-permit-id=\"a404b5a6-1869-11e7-8252-00e04c500937\" data-permit-file=\"residentialview.php\" data-permit-editfile=\"residential.php\" data-application-id=\"4fa153f7-8bb2-11ed-a7ca-12716692ccab\" data-id=\"961\" data-folderpath=\"building\"><i class=\"fa fa-eye\" aria-hidden=\"true\" style=\"
```

### Attleboro — needs_adapter
- https://permiteyes.us/attleboro/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.cityofattleboro.us/167/Building-Inspection → HTTP 200 · título: Building Inspection | Attleboro, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.net/Attleboro/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/attleboro/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.net/Attleboro/building/homepage.asp | https://permiteyes.us/attleboro/loginuser.php
- Endereços de dados candidatos: https://permiteyes.us/attleboro/publicattachments.php?application_id= | https://permiteyes.us/attleboro/controller/getvalues_controller.php | https://www.cityofattleboro.us/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/attleboro/controller/userregistration_controller.php

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

### Taunton — needs_adapter
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.taunton-ma.gov/169/Online-Building-Permits → HTTP 200 · título: Online Building Permits | Taunton, MA · plataforma: Accela, PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/taunton/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/taunton/loginuser.php | https://permiteyes.us/taunton/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/taunton/controller/getvalues_controller.php | https://permiteyes.us/taunton/ajax/getpublicview.php | https://www.taunton-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/taunton/controller/userregistration_controller.php
- Sondagem do PermitEyes em https://permiteyes.us/taunton/publicview.php:
```
script-inline-3:8: } else if (pageURL.indexOf("userapplication.php") > 0 || pageURL.indexOf("userindex.php") > 0 || pageURL.indexOf("publicview.php") > 0) {
script-inline-3:39: var tablePublicView = $('#PublicView').DataTable({
script-inline-3:59: "serverSide":true,
script-inline-3:74: "ajax": {
script-inline-3:75: "url":'ajax/getpublicview.php',
script-inline-3:81: $("#PublicView_wrapper").find('.pull-left').addClass('col-md-7');
script-inline-3:82: $("#PublicView_wrapper").find('.pull-left').prepend('<div class="col-md-8" >&nbsp;</div><div class="col-md-2" style="display:none;cursor:pointer;" id="BuildingHomePointer">  <i class="fa fa-arrows-alt
script-inline-3:91: tablePublicView
script-inline-3:97: //DATE RANGE ISSUE DATE
script-inline-3:100: $('#DisplaySelectedIssueDate').html(picker.startDate.format('DD-MM-YY') + ' To <br>' + picker.endDate.format('DD-MM-YY'));
script-inline-3:104: tablePublicView
script-inline-3:110: $('#searchPublicView input , select').on('keyup change', function(){
script-inline-3:113: tablePublicView
script-inline-3:135: $("#PublicView tbody").on('click','.view_app',function()
script-inline-3:147: tablePublicView.draw(false);
script-inline-3:148: tablePublicView.on( 'draw', function () {
script-inline-3:157: $.ajax
script-inline-3:159: url:DeptName+"/"+$(this).data("permit-file")+"?application_id="+$(this).data("application-id")+"&permit_file="+$(this).parent().find(".view_app").data("permit-file")+"&permit_id=" + $(this).data("perm
script-inline-3:182: $("#PublicView tbody").on('click','.view_permit',function()
script-inline-3:202: $("#PublicView tbody tr").removeClass("active-row");
script-inline-3:204: tablePublicView.draw(false);
script-inline-3:205: tablePublicView.on( 'draw', function () {
script-inline-3:241: $("#PublicView tbody").on('click','.view_Insp',function()
script-inline-3:266: $("#PublicView tbody tr").removeClass("active-row");
script-inline-3:269: tablePublicView.draw(false);
script-inline-3:270: tablePublicView.on( 'draw', function () {
script-inline-3:304: // $("#PublicViewPointer").on('click',function()
script-inline-3:306: //   $("#PublicViewPointer").css("display", "none");
script-inline-3:310: //    tablePublicView.draw(false);
script-inline-3:311: //    tablePublicView.on( 'draw', function () {
script-inline-3:318: $.ajax({
script-inline-3:320: url:"controller/getvalues_controller.php",
script-inline-3:375: $.ajax({
script-inline-3:376: url:"ajax/getpublicview.php",
script-inline-3:390: table1 += '<thead><tr><th>Sq. No.</th><th>Ap. No.</th><th>Appl. Date</th><th>Issue Date</th><th>Site Address</th><th>Owner</th><th>Contractor Name</th><th>Estimated Cost</th><th>Brief Description</th>
script-inline-3:426: var table = $('#PublicView').DataTable();
script-inline-3:429: $('.searchPublicView').hide();
script-inline-3:431: $('#PublicView').tableExport({
script-inline-3:439: $('#searchPublicView').show();
datatable.js:2: Wrapper/Helper Class for datagrid based on jQuery Datatable Plugin
datatable.js:4: var Datatable = function() {
datatable.js:7: var dataTable; // datatable object
datatable.js:12: var ajaxParams = {}; // set filter mode
datatable.js:17: var text = tableOptions.dataTable.language.metronicGroupActions;
datatable.js:30: if (!$().dataTable) {
datatable.js:43: dataTable: {
datatable.js:44: "dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r><'table-responsive't><'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>", // datatable layout
datatable.js:49: "metronicAjaxRequestGeneralError": "Could not complete request. Please check your internet connection",
datatable.js:76: "serverSide": true, // enable/disable server side ajax loading
datatable.js:78: "ajax": { // define ajax settings
datatable.js:79: "url": "", // ajax URL
datatable.js:83: $.each(ajaxParams, function(key, value) {
datatable.js:132: message: tableOptions.dataTable.language.metronicAjaxRequestGeneralError,
datatable.js:149: // callback for ajax data load
datatable.js:163: // apply the special class that used to restyle the default datatable
datatable.js:164: var tmp = $.fn.dataTableExt.oStdClasses;
datatable.js:166: $.fn.dataTableExt.oStdClasses.sWrapper = $.fn.dataTableExt.oStdClasses.sWrapper + " dataTables_extended_wrapper";
datatable.js:167: $.fn.dataTableExt.oStdClasses.sFilterInput = "form-control input-xs input-sm input-inline";
datatable.js:168: $.fn.dataTableExt.oStdClasses.sLengthSelect = "form-control input-xs input-sm input-inline";
datatable.js:170: // initialize a datatable
datatable.js:171: dataTable = table.DataTable(options.dataTable);
datatable.js:174: $.fn.dataTableExt.oStdClasses.sWrapper = tmp.sWrapper;
datatable.js:175: $.fn.dataTableExt.oStdClasses.sFilterInput = tmp.sFilterInput;
datatable.js:176: $.fn.dataTableExt.oStdClasses.sLengthSelect = tmp.sLengthSelect;
datatable.js:179: tableWrapper = table.parents('.dataTables_wrapper');
datatable.js:216: the.setAjaxParam("action", tableOptions.filterApplyAction);
datatable.js:220: the.setAjaxParam($(this).attr("name"), $(this).val());
datatable.js:225: the.addAjaxParam($(this).attr("name"), $(this).val());
datatable.js:230: the.setAjaxParam($(this).attr("name"), $(this).val());
datatable.js:233: dataTable.ajax.reload();
datatable.js:243: the.clearAjaxParams();
datatable.js:244: the.addAjaxParam("action", tableOptions.filterCancelAction);
datatable.js:245: dataTable.ajax.reload();
datatable.js:261: setAjaxParam: function(name, value) {
datatable.js:262: ajaxParams[name] = value;
datatable.js:265: addAjaxParam: function(name, value) {
datatable.js:266: if (!ajaxParams[name]) {
datatable.js:267: ajaxParams[name] = [];
datatable.js:271: for (var i = 0; i < (ajaxParams[name]).length; i++) { // check for duplicates
POST https://permiteyes.us/taunton/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 :: 
GET https://permiteyes.us/taunton/controller/getvalues_controller.php -> HTTP 200 text/html; charset=UTF-8 :: 
POST https://permiteyes.us/taunton/ajax/getpublicview.php -> HTTP 200 text/html; charset=UTF-8 :: {"data":[["<center><a class=\"app_data view_app\" data-permit-id=\"fd4480a3-1869-11e7-8252-00e04c500937\" data-permit-file=\"plumbingview.php\" data-permit-editfile=\"plumbing.php\" data-application-id=\"f6815732-61a6-11ec-9159-122947997c8e\" data-id=\"5990\" data-folderpath=\"building\"><i class=\"fa fa-eye\" aria-hidden=\"true\" style=\" font-
GET https://permiteyes.us/taunton/ajax/getpublicview.php -> HTTP 200 text/html; charset=UTF-8 :: {"data":[["<center><a class=\"app_data view_app\" data-permit-id=\"fd4480a3-1869-11e7-8252-00e04c500937\" data-permit-file=\"plumbingview.php\" data-permit-editfile=\"plumbing.php\" data-application-id=\"f6815732-61a6-11ec-9159-122947997c8e\" data-id=\"5990\" data-folderpath=\"building\"><i class=\"fa fa-eye\" aria-hidden=\"true\" style=\" font-
```

### Falmouth — needs_adapter
- https://permiteyes.us/falmouth/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.falmouthma.gov/313/Online-Permitting → HTTP 200 · título: Online Permitting | Falmouth, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/falmouth/userregistration.php → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/falmouth/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/falmouth/userregistration.php | https://permiteyes.us/falmouth/loginuser.php | https://permiteyes.us/falmouth/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/falmouth/publicattachments.php?application_id= | https://permiteyes.us/falmouth/controller/getvalues_controller.php | https://permiteyes.us/falmouth/ajax/getbuildingpublichome.php | https://www.falmouthma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/falmouth/controller/sitedetails_controller.php | https://permiteyes.us/falmouth/controller/userregistration_controller.php | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Email | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Username

### Stockbridge — needs_adapter
- https://permiteyes.us/berkshire/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.stockbridge-ma.gov/building-inspector/page/permiteyes-how → HTTP 403 · título: Just a moment... · plataforma: PermitEyes · robots.txt: n/d
- https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us//assets/global/plugins/font-awesome/css/font-awesome.min.css | https://permiteyes.us//assets/global/plugins/simple-line-icons/simple-line-icons.min.css | https://permiteyes.us//assets/global/plugins/bootstrap/css/bootstrap.css | https://permiteyes.us//assets/global/plugins/fullcalendar/fullcalendar.min.css | https://permiteyes.us//assets/global/plugins/fullcalendar/scheduler.min.css | https://permiteyes.us//assets/global/plugins/jquery-qtip-custom/jquery.qtip.min.css | https://permiteyes.us//assets/global/css/components-md.css | https://permiteyes.us//assets/global/css/plugins-md.css
- Endereços de dados candidatos: https://permiteyes.us/berkshire/controller/getvalues_controller.php | https://permiteyes.us/berkshire/publicviewmodal.php

### Arlington — to_investigate

### Weston — to_investigate

### Westford — to_investigate

### Milton — to_investigate

### Cohasset — to_investigate

### Holland — to_investigate

### Ludlow — to_investigate
