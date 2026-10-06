# Cobertura de permits em Massachusetts

37 cidades cadastradas. Atualizado em 06/10/2026 com o teste de saúde. O arquivo `health_report.md` traz a verificação ao vivo.

| Cidade | Situação | Tipo de acesso | Observação |
| --- | --- | --- | --- |
| Boston | ✅ No ar (testada) | open_data_api |  |
| Cambridge | ✅ No ar (testada) | open_data_api |  |
| Worcester | ✅ No ar (testada) | open_data_api | Sem valor da obra. Desde ~mai/2026 tipo e contratante quase sempre vêm como N/A (limite da fonte). Servidor limita consultas (o código espera e repete). |
| Reading | 🧪 Em teste | file_report | Relatório mensal em Excel (confirmado). O teste de saúde de 06/10 retornou 0 permits sem erro; falta ver as colunas reais. O portal OpenGov deles não permite coleta (robots.txt). |
| Brookline | 🔧 Falta adaptador | search_by_address_or_record | Accela Citizen Access. Pesquisa por número, endereço ou nome. |
| North Reading | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Permits ativos desde set/2019. |
| Concord | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Building permits emitidos desde 01/01/2021. |
| Mansfield | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). O site da prefeitura bloqueia acesso automático; endereço do PermitEyes ainda a confirmar. |
| Pittsfield | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Região Berkshire; registros desde 1985. |
| Great Barrington | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Colunas: Issue Date, Applicant, tipo e status. |
| Hingham | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Identificado pelo teste de saúde. |
| Attleboro | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Identificado pelo teste de saúde; existe também o arquivo antigo (permiteyes.net). |
| Taunton | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Migrou do Accela para PermitEyes. |
| Falmouth | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Public View sem login. |
| Stockbridge | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (robots.txt permite). Região Berkshire. |
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
