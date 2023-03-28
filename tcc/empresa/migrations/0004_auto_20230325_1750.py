# Generated by Django 3.2.18 on 2023-03-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20230323_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacaorisco',
            options={'verbose_name_plural': 'Avaliações de Risco'},
        ),
        migrations.AlterModelOptions(
            name='classificacaorisco',
            options={'verbose_name_plural': 'Classificação de Riscos'},
        ),
        migrations.AlterModelOptions(
            name='descricaoperigo',
            options={'verbose_name_plural': 'Tipos de Perigo'},
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['nome_empresa']},
        ),
        migrations.AlterModelOptions(
            name='fonterisco',
            options={'verbose_name_plural': 'Fontes de Risco'},
        ),
        migrations.AlterModelOptions(
            name='funcao',
            options={'verbose_name_plural': 'Funcões'},
        ),
        migrations.AlterModelOptions(
            name='inventario',
            options={'verbose_name_plural': 'Inventários de Risco'},
        ),
        migrations.AlterModelOptions(
            name='lesoes',
            options={'verbose_name_plural': 'Tipos de Lesão'},
        ),
        migrations.AlterModelOptions(
            name='medidascontrole',
            options={'verbose_name_plural': 'Medidas de Controle'},
        ),
        migrations.AlterModelOptions(
            name='medidasimplementadas',
            options={'verbose_name_plural': 'Medidas Implementadas'},
        ),
        migrations.AlterModelOptions(
            name='nivelexposicao',
            options={'verbose_name_plural': 'Níveis de Exposição'},
        ),
        migrations.AlterModelOptions(
            name='nivelgravidade',
            options={'verbose_name_plural': 'Níveis de Gravidade'},
        ),
        migrations.AlterModelOptions(
            name='nivelprobabilidade',
            options={'verbose_name_plural': 'Níveis de Probabilidade'},
        ),
        migrations.AlterModelOptions(
            name='nivelrisco',
            options={'verbose_name_plural': 'Níveis de Risco'},
        ),
        migrations.AlterModelOptions(
            name='planoacao',
            options={'verbose_name_plural': 'Planos de Ação'},
        ),
        migrations.AlterModelOptions(
            name='tempoexposicao',
            options={'verbose_name_plural': 'Tempos de exposição'},
        ),
        migrations.AlterModelOptions(
            name='tiporisco',
            options={'verbose_name_plural': 'Tipos de Risco'},
        ),
        migrations.AlterField(
            model_name='descricaoperigo',
            name='descricao_perigo',
            field=models.CharField(choices=[('200004300', 'Impacto de pessoa contra objeto parado'), ('200004600', 'Impacto de pessoa contra objeto em movimento'), ('200008300', 'Impacto sofrido por pessoa de objeto que cai'), ('200008600', 'Impacto sofrido por pessoa de objeto projetado'), ('200008900', 'Impacto sofrido por pessoa, NIC'), ('200012200', 'Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc.'), ('200012300', 'Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus'), ('200012400', 'Queda de pessoa com diferença de nível de material empilhado'), ('200012500', 'Queda de pessoa com diferença de nível de veículo'), ('200012600', 'Queda de pessoa com diferença de nível em escada permanente'), ('200012700', 'Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc.'), ('200012900', 'Queda de pessoa com diferença de nível, NIC'), ('200016300', 'Queda de pessoa em mesmo nível em passagem ou superfície de sustentação'), ('200016600', 'Queda de pessoa em mesmo nível sobre ou contra alguma coisa'), ('200016900', 'Queda de pessoa em mesmo nível, NIC'), ('200020100', 'Aprisionamento em, sobre ou entre objetos em movimento convergente'), ('200020300', 'Aprisionamento em, sobre ou entre objeto parado e outro em movimento'), ('200020500', 'Aprisionamento em, sobre ou entre dois ou mais objetos em movimento'), ('200020700', 'Aprisionamento em, sobre ou entre desabamento ou desmoronamento'), ('200020900', 'Aprisionamento em, sob ou entre, NIC'), ('200024300', 'Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto'), ('200024400', 'Atrito ou abrasão por manusear objeto'), ('200024500', 'Atrito ou abrasão por objeto em vibração'), ('200024600', 'Atrito ou abrasão por corpo estranho no olho'), ('200024700', 'Atrito ou abrasão por compressão repetitiva'), ('200024900', 'Atrito ou abrasão, NIC'), ('200028300', 'Reação do corpo a movimento involuntário'), ('200028600', 'Reação do corpo a movimento voluntário'), ('200032200', 'Esforço excessivo ao erguer objeto'), ('200032400', 'Esforço excessivo ao empurrar ou puxar objeto'), ('200032600', 'Esforço excessivo ao manejar, sacudir ou arremessar objeto'), ('200032900', 'Esforço excessivo, NIC'), ('200036000', 'Elétrica, exposição a energia'), ('200040300', 'Temperatura muito alta, contato com objeto ou substância a'), ('200040600', 'Temperatura muito baixa, contato com objeto ou substância a'), ('200044300', 'Temperatura ambiente elevada, exposição a'), ('200044600', 'Temperatura ambiente baixa, exposição a'), ('200048200', 'Inalação de substância cáustica, tóxica ou nociva'), ('200048400', 'Ingestão de substância cáustica'), ('200048600', 'Absorção de substância cáustica'), ('200048900', 'Inalação, ingestão ou absorção, NIC'), ('200052000', 'Imersão'), ('200056000', 'Radiação não ionizante, exposição a'), ('200060000', 'Radiação ionizante, exposição a'), ('200064000', 'Ruído, exposição a'), ('200068000', 'Vibração, exposição a'), ('200072000', 'Pressão ambiente, exposição a'), ('200072300', 'Exposição à pressão ambiente elevada'), ('200072600', 'Exposição à pressão ambiente baixa'), ('200076200', 'Poluição da água, ação da (exposição à poluição da água)'), ('200076400', 'Poluição do ar, ação da (exposição à poluição do ar)'), ('200076600', 'Poluição do solo, ação da (exposição à poluição do solo)'), ('200076900', 'Poluição, NIC, exposição a (exposição à poluição, NIC)'), ('200080200', 'Ataque de ser vivo por mordedura, picada, chifrada, coice, etc.'), ('200080400', 'Ataque de ser vivo com peçonha'), ('200080600', 'Ataque de ser vivo com transmissão de doença'), ('200080900', 'Ataque de ser vivo, NIC'), ('209000000', 'Tipo, NIC  '), ('209500000', 'Tipo inexistente')], max_length=2000),
        ),
        migrations.AlterField(
            model_name='fonterisco',
            name='fonte_risco',
            field=models.CharField(choices=[('200004300', 'Impacto de pessoa contra objeto parado. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'), ('200004600', 'Impacto de pessoa contra objeto em movimento. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'), ('200008300', 'Impacto sofrido por pessoa, de objeto que cai. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'), ('200008600', 'Impacto sofrido por pessoa, de objeto projetado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'), ('200008900', 'Impacto sofrido por pessoa, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'), ('200012200', 'Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200012300', 'Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus não permitem o apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200012400', 'Queda de pessoa com diferença de nível de material empilhado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200012500', 'Queda de pessoa com diferença de nível de veículo. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200012600', 'Queda de pessoa com diferença de nível em escada permanente cujos degraus permitem apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200012700', 'Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc. (da borda da abertura). Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200012900', 'Queda de pessoa com diferença de nível, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'), ('200016300', 'Queda de pessoa em mesmo nível em passagem ou superfície de sustentação. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'), ('200016600', 'Queda de pessoa em mesmo nível sobre ou contra alguma coisa. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'), ('200016900', 'Queda de pessoa em mesmo nível, NIC. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'), ('200020100', 'Aprisionamento em, sob ou entre objetos em movimento convergente (calandra) ou de encaixe. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'), ('200020300', 'Aprisionamento em, sob ou entre um objeto parado e outro em movimento. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'), ('200020500', 'Aprisionamento em, sob ou entre dois ou mais objetos em movimento (sem encaixe). Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'), ('200020700', 'Aprisionamento em, sob ou entre desabamento ou desmoronamento de edificação, barreira, etc. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'), ('200020900', 'Aprisionamento em, sob ou entre, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'), ('200024300', 'Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto (não em vibração). Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'), ('200024400', 'Atrito ou abrasão por manusear objeto (não em vibração).  Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'), ('200024500', 'Atrito ou abrasão por objeto em vibração. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'), ('200024600', 'Atrito ou abrasão por corpo estranho no olho. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'), ('200024700', 'Atrito ou abrasão por compressão repetitiva Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'), ('200024900', 'Atrito ou abrasão, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'), ('200028300', 'Reação do corpo a seus movimentos - movimento involuntário (escorregão sem queda, etc.). Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'), ('200028600', 'Reação do corpo a seus movimentos - movimento voluntário. Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'), ('200032200', 'Esforço excessivo ao erguer objeto. Ver explicações da classificação anterior (200028000).'), ('200032400', 'Esforço excessivo ao empurrar ou puxar objeto. Ver explicações da classificação anterior (200028000).'), ('200032600', 'Esforço excessivo ao manejar, sacudir ou arremessar objeto. Ver explicações da classificação anterior (200028000).'), ('200032900', 'Esforço excessivo, NIC. Ver explicações da classificação anterior (200028000).'), ('200036000', 'Exposição a energia elétrica. Aplica-se somente a casos sem impacto, em que a lesão consiste em choque elétrico, queimadura ou eletroplessão (eletrocussão).'), ('200040300', 'Contato com objeto ou substância a temperatura muito alta. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'), ('200040600', 'Contato com objeto ou substância a temperatura muito baixa. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'), ('200044300', 'Exposição à temperatura ambiente elevada. Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'), ('200044600', 'Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'), ('200048200', 'Inalação de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'), ('200048400', 'Ingestão de substancia cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'), ('200048600', 'Absorção (por contato) de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'), ('200048900', 'Inalação, ingestão e absorção, NIC. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'), ('200052000', 'Imersão. Aplica-se aos acidentes que têm por consequência o afogamento.'), ('200056000', 'Exposição à radiação não ionizante. Aplica-se a casos em que as lesões são provocadas por exposição à radiação solar ou outras radiações não ionizantes (por exemplo: ultravioleta e infravermelho).'), ('200060000', 'Exposição à radiação ionizante.'), ('200064000', 'Exposição ao ruído.'), ('200068000', 'Exposição à vibração.'), ('200072300', 'Exposição à pressão ambiente elevada.'), ('200072600', 'Exposição à pressão ambiente baixa.'), ('200076200', 'Exposição à poluição da água.'), ('200076400', 'Exposição à poluição do ar.'), ('200076600', 'Exposição à poluição do solo.'), ('200076900', 'Exposição à poluição, NIC.'), ('200080200', 'Ataque de ser vivo por mordedura, picada, chifrada, coice, etc., não se aplicando no caso de haver peçonha ou transmissão de doença.'), ('200080400', 'Ataque de ser vivo com peçonha.'), ('200080600', 'Ataque de ser vivo com transmissão de doença.'), ('200080900', 'Ataque de ser vivo (inclusive do homem), NIC.'), ('200080901', 'Contato com pessoas doentes ou material infecto-contagiante - agentes biológicos.'), ('209000000', 'Tipo, NIC'), ('209500000', 'Tipo inexistente')], max_length=500),
        ),
        migrations.AlterField(
            model_name='planoacao',
            name='quando',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='planoacao',
            name='quanto',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tiporisco',
            name='tipo_risco',
            field=models.CharField(choices=[('F', 'FÍSICOS'), ('Q', 'QUÍMICOS'), ('B', 'BIOLÓGICOS'), ('EB', 'ERGONÔMICOS-BIOMECÂNICOS'), ('EM', 'ERGONÔMICOS-MOBILIÁRIO E EQUIPAMENTOS'), ('EO', 'ERGONÔMICOS-ORGANIZACIONAIS'), ('EA', 'ERGONÔMICOS-AMBIENTAIS'), ('EP', 'ERGONÔMICOS-PSICOSSOCIAIS/COGNITIVOS'), ('A', 'MECÂNICOS/ACIDENTES'), ('P', 'PERIGOSOS'), ('AS', 'ASSOCIAÇÃO DE FATORES DE RISCO'), ('O', 'OUTROS FATORES DE RISCO'), ('NO', 'AUSÊNCIA DE FATORES DE RISCO')], max_length=10),
        ),
    ]