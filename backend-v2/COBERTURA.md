# Cobertura de permits em Massachusetts

37 cidades cadastradas. Atualizado em 06/10/2026. `health_report.md` traz a verificação ao vivo.

| Cidade | Situação | Tipo de acesso | Observação |
| --- | --- | --- | --- |
| Boston | ✅ No ar (testada) | open_data_api |  |
| Cambridge | ✅ No ar (testada) | open_data_api |  |
| Worcester | ✅ No ar (testada) | open_data_api | Sem valor da obra. Desde ~mai/2026 tipo e contratante quase sempre vêm como N/A (limite da fonte). Servidor limita consultas (o código espera e repete). |
| Reading | ✅ No ar (testada) | file_report | Relatório mensal em Excel; robots.txt de readingma.gov permite. Testada ao vivo em 06/10 (90 permits em 45 dias) (record, full_address, date_issued, project_cost, dba...). Sem construtor próprio: usa dba/requerente. O portal OpenGov deles não permite coleta. |
| Hingham | ✅ No ar (testada) | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Testada em 06/10: 54 permits em 14 dias, sem valor nem construtora (a tela não mostra). |
| Taunton | ✅ No ar (testada) | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Testada em 06/10: 59 permits em 14 dias, com construtora e valor. |
| Falmouth | ✅ No ar (testada) | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Testada em 06/10: 99 permits em 14 dias, sem valor nem construtora (a tela não mostra). |
| North Reading | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Permits ativos desde set/2019. Endereço de dados ainda não identificado. |
| Concord | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Building permits emitidos desde 01/01/2021. |
| Mansfield | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Página do PermitEyes confirmada (HTTP 200); o site da prefeitura bloqueia acesso automático. |
| Pittsfield | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Região Berkshire (várias cidades na mesma tela); o robots.txt do site da prefeitura não permite, mas o do PermitEyes sim. |
| Great Barrington | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Região Berkshire. |
| Attleboro | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Existe também o arquivo antigo (permiteyes.net). |
| Stockbridge | 🧪 Em teste | search_by_address_or_record | PermitEyes Public View (robots.txt permite; consulta sem login). Região Berkshire. |
| Brookline | 🔧 Falta adaptador | search_by_address_or_record | Accela Citizen Access. Pesquisa por número, endereço ou nome. |
| Lowell | 🔎 A identificar | search_by_address_or_record | MUNIS Citizen Self Service (Tyler). O site menciona relatórios mensais mediante solicitação. |
| West Springfield | 🔎 A identificar | open_data_api | Portal de dados abertos ArcGIS está no ar, mas não encontramos camada de permits na busca do ArcGIS Hub. |
| Arlington | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: busca por endereço, descrição, proprietário, contratante, data e tipo. Confirmar no site. |
| Weston | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: busca por período e tipo de permit. Confirmar no site. |
| Westford | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: busca por endereço, lote, requerente ou proprietário. |
| Milton | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: status por endereço, data, tipo ou requerente. |
| Cohasset | 🔎 A identificar | file_report | Listada em diretório público: registros mensais de permits desde 2009. |
| Holland | 🔎 A identificar | file_report | Listada em diretório público: lista recente de permits emitidos. |
| Ludlow | 🔎 A identificar | file_report | Listada em diretório público: relatórios mensais de permits emitidos. |
| Danvers | ⚠️ Só por endereço | address_only | OpenGov desde 30/05/2023, busca só por endereço, e o robots.txt do OpenGov não permite coleta automática. A cidade também publica um relatório mensal em PDF com valor da obra e requerente (alternativa possível). |
| Sudbury | ⚠️ Só por endereço | address_only | Pesquisa por endereço no OpenGov (robots.txt não permite coleta automática). |
| Newton | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. O site da prefeitura também bloqueia acesso automático; a página Reports da Inspectional Services pode ter relatórios. |
| Watertown | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| Springfield | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| New Bedford | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| Haverhill | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| Quincy | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| Gloucester | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| Lexington | ⛔ Coleta não permitida (robots.txt) | search_by_address_or_record | OpenGov/ViewpointCloud: o robots.txt não permite coleta automática (verificado em 06/10/2026). Alternativas: relatórios que a cidade publique ou pedido formal de dados. |
| Revere | 🔒 Exige login | login_required | Exige cadastro/login para pesquisar. Não automatizamos. |
| Needham | 🔒 Exige login | login_required | Instruções da prefeitura pedem login; portal OpenGov (robots.txt não permite coleta). Permits emitidos desde 18/03/2020 estão online. |
| Northampton | 📋 Só planejamento | planning_only | Planning & Sustainability (OpenGov): processos pendentes e concluídos; não equivale a building permits; robots.txt não permite coleta. |
