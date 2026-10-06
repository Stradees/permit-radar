# Cobertura de permits em Massachusetts

37 cidades cadastradas. Atualizado em 06/10/2026. O arquivo `health_report.md` (gerado pelo teste de saúde) traz a verificação ao vivo de cada uma.

| Cidade | Situação | Tipo de acesso | Observação |
| --- | --- | --- | --- |
| Boston | ✅ No ar (testada) | open_data_api |  |
| Cambridge | ✅ No ar (testada) | open_data_api |  |
| Worcester | ✅ No ar (testada) | open_data_api | Sem valor da obra. Desde ~mai/2026 tipo e contratante quase sempre vêm como N/A (limite da fonte). Servidor limita consultas (o código espera e repete). |
| Reading | 🧪 Em teste | file_report | Relatório mensal em Excel (confirmado). Colunas ainda não vistas: o primeiro log mostra os nomes reais. |
| Newton | 🔧 Falta adaptador | search_by_address_or_record | OpenGov/ViewpointCloud (NewGov). Consulta sem login por endereço ou número do registro; os detalhes trazem escopo e contratante. |
| Brookline | 🔧 Falta adaptador | search_by_address_or_record | Accela Citizen Access. Pesquisa por número, endereço ou nome. |
| North Reading | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View (permits ativos desde set/2019). |
| Concord | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View: building permits emitidos desde 01/01/2021. |
| Mansfield | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View. |
| Pittsfield | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View: registros desde 1985; busca por número e rua. |
| Great Barrington | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes Public View confirmado: colunas Issue Date, Applicant, tipo e status; a tabela carrega por script (endereço de dados a descobrir). |
| Springfield | 🔧 Falta adaptador | search_by_address_or_record |  |
| New Bedford | 🔧 Falta adaptador | search_by_address_or_record |  |
| Haverhill | 🔧 Falta adaptador | search_by_address_or_record |  |
| Quincy | 🔧 Falta adaptador | search_by_address_or_record |  |
| Gloucester | 🔧 Falta adaptador | search_by_address_or_record |  |
| Lexington | 🔧 Falta adaptador | search_by_address_or_record |  |
| Taunton | 🔧 Falta adaptador | search_by_address_or_record | Migrou do Accela para PermitEyes; a prefeitura diz que dá para pesquisar permits sem conta. |
| Falmouth | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes desde dez/2021, com Public View sem login. |
| Stockbridge | 🔧 Falta adaptador | search_by_address_or_record | PermitEyes (Berkshire), com Public View. |
| Watertown | 🔎 A identificar | search_by_address_or_record | Histórico e status de building permits e processos de planejamento; sistema ainda não identificado. |
| Hingham | 🔎 A identificar | search_by_address_or_record | Pesquisa pública de aplicações e permits emitidos; sistema ainda não identificado. |
| Attleboro | 🔎 A identificar | search_by_address_or_record | Consulta pública online e arquivo eletrônico anterior; sistema ainda não identificado. |
| Lowell | 🔎 A identificar | search_by_address_or_record | MUNIS Citizen Self Service (Tyler). O site menciona relatórios mensais mediante solicitação. |
| West Springfield | 🔎 A identificar | open_data_api | Portal de dados abertos ArcGIS; falta localizar a camada de permits. |
| Arlington | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: busca por endereço, descrição, proprietário, contratante, data e tipo. Confirmar no site. |
| Weston | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: busca por período e tipo de permit. Confirmar no site. |
| Westford | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: busca por endereço, lote, requerente ou proprietário. |
| Milton | 🔎 A identificar | search_by_address_or_record | Listada em diretório público: status por endereço, data, tipo ou requerente. |
| Cohasset | 🔎 A identificar | file_report | Listada em diretório público: registros mensais de permits desde 2009. |
| Holland | 🔎 A identificar | file_report | Listada em diretório público: lista recente de permits emitidos. |
| Ludlow | 🔎 A identificar | file_report | Listada em diretório público: relatórios mensais de permits emitidos. |
| Danvers | ⚠️ Só por endereço | address_only | OpenGov desde 30/05/2023, busca só por endereço. A cidade também publica um relatório mensal em PDF com valor da obra e requerente (alternativa possível). |
| Sudbury | ⚠️ Só por endereço | address_only | Pesquisa pública por endereço de permits emitidos. |
| Revere | 🔒 Exige login | login_required | Exige cadastro/login para pesquisar. Não automatizamos. |
| Needham | 🔒 Exige login | login_required | Instruções da prefeitura pedem login. Permits emitidos desde 18/03/2020 estão online. |
| Northampton | 📋 Só planejamento | planning_only | Planning & Sustainability: processos pendentes e concluídos; não equivale a building permits. |
