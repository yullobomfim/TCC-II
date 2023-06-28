## Imports
from django.db import models
from django.contrib.auth.models import User

## Modelos
# CADASTRO DO AMBIENTE
class Empresa(models.Model):
    nome = models.CharField(max_length=100)    
    responsavel = models.CharField(max_length=100)    
    numero_funcionarios = models.IntegerField()

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"
        ordering = ['nome']
        
    def __str__(self):
        return self.nome
class Funcao(models.Model):
    nome = models.CharField(max_length=50)
    descricao_detalhada = models.TextField()
    cbo_funcao = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "funcao"
        verbose_name_plural = "funcoes"
        ordering = ['nome']

# CADASTRO EMPREGADO
class Empregado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, verbose_name=("empresa"), on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, verbose_name=("funcao"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name = "empregado"
        verbose_name_plural = "empregados"
        ordering = ['user']

# IDENTIFICAÇÃO DOS RISCOS DO AMBIENTE
class Tiporisco(models.Model):    
    choice_tiporisco = (  
        ('FÍSICOS','FÍSICOS'),
        ('QUÍMICOS','QUÍMICOS'),
        ('BIOLÓGICOS','BIOLÓGICOS'),
        ('ERGONÔMICOS-BIOMECÂNICOS','ERGONÔMICOS-BIOMECÂNICOS'),
        ('ERGONÔMICOS-MOBILIÁRIO E EQUIPAMENTOS','ERGONÔMICOS-MOBILIÁRIO E EQUIPAMENTOS'),
        ('ERGONÔMICOS-ORGANIZACIONAIS','ERGONÔMICOS-ORGANIZACIONAIS'),
        ('ERGONÔMICOS-AMBIENTAIS','ERGONÔMICOS-AMBIENTAIS'),
        ('ERGONÔMICOS-PSICOSSOCIAIS/COGNITIVOS','ERGONÔMICOS-PSICOSSOCIAIS/COGNITIVOS'),
        ('MECÂNICOS/ACIDENTES','MECÂNICOS/ACIDENTES'),
        ('PERIGOSOS','PERIGOSOS'),
        ('ASSOCIAÇÃO DE FATORES DE RISCO','ASSOCIAÇÃO DE FATORES DE RISCO'),
        ('OUTROS FATORES DE RISCO','OUTROS FATORES DE RISCO'),
        ('AUSÊNCIA DE FATORES DE RISCO','AUSÊNCIA DE FATORES DE RISCO'),  
    )
    
    tipo_risco = models.CharField(max_length=250, choices=choice_tiporisco)
    
    def __str__(self):
        return self.tipo_risco
    class Meta:
        verbose_name = "tipo_risco"
        verbose_name_plural = "tipo_riscos"
        ordering = ['tipo_risco']
class Descricaoperigo(models.Model):
    choice_perigo = (
        ('Infrassom e sons de baixa frequência','Infrassom e sons de baixa frequência'),
        ('Ruído contínuo ou intermitente (legislação previdenciária','Ruído contínuo ou intermitente (legislação previdenciária)'),
        ('Ruído impulsivo ou de impacto','Ruído impulsivo ou de impacto'),
        ('Ultrassom','Ultrassom'),
        ('Campos magnéticos estáticos','Campos magnéticos estáticos'),
        ('Campos magnéticos de sub-radiofrequência (30 kHz e abaixo','Campos magnéticos de sub-radiofrequência (30 kHz e abaixo)'),
        ('Sub-radiofrequência (30 kHz e abaixo) e campos eletrostáticos','Sub-radiofrequência (30 kHz e abaixo) e campos eletrostáticos'),
        ('Radiação de radiofrequência','Radiação de radiofrequência'),
        ('Micro-ondas','Micro-ondas'),
        ('Radiação visível e infravermelho próximo','Radiação visível e infravermelho próximo'),
        ('Radiação ultravioleta, exceto radiação n a faixa 400 a 320 nm (Luz Negra','Radiação ultravioleta, exceto radiação n a faixa 400 a 320 nm (Luz Negra)'),
        ('Radiação ultravioleta na faixa 400 a 320 nm (Luz Negra','Radiação ultravioleta na faixa 400 a 320 nm (Luz Negra)'),
        ('LASER','LASER'),
        ('Radiações ionizantes','Radiações ionizantes'),
        ('Vibrações localizadas (mão-braço','Vibrações localizadas (mão-braço)'),
        ('Vibração de corpo inteiro (aceleração resultante de exposição normalizada - aren)','Vibração de corpo inteiro (aceleração resultante de exposição normalizada - aren)'),
        ('Frio','Frio'),
        ('Temperaturas anormais (calor) (legislação previdenciária)','Temperaturas anormais (calor) (legislação previdenciária)'),
        ('Pressão hiperbárica','Pressão hiperbárica'),
        ('Pressão hipobárica','Pressão hipobárica'),
        ('Ruído contínuo ou intermitente (legislação trabalhista)','Ruído contínuo ou intermitente (legislação trabalhista)'),
        ('Vibração de corpo inteiro (Valor da Dose de Vibração Resultante - VDVR','Vibração de corpo inteiro (Valor da Dose de Vibração Resultante - VDVR)'),
        ('Temperaturas anormais (calor) (legislação trabalhista','Temperaturas anormais (calor) (legislação trabalhista)'),
        ('Outros','Outros'),
        ('Acetaldeído (aldeído acético','Acetaldeído (aldeído acético)'),
        ('Acetato de benzila','Acetato de benzila'),
        ('Acetato de n-butila','Acetato de n-butila'),
        ('Acetato de sec-butila','Acetato de sec-butila'),
        ('Acetato de terc-butila','Acetato de terc-butila'),
        ('Acetato de 2-butoxietila','Acetato de 2-butoxietila'),
        ('Sais de Cianeto','Sais de Cianeto'),
        ('Acetato de etila','Acetato de etila'),
        ('Acetato de 2-etoxi etila (Acetato de cellosolve ou Acetato de éter monoetílico de etileno glicol','Acetato de 2-etoxi etila (Acetato de cellosolve ou Acetato de éter monoetílico de etileno glicol)'),
        ('Acetato de sec-hexila','Acetato de sec-hexila'),
        ('Acetato de isobutila','Acetato de isobutila'),
        ('Acetato de isopropila','Acetato de isopropila'),
        ('Acetato de metila','Acetato de metila'),
        ('Acetato de 2-metoxietila (EGMEA) ','Acetato de 2-metoxietila (EGMEA) '),
        ('Acetato de n-propila','Acetato de n-propila'),
        ('Acetato de pentila, todos os isômeros','Acetato de pentila, todos os isômeros'),
        ('Acetato de vinila','Acetato de vinila'),
        ('Acetileno','Acetileno'),
        ('Acetofenona','Acetofenona'),
        ('Acetona (propanona','Acetona (propanona)'),
        ('Acetona cianidrina','Acetona cianidrina'),
        ('Acetonitrila (cianeto de metila','Acetonitrila (cianeto de metila)'),
        ('Ácido acético (ácido etanoico','Ácido acético (ácido etanoico)'),
        ('Ácido acetilsalicílico (aspirina','Ácido acetilsalicílico (aspirina)'),
        ('Ácido acrílico','Ácido acrílico'),
        ('Ácido adípico','Ácido adípico'),
        ('Ácido aristolóquico','Ácido aristolóquico'),
        ('Ácido bromídrico (brometo de hidrogênio','Ácido bromídrico (brometo de hidrogênio)'),
        ('Ácido carbônico','Ácido carbônico'),
        ('Ácido cianídrico (cianeto de hidrogênio, gás cianídrico','Ácido cianídrico (cianeto de hidrogênio, gás cianídrico)'),
        ('Ácido clorídrico (cloreto de hidrogênio, gás clorídrico','Ácido clorídrico (cloreto de hidrogênio, gás clorídrico)'),
        ('Ácido 2-cloropropiônico','Ácido 2-cloropropiônico'),
        ('Ácido crômico (névoa','Ácido crômico (névoa)'),
        ('Ácido dicloroacético','Ácido dicloroacético'),
        ('Ácido 2,2-dicloropropiônico','Ácido 2,2-dicloropropiônico'),
        ('Ácido 2-etil hexanoico','Ácido 2-etil hexanoico'),
        ('Ácido fluorídrico','Ácido fluorídrico'),
        ('Ácido fosfórico','Ácido fosfórico'),
        ('Ácido metacrílico','Ácido metacrílico'),
        ('Ácido metanoico (ácido fórmico','Ácido metanoico (ácido fórmico)'),
        ('Ácido monocloroacético','Ácido monocloroacético'),
        ('Ácido nítrico','Ácido nítrico'),
        ('Ácido oxálico, anidro e diidratado','Ácido oxálico, anidro e diidratado'),
        ('Ácido peracético','Ácido peracético'),
        ('Ácido pícrico','Ácido pícrico'),
        ('Ácido propiônico','Ácido propiônico'),
        ('Ácido sulfúrico','Ácido sulfúrico'),
        ('Ácido tereftálico','Ácido tereftálico'),
        ('Ácido tioglicólico','Ácido tioglicólico'),
        ('Ácido tricloroacético','Ácido tricloroacético'),
        ('Acrilamida','Acrilamida'),
        ('Acrilato de n-butila','Acrilato de n-butila'),
        ('Acrilato de etila','Acrilato de etila'),
        ('Acrilato de 2-hidroxipropila','Acrilato de 2-hidroxipropila'),
        ('Acrilato de metila','Acrilato de metila'),
        ('Acrilonitrila (cianeto de vinila','Acrilonitrila (cianeto de vinila)'),
        ('Acroleína','Acroleína'),
        ('Adiponitrila','Adiponitrila'),
        ('Aflatoxinas','Aflatoxinas'),
        ('Aguarrás mineral (solvente de Stoddard','Aguarrás mineral (solvente de Stoddard)'),
        ('Alaclor','Alaclor'),
        ('Álcalis cáusticos','Álcalis cáusticos'),
        ('Alcatrão de hulha, produtos voláteis como aerossóis solúveis em benzeno (breu de alcatrão de hulha','Alcatrão de hulha, produtos voláteis como aerossóis solúveis em benzeno (breu de alcatrão de hulha)'),
        ('Álcool alílico','Álcool alílico'),
        ('Álcool n-butílico (n-butanol','Álcool n-butílico (n-butanol)'),
        ('Álcool sec-butílico (sec-butanol','Álcool sec-butílico (sec-butanol)'),
        ('Álcool terc-butílico','Álcool terc-butílico'),
        ('Álcool etílico (etanol','Álcool etílico (etanol)'),
        ('Álcool furfurílico','Álcool furfurílico'),
        ('Álcool isoamílico','Álcool isoamílico'),
        ('Álcool isobutílico (isobutanol','Álcool isobutílico (isobutanol)'),
        ('Álcool isooctílico','Álcool isooctílico'),
        ('Álcool isopropílico (isopropanol ou 2-propanol','Álcool isopropílico (isopropanol ou 2-propanol)'),
        ('Álcool propargílico','Álcool propargílico'),
        ('Álcool metil amílico (metil isobutilcarbinol','Álcool metil amílico (metil isobutilcarbinol)'),
        ('Álcool metílico (metanol','Álcool metílico (metanol)'),
        ('Álcool n-propílico (n-propanol','Álcool n-propílico (n-propanol)'),
        ('Aldrin','Aldrin'),
        ('Algodão, bruto, sem tratamento, poeira','Algodão, bruto, sem tratamento, poeira'),
        ('Alumínio metal e compostos insolúveis','Alumínio metal e compostos insolúveis'),
        ('Amido','Amido'),
        ('Aminas aromáticas','Aminas aromáticas'),
        ('4-Aminodifenil (p-xenilamina; aminobifenila; 4-aminobifenila','4-Aminodifenil (p-xenilamina; aminobifenila; 4-aminobifenila)'),
        ('2-Aminopiridina','2-Aminopiridina'),
        ('Amitrol (3-amina-1,2,4-triazol','Amitrol (3-amina-1,2,4-triazol)'),
        ('Amônia (gás amoníaco','Amônia (gás amoníaco)'),
        ('Anidro sulfuroso (dióxido de enxofre','Anidro sulfuroso (dióxido de enxofre)'),
        ('Anidrido acético','Anidrido acético'),
        ('Anidrido ftálico','Anidrido ftálico'),
        ('Anidrido hexahidroftálico, todos os isômeros','Anidrido hexahidroftálico, todos os isômeros'),
        ('Anidrido maleico','Anidrido maleico'),
        ('Anidrido trimelítico','Anidrido trimelítico'),
        ('Anilina','Anilina'),
        ('o-Anisidina','o-Anisidina'),
        ('p-Anisidina','p-Anisidina'),
        ('Antimônio e seus compostos','Antimônio e seus compostos'),
        ('Antraceno','Antraceno'),
        ('ANTU','ANTU'),
        ('Argônio','Argônio'),
        ('Arseneto de gálio','Arseneto de gálio'),
        ('Arsênio e seus compostos (arsênico','Arsênio e seus compostos (arsênico)'),
        ('Arsina','Arsina'),
        ('Asbestos, todas as formas','Asbestos, todas as formas'),
        ('Asfalto (betume), fumos, como aerossol solúvel em benzeno','Asfalto (betume), fumos, como aerossol solúvel em benzeno'),
        ('Atrazine (e triazinas simétricas relacionadas','Atrazine (e triazinas simétricas relacionadas)'),
        ('Auramina','Auramina'),
        ('Azatioprina','Azatioprina'),
        ('Azida de sódio (como azida de sódio; como vapor de ácido hidrazoico','Azida de sódio (como azida de sódio; como vapor de ácido hidrazoico)'),
        ('Azinfos metil','Azinfos metil'),
        ('Bário e compostos solúveis','Bário e compostos solúveis'),
        ('Benomil','Benomil'),
        ('Benzeno e seus compostos tóxicos','Benzeno e seus compostos tóxicos'),
        ('Benzidina','Benzidina'),
        ('Benzo[a]antraceno','Benzo[a]antraceno'),
        ('Benzo[b]fluoranteno','Benzo[b]fluoranteno'),
        ('Benzopireno (benzo[a]pireno','Benzopireno (benzo[a]pireno)'),
        ('Berílio e seus compostos tóxicos (compostos solúveis e insolúveis','Berílio e seus compostos tóxicos (compostos solúveis e insolúveis)'),
        ('BHC (hexacloreto de benzeno ou hexaclorobenzeno','BHC (hexacloreto de benzeno ou hexaclorobenzeno)'),
        ('Bifenil','Bifenil'),
        ('Bifenis policlorados','Bifenis policlorados'),
        ('Biscloroetileter (éter dicloroetílico','Biscloroetileter (éter dicloroetílico)'),
        ('Bis (cloro metil) éter, clorometileter, éter bis (clorometílico) ou éter metílico de clorometila','Bis (cloro metil) éter, clorometileter, éter bis (clorometílico) ou éter metílico de clorometila'),
        ('Bissulfito de sódio','Bissulfito de sódio'),
        ('Borracha natural, látex como proteínas alergênicas inaláveis','Borracha natural, látex como proteínas alergênicas inaláveis'),
        ('Borato, compostos inorgânicos','Borato, compostos inorgânicos'),
        ('Bromacil','Bromacil'),
        ('Brometo de alila','Brometo de alila'),
        ('Brometo de etila (bromoetano','Brometo de etila (bromoetano)'),
        ('Brometo de metila (bromometano','Brometo de metila (bromometano)'),
        ('Bromo e seus compostos tóxicos','Bromo e seus compostos tóxicos'),
        ('1-Bromopropano','1-Bromopropano'),
        ('1,3-Butadieno','1,3-Butadieno'),
        ('Butadieno-estireno','Butadieno-estireno'),
        ('n-Butano','n-Butano'),
        ('Bussulfano (Myleran ou 1,4-butanodiol dimetanosulfonato','Bussulfano (Myleran ou 1,4-butanodiol dimetanosulfonato)'),
        ('Butenos, todos os isômeros','Butenos, todos os isômeros'),
        ('1-Butanotiol (n-Butil mercaptana','1-Butanotiol (n-Butil mercaptana)'),
        ('n-Butilamina','n-Butilamina'),
        ('o-sec Butilfenol','o-sec Butilfenol'),
        ('p-terc-Butiltolueno','p-terc-Butiltolueno'),
        ('2-Butóxi etanol (EGBE) (butil cellosolve) (éter monobutílico do etileno glicol','2-Butóxi etanol (EGBE) (butil cellosolve) (éter monobutílico do etileno glicol)'),
        ('Cádmio e seus compostos tóxicos','Cádmio e seus compostos tóxicos'),
        ('Canfeno clorado','Canfeno clorado'),
        ('Cânfora, sintética','Cânfora, sintética'),
        ('Caolim','Caolim'),
        ('Caprolactama','Caprolactama'),
        ('Captafol','Captafol'),
        ('Captan','Captan'),
        ('Carbaril','Carbaril'),
        ('Carbeto de silício','Carbeto de silício'),
        ('Carbofuran','Carbofuran'),
        ('Carvão mineral e seus derivados','Carvão mineral e seus derivados'),
        ('Catecol','Catecol'),
        ('Celulose','Celulose'),
        ('Cereais, poeira (aveia, cevada, trigo','Cereais, poeira (aveia, cevada, trigo)'),
        ('Ceteno','Ceteno'),
        ('Chumbo e seus compostos tóxicos','Chumbo e seus compostos tóxicos'),
        ('Chumbo tetraetila','Chumbo tetraetila'),
        ('Chumbo tetrametila','Chumbo tetrametila'),
        ('Cianamida','Cianamida'),
        ('Cianamida de cálcio','Cianamida de cálcio'),
        ('Cianoacrilato de etila','Cianoacrilato de etila'),
        ('2-Cianoacrilato de metila','2-Cianoacrilato de metila'),
        ('Cianogênio','Cianogênio'),
        ('Ciclofosfamida','Ciclofosfamida'),
        ('Ciclohexano','Ciclohexano'),
        ('Ciclohexanol','Ciclohexanol'),
        ('Ciclohexanona','Ciclohexanona'),
        ('Ciclohexeno','Ciclohexeno'),
        ('Ciclohexilamina','Ciclohexilamina'),
        ('Ciclonita','Ciclonita'),
        ('Ciclopentadieno','Ciclopentadieno'),
        ('Ciclopentano','Ciclopentano'),
        ('Ciclosporina','Ciclosporina'),
        ('Cihexatin','Cihexatin'),
        ('Cimento portland','Cimento portland'),
        ('Citral','Citral'),
        ('Clopidol','Clopidol'),
        ('Clorambucil (cloroambucil','Clorambucil (cloroambucil)'),
        ('Clordane','Clordane'),
        ('Cloreto de alila','Cloreto de alila'),
        ('Cloreto de amônio - fumos','Cloreto de amônio - fumos'),
        ('Cloreto de benzila','Cloreto de benzila'),
        ('Cloreto de benzoíla','Cloreto de benzoíla'),
        ('Cloreto de cianogênio','Cloreto de cianogênio'),
        ('Cloreto de cloroacetila','Cloreto de cloroacetila'),
        ('Cloreto de cromila','Cloreto de cromila'),
        ('Cloreto de dimetil carbamila','Cloreto de dimetil carbamila'),
        ('Cloreto de enxofre','Cloreto de enxofre'),
        ('Cloreto de etila (cloroetano','Cloreto de etila (cloroetano)'),
        ('Cloreto de fenila (clorobenzeno','Cloreto de fenila (clorobenzeno)'),
        ('Cloreto de metila','Cloreto de metila'),
        ('Cloreto de polivinila (PVC (policloreto de vinila','Cloreto de polivinila (PVC (policloreto de vinila))'),
        ('Cloreto de tionila','Cloreto de tionila'),
        ('Cloreto de vinila (cloroetílico','Cloreto de vinila (cloroetílico)'),
        ('Cloreto de vinilideno (1,1-Dicloreotileno','Cloreto de vinilideno (1,1-Dicloreotileno)'),
        ('Cloreto de zinco, fumos','Cloreto de zinco, fumos'),
        ('Clornafazina','Clornafazina'),
        ('Cloro e seus composto tóxicos','Cloro e seus composto tóxicos'),
        ('Cloroacetaldeído','Cloroacetaldeído'),
        ('2-Cloroacetofenona','2-Cloroacetofenona'),
        ('Cloroacetona','Cloroacetona'),
        ('o-Clorobenzilideno malononitrila','o-Clorobenzilideno malononitrila'),
        ('Clorobromometano','Clorobromometano'),
        ('Clorodifenil (42% de Cloro','Clorodifenil (42% de Cloro)'),
        ('Clorodifenil (54% de Cloro','Clorodifenil (54% de Cloro)'),
        ('Clorodifluormetano (freon 22','Clorodifluormetano (freon 22)'),
        ('o-Cloroestireno','o-Cloroestireno'),
        ('Clorofórmio (Triclorometano','Clorofórmio (Triclorometano)'),
        ('1-Cloro-1-nitropropano','1-Cloro-1-nitropropano'),
        ('Cloropentafluoretano','Cloropentafluoretano'),
        ('Cloropicrina','Cloropicrina'),
        ('Cloropirifos','Cloropirifos'),
        ('Cloropreno (Cloroprene','Cloropreno (Cloroprene)'),
        ('1-Cloro-2-propanol','1-Cloro-2-propanol'),
        ('2-Cloro-1-propanol','2-Cloro-1-propanol'),
        ('o-Clorotolueno','o-Clorotolueno'),
        ('Cobalto e seus compostos inorgânicos','Cobalto e seus compostos inorgânicos'),
        ('Cobalto carbonila','Cobalto carbonila'),
        ('Cobalto hidrocarbonila','Cobalto hidrocarbonila'),
        ('Cobre','Cobre'),
        ('Coumafos','Coumafos'),
        ('Cresol, todos os isômeros','Cresol, todos os isômeros'),
        ('Creosoto','Creosoto'),
        ('Criseno','Criseno'),
        ('Cromato de terc-butila','Cromato de terc-butila'),
        ('Cromato de cálcio','Cromato de cálcio'),
        ('Cromato de chumbo','Cromato de chumbo'),
        ('Cromato de estrôncio','Cromato de estrôncio'),
        ('Cromatos de zinco','Cromatos de zinco'),
        ('Cromita - processamento do minério (cromato','Cromita - processamento do minério (cromato)'),
        ('Cromo e seus compostos tóxicos (inclui metal e compostos de Cr III, compostos de Cr VI solúveis em água e compostos de Cr VI insolúveis','Cromo e seus compostos tóxicos (inclui metal e compostos de Cr III, compostos de Cr VI solúveis em água e compostos de Cr VI insolúveis)'),
        ('Crotonaldeído','Crotonaldeído'),
        ('Crufomate','Crufomate'),
        ('2,4 D','2,4 D'),
        ('DDD (diclorodifenildicloretano','DDD (diclorodifenildicloretano)'),
        ('DDT','DDT'),
        ('Decaborano','Decaborano'),
        ('Demeton (Systox','Demeton (Systox)'),
        ('Demeton-S-metila','Demeton-S-metila'),
        ('Destilação do alcatrão de hulha','Destilação do alcatrão de hulha'),
        ('Diacetil','Diacetil'),
        ('Diacetona álcool','Diacetona álcool'),
        ('Diamina m-xileno','Diamina m-xileno'),
        ('Dianizidina','Dianizidina'),
        ('Diazinon','Diazinon'),
        ('Diazometano','Diazometano'),
        ('Diborano','Diborano'),
        ('1,2-Dibramoetano (dibrometo de etileno','1,2-Dibramoetano (dibrometo de etileno)'),
        ('2-N-Dibutilaminoetanol','2-N-Dibutilaminoetanol'),
        ('Dibutilftalato (ftalato de dibutila','Dibutilftalato (ftalato de dibutila)'),
        ('Diciclopentadieno','Diciclopentadieno'),
        ('Dicloreto de propileno (1,2-Dicloropropano','Dicloreto de propileno (1,2-Dicloropropano)'),
        ('o-Diclorobenzeno','o-Diclorobenzeno'),
        ('p-Diclorobenzeno','p-Diclorobenzeno'),
        ('3,3-Dicloro-benzidina (Diclorobenzidina','3,3-Dicloro-benzidina (Diclorobenzidina)'),
        ('1,4-Dicloro-2-buteno','1,4-Dicloro-2-buteno'),
        ('Diclorodifluormetano','Diclorodifluormetano'),
        ('1,3-Dicloro-5,5-dimetil hidantoina','1,3-Dicloro-5,5-dimetil hidantoina'),
        ('1,1-Dicloroetano','1,1-Dicloroetano'),
        ('1,2 Dicloroetano (Dicloreto de etileno','1,2 Dicloroetano (Dicloreto de etileno)'),
        ('1,2 Dicloroetileno','1,2 Dicloroetileno'),
        ('Diclorofluormetano (freon 12','Diclorofluormetano (freon 12)'),
        ('Diclorometano (Cloreto de metileno','Diclorometano (Cloreto de metileno)'),
        ('1,1-Dicloro-1-nitroetano','1,1-Dicloro-1-nitroetano'),
        ('Dicloroacetileno','Dicloroacetileno'),
        ('1,3-Dicloropropeno','1,3-Dicloropropeno'),
        ('Diclorotetrafluoretano (freon 114','Diclorotetrafluoretano (freon 114)'),
        ('Diclorvos (DDVP','Diclorvos (DDVP)'),
        ('Dicrotofós','Dicrotofós'),
        ('Dieldrin','Dieldrin'),
        ('Dietanolamina','Dietanolamina'),
        ('Dietilamina','Dietilamina'),
        ('2-Dietilaminoetanol','2-Dietilaminoetanol'),
        ('Dietilcetona','Dietilcetona'),
        ('Dietil éter (Éter etílico','Dietil éter (Éter etílico)'),
        ('Dietileno triamina','Dietileno triamina'),
        ('Dietilestilbestrol','Dietilestilbestrol'),
        ('Dietilftalato (ftalato de dietila','Dietilftalato (ftalato de dietila)'),
        ('Dietilsulfato','Dietilsulfato'),
        ('Difenilamina','Difenilamina'),
        ('Difluordibromometano','Difluordibromometano'),
        ('Difluoreto de oxigênio','Difluoreto de oxigênio'),
        ('Pirperazina e sais (dihidrocloreto de piperazina','Pirperazina e sais (dihidrocloreto de piperazina)'),
        ('Diisobutil cetona','Diisobutil cetona'),
        ('Diisocianato de isoforona','Diisocianato de isoforona'),
        ('Diisocianato de tolueno (TDI) (2,4 Diisocianato de tolueno','Diisocianato de tolueno (TDI) (2,4 Diisocianato de tolueno)'),
        ('Diisopropilamina','Diisopropilamina'),
        ('N,N-Dietilhidroxilamina','N,N-Dietilhidroxilamina'),
        ('Dimetilacetamida (N,N-Dimetilacetamida','Dimetilacetamida (N,N-Dimetilacetamida)'),
        ('Dimetilamina','Dimetilamina'),
        ('Dimetilanilina','Dimetilanilina'),
        ('Dimetiletoxisilano','Dimetiletoxisilano'),
        ('Dimetilformamida','Dimetilformamida'),
        ('Dimetilftalato','Dimetilftalato'),
        ('1,1-Dimetil hidrazina','1,1-Dimetil hidrazina'),
        ('Dinitrato de etileno glicol','Dinitrato de etileno glicol'),
        ('Dinitrato de propileno glicol','Dinitrato de propileno glicol'),
        ('Dinitrobenzeno, todos os isômeros','Dinitrobenzeno, todos os isômeros'),
        ('Dinitro-o-cresol','Dinitro-o-cresol'),
        ('3,5-Dinitro-o-toluamida','3,5-Dinitro-o-toluamida'),
        ('Dinitrotolueno','Dinitrotolueno'),
        ('1,4-Dioxano','1,4-Dioxano'),
        ('Dioxation','Dioxation'),
        ('Dióxido de carbono (gás carbônico','Dióxido de carbono (gás carbônico)'),
        ('Dióxido de cloro','Dióxido de cloro'),
        ('1,3-Dioxolane','1,3-Dioxolane'),
        ('Dióxido de nitrogênio','Dióxido de nitrogênio'),
        ('Dióxido de titânio','Dióxido de titânio'),
        ('Dióxido de vinil ciclohexano','Dióxido de vinil ciclohexano'),
        ('Dipropil cetona','Dipropil cetona'),
        ('Diquat','Diquat'),
        ('Dissulfeto de alil propila','Dissulfeto de alil propila'),
        ('Dissulfeto de carbono','Dissulfeto de carbono'),
        ('Dissulfeto de dimetila','Dissulfeto de dimetila'),
        ('Dissulfiram','Dissulfiram'),
        ('Dissulfoton','Dissulfoton'),
        ('Diuron','Diuron'),
        ('Divinil benzeno','Divinil benzeno'),
        ('Dodecil mercaptana','Dodecil mercaptana'),
        ('Endosulfan','Endosulfan'),
        ('Endrin','Endrin'),
        ('Enflurano','Enflurano'),
        ('1-Cloro-2,3-Epoxipropano (epicloridrina','1-Cloro-2,3-Epoxipropano (epicloridrina)'),
        ('EPN','EPN'),
        ('Erionita','Erionita'),
        ('Estanho e seus compostos orgânicos','Estanho e seus compostos orgânicos'),
        ('Estanho - metal','Estanho - metal'),
        ('Estanho - compostos inorgânicos e óxido, exceto hidreto de estanho','Estanho - compostos inorgânicos e óxido, exceto hidreto de estanho'),
        ('Estireno (vinibenzeno','Estireno (vinibenzeno)'),
        ('Estriquinina','Estriquinina'),
        ('Etano','Etano'),
        ('Etanolamina','Etanolamina'),
        ('Éter alil glicidílico','Éter alil glicidílico'),
        ('Éter n-Butil glicidílico','Éter n-Butil glicidílico'),
        ('Éter diglicidílico','Éter diglicidílico'),
        ('Éter etil terc-butílico','Éter etil terc-butílico'),
        ('Éter fenílico, vapor','Éter fenílico, vapor'),
        ('Éter fenil glicidílico','Éter fenil glicidílico'),
        ('Éter isopropil glicidílico (IGE','Éter isopropil glicidílico (IGE)'),
        ('Éter isopropílico','Éter isopropílico'),
        ('Éter isopropílico de monoetileno glicol (2-isopropoxietanol','Éter isopropílico de monoetileno glicol (2-isopropoxietanol)'),
        ('Éter metil terc-amílico','Éter metil terc-amílico'),
        ('Éter metil terc-butílico (MTBE','Éter metil terc-butílico (MTBE)'),
        ('Éter metílico de dipropilenoglicol (2-Metoximetiletoxi) propanol (DPGME','Éter metílico de dipropilenoglicol (2-Metoximetiletoxi) propanol (DPGME))'),
        ('Éter monobutílico de dietileno glicol','Éter monobutílico de dietileno glicol'),
        ('Éter monometílico do etileno glicol (metil cellosolve ou 2-Metoxi etanol (EGME','Éter monometílico do etileno glicol (metil cellosolve ou 2-Metoxi etanol (EGME))'),
        ('Etil amil cetona','Etil amil cetona'),
        ('Etil butil cetona','Etil butil cetona'),
        ('Etil mercaptana (Etanotiol','Etil mercaptana (Etanotiol)'),
        ('n-Etil morfolina','n-Etil morfolina'),
        ('Etilamina','Etilamina'),
        ('Etilbenzeno (estilbenzeno','Etilbenzeno (estilbenzeno)'),
        ('Etileno','Etileno'),
        ('Etilenoamina','Etilenoamina'),
        ('Etilenotiureia','Etilenotiureia'),
        ('Etileno cloridrina','Etileno cloridrina'),
        ('Etileno diamina','Etileno diamina'),
        ('Etileno glicol','Etileno glicol'),
        ('Etilideno norborneno','Etilideno norborneno'),
        ('Etilenoimina','Etilenoimina'),
        ('Etilnitrosuréias','Etilnitrosuréias'),
        ('Etion','Etion'),
        ('Etoposide','Etoposide'),
        ('Etoposide em associação com cisplatina e bleomicina','Etoposide em associação com cisplatina e bleomicina'),
        ('2-Etoxietanol (cellosolve ou Éter monoetílico do etileno glicol','2-Etoxietanol (cellosolve ou Éter monoetílico do etileno glicol)'),
        ('Farinha (poeiras','Farinha (poeiras)'),
        ('Fenacetina','Fenacetina'),
        ('Fenamifos','Fenamifos'),
        ('n-Fenil-ß-naftilamina','n-Fenil-ß-naftilamina'),
        ('o-Fenileno diamina','o-Fenileno diamina'),
        ('m-Fenileno diamina','m-Fenileno diamina'),
        ('p-Fenileno diamina','p-Fenileno diamina'),
        ('Fenil isocianato','Fenil isocianato'),
        ('Fenilfosfina','Fenilfosfina'),
        ('Fenilhidrazina','Fenilhidrazina'),
        ('Fenil mercaptana','Fenil mercaptana'),
        ('Fenol','Fenol'),
        ('Fenotiazine','Fenotiazine'),
        ('Fensulfotion','Fensulfotion'),
        ('Fention','Fention'),
        ('Ferbam','Ferbam'),
        ('Ferro, sais solúveis','Ferro, sais solúveis'),
        ('Ferro diciclopentadienila','Ferro diciclopentadienila'),
        ('Ferro, óxido (Fe2O3','Ferro, óxido (Fe2O3)'),
        ('Ferro pentacarbonila','Ferro pentacarbonila'),
        ('Ferrovanádio, poeira','Ferrovanádio, poeira'),
        ('Fibras Vítreas Sintéticas - Fibras de vidro de filamento contínuo','Fibras Vítreas Sintéticas - Fibras de vidro de filamento contínuo'),
        ('Fibras Vítreas Sintéticas - Fibras de lã de vidro','Fibras Vítreas Sintéticas - Fibras de lã de vidro'),
        ('Fibras Vítreas Sintéticas - Fibras de lã de rocha','Fibras Vítreas Sintéticas - Fibras de lã de rocha'),
        ('Fibras Vítreas Sintéticas - Fibras de escória mineral','Fibras Vítreas Sintéticas - Fibras de escória mineral'),
        ('Fibras Vítreas Sintéticas - Fibras de vídeo finalidades especiais','Fibras Vítreas Sintéticas - Fibras de vídeo finalidades especiais'),
        ('Fibras Vítreas Sintéticas - Fibras cerâmicas refratárias','Fibras Vítreas Sintéticas - Fibras cerâmicas refratárias'),
        ('Flúor','Flúor'),
        ('Fluoracetato de sódio','Fluoracetato de sódio'),
        ('Fluoreto de carbonila','Fluoreto de carbonila'),
        ('Fluoreto de perclorila','Fluoreto de perclorila'),
        ('Fluoreto de sulfurila','Fluoreto de sulfurila'),
        ('Fluoreto de vinila','Fluoreto de vinila'),
        ('Fluoreto de vinilideno','Fluoreto de vinilideno'),
        ('Fonofos','Fonofos'),
        ('Forato','Forato'),
        ('Formaldeído (formol ou Aldeído fórmico','Formaldeído (formol ou Aldeído fórmico)'),
        ('Formamida','Formamida'),
        ('Formiato de etila','Formiato de etila'),
        ('Formiato de metila','Formiato de metila'),
        ('Fosfato de dibutila','Fosfato de dibutila'),
        ('Fosfato de dibutil fenila','Fosfato de dibutil fenila'),
        ('Fosfato de tributila','Fosfato de tributila'),
        ('Fosfato de trifenila','Fosfato de trifenila'),
        ('Fosfato de triortocresila','Fosfato de triortocresila'),
        ('Fosfina (fosfamina','Fosfina (fosfamina)'),
        ('Fosfito de trimetila','Fosfito de trimetila'),
        ('Fósforo e seus compostos tóxicos','Fósforo e seus compostos tóxicos'),
        ('Fosgênio (cloreto de carbonila','Fosgênio (cloreto de carbonila)'),
        ('Fluortriclorometano (triclorofluormetano ou freon 11','Fluortriclorometano (triclorofluormetano ou freon 11)'),
        ('Ftalato de di(2-etilhexila','Ftalato de di(2-etilhexila)'),
        ('m-Ftalodinitrila','m-Ftalodinitrila'),
        ('o-Ftalodinitrila','o-Ftalodinitrila'),
        ('Furfural','Furfural'),
        ('Gás mostarda','Gás mostarda'),
        ('Gás natural e seus derivados','Gás natural e seus derivados'),
        ('Gasolina','Gasolina'),
        ('Glicerina, névoas','Glicerina, névoas'),
        ('Glicidol','Glicidol'),
        ('Glioxal','Glioxal'),
        ('GLP (gás liquefeito do petróleo','GLP (gás liquefeito do petróleo)'),
        ('Glutaraldeído, ativado e não ativado','Glutaraldeído, ativado e não ativado'),
        ('Grafite (todas as formas, exceto fibras de grafite','Grafite (todas as formas, exceto fibras de grafite)'),
        ('Háfnio e seus compostos','Háfnio e seus compostos'),
        ('Halotano','Halotano'),
        ('Hélio','Hélio'),
        ('Heptacloro','Heptacloro'),
        ('Heptacloro epóxido','Heptacloro epóxido'),
        ('Heptano, todos os isômeros','Heptano, todos os isômeros'),
        ('Hexaclorobutadieno','Hexaclorobutadieno'),
        ('Hexaclorociclopentadieno','Hexaclorociclopentadieno'),
        ('Hexacloroetano','Hexacloroetano'),
        ('Hexacloronaftaleno','Hexacloronaftaleno'),
        ('Hexafluoracetona','Hexafluoracetona'),
        ('Hexafluorpropileno','Hexafluorpropileno'),
        ('Hexafluoreto de enxofre','Hexafluoreto de enxofre'),
        ('Hexafluoreto de selênio','Hexafluoreto de selênio'),
        ('Hexafluoreto de telúrio','Hexafluoreto de telúrio'),
        ('Hexametileno diisocianato (HDI','Hexametileno diisocianato (HDI)'),
        ('Hexametilfosforamida','Hexametilfosforamida'),
        ('n-Hexano','n-Hexano'),
        ('Hexano, outros isômeros que não o n-Hexano','Hexano, outros isômeros que não o n-Hexano'),
        ('1,6-Hexanodiamina','1,6-Hexanodiamina'),
        ('1-Hexeno','1-Hexeno'),
        ('Hexileno glicol','Hexileno glicol'),
        ('Hidrazina (diamina','Hidrazina (diamina)'),
        ('Hidreto de antimônio (Estibina','Hidreto de antimônio (Estibina)'),
        ('Hidreto de lítio','Hidreto de lítio'),
        ('Hidrocarbonetos alifáticos gasosos Alcanos','Hidrocarbonetos alifáticos gasosos Alcanos'),
        ('Hidrocarbonetos e outros compostos de carbono','Hidrocarbonetos e outros compostos de carbono'),
        ('Hidrocarbonetos aromáticos','Hidrocarbonetos aromáticos'),
        ('Hidrocarbonetos cíclicos','Hidrocarbonetos cíclicos'),
        ('Hidrogênio','Hidrogênio'),
        ('Hidroquinona','Hidroquinona'),
        ('Hidróxido de cálcio','Hidróxido de cálcio'),
        ('Hidróxido de césio','Hidróxido de césio'),
        ('Hidróxido de potássio','Hidróxido de potássio'),
        ('Hidróxido de sódio','Hidróxido de sódio'),
        ('Hidroxitolueno butilado','Hidroxitolueno butilado'),
        ('Indeno','Indeno'),
        ('Iodeto de metila','Iodeto de metila'),
        ('Índio e seus compostos','Índio e seus compostos'),
        ('Iodo','Iodo'),
        ('Iodofórmio','Iodofórmio'),
        ('Isobuteno','Isobuteno'),
        ('Isocianato de metila','Isocianato de metila'),
        ('Isoforona','Isoforona'),
        ('Isopropilamina','Isopropilamina'),
        ('n-Isopropilanilina','n-Isopropilanilina'),
        ('Isopropil benzeno (cumeno','Isopropil benzeno (cumeno)'),
        ('Ítrio e compostos','Ítrio e compostos'),
        ('Lactato de n-butila','Lactato de n-butila'),
        ('Lindano','Lindano'),
        ('Madeira, poeiras - Cedro Vermelho do Oeste','Madeira, poeiras - Cedro Vermelho do Oeste'),
        ('Madeira, poeiras - Todas as outras espécies','Madeira, poeiras - Todas as outras espécies'),
        ('Malation','Malation'),
        ('Manganês e seus compostos, poeira ','Manganês e seus compostos, poeira '),
        ('Manganês e seus compostos, fumos','Manganês e seus compostos, fumos'),
        ('Melfalano','Melfalano'),
        ('Mercaptanos','Mercaptanos'),
        ('Mercúrio e seus compostos','Mercúrio e seus compostos'),
        ('Metabisulfito de sódio','Metabisulfito de sódio'),
        ('Metacrilato de metila','Metacrilato de metila'),
        ('Metais duros contendo carboneto de tungstênio e cobalto','Metais duros contendo carboneto de tungstênio e cobalto'),
        ('Metano','Metano'),
        ('Metil acetileno','Metil acetileno'),
        ('Metil acetileno-propadieno, mistura (MAPP','Metil acetileno-propadieno, mistura (MAPP)'),
        ('Metilacrilonitrila','Metilacrilonitrila'),
        ('Metilal','Metilal'),
        ('Metilamina','Metilamina'),
        ('Metil n-amil cetona','Metil n-amil cetona'),
        ('n-Metil anilina','n-Metil anilina'),
        ('Metil n-butil cetona','Metil n-butil cetona'),
        ('Metil ciclohexano','Metil ciclohexano'),
        ('Metilciclohexanol','Metilciclohexanol'),
        ('o-Metilciclohexanona','o-Metilciclohexanona'),
        ('2-Metilciclopentadienil manganês tricarbonila','2-Metilciclopentadienil manganês tricarbonila'),
        ('Metil demeton','Metil demeton'),
        ('Metil etil cetona (MEK) (Butanona','Metil etil cetona (MEK) (Butanona)'),
        ('α-Metil estireno','α-Metil estireno'),
        ('Metil isoamil cetona','Metil isoamil cetona'),
        ('Metil isobutil cetona','Metil isobutil cetona'),
        ('Metil isopropil cetona','Metil isopropil cetona'),
        ('Metil mercaptana (metanotiol','Metil mercaptana (metanotiol)'),
        ('1-Metil naftaleno','1-Metil naftaleno'),
        ('2-Metil naftaleno','2-Metil naftaleno'),
        ('Metil paration (paration','Metil paration (paration)'),
        ('Metil propil cetona','Metil propil cetona'),
        ('Metil vinil cetona','Metil vinil cetona'),
        ('Metileno-bis-(4-ciclohexilisocianato','Metileno-bis-(4-ciclohexilisocianato)'),
        ('4,4-metileno-bis-(2-cloroanilina) (metileno-ortocloroanilina, MOCA®, MBOCA®','4,4-metileno-bis-(2-cloroanilina) (metileno-ortocloroanilina, MOCA®, MBOCA®)'),
        ('Metileno bisfenil isocianato (MDI','Metileno bisfenil isocianato (MDI)'),
        ('4,4''-Metileno dianilina','4,4''-Metileno dianilina'),
        ('Metomil','Metomil'),
        ('Metoxicloro','Metoxicloro'),
        ('4-Metoxifenol','4-Metoxifenol'),
        ('1-Metoxi-2-propanol','1-Metoxi-2-propanol'),
        ('Metoxsalen associado com radiação ultravioleta A','Metoxsalen associado com radiação ultravioleta A'),
        ('Monometil hidrazina (metil hidrazina','Monometil hidrazina (metil hidrazina)'),
        ('Metribuzin','Metribuzin'),
        ('Mevinfos','Mevinfos'),
        ('Mica','Mica'),
        ('Molibdênio - compostos solúveis','Molibdênio - compostos solúveis'),
        ('Molibdênio - metal e compostos insolúveis (fração inalável','Molibdênio - metal e compostos insolúveis (fração inalável)'),
        ('Molibdênio - metal e compostos insolúveis (fração respirável','Molibdênio - metal e compostos insolúveis (fração respirável)'),
        ('Monocrotofós','Monocrotofós'),
        ('Monóxido de carbono','Monóxido de carbono'),
        ('Morfolina','Morfolina'),
        ('Naftaleno','Naftaleno'),
        ('ß-Naftilamina (Betanaftilamina','ß-Naftilamina (Betanaftilamina)'),
        ('Naftóis (1-Naftol, 2-Naftol','Naftóis (1-Naftol, 2-Naftol)'),
        ('Naled','Naled'),
        ('Negro de fumo','Negro de fumo'),
        ('Neônio','Neônio'),
        ('Nicotina','Nicotina'),
        ('Níquel e seus compostos tóxicos (inclui níquel carbonila e níquel tetracarbonila','Níquel e seus compostos tóxicos (inclui níquel carbonila e níquel tetracarbonila)'),
        ('Nitrapirin','Nitrapirin'),
        ('Nitrato de n-propila','Nitrato de n-propila'),
        ('Nitrito de isobutila','Nitrito de isobutila'),
        ('p-Nitroanilina','p-Nitroanilina'),
        ('Nitrobenzeno','Nitrobenzeno'),
        ('p-Nitroclorobenzeno','p-Nitroclorobenzeno'),
        ('4-Nitrodifenil (4-Nitrodifenila','4-Nitrodifenil (4-Nitrodifenila)'),
        ('Nitroetano','Nitroetano'),
        ('Nitrogênio','Nitrogênio'),
        ('Nitroglicerina','Nitroglicerina'),
        ('Nitrometano','Nitrometano'),
        ('Nitronaftilamina','Nitronaftilamina'),
        ('1-Nitropropano','1-Nitropropano'),
        ('2-Nitropropano','2-Nitropropano'),
        ('Nitrosamina','Nitrosamina'),
        ('N-Nitrosodimetilamina','N-Nitrosodimetilamina'),
        ('4-(metilnitrosamino)-1-(3-piridil)1-butanona (NNK','4-(metilnitrosamino)-1-(3-piridil)1-butanona (NNK)'),
        ('Nitrotolueno, todos os isômeros','Nitrotolueno, todos os isômeros'),
        ('5-Nitro-o-toluidina','5-Nitro-o-toluidina'),
        ('Nonano','Nonano'),
        ('Octacloronaftaleno','Octacloronaftaleno'),
        ('Octano, todos os isômeros','Octano, todos os isômeros'),
        ('Óleo diesel, como hidrocarbonetos totais','Óleo diesel, como hidrocarbonetos totais'),
        ('Óleo mineral, excluídos os fluídos de trabalho com metais - Puro, alta e severamente refinado','Óleo mineral, excluídos os fluídos de trabalho com metais - Puro, alta e severamente refinado'),
        ('Óleo mineral, excluídos os fluídos de trabalho com metais - Refinação fraca ou média','Óleo mineral, excluídos os fluídos de trabalho com metais - Refinação fraca ou média'),
        ('Óleo queimado','Óleo queimado'),
        ('Ortotoluidina (o-toluidina','Ortotoluidina (o-toluidina)'),
        ('p,p''-Oxibis(benzeno sulfonila hidrazida','p,p''-Oxibis(benzeno sulfonila hidrazida)'),
        ('Oxicloreto de fósforo','Oxicloreto de fósforo'),
        ('Óxido de boro','Óxido de boro'),
        ('Óxido de cálcio','Óxido de cálcio'),
        ('Óxido de difenila o-clorada','Óxido de difenila o-clorada'),
        ('Óxido de etileno','Óxido de etileno'),
        ('Óxido de magnésio','Óxido de magnésio'),
        ('Óxido de mesitila','Óxido de mesitila'),
        ('Óxido de propileno','Óxido de propileno'),
        ('Óxido de zinco','Óxido de zinco'),
        ('Óxido nítrico','Óxido nítrico'),
        ('Óxido nitroso','Óxido nitroso'),
        ('Oximetalona','Oximetalona'),
        ('Ozona (ozônio','Ozona (ozônio)'),
        ('Parafina, cera (fumos','Parafina, cera (fumos)'),
        ('Paraquat, como o cátion','Paraquat, como o cátion'),
        ('Particulados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS) - respiráveis','Particulados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS) - respiráveis'),
        ('Pentaborano','Pentaborano'),
        ('Pentacloreto de fósforo','Pentacloreto de fósforo'),
        ('3,4,5,3,4-Pentaclorobifenil (PCB - 126','3,4,5,3,4-Pentaclorobifenil (PCB - 126)'),
        ('2,3,4,7,8-Pentaclorodibenzofurano','2,3,4,7,8-Pentaclorodibenzofurano'),
        ('Pentaclorofenol','Pentaclorofenol'),
        ('Pentacloronaftaleno','Pentacloronaftaleno'),
        ('Pentacloronitrobenzeno','Pentacloronitrobenzeno'),
        ('Pentaeritritol','Pentaeritritol'),
        ('Pentafluoreto de bromo','Pentafluoreto de bromo'),
        ('Pentafluoreto de enxofre','Pentafluoreto de enxofre'),
        ('n-Pentano','n-Pentano'),
        ('2,4-Pentanodiona','2,4-Pentanodiona'),
        ('Pentassulfeto de fósforo','Pentassulfeto de fósforo'),
        ('Pentóxido de vanádio','Pentóxido de vanádio'),
        ('Percloroetileno (Tetracloroetileno','Percloroetileno (Tetracloroetileno)'),
        ('Perclorometil mercaptana','Perclorometil mercaptana'),
        ('Perfluorobutil etileno','Perfluorobutil etileno'),
        ('Perfluorisobutileno','Perfluorisobutileno'),
        ('Perfluoroctanoato de amônio','Perfluoroctanoato de amônio'),
        ('Peróxido de benzoíla','Peróxido de benzoíla'),
        ('Peróxido de hidrogênio','Peróxido de hidrogênio'),
        ('Peróxido de metil etil cetona','Peróxido de metil etil cetona'),
        ('Persulfatos, como persulfato','Persulfatos, como persulfato'),
        ('Petróleo e seus derivados, exceto óleo diesel, gasolina, querosene e nafta','Petróleo e seus derivados, exceto óleo diesel, gasolina, querosene e nafta'),
        ('Picloram','Picloram'),
        ('Pindone','Pindone'),
        ('Piretro','Piretro'),
        ('Piridina','Piridina'),
        ('Pirofosfato de tetraetila','Pirofosfato de tetraetila'),
        ('Platina e sais solúveis - Metal','Platina e sais solúveis - Metal'),
        ('Platina e sais solúveis - Sais solúveis','Platina e sais solúveis - Sais solúveis'),
        ('Plutônio','Plutônio'),
        ('Poliisocianetos','Poliisocianetos'),
        ('Poliuretanas','Poliuretanas'),
        ('Prata e seus compostos - metal, poeira e fumos','Prata e seus compostos - metal, poeira e fumos'),
        ('Prata e seus compostos - compostos solúveis','Prata e seus compostos - compostos solúveis'),
        ('Procarbazina','Procarbazina'),
        ('n-propano (propano','n-propano (propano)'),
        ('Propanosultona (propano sultone','Propanosultona (propano sultone)'),
        ('Propileno','Propileno'),
        ('Propileno imina','Propileno imina'),
        ('ß-Propiolactona (beta-propiolactona ou betapropiolactona','ß-Propiolactona (beta-propiolactona ou betapropiolactona)'),
        ('Propionaldeído','Propionaldeído'),
        ('Propoxur','Propoxur'),
        ('Querosene combustível de avião, como vapor de hidrocarbonetos totais','Querosene combustível de avião, como vapor de hidrocarbonetos totais'),
        ('Quinona','Quinona'),
        ('Rádio-224 e seus produtos de decaimento','Rádio-224 e seus produtos de decaimento'),
        ('Rádio-226 e seus produtos de decaimento','Rádio-226 e seus produtos de decaimento'),
        ('Rádio-228 e seus produtos de decaimento','Rádio-228 e seus produtos de decaimento'),
        ('Radônio-222 e seus produtos de decaimento','Radônio-222 e seus produtos de decaimento'),
        ('Resina de vareta (eletrodo arame) de solda, produtos da decomposição térmica (breu','Resina de vareta (eletrodo arame) de solda, produtos da decomposição térmica (breu)'),
        ('Resorcinol','Resorcinol'),
        ('Ródio - metal e compostos insolúveis','Ródio - metal e compostos insolúveis'),
        ('Ródio - compostos solúveis','Ródio - compostos solúveis'),
        ('Ronel','Ronel'),
        ('Rotenona (comercial','Rotenona (comercial)'),
        ('Sacarose','Sacarose'),
        ('Seleneto de hidrogênio','Seleneto de hidrogênio'),
        ('Selênio e seus compostos','Selênio e seus compostos'),
        ('Semustina [1-(2 -cloroetil) -3-(4-metilciclohexil)-1-nitrosourea, Metil CC- NU','Semustina [1-(2 -cloroetil) -3-(4-metilciclohexil)-1-nitrosourea, Metil CC- NU]'),
        ('Sesone','Sesone'),
        ('Sílica livre (sílica livre cristalizada) - poeira respirável','Sílica livre (sílica livre cristalizada) - poeira respirável'),
        ('Sílica cristobalita','Sílica cristobalita'),
        ('Silicato de cálcio, sintético não fibroso','Silicato de cálcio, sintético não fibroso'),
        ('Salicilato de etila','Salicilato de etila'),
        ('Salicilato de metila','Salicilato de metila'),
        ('Silicatos','Silicatos'),
        ('Simazine','Simazine'),
        ('Subtilisins, como 100% enzima cristalina ativa cristalina','Subtilisins, como 100% enzima cristalina ativa cristalina'),
        ('Sulfamato de amônio','Sulfamato de amônio'),
        ('Sulfato de bário','Sulfato de bário'),
        ('Sulfato de cálcio','Sulfato de cálcio'),
        ('Sulfato de dimetila (dimetilsulfato','Sulfato de dimetila (dimetilsulfato)'),
        ('Sulfato de carbonila','Sulfato de carbonila'),
        ('Sulfeto de hidrogênio (Gás sulfídrico','Sulfeto de hidrogênio (Gás sulfídrico)'),
        ('Sulfeto de dimetila','Sulfeto de dimetila'),
        ('Sulfeto de níquel','Sulfeto de níquel'),
        ('Sulfometuron metil','Sulfometuron metil'),
        ('Sulfotep (TEDP','Sulfotep (TEDP)'),
        ('Sulprofos','Sulprofos'),
        ('2,4,5-T','2,4,5-T'),
        ('Talco','Talco'),
        ('Tálio','Tálio'),
        ('Tamoxifeno ','Tamoxifeno '),
        ('Telureto de bismuto - não aditivado, como Bi2Te3 ','Telureto de bismuto - não aditivado, como Bi2Te3 '),
        ('Telureto de bismuto - aditivado com Se, como Bi2Te3','Telureto de bismuto - aditivado com Se, como Bi2Te3'),
        ('Telúrio e compostos (NOS), como Te, excluído telureto de hidrogênio','Telúrio e compostos (NOS), como Te, excluído telureto de hidrogênio'),
        ('Temefós','Temefós'),
        ('Terbufos','Terbufos'),
        ('Terebentina e monoterpenos selecionados','Terebentina e monoterpenos selecionados'),
        ('Terfenilas (o,m,p-isômeros','Terfenilas (o,m,p-isômeros)'),
        ('Terfenilas hidrogenadas (não irradiadas','Terfenilas hidrogenadas (não irradiadas)'),
        ('Tetrabrometo de acetileno (1,1,2,2-Tetrabromoetano','Tetrabrometo de acetileno (1,1,2,2-Tetrabromoetano)'),
        ('Tetrabrometo de carbono','Tetrabrometo de carbono'),
        ('Tetracloreto de carbono','Tetracloreto de carbono'),
        ('2,3,7,8-Tetraclorodibenzo-para-dioxina','2,3,7,8-Tetraclorodibenzo-para-dioxina'),
        ('1,1,1,2-Tetracloro-2,2-difluoretano','1,1,1,2-Tetracloro-2,2-difluoretano'),
        ('1,1,2,2-Tetracloro-1,2-difluoretano','1,1,2,2-Tetracloro-1,2-difluoretano'),
        ('Tetracloroetano (1,1,2,2-Tetracloroetano','Tetracloroetano (1,1,2,2-Tetracloroetano)'),
        ('Tetracloronaftaleno','Tetracloronaftaleno'),
        ('Tetrafluoretileno','Tetrafluoretileno'),
        ('Tetrafluoreto de enxofre','Tetrafluoreto de enxofre'),
        ('Tetrahidreto de germânio','Tetrahidreto de germânio'),
        ('Tetrahidreto de silício','Tetrahidreto de silício'),
        ('Tetrahidrofurano','Tetrahidrofurano'),
        ('Tetraquis (hidroximetil) fosfônio, sais - Cloreto de tetraquis (hidroximetil) fosfônio','Tetraquis (hidroximetil) fosfônio, sais - Cloreto de tetraquis (hidroximetil) fosfônio'),
        ('Tetraquis (hidroximetil) fosfônio, sais - Sulfato de tetraquis (hidroximetil) fosfônio','Tetraquis (hidroximetil) fosfônio, sais - Sulfato de tetraquis (hidroximetil) fosfônio'),
        ('Tetrametil succinonitrila','Tetrametil succinonitrila'),
        ('Tetranitrometano','Tetranitrometano'),
        ('Tetril','Tetril'),
        ('Tetróxido de ósmio','Tetróxido de ósmio'),
        ('Thiram','Thiram'),
        ('Tiotepa','Tiotepa'),
        ('Titânio','Titânio'),
        ('4,4''-Tiobis (6-terc-butil-m-cresol','4,4''-Tiobis (6-terc-butil-m-cresol)'),
        ('o-Tolidina','o-Tolidina'),
        ('Tolueno (toluol','Tolueno (toluol)'),
        ('m-Toluidina','m-Toluidina'),
        ('p-Toluidina','p-Toluidina'),
        ('Tório-232 e seus produtos de decaimento','Tório-232 e seus produtos de decaimento'),
        ('Tribrometo de boro','Tribrometo de boro'),
        ('Tricloreto de boro','Tricloreto de boro'),
        ('Tribromometano (Bromofórmio','Tribromometano (Bromofórmio)'),
        ('Tricloreto de fósforo','Tricloreto de fósforo'),
        ('Triclorfon','Triclorfon'),
        ('Triclorometil benzeno','Triclorometil benzeno'),
        ('1,1,2-Tricloro-1,2,2-trifluoretano (freon 113','1,1,2-Tricloro-1,2,2-trifluoretano (freon 113)'),
        ('1,2,4-Triclorobenzeno','1,2,4-Triclorobenzeno'),
        ('1,1,1 Tricloroetano (Metilclorofórmio','1,1,1 Tricloroetano (Metilclorofórmio)'),
        ('1,1,2-Tricloroetano (Tricloreto de vinila','1,1,2-Tricloroetano (Tricloreto de vinila)'),
        ('Tricloroetileno','Tricloroetileno'),
        ('Tricloronaftaleno','Tricloronaftaleno'),
        ('1,2,3-Tricloropropano','1,2,3-Tricloropropano'),
        ('Trietanolamina','Trietanolamina'),
        ('Trietilamina','Trietilamina'),
        ('Trifluorbromometano','Trifluorbromometano'),
        ('Trifluoreto de boro','Trifluoreto de boro'),
        ('Trifluoreto de cloro','Trifluoreto de cloro'),
        ('Trifluoreto de nitrogênio','Trifluoreto de nitrogênio'),
        ('1,3,5-Triglicidil-s-triazinetriona','1,3,5-Triglicidil-s-triazinetriona'),
        ('Trimetilamina','Trimetilamina'),
        ('Trimetil benzeno (mistura de isômeros','Trimetil benzeno (mistura de isômeros)'),
        ('2,4,6-Trinitrotolueno','2,4,6-Trinitrotolueno'),
        ('Trióxido de antimônio','Trióxido de antimônio'),
        ('Tungstênio - compostos solúveis','Tungstênio - compostos solúveis'),
        ('Tungstênio - metal e compostos insolúveis','Tungstênio - metal e compostos insolúveis'),
        ('Urânio (natural) compostos solúveis e insolúveis','Urânio (natural) compostos solúveis e insolúveis'),
        ('n-Valeraldeído','n-Valeraldeído'),
        ('4-Vinilciclohexeno','4-Vinilciclohexeno'),
        ('n-Vinil-2-pirrolidone','n-Vinil-2-pirrolidone'),
        ('Vinil tolueno','Vinil tolueno'),
        ('Warfarin (Varfarina','Warfarin (Varfarina)'),
        ('Xileno (xilol','Xileno (xilol)'),
        ('Xilidina (mistura de isômeros','Xilidina (mistura de isômeros)'),
        ('Xisto betuminoso e seus derivados','Xisto betuminoso e seus derivados'),
        ('Zircônio e compostos','Zircônio e compostos'),
        ('Hormônios sexuais femininos (apenas para homens','Hormônios sexuais femininos (apenas para homens)'),
        ('4-Dimetil-aminoazobenzeno','4-Dimetil-aminoazobenzeno'),
        ('N''-Nitrosonornicotina (NNN','N''-Nitrosonornicotina (NNN)'),
        ('Sílica livre (sílica livre cristalizada) - poeira total','Sílica livre (sílica livre cristalizada) - poeira total'),
        ('Particulados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS) - não respiráveis','Particulados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS) - não respiráveis'),
        ('Outros','Outros'),
        ('Agentes biológicos infecciosos e infectocontagiosos (bactérias, vírus, protozoários, fungos, príons, parasitas e outros','Agentes biológicos infecciosos e infectocontagiosos (bactérias, vírus, protozoários, fungos, príons, parasitas e outros)'),
        ('Outros','Outros'),
        ('Trabalho em posturas incômodas ou pouco confortáveis por longos períodos','Trabalho em posturas incômodas ou pouco confortáveis por longos períodos'),
        ('Postura sentada por longos períodos','Postura sentada por longos períodos'),
        ('Postura de pé por longos períodos','Postura de pé por longos períodos'),
        ('Frequente deslocamento a pé durante a jornada de trabalho','Frequente deslocamento a pé durante a jornada de trabalho'),
        ('Trabalho com esforço físico intenso','Trabalho com esforço físico intenso'),
        ('Levantamento e transporte manual de cargas ou volumes','Levantamento e transporte manual de cargas ou volumes'),
        ('Frequente ação de puxar/empurrar cargas ou volumes','Frequente ação de puxar/empurrar cargas ou volumes'),
        ('Frequente execução de movimentos repetitivos','Frequente execução de movimentos repetitivos'),
        ('Manuseio de ferramentas e/ou objetos pesados por longos períodos','Manuseio de ferramentas e/ou objetos pesados por longos períodos'),
        ('Exigência de uso frequente de força, pressão, preensão, flexão, extensão ou torção dos segmentos corporais','Exigência de uso frequente de força, pressão, preensão, flexão, extensão ou torção dos segmentos corporais'),
        ('Compressão de partes do corpo por superfícies rígidas ou com quinas','Compressão de partes do corpo por superfícies rígidas ou com quinas'),
        ('Exigência de flexões de coluna vertebral frequentes','Exigência de flexões de coluna vertebral frequentes'),
        ('Uso frequente de pedais','Uso frequente de pedais'),
        ('Uso frequente de alavancas','Uso frequente de alavancas'),
        ('Exigência de elevação frequente de membros superiores','Exigência de elevação frequente de membros superiores'),
        ('Manuseio ou movimentação de cargas e volumes sem pega ou com “pega pobre”','Manuseio ou movimentação de cargas e volumes sem pega ou com “pega pobre”'),
        ('Exposição a vibração de corpo inteiro','Exposição a vibração de corpo inteiro'),
        ('Exposição a vibrações localizadas (mão-braço','Exposição a vibrações localizadas (mão-braço)'),
        ('Uso frequente de escadas','Uso frequente de escadas'),
        ('Trabalho intensivo com teclado ou outros dispositivos de entrada de dados','Trabalho intensivo com teclado ou outros dispositivos de entrada de dados'),
        ('Outros','Outros'),
        ('Posto de trabalho improvisado','Posto de trabalho improvisado'),
        ('Mobiliário sem meios de regulagem de ajuste','Mobiliário sem meios de regulagem de ajuste'),
        ('Equipamentos e/ou máquinas sem meios de regulagem de ajuste ou sem condições de uso','Equipamentos e/ou máquinas sem meios de regulagem de ajuste ou sem condições de uso'),
        ('Posto de trabalho não planejado/adaptado para a posição sentada','Posto de trabalho não planejado/adaptado para a posição sentada'),
        ('Assento inadequado ','Assento inadequado '),
        ('Encosto do assento inadequado ou ausente','Encosto do assento inadequado ou ausente'),
        ('Mobiliário ou equipamento sem espaço para movimentação de segmentos corporais','Mobiliário ou equipamento sem espaço para movimentação de segmentos corporais'),
        ('Trabalho com necessidade de alcançar objetos, documentos, controles ou qualquer ponto além das zonas de alcance ideais para as características antropométricas do trabalhador','Trabalho com necessidade de alcançar objetos, documentos, controles ou qualquer ponto além das zonas de alcance ideais para as características antropométricas do trabalhador'),
        ('Equipamentos ou mobiliários não adaptados à antropometria do trabalhador','Equipamentos ou mobiliários não adaptados à antropometria do trabalhador'),
        ('Outros','Outros'),
        ('Trabalho realizado sem pausas pré-definidas para descanso','Trabalho realizado sem pausas pré-definidas para descanso'),
        ('Necessidade de manter ritmos intensos de trabalho','Necessidade de manter ritmos intensos de trabalho'),
        ('Trabalho com necessidade de variação de turnos ','Trabalho com necessidade de variação de turnos '),
        ('Monotonia ','Monotonia '),
        ('Trabalho noturno','Trabalho noturno'),
        ('Insuficiência de capacitação para execução da tarefa','Insuficiência de capacitação para execução da tarefa'),
        ('Trabalho com utilização rigorosa de metas de produção','Trabalho com utilização rigorosa de metas de produção'),
        ('Trabalho remunerado por produção','Trabalho remunerado por produção'),
        ('Cadência do trabalho imposta por um equipamento','Cadência do trabalho imposta por um equipamento'),
        ('Desequilíbrio entre tempo de trabalho e tempo de repouso','Desequilíbrio entre tempo de trabalho e tempo de repouso'),
        ('Outros','Outros'),
        ('Condições de trabalho com níveis de pressão sonora fora dos parâmetros de conforto','Condições de trabalho com níveis de pressão sonora fora dos parâmetros de conforto'),
        ('Condições de trabalho com índice de temperatura efetiva fora dos parâmetros de conforto','Condições de trabalho com índice de temperatura efetiva fora dos parâmetros de conforto'),
        ('Condições de trabalho com velocidade do ar fora dos parâmetros de conforto','Condições de trabalho com velocidade do ar fora dos parâmetros de conforto'),
        ('Condições de trabalho com umidade do ar fora dos parâmetros de conforto','Condições de trabalho com umidade do ar fora dos parâmetros de conforto'),
        ('Condições de trabalho com Iluminação diurna inadequada ','Condições de trabalho com Iluminação diurna inadequada '),
        ('Condições de trabalho com Iluminação noturna inadequada ','Condições de trabalho com Iluminação noturna inadequada '),
        ('Presença de reflexos em telas, painéis, vidros, monitores ou qualquer superfície, que causem desconforto ou prejudiquem a visualização','Presença de reflexos em telas, painéis, vidros, monitores ou qualquer superfície, que causem desconforto ou prejudiquem a visualização'),
        ('Piso escorregadio e/ou irregular','Piso escorregadio e/ou irregular'),
        ('Outros','Outros'),
        ('Excesso de situações de estresse','Excesso de situações de estresse'),
        ('Situações de sobrecarga de trabalho mental','Situações de sobrecarga de trabalho mental'),
        ('Exigência de alto nível de concentração, atenção e memória','Exigência de alto nível de concentração, atenção e memória'),
        ('Trabalho em condições de difícil comunicação','Trabalho em condições de difícil comunicação'),
        ('Excesso de conflitos hierárquicos no trabalho','Excesso de conflitos hierárquicos no trabalho'),
        ('Excesso de demandas emocionais/afetivas no trabalho','Excesso de demandas emocionais/afetivas no trabalho'),
        ('Assédio de qualquer natureza no trabalho','Assédio de qualquer natureza no trabalho'),
        ('Trabalho com demandas divergentes (ordens divergentes, metas incompatíveis entre si, exigência de qualidade X quantidade, entre outras','Trabalho com demandas divergentes (ordens divergentes, metas incompatíveis entre si, exigência de qualidade X quantidade, entre outras)'),
        ('Exigência de realização de múltiplas tarefas, com alta demanda cognitiva','Exigência de realização de múltiplas tarefas, com alta demanda cognitiva'),
        ('Insatisfação no trabalho','Insatisfação no trabalho'),
        ('Falta de autonomia no trabalho','Falta de autonomia no trabalho'),
        ('Outros','Outros'),
        ('Diferença de nível menor ou igual a dois metros','Diferença de nível menor ou igual a dois metros'),
        ('Diferença de nível maior que dois metros','Diferença de nível maior que dois metros'),
        ('Iluminação diurna inadequada ','Iluminação diurna inadequada '),
        ('Iluminação noturna inadequada ','Iluminação noturna inadequada '),
        ('Condições ou procedimentos que possam provocar contato com eletricidade','Condições ou procedimentos que possam provocar contato com eletricidade'),
        ('Arranjo físico deficiente ou inadequado','Arranjo físico deficiente ou inadequado'),
        ('Máquinas e equipamentos sem proteção','Máquinas e equipamentos sem proteção'),
        ('Armazenamento inadequado','Armazenamento inadequado'),
        ('Ferramentas necessitando de ajustes e manutenção','Ferramentas necessitando de ajustes e manutenção'),
        ('Ferramentas inadequadas','Ferramentas inadequadas'),
        ('Ambientes com risco de engolfamento','Ambientes com risco de engolfamento'),
        ('Ambientes com risco de afogamento','Ambientes com risco de afogamento'),
        ('Áreas classificadas','Áreas classificadas'),
        ('Queda de objetos','Queda de objetos'),
        ('Intempéries','Intempéries'),
        ('Ambientes com risco de soterramento','Ambientes com risco de soterramento'),
        ('Animais peçonhentos','Animais peçonhentos'),
        ('Animais domésticos','Animais domésticos'),
        ('Animais selvagens','Animais selvagens'),
        ('Mobiliário e/ou superfícies com quinas vivas, rebarbas ou elementos de fixação expostos','Mobiliário e/ou superfícies com quinas vivas, rebarbas ou elementos de fixação expostos'),
        ('Pisos, passagens, passarelas, plataformas, rampas e corredores com saliências, descontinuidades, aberturas ou obstruções, ou escorregadios','Pisos, passagens, passarelas, plataformas, rampas e corredores com saliências, descontinuidades, aberturas ou obstruções, ou escorregadios'),
        ('Escadas e rampas inadequadas','Escadas e rampas inadequadas'),
        ('Superfícies e/ou materiais aquecidos expostos','Superfícies e/ou materiais aquecidos expostos'),
        ('Superfícies e/ou materiais em baixa temperatura expostos','Superfícies e/ou materiais em baixa temperatura expostos'),
        ('Áreas de trânsito de pedestres sem demarcação','Áreas de trânsito de pedestres sem demarcação'),
        ('Áreas de trânsito de veículos sem demarcação','Áreas de trânsito de veículos sem demarcação'),
        ('Áreas de movimentação de materiais sem demarcação','Áreas de movimentação de materiais sem demarcação'),
        ('Condução de veículos de qualquer natureza em vias públicas','Condução de veículos de qualquer natureza em vias públicas'),
        ('Objetos cortantes e/ou perfurocortantes','Objetos cortantes e/ou perfurocortantes'),
        ('Movimentação de materiais','Movimentação de materiais'),
        ('Máquinas e equipamentos necessitando ajustes e manutenção','Máquinas e equipamentos necessitando ajustes e manutenção'),
        ('Procedimentos de ajuste, limpeza, manutenção e inspeção deficientes ou inexistentes','Procedimentos de ajuste, limpeza, manutenção e inspeção deficientes ou inexistentes'),
        ('Outros','Outros'),
        ('Condições perigosas previstas na legislação trabalhista','Condições perigosas previstas na legislação trabalhista'),
        ('Associação de fatores de risco prevista na legislação previdenciária para fins de aposentadoria especial','Associação de fatores de risco prevista na legislação previdenciária para fins de aposentadoria especial'),
        ('Umidade','Umidade'),
        ('Ausência de Fator de Risco','Ausência de Fator de Risco'),
    )

    tipo_risco = models.ForeignKey(Tiporisco, on_delete=models.CASCADE)
    descricao_perigo = models.CharField(max_length=250, choices=choice_perigo)

    def __str__(self):
        return f"{self.descricao_perigo}"

    class Meta:
        verbose_name = "descricao_perigo"
        verbose_name_plural = "descricao_perigos"
        ordering = ['descricao_perigo']
class Lesoes(models.Model):
    choice_lesao = (
            ('Lesão imediata','Lesão imediata'),
            ('Escoriação, abrasão (ferimento superficial','Escoriação, abrasão (ferimento superficial)'),
            ('Corte, laceração, ferida contusa, punctura (ferida aberta','Corte, laceração, ferida contusa, punctura (ferida aberta)'),
            ('Contusão, esmagamento (superfície cutânea intacta','Contusão, esmagamento (superfície cutânea intacta)'),
            ('Distensão, torção','Distensão, torção'),
            ('Inflamação de articulação, tendão ou músculo - inclui sinovite, tenossionovite, etc. Não inclui distensão, torção ou suas consequências','Inflamação de articulação, tendão ou músculo - inclui sinovite, tenossionovite, etc. Não inclui distensão, torção ou suas consequências'),
            ('Luxação','Luxação'),
            ('Fratura','Fratura'),
            ('Queimadura ou escaldadura - efeito de temperatura elevada. Efeito do contato com substância quente. Inclui queimadura por eletricidade, mas não inclui choque elétrico. Não inclui queimadura por substância química, efeito de radiação, queimadura de sol, incapacidade sistêmica como intermação, queimadura por atrito, etc','Queimadura ou escaldadura - efeito de temperatura elevada. Efeito do contato com substância quente. Inclui queimadura por eletricidade, mas não inclui choque elétrico. Não inclui queimadura por substância química, efeito de radiação, queimadura de sol, incapacidade sistêmica como intermação, queimadura por atrito, etc.'),
            ('Queimadura química (lesão de tecido provocada pela ação corrosiva de produto químico, suas emanações, etc','Queimadura química (lesão de tecido provocada pela ação corrosiva de produto químico, suas emanações, etc.)'),
            ('Efeito de radiação (imediato) - queimadura de sol e toda forma de lesão de tecido, osso ou fluido orgânico, por exposição à radiação','Efeito de radiação (imediato) - queimadura de sol e toda forma de lesão de tecido, osso ou fluido orgânico, por exposição à radiação'),
            ('Congelamento, geladura e outros efeitos da exposição à baixa temperatura','Congelamento, geladura e outros efeitos da exposição à baixa temperatura'),
            ('Asfixia, estrangulamento, afogamento','Asfixia, estrangulamento, afogamento'),
            ('Intermação, insolação, cãibra, exaustão e outros efeitos da temperatura ambiente elevada - não inclui queimadura de sol ou outros efeitos de radiação','Intermação, insolação, cãibra, exaustão e outros efeitos da temperatura ambiente elevada - não inclui queimadura de sol ou outros efeitos de radiação'),
            ('Choque elétrico e eletroplessão (eletrocussão','Choque elétrico e eletroplessão (eletrocussão)'),
            ('Hérnia de qualquer natureza, ruptura','Hérnia de qualquer natureza, ruptura'),
            ('Amputação ou enucleação','Amputação ou enucleação'),
            ('Perda ou diminuição de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão','Perda ou diminuição de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
            ('Concussão cerebral','Concussão cerebral'),
            ('Lesão imediata, NIC','Lesão imediata, NIC'),
            ('Doença contagiosa ou infecciosa (tuberculose, brucelose, etc','Doença contagiosa ou infecciosa (tuberculose, brucelose, etc.)'),
            ('Pneumoconiose (silicose, asbestose, etc','Pneumoconiose (silicose, asbestose, etc.)'),
            ('Dermatose (erupção, inflamação da pele, inclusive furúnculo, etc.). Geralmente provocada pelo contato direto com substâncias ou agentes sensibilizantes ou irritantes, tais como medicamentos, óleos, agentes biológicos, plantas, madeiras ou metais. Não inclui lesão provocada pela ação corrosiva de produtos químicos, queimadura por contato com substâncias quentes, efeito de exposição à radiação, efeito de exposição a baixas temperaturas ou inflamação ou irritação causada por fricção ou impacto','Dermatose (erupção, inflamação da pele, inclusive furúnculo, etc.). Geralmente provocada pelo contato direto com substâncias ou agentes sensibilizantes ou irritantes, tais como medicamentos, óleos, agentes biológicos, plantas, madeiras ou metais. Não inclui lesão provocada pela ação corrosiva de produtos químicos, queimadura por contato com substâncias quentes, efeito de exposição à radiação, efeito de exposição a baixas temperaturas ou inflamação ou irritação causada por fricção ou impacto'),
            ('Envenenamento sistêmico - condição mórbida sistêmica provocada por inalação, ingestão ou absorção cutânea de substância tóxica, que afete o metabolismo, o funcionamento do sistema nervoso, do aparelho circulatório, do aparelho digestivo, do aparelho respiratório, dos órgãos de excreção, do sistema músculoesquelético, etc., inclui ação de produto químico, medicamento, metal ou peçonha. Não inclui efeito de radiação, pneumoconiose, efeito corrosivo de produto químico, irritação cutânea, septicemia ou caso de ferida infectada','Envenenamento sistêmico - condição mórbida sistêmica provocada por inalação, ingestão ou absorção cutânea de substância tóxica, que afete o metabolismo, o funcionamento do sistema nervoso, do aparelho circulatório, do aparelho digestivo, do aparelho respiratório, dos órgãos de excreção, do sistema músculoesquelético, etc., inclui ação de produto químico, medicamento, metal ou peçonha. Não inclui efeito de radiação, pneumoconiose, efeito corrosivo de produto químico, irritação cutânea, septicemia ou caso de ferida infectada'),
            ('Perda ou diminuição mediatas de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão','Perda ou diminuição mediatas de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
            ('Efeito de radiação (mediato) - queimadura do sol e toda forma de lesão de tecido, osso, ou fluido orgânico por exposição à radiação','Efeito de radiação (mediato) - queimadura do sol e toda forma de lesão de tecido, osso, ou fluido orgânico por exposição à radiação.'),
            ('Doença, NIC','Doença, NIC'),
            ('Lesões múltiplas','Lesões múltiplas'),
            ('Outras lesões, NIC','Outras lesões, NIC'),
    )
    descricao_lesao = models.CharField(max_length=2000, choices=choice_lesao)

    def __str__(self):
        return self.descricao_lesao
    
    class Meta:
        verbose_name = "lesao"
        verbose_name_plural = "lesoes"
        ordering = ['descricao_lesao']
class Fonterisco(models.Model):
    choice_fonte = (
        ('Impacto de pessoa contra objeto parado. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior','Impacto de pessoa contra objeto parado. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'),
        ('Impacto de pessoa contra objeto em movimento. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior','Impacto de pessoa contra objeto em movimento. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'),
        ('Impacto sofrido por pessoa, de objeto que cai. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato','Impacto sofrido por pessoa, de objeto que cai. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
        ('Impacto sofrido por pessoa, de objeto projetado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato','Impacto sofrido por pessoa, de objeto projetado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
        ('Impacto sofrido por pessoa, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato','Impacto sofrido por pessoa, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
        ('Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus não permitem o apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus não permitem o apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa com diferença de nível de material empilhado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível de material empilhado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa com diferença de nível de veículo. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível de veículo. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa com diferença de nível em escada permanente cujos degraus permitem apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível em escada permanente cujos degraus permitem apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc. (da borda da abertura). Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc. (da borda da abertura). Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa com diferença de nível, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior','Queda de pessoa com diferença de nível, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('Queda de pessoa em mesmo nível em passagem ou superfície de sustentação. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado','Queda de pessoa em mesmo nível em passagem ou superfície de sustentação. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
        ('Queda de pessoa em mesmo nível sobre ou contra alguma coisa. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado','Queda de pessoa em mesmo nível sobre ou contra alguma coisa. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
        ('Queda de pessoa em mesmo nível, NIC. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado','Queda de pessoa em mesmo nível, NIC. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
        ('Aprisionamento em, sob ou entre objetos em movimento convergente (calandra) ou de encaixe. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre','Aprisionamento em, sob ou entre objetos em movimento convergente (calandra) ou de encaixe. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('Aprisionamento em, sob ou entre um objeto parado e outro em movimento. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre','Aprisionamento em, sob ou entre um objeto parado e outro em movimento. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('Aprisionamento em, sob ou entre dois ou mais objetos em movimento (sem encaixe). Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre','Aprisionamento em, sob ou entre dois ou mais objetos em movimento (sem encaixe). Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('Aprisionamento em, sob ou entre desabamento ou desmoronamento de edificação, barreira, etc. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre','Aprisionamento em, sob ou entre desabamento ou desmoronamento de edificação, barreira, etc. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('Aprisionamento em, sob ou entre, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre','Aprisionamento em, sob ou entre, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto (não em vibração). Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão','Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto (não em vibração). Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('Atrito ou abrasão por manusear objeto (não em vibração).  Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão','Atrito ou abrasão por manusear objeto (não em vibração).  Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('Atrito ou abrasão por objeto em vibração. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão','Atrito ou abrasão por objeto em vibração. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('Atrito ou abrasão por corpo estranho no olho. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão','Atrito ou abrasão por corpo estranho no olho. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('Atrito ou abrasão por compressão repetitiva Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão','Atrito ou abrasão por compressão repetitiva Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('Atrito ou abrasão, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão','Atrito ou abrasão, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('Reação do corpo a seus movimentos - movimento involuntário (escorregão sem queda, etc.). Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto','Reação do corpo a seus movimentos - movimento involuntário (escorregão sem queda, etc.). Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'),
        ('Reação do corpo a seus movimentos - movimento voluntário. Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto','Reação do corpo a seus movimentos - movimento voluntário. Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'),
        ('Esforço excessivo ao erguer objeto. Ver explicações da classificação anterior (200028000','Esforço excessivo ao erguer objeto. Ver explicações da classificação anterior (200028000).'),
        ('Esforço excessivo ao empurrar ou puxar objeto. Ver explicações da classificação anterior (200028000','Esforço excessivo ao empurrar ou puxar objeto. Ver explicações da classificação anterior (200028000).'),
        ('Esforço excessivo ao manejar, sacudir ou arremessar objeto. Ver explicações da classificação anterior (200028000','Esforço excessivo ao manejar, sacudir ou arremessar objeto. Ver explicações da classificação anterior (200028000).'),
        ('Esforço excessivo, NIC. Ver explicações da classificação anterior (200028000','Esforço excessivo, NIC. Ver explicações da classificação anterior (200028000).'),
        ('Exposição a energia elétrica. Aplica-se somente a casos sem impacto, em que a lesão consiste em choque elétrico, queimadura ou eletroplessão (eletrocussão','Exposição a energia elétrica. Aplica-se somente a casos sem impacto, em que a lesão consiste em choque elétrico, queimadura ou eletroplessão (eletrocussão).'),
        ('Contato com objeto ou substância a temperatura muito alta. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica','Contato com objeto ou substância a temperatura muito alta. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'),
        ('Contato com objeto ou substância a temperatura muito baixa. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica','Contato com objeto ou substância a temperatura muito baixa. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'),
        ('Exposição à temperatura ambiente elevada. Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica','Exposição à temperatura ambiente elevada. Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'),
        ('Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica','Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'),
        ('Inalação de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos','Inalação de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('Ingestão de substancia cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos','Ingestão de substancia cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('Absorção (por contato) de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos','Absorção (por contato) de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('Inalação, ingestão e absorção, NIC. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos','Inalação, ingestão e absorção, NIC. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('Imersão. Aplica-se aos acidentes que têm por consequência o afogamento','Imersão. Aplica-se aos acidentes que têm por consequência o afogamento.'),
        ('Exposição à radiação não ionizante. Aplica-se a casos em que as lesões são provocadas por exposição à radiação solar ou outras radiações não ionizantes (por exemplo: ultravioleta e infravermelho','Exposição à radiação não ionizante. Aplica-se a casos em que as lesões são provocadas por exposição à radiação solar ou outras radiações não ionizantes (por exemplo: ultravioleta e infravermelho).'),
        ('Exposição à radiação ionizante','Exposição à radiação ionizante.'),
        ('Exposição ao ruído','Exposição ao ruído.'),
        ('Exposição à vibração','Exposição à vibração.'),
        ('Exposição à pressão ambiente elevada','Exposição à pressão ambiente elevada.'),
        ('Exposição à pressão ambiente baixa','Exposição à pressão ambiente baixa.'),
        ('Exposição à poluição da água','Exposição à poluição da água.'),
        ('Exposição à poluição do ar','Exposição à poluição do ar.'),
        ('Exposição à poluição do solo','Exposição à poluição do solo.'),
        ('Exposição à poluição, NIC','Exposição à poluição, NIC.'),
        ('Ataque de ser vivo por mordedura, picada, chifrada, coice, etc., não se aplicando no caso de haver peçonha ou transmissão de doença','Ataque de ser vivo por mordedura, picada, chifrada, coice, etc., não se aplicando no caso de haver peçonha ou transmissão de doença.'),
        ('Ataque de ser vivo com peçonha','Ataque de ser vivo com peçonha.'),
        ('Ataque de ser vivo com transmissão de doença','Ataque de ser vivo com transmissão de doença.'),
        ('Ataque de ser vivo (inclusive do homem), NIC','Ataque de ser vivo (inclusive do homem), NIC.'),
        ('Contato com pessoas doentes ou material infecto-contagiante - agentes biológicos','Contato com pessoas doentes ou material infecto-contagiante - agentes biológicos.'),
        ('Tipo, NIC','Tipo, NIC'),
        ('Tipo inexistente','Tipo inexistente'),
    )
    fonte_risco = models.CharField(max_length=2500, choices=choice_fonte)
    
    def __str__(self):
        return self.fonte_risco
    class Meta:
        verbose_name = "fonte_risco"
        verbose_name_plural = "fonte_riscos"
        ordering = ['fonte_risco']
class Medidasimplementadas(models.Model):
    medidas_implementadas = models.CharField(max_length=200)
    
    def __str__(self):
        return self.medidas_implementadas
    
    class Meta:
        verbose_name = "medida_implementada"
        verbose_name_plural = "medidas_implementadas"
        ordering = ['medidas_implementadas']
class Tempoexposicao(models.Model):
    choice_exposicao = (
        ('Até 1 hora por dia','Até 1 hora por dia'),
        ('Até 2 horas por dia','Até 2 horas por dia'),
        ('Até 4 horas por dia','Até 4 horas por dia'),
        ('Até 6 horas por dia','Até 6 horas por dia'),
        ('Até 8 horas por dia','Até 8 horas por dia'),
        )
    tempo_exposicao = models.CharField(max_length=200, choices=choice_exposicao)
    
    def __str__(self):
        return self.tempo_exposicao
    
    class Meta:
        verbose_name = "tempo_exposicao"
        verbose_name_plural = "tempos_exposicao"
        ordering = ['tempo_exposicao']

#  AVALIAÇÃO DOS RISCOS DO AMBIENTE
class Medidascontrole(models.Model):
    choice_medidas_controle = (
        ('Aceitável','Aceitável'),
        ('Ineficiente','Ineficiente'),
        ('Deficiente','Deficiente'),
        ('Muito Deficiente','Muito Deficiente'),
        ('Deficiência Total','Deficiência Total'),
        )
    choice_nmc = (
        ('1','1'),
        ('2','2'),
        ('6','6'),
        ('10','10'),
        ('14','14'),
        )
    choice_significado = (
        ('Não Foram detectadas anomalias','Não Foram detectadas anomalias'),
        ('O perigo está controlado','O perigo está controlado'),
        ('Foram detectados fatores de risco de menor importancia','Foram detectados fatores de risco de menor importancia'),
        ('O dano pode ocorrer algumas vezes','O dano pode ocorrer algumas vezes'),
        ('Foram detectados alguns fatores de risco significativos','Foram detectados alguns fatores de risco significativos'),
        ('As medidas preventivas existentes tem sua eficávia reduzida','As medidas preventivas existentes tem sua eficávia reduzida'),
        ('Foram detectados fatores de risco significativos','Foram detectados fatores de risco significativos'),
        ('As medidas preventivas existentes são ineficazes','As medidas preventivas existentes são ineficazes'),
        ('O dano ocorerá na maior parte das circunstâncias','O dano ocorerá na maior parte das circunstâncias'),
        ('Medidas preventivas inexistentes ou desadequadas','Medidas preventivas inexistentes ou desadequadas'),
        ('São esperados danos na maior parte das situações','São esperados danos na maior parte das situações'),
        )

    medida_controle = models.CharField(max_length=200, choices=choice_medidas_controle)
    nmc = models.CharField(max_length=200, choices=choice_nmc)
    significado = models.CharField(max_length=200, choices=choice_significado)
    def __str__(self):
        return f"{self.medida_controle} - {self.significado}"
    class Meta:
        verbose_name = "medida_controle"
        verbose_name_plural = "medida_controles"
        ordering = ['nmc']
class Nivelexposicao(models.Model):
    choice_nivel_exposicao = (
    ('Exporádica','Exporádica'),
    ('Pouco Frequente','Pouco Frequente'),
    ('Ocasional','Ocasional'),
    ('Frequente','Frequente'),
    ('Continuada','Continuada'),
    )
    choice_ne = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        )
    choice_significado = (
        ('Uma vez por ano, por pouco tempo(minutos)','Uma vez por ano, por pouco tempo(minutos)'),
        ('Algumas vezes por ano e por período de tempo determinado','Algumas vezes por ano e por período de tempo determinado'),
        ('Algumas vezes por mês','Algumas vezes por mês'),
        ('Várias vezes durante o período laboral, ainda que com tempos curtos','Várias vezes durante o período laboral, ainda que com tempos curtos'),
        ('Várias vezes por semana ou diário','Várias vezes por semana ou diário'),
        ('Várias vezes por dia com tempo prolongado ou continuamente','Várias vezes por dia com tempo prolongado ou continuamente'),
        )

    nivel_exposicao = models.CharField(max_length=200, choices=choice_nivel_exposicao)
    ne = models.CharField(max_length=200, choices=choice_ne)
    significado = models.CharField(max_length=200, choices=choice_significado)
    def __str__(self):
        return f"{self.nivel_exposicao} - {self.significado}"
    class Meta:
        verbose_name = "nivel_exposicao"
        verbose_name_plural = "nivel_exposicaos"
        ordering = ['ne']
class Nivelprobabilidade(models.Model):
    choice_nivel_probabilidade = (
    ('Muito Baixa','Muito Baixa'),
    ('Pouco Frequente','Pouco Frequente'),
    ('Média','Média'),
    ('Alta','Alta'),
    ('Muito Alta','Muito Alta'),
    )
    choice_np = (
        ('1','1 a 3'),
        ('4','4 a 6'),
        ('8','8 a 20'),
        ('24','24 a 30'),
        ('40','40 a 70'),
        )
    choice_significado = (
        ('Não é de se esperar que a situação perigosa se materialize, ainda que possa ser concebida','Não é de se esperar que a situação perigosa se materialize, ainda que possa ser concebida'),
        ('A materialização da situação perigosa pode ocorrer','A materialização da situação perigosa pode ocorrer'),
        ('A materialização da situação perigosa é passível de ocorrer pelo menos uma vez com danos','A materialização da situação perigosa é passível de ocorrer pelo menos uma vez com danos'),
        ('A materizalização da situação perigosa pode ocorrer várias vezes durante o peródo de trabalho','A materizalização da situação perigosa pode ocorrer várias vezes durante o peródo de trabalho'),
        ('Normalmente a materizalização da situação perigosa ocorre com frequência','Normalmente a materizalização da situação perigosa ocorre com frequência'),
        )

    nivel_probabilidade = models.CharField(max_length=200, choices=choice_nivel_probabilidade)
    np = models.CharField(max_length=200, choices=choice_np)
    significado = models.CharField(max_length=200, choices=choice_significado)

    def __str__(self):
        return f"{self.nivel_probabilidade} - {self.significado}"

    class Meta:
        verbose_name = "nivel_probabilidade"
        verbose_name_plural = "nivel_probabilidades"
        ordering = ['np']
class Nivelgravidade(models.Model):
    choice_nivel_gravidade = (
    ('Insignificante','Insignificante'),
    ('Leve','Leve'),
    ('Moderado','Moderado'),
    ('Grave','Grave'),
    ('Mortal','Mortal'),
    )
    choice_ng = (
        ('10','10'),
        ('25','25'),
        ('60','60'),
        ('90','90'),
        ('155','155'),
        )
    choice_significado = (
        ('Não há danos pessoais','Não há danos pessoais'),
        ('Pequenas lesões que não requerem hospitalização. Apenas primeiros socorros','Pequenas lesões que não requerem hospitalização. Apenas primeiros socorros'),
        ('Lesões com incapacidade transitória. REquerem tratamento médico','Lesões com incapacidade transitória. REquerem tratamento médico'),
        ('Lesões graves que podem ser irreparáveis','Lesões graves que podem ser irreparáveis'),
        ('Morte ou incapacidade permanente','Morte ou incapacidade permanente'),
        )

    nivel_gravidade = models.CharField(max_length=200, choices=choice_nivel_gravidade)
    ng = models.CharField(max_length=200, choices=choice_ng)
    significado = models.CharField(max_length=200, choices=choice_significado)

    def __str__(self):
        return f"{self.nivel_gravidade} - {self.significado}"
    
    class Meta:
        verbose_name = "nivel_gravidade"
        verbose_name_plural = "nivel_gravidades"
        ordering = ['ng']
class Classificacaorisco(models.Model):
    choice_classificacao_risco = (
    ('Crítico','Crítico'),
    ('Alto','Alto'),
    ('Moderado','Moderado'),
    ('Baixo','Baixo'),
    ('Irrelevante','Irrelevante'),
    )
    choice_nr = (
        ('10850','3360 a 10850'),
        ('3100','1240 a 3100'),
        ('1200','360 a 1200'),
        ('300','90 a 300'),
        ('80','10 a 80'),
        )
    choice_significado = (
        ('Situação CRITÍCA','Situação CRITÍCA'),
        ('Intervenção imediata','Intervenção imediata'),
        ('Isolar o perigo até serem adaptadas às medidas de controle','Isolar o perigo até serem adaptadas às medidas de controle'),
        ('Situação a CORRIGIR','Situação a CORRIGIR'),
        ('Adaptar medidas de controle enquanto a situação perigosa não for eliminada ou reduzida','Adaptar medidas de controle enquanto a situação perigosa não for eliminada ou reduzida'),
        ('Situação a MELHORAR','Situação a MELHORAR'),
        ('Deverão ser elaborados planos, programas ou procedimentos, documentados de intervenção','Deverão ser elaborados planos, programas ou procedimentos, documentados de intervenção'),
        ('MELHORAR SE POSSÍVEL, justificando a intervenção','MELHORAR SE POSSÍVEL, justificando a intervenção'),
        ('Intervir apenas se uma análise mais pormenorizada o justificar','Intervir apenas se uma análise mais pormenorizada o justificar'),
        )

    nr = models.CharField(max_length=200, choices=choice_nr)
    classificacao_risco = models.CharField(max_length=200, choices=choice_classificacao_risco)
    significado = models.CharField(max_length=200, choices=choice_significado)
    
    def __str__(self):
        return f"{self.classificacao_risco} - {self.significado}"
    
    class Meta:
        verbose_name = "classificacao_risco"
        verbose_name_plural = "classificacao_riscos"
        ordering = ['classificacao_risco']
class Nivelrisco(models.Model):
    ng = models.ForeignKey(Nivelgravidade, on_delete=models.CASCADE)
    np = models.ForeignKey(Nivelprobabilidade, on_delete=models.CASCADE)
    classificacao_risco = models.ForeignKey(Classificacaorisco, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.ng} - {self.classificacao_risco}"

    class Meta:
        verbose_name = "nivel_risco"
        verbose_name_plural = "nivel_riscos" 
        ordering = ['classificacao_risco']

## INVENTÁRIO DA FUNÇÃO
# IDENTIFICAÇÃO
class Identificacaorisco(models.Model):
    funcao = models.ForeignKey(Funcao, verbose_name=("funcao"), on_delete=models.CASCADE)
    descricao_perigo = models.ForeignKey(Descricaoperigo, verbose_name= ("descricao_perigo"), on_delete=models.CASCADE)
    descricao_lesao = models.ForeignKey(Lesoes, verbose_name=("lesao"), on_delete=models.CASCADE)
    fonte_risco = models.ForeignKey(Fonterisco, verbose_name=("fonte"), on_delete=models.CASCADE)
    medidas_implementadas = models.ForeignKey(Medidasimplementadas, verbose_name=("medidas"), on_delete=models.CASCADE)
    tempo_exposicao = models.ForeignKey(Tempoexposicao, verbose_name=("exposicao"), on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.descricao_perigo}"
    
    class Meta:
        verbose_name = "identificacao_risco"
        verbose_name_plural = "identificacao_riscos"
        ordering = ['funcao']
# AVALIAÇÃO
class Avaliacaorisco(models.Model):
    descricao_perigo = models.ForeignKey(Descricaoperigo, verbose_name= ("descricao_perigo"), on_delete=models.CASCADE)
    classificacao_risco = models.ForeignKey(Classificacaorisco, verbose_name=('classificacao_risco'), on_delete=models.CASCADE)
    medidas_controle = models.ForeignKey(Medidascontrole, verbose_name=('medidas_controle'), on_delete=models.CASCADE)
    nivel_exposicao = models.ForeignKey(Nivelexposicao, verbose_name=('nivel_exposicao'), on_delete=models.CASCADE)
    nivel_probabilidade = models.ForeignKey(Nivelprobabilidade, verbose_name=('nivel_probabilidade'), on_delete=models.CASCADE)
    nivel_gravidade = models.ForeignKey(Nivelgravidade, verbose_name=('nivel_gravidade'), on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.classificacao_risco}"

    class Meta:
        verbose_name = "avaliacao_risco"
        verbose_name_plural = "avaliacao_riscos"
        ordering = ['descricao_perigo']
# INVENTÁRIO (IDENTIFICACAO+AVALIACAO)
class Inventario(models.Model):
    identificacao_risco = models.ForeignKey(Identificacaorisco, verbose_name=("identificacao_risco"), on_delete=models.CASCADE)
    avaliacao_risco = models.ForeignKey(Avaliacaorisco, verbose_name=("avaliacao_risco"), on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.identificacao_risco)

    class Meta:
        verbose_name = "inventario"
        verbose_name_plural = "inventarios"
        ordering = ['avaliacao_risco']

## PLANO DE AÇÃO
class Planoacao(models.Model):
    inventario = models.ForeignKey(Inventario, verbose_name=("inventario"), on_delete=models.CASCADE)
    oque = models.CharField(max_length=1000)
    porque = models.CharField(max_length=1000)
    quando = models.CharField(max_length=1000)
    quem = models.CharField(max_length=1000)
    onde = models.CharField(max_length=1000)
    como = models.CharField(max_length=1000)
    quanto = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return str(self.oque)
    
    class Meta:
        verbose_name = "plano_acao"
        verbose_name_plural = "planos_acao"
        ordering = ['oque']

## CONTROLE DOS RISCOS
#  INVENTÁRIO DO EMPREGADO
class Empregadoinventario(models.Model):
    empregado = models.ForeignKey(Empregado, verbose_name=("empregado"), on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, verbose_name=("inventario"), on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.empregado} - {self.inventario}"

    class Meta:
        verbose_name = "empregadoinventario"
        verbose_name_plural = "empregadosinventarios"
        ordering = ['empregado']
# PLANO DE AÇÃO DO EMPREGADO
class Empregadoplano(models.Model):
    empregado = models.ForeignKey(Empregado, verbose_name=("empregado"), on_delete=models.CASCADE)
    plano_acao = models.ForeignKey(Planoacao, verbose_name=("plano_acao"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.empregado} - {self.plano_acao}"


    class Meta:
        verbose_name = "empregadoplano"
        verbose_name_plural = "empregadosplanos"
        ordering = ['empregado']
