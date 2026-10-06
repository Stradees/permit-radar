# Permit Radar — teste de saúde das cidades (2026-10-06)

Resumo por situação: address_only: 2, confirmed: 3, experimental: 1, login_required: 2, needs_adapter: 16, planning_only: 1, to_investigate: 12

| Cidade | Situação | Acesso | Páginas no ar | Plataforma detectada | Coleta de teste |
| --- | --- | --- | --- | --- | --- |
| Boston | confirmed | open_data_api | — | — | 346 permits |
| Cambridge | confirmed | open_data_api | — | — | 28 permits |
| Worcester | confirmed | open_data_api | — | — | 225 permits |
| Reading | experimental | file_report | 1/1 | OpenGov/ViewpointCloud | 0 permits |
| Newton | needs_adapter | search_by_address_or_record | 1/2 | OpenGov/ViewpointCloud | — |
| Brookline | needs_adapter | search_by_address_or_record | 4/4 | Accela | — |
| North Reading | needs_adapter | search_by_address_or_record | 2/2 | CivicPlus, PermitEyes | — |
| Concord | needs_adapter | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | — |
| Mansfield | needs_adapter | search_by_address_or_record | 0/1 | — | — |
| Pittsfield | needs_adapter | search_by_address_or_record | 2/2 | CivicPlus, PermitEyes | — |
| Great Barrington | needs_adapter | search_by_address_or_record | 3/4 | CivicPlus, PermitEyes | — |
| Danvers | address_only | address_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Sudbury | address_only | address_only | 3/3 | OpenGov/ViewpointCloud | — |
| Revere | login_required | login_required | 1/1 | — | — |
| Needham | login_required | login_required | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Northampton | planning_only | planning_only | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Watertown | to_investigate | search_by_address_or_record | 3/3 | CivicPlus, OpenGov/ViewpointCloud | — |
| Hingham | to_investigate | search_by_address_or_record | 2/2 | CivicPlus, PermitEyes | — |
| Attleboro | to_investigate | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | — |
| Springfield | needs_adapter | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| New Bedford | needs_adapter | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Haverhill | needs_adapter | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Quincy | needs_adapter | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Gloucester | needs_adapter | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lexington | needs_adapter | search_by_address_or_record | 1/1 | OpenGov/ViewpointCloud | — |
| Lowell | to_investigate | search_by_address_or_record | 1/1 | CivicPlus | — |
| West Springfield | to_investigate | open_data_api | 1/1 | ArcGIS | — |
| Taunton | needs_adapter | search_by_address_or_record | 4/4 | Accela, CivicPlus, PermitEyes | — |
| Falmouth | needs_adapter | search_by_address_or_record | 3/3 | CivicPlus, PermitEyes | — |
| Stockbridge | needs_adapter | search_by_address_or_record | 0/1 | PermitEyes | — |
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

### Worcester — confirmed
- Coleta de teste (14 dias): 225 permits. Exemplo: {'permit_number': 'B-26-4061', 'address': '577 Grove St Worcester MA 01605', 'permit_type': 'Building Permit (type not listed)', 'category': 'Unspecified', 'estimated_value': None, 'contractor': None, 'issue_date': '2026-10-03'}

### Reading — experimental
- https://readingma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places
- Coleta de teste (14 dias): 0 permits. Exemplo: None

### Newton — needs_adapter
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
- https://www.northreadingma.gov/210/Project-Updates → HTTP 200 · título: Project Updates | North Reading, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/northreading/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/northreading/publicview.php
- Endereços de dados candidatos: https://www.northreadingma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/northreading/controller/getvalues_controller.php

### Concord — needs_adapter
- https://www.concordma.gov/589/Building-Permit-Information → HTTP 200 · título: Building Permit Information&#160; &#160; --&#160; &#160; (Scroll down for Public View) | C · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/concord/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/concord/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/concord/loginuser.php | https://permiteyes.us/concord/publicview.php
- Endereços de dados candidatos: https://www.concordma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/concord/controller/userregistration_controller.php | https://permiteyes.us/concord/controller/getvalues_controller.php

### Mansfield — needs_adapter
- https://www.mansfieldma.com/156/Building-Department → HTTP 403 · título: Just a moment... · robots.txt: n/d

### Pittsfield — needs_adapter
- https://www.pittsfieldma.gov/226/Public-View---Permit-Records → HTTP 200 · título: Public View - Permit Records | Pittsfield, MA · plataforma: PermitEyes, CivicPlus · robots.txt: NÃO permitido
- https://permiteyes.us/berkshire/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/berkshire/publicview.php
- Endereços de dados candidatos: https://residentagent-api-production.azurewebsites.net | https://www.pittsfieldma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/berkshire/controller/getvalues_controller.php | https://permiteyes.us/berkshire/publicviewmodal.php

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

### Watertown — to_investigate
- https://www.watertown-ma.gov/code-enforcement-zoning-and-planning-search → HTTP 200 · título: Code enforcement, Zoning and Planning Search | Watertown, MA - Official Website · plataforma: OpenGov/ViewpointCloud, CivicPlus · robots.txt: permitido
- https://watertownma.viewpointcloud.com/categories/1071 → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- https://watertownma.viewpointcloud.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Portais encontrados na página da prefeitura: https://watertownma.viewpointcloud.com/categories/1071 | https://watertownma.viewpointcloud.com/ | https://watertownma.viewpointcloud.com/\\
- Endereços de dados candidatos: https://content.civicplus.com/api/assets/9a094458-af4c-4fcd-bc9b-3e8d34d23966?height=150 | https://content.civicplus.com/api/assets/7468d5ea-1026-4b52-b101-4a477b8be65f?height=150 | https://content.civicplus.com/api/assets/efcb4763-bfa7-48b8-b634-2a5c7b1cf114?width=180&amp;height=180&amp;mode=crop | https://content.civicplus.com/api/assets/efcb4763-bfa7-48b8-b634-2a5c7b1cf114?width=32&amp;height=32&amp;mode=crop | https://content.civicplus.com/api/assets/efcb4763-bfa7-48b8-b634-2a5c7b1cf114?width=16&amp;height=16&amp;mode=crop | https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&amp;family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&amp;display=fallback | https://content.civicplus.com/api/assets/e3e0dfb8-75ce-4bfe-8987-27b0ff4ea994?cache=1800&amp;width=300&amp;mode=min 300w,https://content.civicplus.com/api/assets/e3e0dfb8-75ce-4bfe-8987-27b0ff4ea994?cache=1800&amp;width=687&amp;mode=min 687w | https://content.civicplus.com/api/assets/e3e0dfb8-75ce-4bfe-8987-27b0ff4ea994?cache=1800 | https://watertownma.viewpointcloud.com/categories/1071 | https://watertownma.viewpointcloud.com/ | https://content.civicplus.com/api/assets/ma-watertown/{{id}} | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Hingham — to_investigate
- https://www.hingham-ma.gov/577/View → HTTP 200 · título: View | Hingham, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- http://www.permiteyes.net/hingham/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: http://www.permiteyes.net/hingham/building/homepage.asp
- Endereços de dados candidatos: https://www.hingham-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/hingham/publicattachments.php?application_id= | https://permiteyes.us/hingham/controller/getvalues_controller.php | https://permiteyes.us/hingham/ajax/getbuildingpublichome.php

### Attleboro — to_investigate
- https://www.cityofattleboro.us/167/Building-Inspection → HTTP 200 · título: Building Inspection | Attleboro, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.net/Attleboro/building/homepage.asp → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/attleboro/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.net/Attleboro/building/homepage.asp | https://permiteyes.us/attleboro/loginuser.php
- Endereços de dados candidatos: https://www.cityofattleboro.us/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/attleboro/publicattachments.php?application_id= | https://permiteyes.us/attleboro/controller/getvalues_controller.php | https://permiteyes.us/attleboro/controller/userregistration_controller.php

### Springfield — needs_adapter
- https://springfieldma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### New Bedford — needs_adapter
- https://newbedfordma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Haverhill — needs_adapter
- https://haverhillma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Quincy — needs_adapter
- https://quincyma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Gloucester — needs_adapter
- https://gloucesterma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Lexington — needs_adapter
- https://lexingtonma.portal.opengov.com/ → HTTP 200 · título: OpenGov · plataforma: OpenGov/ViewpointCloud · robots.txt: NÃO permitido
- Endereços de dados candidatos: https://fonts.googleapis.com | https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap | https://www.google.com/jsapi | https://maps.googleapis.com/maps/api/js?key=AIzaSyD951Jc3dCSGNQGiOzIgzGUtA-bfsJrpAA&libraries=geometry,places

### Lowell — to_investigate
- https://www.lowellma.gov/1631/Online-Permitting → HTTP 200 · título: Online Permitting | Lowell, MA · plataforma: CivicPlus · robots.txt: permitido

### West Springfield — to_investigate
- https://opendata-westspringfield.hub.arcgis.com/ → HTTP 200 · título: West Springfield Open Data · plataforma: ArcGIS · robots.txt: permitido

### Taunton — needs_adapter
- https://permiteyes.us/taunton/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://www.taunton-ma.gov/169/Online-Building-Permits → HTTP 200 · título: Online Building Permits | Taunton, MA · plataforma: Accela, PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/taunton/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/taunton/publicview.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/taunton/loginuser.php | https://permiteyes.us/taunton/publicview.php
- Endereços de dados candidatos: https://permiteyes.us/taunton/controller/userregistration_controller.php | https://www.taunton-ma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/taunton/controller/getvalues_controller.php | https://permiteyes.us/taunton/ajax/getpublicview.php

### Falmouth — needs_adapter
- https://www.falmouthma.gov/313/Online-Permitting → HTTP 200 · título: Online Permitting | Falmouth, MA · plataforma: PermitEyes, CivicPlus · robots.txt: permitido
- https://permiteyes.us/falmouth/userregistration.php → HTTP 200 · plataforma: PermitEyes · robots.txt: permitido
- https://permiteyes.us/falmouth/loginuser.php → HTTP 200 · título: Permiteyes · plataforma: PermitEyes · robots.txt: permitido
- Portais encontrados na página da prefeitura: https://permiteyes.us/falmouth/userregistration.php | https://permiteyes.us/falmouth/loginuser.php | https://permiteyes.us/falmouth/publicview.php
- Endereços de dados candidatos: https://www.falmouthma.gov/api/v1/SplashModal/Get | https://maps.googleapis.com/maps/api/js?v=3.exp&key= | https://maps.googleapis.com/maps/api/js?v=3.exp&callback= | https://permiteyes.us/falmouth/controller/sitedetails_controller.php | https://permiteyes.us/falmouth/controller/userregistration_controller.php | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Email | https://permiteyes.us/falmouth/controller/duplicationcheck_controller.php?action=Username

### Stockbridge — needs_adapter
- https://www.stockbridge-ma.gov/building-inspector/page/permiteyes-how → HTTP 403 · título: Just a moment... · plataforma: PermitEyes · robots.txt: n/d

### Arlington — to_investigate

### Weston — to_investigate

### Westford — to_investigate

### Milton — to_investigate

### Cohasset — to_investigate

### Holland — to_investigate

### Ludlow — to_investigate
