from django.db import models
# from smart_selects.db_fields import ChainedForeignKey

# Modelos
class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100)    
    responsavel = models.CharField(max_length=100)    
    numero_funcionarios = models.IntegerField()

    class Meta:
        ordering = ['nome_empresa']
        
    def __str__(self):
        return self.nome_empresa

class Funcao(models.Model):
    cargo = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    descricao_sumaria = models.TextField()
    descricao_detalhada = models.TextField()
    cbo_funcao = models.CharField(max_length=50)
    
    def __str__(self):
        return self.funcao
    
    class Meta:
        verbose_name_plural = "funcoes"
        
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
# # Selecao Encadeada
# class Funcao(models.Model):
#     cargo = models.CharField(max_length=200)
#     funcao = models.CharField(max_length=200)


# class Fator(models.Model):
#     tipo = models.ForeignKey(Funcao)
#     nome = ChainedForeignKey(Funcao,
#         chained_field="tipo",
#         chained_model_field="tipo",
#         show_all=False,
#         auto_choose=True,
#         sort=True)

# Selecao Encadeada
# class Tipo(models.Model):
#     nome = models.CharField(max_length=200)

# class Risco(models.Model):
#     choice_risco = (
#         ('F'),('FÍSICOS'),
#         ('Q'),('QUÍMICOS'),
#         ('B'),('BIOLÓGICOS'),
#         ('EB'),('ERGONÔMICOS-BIOMECÂNICOS'),
#         ('EM'),('ERGONÔMICOS-MOBILIÁRIO E EQUIPAMENTOS'),
#         ('EO'),('ERGONÔMICOS-ORGANIZACIONAIS'),
#         ('EA'),('ERGONÔMICOS-AMBIENTAIS'),
#         ('EP'),('ERGONÔMICOS-PSICOSSOCIAIS/COGNITIVOS'),
#         ('A'),('MECÂNICOS/ACIDENTES'),
#         ('P'),('PERIGOSOS'),
#         ('AS'),('ASSOCIAÇÃO DE FATORES DE RISCO'),
#         ('O'),('OUTROS FATORES DE RISCO'),
#         ('NO'),('AUSÊNCIA DE FATORES DE RISCO'),  
#     )
#     tipo = models.ForeignKey(Tipo)
#     nome = models.CharField(max_length=200, choices=choice_risco)

# class Fator(models.Model):
#     tipo = models.ForeignKey(Tipo)
#     nome = ChainedForeignKey(
#         Risco,
#         chained_field="tipo",
#         chained_model_field="tipo",
#         show_all=False,
#         auto_choose=True,
#         sort=True)


class Tiporisco(models.Model):    
    choice_riscos = (
        ('01.01.001','Infrassom e sons de baixa frequência'),
        ('01.01.002','Ruído contínuo ou intermitente (legislação previdenciária)'),
        ('01.01.003','Ruído impulsivo ou de impacto'),
        ('01.01.004','Ultrassom'),
        ('01.01.005','Campos magnéticos estáticos'),
        ('01.01.006','Campos magnéticos de sub-radiofrequência (30 kHz e abaixo)'),
        ('01.01.007','Sub-radiofrequência (30 kHz e abaixo) e campos eletrostáticos'),
        ('01.01.008','Radiação de radiofrequência'),
        ('01.01.009','Micro-ondas'),
        ('01.01.010','Radiação visível e infravermelho próximo'),
        ('01.01.011','Radiação ultravioleta, exceto radiação n a faixa 400 a 320 nm (Luz Negra)'),
        ('01.01.012','Radiação ultravioleta na faixa 400 a 320 nm (Luz Negra)'),
        ('01.01.013','LASER'),
        ('01.01.014','Radiações ionizantes'),
        ('01.01.015','Vibrações localizadas (mão-braço)'),
        ('01.01.016','Vibração de corpo inteiro (aceleração resultante de exposição normalizada - aren)'),
        ('01.01.017','Frio'),
        ('01.01.018','Temperaturas anormais (calor) (legislação previdenciária)'),
        ('01.01.019','Pressão hiperbárica'),
        ('01.01.020','Pressão hipobárica'),
        ('01.01.021','Ruído contínuo ou intermitente (legislação trabalhista)'),
        ('01.01.022','Vibração de corpo inteiro (Valor da Dose de Vibração Resultante - VDVR)'),
        ('01.01.023','Temperaturas anormais (calor) (legislação trabalhista)'),
        ('01.01.999','Outros'),
        ('02.01.001','Acetaldeído (aldeído acético)'),
        ('02.01.002','Acetato de benzila'),
        ('02.01.003','Acetato de n-butila'),
        ('02.01.004','Acetato de sec-butila'),
        ('02.01.005','Acetato de terc-butila'),
        ('02.01.006','Acetato de 2-butoxietila'),
        ('02.01.007','Sais de Cianeto'),
        ('02.01.008','Acetato de etila'),
        ('02.01.009','Acetato de 2-etoxi etila (Acetato de cellosolve ou Acetato de éter monoetílico de etileno glicol)'),
        ('02.01.010','Acetato de sec-hexila'),
        ('02.01.011','Acetato de isobutila'),
        ('02.01.012','Acetato de isopropila'),
        ('02.01.013','Acetato de metila'),
        ('02.01.014','Acetato de 2-metoxietila (EGMEA) '),
        ('02.01.015','Acetato de n-propila'),
        ('02.01.016','Acetato de pentila, todos os isômeros'),
        ('02.01.017','Acetato de vinila'),
        ('02.01.018','Acetileno'),
        ('02.01.019','Acetofenona'),
        ('02.01.020','Acetona (propanona)'),
        ('02.01.021','Acetona cianidrina'),
        ('02.01.022','Acetonitrila (cianeto de metila)'),
        ('02.01.023','Ácido acético (ácido etanoico)'),
        ('02.01.024','Ácido acetilsalicílico (aspirina)'),
        ('02.01.025','Ácido acrílico'),
        ('02.01.026','Ácido adípico'),
        ('02.01.027','Ácido aristolóquico'),
        ('02.01.028','Ácido bromídrico (brometo de hidrogênio)'),
        ('02.01.029','Ácido carbônico'),
        ('02.01.030','Ácido cianídrico (cianeto de hidrogênio, gás cianídrico)'),
        ('02.01.031','Ácido clorídrico (cloreto de hidrogênio, gás clorídrico)'),
        ('02.01.032','Ácido 2-cloropropiônico'),
        ('02.01.033','Ácido crômico (névoa)'),
        ('02.01.034','Ácido dicloroacético'),
        ('02.01.035','Ácido 2,2-dicloropropiônico'),
        ('02.01.036','Ácido 2-etil hexanoico'),
        ('02.01.037','Ácido fluorídrico'),
        ('02.01.038','Ácido fosfórico'),
        ('02.01.039','Ácido metacrílico'),
        ('02.01.040','Ácido metanoico (ácido fórmico)'),
        ('02.01.041','Ácido monocloroacético'),
        ('02.01.042','Ácido nítrico'),
        ('02.01.043','Ácido oxálico, anidro e diidratado'),
        ('02.01.044','Ácido peracético'),
        ('02.01.045','Ácido pícrico'),
        ('02.01.046','Ácido propiônico'),
        ('02.01.047','Ácido sulfúrico'),
        ('02.01.048','Ácido tereftálico'),
        ('02.01.049','Ácido tioglicólico'),
        ('02.01.050','Ácido tricloroacético'),
        ('02.01.051','Acrilamida'),
        ('02.01.052','Acrilato de n-butila'),
        ('02.01.053','Acrilato de etila'),
        ('02.01.054','Acrilato de 2-hidroxipropila'),
        ('02.01.055','Acrilato de metila'),
        ('02.01.056','Acrilonitrila (cianeto de vinila)'),
        ('02.01.057','Acroleína'),
        ('02.01.059','Adiponitrila'),
        ('02.01.060','Aflatoxinas'),
        ('02.01.061','Aguarrás mineral (solvente de Stoddard)'),
        ('02.01.062','Alaclor'),
        ('02.01.063','Álcalis cáusticos'),
        ('02.01.064','Alcatrão de hulha, produtos voláteis como aerossóis solúveis em benzeno (breu de alcatrão de hulha)'),
        ('02.01.065','Álcool alílico'),
        ('02.01.066','Álcool n-butílico (n-butanol)'),
        ('02.01.067','Álcool sec-butílico (sec-butanol)'),
        ('02.01.068','Álcool terc-butílico'),
        ('02.01.069','Álcool etílico (etanol)'),
        ('02.01.070','Álcool furfurílico'),
        ('02.01.071','Álcool isoamílico'),
        ('02.01.072','Álcool isobutílico (isobutanol)'),
        ('02.01.073','Álcool isooctílico'),
        ('02.01.074','Álcool isopropílico (isopropanol ou 2-propanol)'),
        ('02.01.075','Álcool propargílico'),
        ('02.01.076','Álcool metil amílico (metil isobutilcarbinol)'),
        ('02.01.077','Álcool metílico (metanol)'),
        ('02.01.078','Álcool n-propílico (n-propanol)'),
        ('02.01.079','Aldrin'),
        ('02.01.080','Algodão, bruto, sem tratamento, poeira'),
        ('02.01.081','Alumínio metal e compostos insolúveis'),
        ('02.01.082','Amido'),
        ('02.01.083','Aminas aromáticas'),
        ('02.01.084','4-Aminodifenil (p-xenilamina; aminobifenila; 4-aminobifenila)'),
        ('02.01.086','2-Aminopiridina'),
        ('02.01.087','Amitrol (3-amina-1,2,4-triazol)'),
        ('02.01.088','Amônia (gás amoníaco)'),
        ('02.01.089','Anidro sulfuroso (dióxido de enxofre)'),
        ('02.01.090','Anidrido acético'),
        ('02.01.091','Anidrido ftálico'),
        ('02.01.092','Anidrido hexahidroftálico, todos os isômeros'),
        ('02.01.093','Anidrido maleico'),
        ('02.01.094','Anidrido trimelítico'),
        ('02.01.095','Anilina'),
        ('02.01.096','o-Anisidina'),
        ('02.01.097','p-Anisidina'),
        ('02.01.098','Antimônio e seus compostos'),
        ('02.01.099','Antraceno'),
        ('02.01.100','ANTU'),
        ('02.01.101','Argônio'),
        ('02.01.102','Arseneto de gálio'),
        ('02.01.103','Arsênio e seus compostos (arsênico)'),
        ('02.01.104','Arsina'),
        ('02.01.105','Asbestos, todas as formas'),
        ('02.01.106','Asfalto (betume), fumos, como aerossol solúvel em benzeno'),
        ('02.01.107','Atrazine (e triazinas simétricas relacionadas)'),
        ('02.01.108','Auramina'),
        ('02.01.109','Azatioprina'),
        ('02.01.110','Azida de sódio (como azida de sódio; como vapor de ácido hidrazoico)'),
        ('02.01.111','Azinfos metil'),
        ('02.01.112','Bário e compostos solúveis'),
        ('02.01.113','Benomil'),
        ('02.01.114','Benzeno e seus compostos tóxicos'),
        ('02.01.115','Benzidina'),
        ('02.01.116','Benzo[a]antraceno'),
        ('02.01.117','Benzo[b]fluoranteno'),
        ('02.01.118','Benzopireno (benzo[a]pireno)'),
        ('02.01.119','Berílio e seus compostos tóxicos (compostos solúveis e insolúveis)'),
        ('02.01.121','BHC (hexacloreto de benzeno ou hexaclorobenzeno)'),
        ('02.01.122','Bifenil'),
        ('02.01.123','Bifenis policlorados'),
        ('02.01.124','Biscloroetileter (éter dicloroetílico)'),
        ('02.01.125','Bis (cloro metil) éter, clorometileter, éter bis (clorometílico) ou éter metílico de clorometila'),
        ('02.01.126','Bissulfito de sódio'),
        ('02.01.127','Borracha natural, látex como proteínas alergênicas inaláveis'),
        ('02.01.128','Borato, compostos inorgânicos'),
        ('02.01.130','Bromacil'),
        ('02.01.131','Brometo de alila'),
        ('02.01.132','Brometo de etila (bromoetano)'),
        ('02.01.133','Brometo de metila (bromometano)'),
        ('02.01.135','Bromo e seus compostos tóxicos'),
        ('02.01.136','1-Bromopropano'),
        ('02.01.137','1,3-Butadieno'),
        ('02.01.138','Butadieno-estireno'),
        ('02.01.139','n-Butano'),
        ('02.01.140','Bussulfano (Myleran ou 1,4-butanodiol dimetanosulfonato)'),
        ('02.01.141','Butenos, todos os isômeros'),
        ('02.01.143','1-Butanotiol (n-Butil mercaptana)'),
        ('02.01.144','n-Butilamina'),
        ('02.01.145','o-sec Butilfenol'),
        ('02.01.146','p-terc-Butiltolueno'),
        ('02.01.147','2-Butóxi etanol (EGBE) (butil cellosolve) (éter monobutílico do etileno glicol)'),
        ('02.01.148','Cádmio e seus compostos tóxicos'),
        ('02.01.149','Canfeno clorado'),
        ('02.01.150','Cânfora, sintética'),
        ('02.01.151','Caolim'),
        ('02.01.152','Caprolactama'),
        ('02.01.153','Captafol'),
        ('02.01.154','Captan'),
        ('02.01.155','Carbaril'),
        ('02.01.156','Carbeto de silício'),
        ('02.01.157','Carbofuran'),
        ('02.01.158','Carvão mineral e seus derivados'),
        ('02.01.159','Catecol'),
        ('02.01.160','Celulose'),
        ('02.01.161','Cereais, poeira (aveia, cevada, trigo)'),
        ('02.01.162','Ceteno'),
        ('02.01.163','Chumbo e seus compostos tóxicos'),
        ('02.01.164','Chumbo tetraetila'),
        ('02.01.165','Chumbo tetrametila'),
        ('02.01.166','Cianamida'),
        ('02.01.167','Cianamida de cálcio'),
        ('02.01.169','Cianoacrilato de etila'),
        ('02.01.170','2-Cianoacrilato de metila'),
        ('02.01.171','Cianogênio'),
        ('02.01.172','Ciclofosfamida'),
        ('02.01.173','Ciclohexano'),
        ('02.01.174','Ciclohexanol'),
        ('02.01.175','Ciclohexanona'),
        ('02.01.176','Ciclohexeno'),
        ('02.01.177','Ciclohexilamina'),
        ('02.01.178','Ciclonita'),
        ('02.01.179','Ciclopentadieno'),
        ('02.01.180','Ciclopentano'),
        ('02.01.181','Ciclosporina'),
        ('02.01.182','Cihexatin'),
        ('02.01.183','Cimento portland'),
        ('02.01.184','Citral'),
        ('02.01.185','Clopidol'),
        ('02.01.186','Clorambucil (cloroambucil)'),
        ('02.01.187','Clordane'),
        ('02.01.188','Cloreto de alila'),
        ('02.01.189','Cloreto de amônio - fumos'),
        ('02.01.190','Cloreto de benzila'),
        ('02.01.191','Cloreto de benzoíla'),
        ('02.01.192','Cloreto de cianogênio'),
        ('02.01.193','Cloreto de cloroacetila'),
        ('02.01.194','Cloreto de cromila'),
        ('02.01.195','Cloreto de dimetil carbamila'),
        ('02.01.196','Cloreto de enxofre'),
        ('02.01.197','Cloreto de etila (cloroetano)'),
        ('02.01.198','Cloreto de fenila (clorobenzeno)'),
        ('02.01.200','Cloreto de metila'),
        ('02.01.201','Cloreto de polivinila (PVC (policloreto de vinila))'),
        ('02.01.202','Cloreto de tionila'),
        ('02.01.203','Cloreto de vinila (cloroetílico)'),
        ('02.01.204','Cloreto de vinilideno (1,1-Dicloreotileno)'),
        ('02.01.205','Cloreto de zinco, fumos'),
        ('02.01.206','Clornafazina'),
        ('02.01.207','Cloro e seus composto tóxicos'),
        ('02.01.208','Cloroacetaldeído'),
        ('02.01.209','2-Cloroacetofenona'),
        ('02.01.210','Cloroacetona'),
        ('02.01.212','o-Clorobenzilideno malononitrila'),
        ('02.01.213','Clorobromometano'),
        ('02.01.214','Clorodifenil (42% de Cloro)'),
        ('02.01.215','Clorodifenil (54% de Cloro)'),
        ('02.01.216','Clorodifluormetano (freon 22)'),
        ('02.01.217','o-Cloroestireno'),
        ('02.01.219','Clorofórmio (Triclorometano)'),
        ('02.01.220','1-Cloro-1-nitropropano'),
        ('02.01.223','Cloropentafluoretano'),
        ('02.01.224','Cloropicrina'),
        ('02.01.225','Cloropirifos'),
        ('02.01.226','Cloropreno (Cloroprene)'),
        ('02.01.227','1-Cloro-2-propanol'),
        ('02.01.228','2-Cloro-1-propanol'),
        ('02.01.229','o-Clorotolueno'),
        ('02.01.230','Cobalto e seus compostos inorgânicos'),
        ('02.01.231','Cobalto carbonila'),
        ('02.01.232','Cobalto hidrocarbonila'),
        ('02.01.233','Cobre'),
        ('02.01.234','Coumafos'),
        ('02.01.235','Cresol, todos os isômeros'),
        ('02.01.236','Creosoto'),
        ('02.01.237','Criseno'),
        ('02.01.238','Cromato de terc-butila'),
        ('02.01.239','Cromato de cálcio'),
        ('02.01.240','Cromato de chumbo'),
        ('02.01.241','Cromato de estrôncio'),
        ('02.01.242','Cromatos de zinco'),
        ('02.01.243','Cromita - processamento do minério (cromato)'),
        ('02.01.244','Cromo e seus compostos tóxicos (inclui metal e compostos de Cr III, compostos de Cr VI solúveis em água e compostos de Cr VI insolúveis)'),
        ('02.01.245','Crotonaldeído'),
        ('02.01.246','Crufomate'),
        ('02.01.247','2,4 D'),
        ('02.01.248','DDD (diclorodifenildicloretano)'),
        ('02.01.249','DDT'),
        ('02.01.250','Decaborano'),
        ('02.01.251','Demeton (Systox)'),
        ('02.01.252','Demeton-S-metila'),
        ('02.01.253','Destilação do alcatrão de hulha'),
        ('02.01.254','Diacetil'),
        ('02.01.255','Diacetona álcool'),
        ('02.01.257','Diamina m-xileno'),
        ('02.01.258','Dianizidina'),
        ('02.01.259','Diazinon'),
        ('02.01.260','Diazometano'),
        ('02.01.261','Diborano'),
        ('02.01.262','1,2-Dibramoetano (dibrometo de etileno)'),
        ('02.01.263','2-N-Dibutilaminoetanol'),
        ('02.01.264','Dibutilftalato (ftalato de dibutila)'),
        ('02.01.265','Diciclopentadieno'),
        ('02.01.266','Dicloreto de propileno (1,2-Dicloropropano)'),
        ('02.01.267','o-Diclorobenzeno'),
        ('02.01.268','p-Diclorobenzeno'),
        ('02.01.269','3,3-Dicloro-benzidina (Diclorobenzidina)'),
        ('02.01.270','1,4-Dicloro-2-buteno'),
        ('02.01.271','Diclorodifluormetano'),
        ('02.01.272','1,3-Dicloro-5,5-dimetil hidantoina'),
        ('02.01.273','1,1-Dicloroetano'),
        ('02.01.274','1,2 Dicloroetano (Dicloreto de etileno)'),
        ('02.01.275','1,2 Dicloroetileno'),
        ('02.01.276','Diclorofluormetano (freon 12)'),
        ('02.01.277','Diclorometano (Cloreto de metileno)'),
        ('02.01.278','1,1-Dicloro-1-nitroetano'),
        ('02.01.279','Dicloroacetileno'),
        ('02.01.280','1,3-Dicloropropeno'),
        ('02.01.281','Diclorotetrafluoretano (freon 114)'),
        ('02.01.282','Diclorvos (DDVP)'),
        ('02.01.283','Dicrotofós'),
        ('02.01.284','Dieldrin'),
        ('02.01.285','Dietanolamina'),
        ('02.01.286','Dietilamina'),
        ('02.01.287','2-Dietilaminoetanol'),
        ('02.01.288','Dietilcetona'),
        ('02.01.289','Dietil éter (Éter etílico)'),
        ('02.01.290','Dietileno triamina'),
        ('02.01.291','Dietilestilbestrol'),
        ('02.01.292','Dietilftalato (ftalato de dietila)'),
        ('02.01.293','Dietilsulfato'),
        ('02.01.294','Difenilamina'),
        ('02.01.295','Difluordibromometano'),
        ('02.01.296','Difluoreto de oxigênio'),
        ('02.01.297','Pirperazina e sais (dihidrocloreto de piperazina)'),
        ('02.01.298','Diisobutil cetona'),
        ('02.01.299','Diisocianato de isoforona'),
        ('02.01.300','Diisocianato de tolueno (TDI) (2,4 Diisocianato de tolueno)'),
        ('02.01.301','Diisopropilamina'),
        ('02.01.302','N,N-Dietilhidroxilamina'),
        ('02.01.304','Dimetilacetamida (N,N-Dimetilacetamida)'),
        ('02.01.305','Dimetilamina'),
        ('02.01.306','Dimetilanilina'),
        ('02.01.307','Dimetiletoxisilano'),
        ('02.01.308','Dimetilformamida'),
        ('02.01.309','Dimetilftalato'),
        ('02.01.310','1,1-Dimetil hidrazina'),
        ('02.01.311','Dinitrato de etileno glicol'),
        ('02.01.312','Dinitrato de propileno glicol'),
        ('02.01.313','Dinitrobenzeno, todos os isômeros'),
        ('02.01.314','Dinitro-o-cresol'),
        ('02.01.315','3,5-Dinitro-o-toluamida'),
        ('02.01.316','Dinitrotolueno'),
        ('02.01.317','1,4-Dioxano'),
        ('02.01.318','Dioxation'),
        ('02.01.319','Dióxido de carbono (gás carbônico)'),
        ('02.01.320','Dióxido de cloro'),
        ('02.01.321','1,3-Dioxolane'),
        ('02.01.322','Dióxido de nitrogênio'),
        ('02.01.323','Dióxido de titânio'),
        ('02.01.324','Dióxido de vinil ciclohexano'),
        ('02.01.325','Dipropil cetona'),
        ('02.01.326','Diquat'),
        ('02.01.327','Dissulfeto de alil propila'),
        ('02.01.328','Dissulfeto de carbono'),
        ('02.01.329','Dissulfeto de dimetila'),
        ('02.01.330','Dissulfiram'),
        ('02.01.331','Dissulfoton'),
        ('02.01.332','Diuron'),
        ('02.01.333','Divinil benzeno'),
        ('02.01.334','Dodecil mercaptana'),
        ('02.01.335','Endosulfan'),
        ('02.01.336','Endrin'),
        ('02.01.337','Enflurano'),
        ('02.01.338','1-Cloro-2,3-Epoxipropano (epicloridrina)'),
        ('02.01.339','EPN'),
        ('02.01.340','Erionita'),
        ('02.01.341','Estanho e seus compostos orgânicos'),
        ('02.01.342','Estanho - metal'),
        ('02.01.343','Estanho - compostos inorgânicos e óxido, exceto hidreto de estanho'),
        ('02.01.344','Estireno (vinibenzeno)'),
        ('02.01.345','Estriquinina'),
        ('02.01.346','Etano'),
        ('02.01.347','Etanolamina'),
        ('02.01.348','Éter alil glicidílico'),
        ('02.01.349','Éter n-Butil glicidílico'),
        ('02.01.352','Éter diglicidílico'),
        ('02.01.353','Éter etil terc-butílico'),
        ('02.01.354','Éter fenílico, vapor'),
        ('02.01.355','Éter fenil glicidílico'),
        ('02.01.356','Éter isopropil glicidílico (IGE)'),
        ('02.01.357','Éter isopropílico'),
        ('02.01.358','Éter isopropílico de monoetileno glicol (2-isopropoxietanol)'),
        ('02.01.359','Éter metil terc-amílico'),
        ('02.01.360','Éter metil terc-butílico (MTBE)'),
        ('02.01.362','Éter metílico de dipropilenoglicol (2-Metoximetiletoxi) propanol (DPGME))'),
        ('02.01.363','Éter monobutílico de dietileno glicol'),
        ('02.01.365','Éter monometílico do etileno glicol (metil cellosolve ou 2-Metoxi etanol (EGME))'),
        ('02.01.366','Etil amil cetona'),
        ('02.01.367','Etil butil cetona'),
        ('02.01.368','Etil mercaptana (Etanotiol)'),
        ('02.01.369','n-Etil morfolina'),
        ('02.01.370','Etilamina'),
        ('02.01.371','Etilbenzeno (estilbenzeno)'),
        ('02.01.372','Etileno'),
        ('02.01.373','Etilenoamina'),
        ('02.01.374','Etilenotiureia'),
        ('02.01.375','Etileno cloridrina'),
        ('02.01.376','Etileno diamina'),
        ('02.01.377','Etileno glicol'),
        ('02.01.378','Etilideno norborneno'),
        ('02.01.380','Etilenoimina'),
        ('02.01.381','Etilnitrosuréias'),
        ('02.01.382','Etion'),
        ('02.01.383','Etoposide'),
        ('02.01.384','Etoposide em associação com cisplatina e bleomicina'),
        ('02.01.385','2-Etoxietanol (cellosolve ou Éter monoetílico do etileno glicol)'),
        ('02.01.386','Farinha (poeiras)'),
        ('02.01.387','Fenacetina'),
        ('02.01.388','Fenamifos'),
        ('02.01.389','n-Fenil-ß-naftilamina'),
        ('02.01.390','o-Fenileno diamina'),
        ('02.01.391','m-Fenileno diamina'),
        ('02.01.392','p-Fenileno diamina'),
        ('02.01.393','Fenil isocianato'),
        ('02.01.394','Fenilfosfina'),
        ('02.01.395','Fenilhidrazina'),
        ('02.01.396','Fenil mercaptana'),
        ('02.01.397','Fenol'),
        ('02.01.398','Fenotiazine'),
        ('02.01.399','Fensulfotion'),
        ('02.01.400','Fention'),
        ('02.01.401','Ferbam'),
        ('02.01.402','Ferro, sais solúveis'),
        ('02.01.403','Ferro diciclopentadienila'),
        ('02.01.404','Ferro, óxido (Fe2O3)'),
        ('02.01.405','Ferro pentacarbonila'),
        ('02.01.406','Ferrovanádio, poeira'),
        ('02.01.407','Fibras Vítreas Sintéticas - Fibras de vidro de filamento contínuo'),
        ('02.01.408','Fibras Vítreas Sintéticas - Fibras de lã de vidro'),
        ('02.01.409','Fibras Vítreas Sintéticas - Fibras de lã de rocha'),
        ('02.01.410','Fibras Vítreas Sintéticas - Fibras de escória mineral'),
        ('02.01.411','Fibras Vítreas Sintéticas - Fibras de vídeo finalidades especiais'),
        ('02.01.412','Fibras Vítreas Sintéticas - Fibras cerâmicas refratárias'),
        ('02.01.413','Flúor'),
        ('02.01.414','Fluoracetato de sódio'),
        ('02.01.416','Fluoreto de carbonila'),
        ('02.01.417','Fluoreto de perclorila'),
        ('02.01.418','Fluoreto de sulfurila'),
        ('02.01.419','Fluoreto de vinila'),
        ('02.01.420','Fluoreto de vinilideno'),
        ('02.01.421','Fonofos'),
        ('02.01.422','Forato'),
        ('02.01.423','Formaldeído (formol ou Aldeído fórmico)'),
        ('02.01.424','Formamida'),
        ('02.01.425','Formiato de etila'),
        ('02.01.426','Formiato de metila'),
        ('02.01.427','Fosfato de dibutila'),
        ('02.01.428','Fosfato de dibutil fenila'),
        ('02.01.429','Fosfato de tributila'),
        ('02.01.430','Fosfato de trifenila'),
        ('02.01.431','Fosfato de triortocresila'),
        ('02.01.432','Fosfina (fosfamina)'),
        ('02.01.433','Fosfito de trimetila'),
        ('02.01.434','Fósforo e seus compostos tóxicos'),
        ('02.01.435','Fosgênio (cloreto de carbonila)'),
        ('02.01.436','Fluortriclorometano (triclorofluormetano ou freon 11)'),
        ('02.01.438','Ftalato de di(2-etilhexila)'),
        ('02.01.440','m-Ftalodinitrila'),
        ('02.01.441','o-Ftalodinitrila'),
        ('02.01.442','Furfural'),
        ('02.01.445','Gás mostarda'),
        ('02.01.446','Gás natural e seus derivados'),
        ('02.01.447','Gasolina'),
        ('02.01.448','Glicerina, névoas'),
        ('02.01.449','Glicidol'),
        ('02.01.450','Glioxal'),
        ('02.01.451','GLP (gás liquefeito do petróleo)'),
        ('02.01.452','Glutaraldeído, ativado e não ativado'),
        ('02.01.453','Grafite (todas as formas, exceto fibras de grafite)'),
        ('02.01.455','Háfnio e seus compostos'),
        ('02.01.457','Halotano'),
        ('02.01.458','Hélio'),
        ('02.01.459','Heptacloro'),
        ('02.01.460','Heptacloro epóxido'),
        ('02.01.461','Heptano, todos os isômeros'),
        ('02.01.462','Hexaclorobutadieno'),
        ('02.01.463','Hexaclorociclopentadieno'),
        ('02.01.464','Hexacloroetano'),
        ('02.01.465','Hexacloronaftaleno'),
        ('02.01.466','Hexafluoracetona'),
        ('02.01.467','Hexafluorpropileno'),
        ('02.01.468','Hexafluoreto de enxofre'),
        ('02.01.469','Hexafluoreto de selênio'),
        ('02.01.470','Hexafluoreto de telúrio'),
        ('02.01.471','Hexametileno diisocianato (HDI)'),
        ('02.01.472','Hexametilfosforamida'),
        ('02.01.473','n-Hexano'),
        ('02.01.474','Hexano, outros isômeros que não o n-Hexano'),
        ('02.01.475','1,6-Hexanodiamina'),
        ('02.01.476','1-Hexeno'),
        ('02.01.477','Hexileno glicol'),
        ('02.01.478','Hidrazina (diamina)'),
        ('02.01.479','Hidreto de antimônio (Estibina)'),
        ('02.01.480','Hidreto de lítio'),
        ('02.01.481','Hidrocarbonetos alifáticos gasosos Alcanos'),
        ('02.01.482','Hidrocarbonetos e outros compostos de carbono'),
        ('02.01.483','Hidrocarbonetos aromáticos'),
        ('02.01.484','Hidrocarbonetos cíclicos'),
        ('02.01.485','Hidrogênio'),
        ('02.01.486','Hidroquinona'),
        ('02.01.487','Hidróxido de cálcio'),
        ('02.01.488','Hidróxido de césio'),
        ('02.01.489','Hidróxido de potássio'),
        ('02.01.490','Hidróxido de sódio'),
        ('02.01.491','Hidroxitolueno butilado'),
        ('02.01.492','Indeno'),
        ('02.01.493','Iodeto de metila'),
        ('02.01.494','Índio e seus compostos'),
        ('02.01.495','Iodo'),
        ('02.01.497','Iodofórmio'),
        ('02.01.498','Isobuteno'),
        ('02.01.499','Isocianato de metila'),
        ('02.01.500','Isoforona'),
        ('02.01.501','Isopropilamina'),
        ('02.01.502','n-Isopropilanilina'),
        ('02.01.503','Isopropil benzeno (cumeno)'),
        ('02.01.505','Ítrio e compostos'),
        ('02.01.506','Lactato de n-butila'),
        ('02.01.507','Lindano'),
        ('02.01.508','Madeira, poeiras - Cedro Vermelho do Oeste'),
        ('02.01.509','Madeira, poeiras - Todas as outras espécies'),
        ('02.01.510','Malation'),
        ('02.01.511','Manganês e seus compostos, poeira '),
        ('02.01.512','Manganês e seus compostos, fumos'),
        ('02.01.513','Melfalano'),
        ('02.01.514','Mercaptanos'),
        ('02.01.515','Mercúrio e seus compostos'),
        ('02.01.518','Metabisulfito de sódio'),
        ('02.01.519','Metacrilato de metila'),
        ('02.01.520','Metais duros contendo carboneto de tungstênio e cobalto'),
        ('02.01.521','Metano'),
        ('02.01.522','Metil acetileno'),
        ('02.01.523','Metil acetileno-propadieno, mistura (MAPP)'),
        ('02.01.524','Metilacrilonitrila'),
        ('02.01.525','Metilal'),
        ('02.01.526','Metilamina'),
        ('02.01.527','Metil n-amil cetona'),
        ('02.01.528','n-Metil anilina'),
        ('02.01.529','Metil n-butil cetona'),
        ('02.01.530','Metil ciclohexano'),
        ('02.01.531','Metilciclohexanol'),
        ('02.01.532','o-Metilciclohexanona'),
        ('02.01.533','2-Metilciclopentadienil manganês tricarbonila'),
        ('02.01.534','Metil demeton'),
        ('02.01.535','Metil etil cetona (MEK) (Butanona)'),
        ('02.01.536','α-Metil estireno'),
        ('02.01.537','Metil isoamil cetona'),
        ('02.01.539','Metil isobutil cetona'),
        ('02.01.540','Metil isopropil cetona'),
        ('02.01.541','Metil mercaptana (metanotiol)'),
        ('02.01.542','1-Metil naftaleno'),
        ('02.01.543','2-Metil naftaleno'),
        ('02.01.544','Metil paration (paration)'),
        ('02.01.545','Metil propil cetona'),
        ('02.01.546','Metil vinil cetona'),
        ('02.01.547','Metileno-bis-(4-ciclohexilisocianato)'),
        ('02.01.548','4,4-metileno-bis-(2-cloroanilina) (metileno-ortocloroanilina, MOCA®, MBOCA®)'),
        ('02.01.549','Metileno bisfenil isocianato (MDI)'),
        ('02.01.550','4,4''-Metileno dianilina'),
        ('02.01.552','Metomil'),
        ('02.01.553','Metoxicloro'),
        ('02.01.555','4-Metoxifenol'),
        ('02.01.556','1-Metoxi-2-propanol'),
        ('02.01.557','Metoxsalen associado com radiação ultravioleta A'),
        ('02.01.558','Monometil hidrazina (metil hidrazina)'),
        ('02.01.559','Metribuzin'),
        ('02.01.560','Mevinfos'),
        ('02.01.561','Mica'),
        ('02.01.562','Molibdênio - compostos solúveis'),
        ('02.01.563','Molibdênio - metal e compostos insolúveis (fração inalável)'),
        ('02.01.564','Molibdênio - metal e compostos insolúveis (fração respirável)'),
        ('02.01.565','Monocrotofós'),
        ('02.01.566','Monóxido de carbono'),
        ('02.01.567','Morfolina'),
        ('02.01.568','Naftaleno'),
        ('02.01.569','ß-Naftilamina (Betanaftilamina)'),
        ('02.01.570','Naftóis (1-Naftol, 2-Naftol)'),
        ('02.01.571','Naled'),
        ('02.01.572','Negro de fumo'),
        ('02.01.573','Neônio'),
        ('02.01.574','Nicotina'),
        ('02.01.575','Níquel e seus compostos tóxicos (inclui níquel carbonila e níquel tetracarbonila)'),
        ('02.01.576','Nitrapirin'),
        ('02.01.577','Nitrato de n-propila'),
        ('02.01.578','Nitrito de isobutila'),
        ('02.01.579','p-Nitroanilina'),
        ('02.01.580','Nitrobenzeno'),
        ('02.01.581','p-Nitroclorobenzeno'),
        ('02.01.583','4-Nitrodifenil (4-Nitrodifenila)'),
        ('02.01.584','Nitroetano'),
        ('02.01.585','Nitrogênio'),
        ('02.01.586','Nitroglicerina'),
        ('02.01.587','Nitrometano'),
        ('02.01.588','Nitronaftilamina'),
        ('02.01.589','1-Nitropropano'),
        ('02.01.590','2-Nitropropano'),
        ('02.01.591','Nitrosamina'),
        ('02.01.592','N-Nitrosodimetilamina'),
        ('02.01.593','4-(metilnitrosamino)-1-(3-piridil)1-butanona (NNK)'),
        ('02.01.594','Nitrotolueno, todos os isômeros'),
        ('02.01.595','5-Nitro-o-toluidina'),
        ('02.01.596','Nonano'),
        ('02.01.597','Octacloronaftaleno'),
        ('02.01.598','Octano, todos os isômeros'),
        ('02.01.599','Óleo diesel, como hidrocarbonetos totais'),
        ('02.01.600','Óleo mineral, excluídos os fluídos de trabalho com metais - Puro, alta e severamente refinado'),
        ('02.01.601','Óleo mineral, excluídos os fluídos de trabalho com metais - Refinação fraca ou média'),
        ('02.01.602','Óleo queimado'),
        ('02.01.603','Ortotoluidina (o-toluidina)'),
        ('02.01.604','p,p''-Oxibis(benzeno sulfonila hidrazida)'),
        ('02.01.605','Oxicloreto de fósforo'),
        ('02.01.606','Óxido de boro'),
        ('02.01.607','Óxido de cálcio'),
        ('02.01.608','Óxido de difenila o-clorada'),
        ('02.01.609','Óxido de etileno'),
        ('02.01.610','Óxido de magnésio'),
        ('02.01.611','Óxido de mesitila'),
        ('02.01.612','Óxido de propileno'),
        ('02.01.613','Óxido de zinco'),
        ('02.01.614','Óxido nítrico'),
        ('02.01.615','Óxido nitroso'),
        ('02.01.616','Oximetalona'),
        ('02.01.617','Ozona (ozônio)'),
        ('02.01.618','Parafina, cera (fumos)'),
        ('02.01.619','Paraquat, como o cátion'),
        ('02.01.620','Particulados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS) - respiráveis'),
        ('02.01.621','Pentaborano'),
        ('02.01.622','Pentacloreto de fósforo'),
        ('02.01.623','3,4,5,3,4-Pentaclorobifenil (PCB - 126)'),
        ('02.01.624','2,3,4,7,8-Pentaclorodibenzofurano'),
        ('02.01.625','Pentaclorofenol'),
        ('02.01.626','Pentacloronaftaleno'),
        ('02.01.627','Pentacloronitrobenzeno'),
        ('02.01.628','Pentaeritritol'),
        ('02.01.629','Pentafluoreto de bromo'),
        ('02.01.630','Pentafluoreto de enxofre'),
        ('02.01.631','n-Pentano'),
        ('02.01.632','2,4-Pentanodiona'),
        ('02.01.633','Pentassulfeto de fósforo'),
        ('02.01.634','Pentóxido de vanádio'),
        ('02.01.635','Percloroetileno (Tetracloroetileno)'),
        ('02.01.636','Perclorometil mercaptana'),
        ('02.01.637','Perfluorobutil etileno'),
        ('02.01.638','Perfluorisobutileno'),
        ('02.01.639','Perfluoroctanoato de amônio'),
        ('02.01.640','Peróxido de benzoíla'),
        ('02.01.641','Peróxido de hidrogênio'),
        ('02.01.642','Peróxido de metil etil cetona'),
        ('02.01.643','Persulfatos, como persulfato'),
        ('02.01.644','Petróleo e seus derivados, exceto óleo diesel, gasolina, querosene e nafta'),
        ('02.01.645','Picloram'),
        ('02.01.646','Pindone'),
        ('02.01.648','Piretro'),
        ('02.01.649','Piridina'),
        ('02.01.650','Pirofosfato de tetraetila'),
        ('02.01.651','Platina e sais solúveis - Metal'),
        ('02.01.652','Platina e sais solúveis - Sais solúveis'),
        ('02.01.653','Plutônio'),
        ('02.01.654','Poliisocianetos'),
        ('02.01.655','Poliuretanas'),
        ('02.01.657','Prata e seus compostos - metal, poeira e fumos'),
        ('02.01.658','Prata e seus compostos - compostos solúveis'),
        ('02.01.659','Procarbazina'),
        ('02.01.661','n-propano (propano)'),
        ('02.01.662','Propanosultona (propano sultone)'),
        ('02.01.664','Propileno'),
        ('02.01.665','Propileno imina'),
        ('02.01.666','ß-Propiolactona (beta-propiolactona ou betapropiolactona)'),
        ('02.01.667','Propionaldeído'),
        ('02.01.668','Propoxur'),
        ('02.01.670','Querosene combustível de avião, como vapor de hidrocarbonetos totais'),
        ('02.01.671','Quinona'),
        ('02.01.672','Rádio-224 e seus produtos de decaimento'),
        ('02.01.673','Rádio-226 e seus produtos de decaimento'),
        ('02.01.674','Rádio-228 e seus produtos de decaimento'),
        ('02.01.675','Radônio-222 e seus produtos de decaimento'),
        ('02.01.676','Resina de vareta (eletrodo arame) de solda, produtos da decomposição térmica (breu)'),
        ('02.01.677','Resorcinol'),
        ('02.01.678','Ródio - metal e compostos insolúveis'),
        ('02.01.679','Ródio - compostos solúveis'),
        ('02.01.680','Ronel'),
        ('02.01.681','Rotenona (comercial)'),
        ('02.01.682','Sacarose'),
        ('02.01.683','Seleneto de hidrogênio'),
        ('02.01.684','Selênio e seus compostos'),
        ('02.01.685','Semustina [1-(2 -cloroetil) -3-(4-metilciclohexil)-1-nitrosourea, Metil CC- NU]'),
        ('02.01.686','Sesone'),
        ('02.01.687','Sílica livre (sílica livre cristalizada) - poeira respirável'),
        ('02.01.688','Sílica cristobalita'),
        ('02.01.689','Silicato de cálcio, sintético não fibroso'),
        ('02.01.690','Salicilato de etila'),
        ('02.01.691','Salicilato de metila'),
        ('02.01.692','Silicatos'),
        ('02.01.693','Simazine'),
        ('02.01.694','Subtilisins, como 100% enzima cristalina ativa cristalina'),
        ('02.01.695','Sulfamato de amônio'),
        ('02.01.696','Sulfato de bário'),
        ('02.01.697','Sulfato de cálcio'),
        ('02.01.698','Sulfato de dimetila (dimetilsulfato)'),
        ('02.01.699','Sulfato de carbonila'),
        ('02.01.700','Sulfeto de hidrogênio (Gás sulfídrico)'),
        ('02.01.701','Sulfeto de dimetila'),
        ('02.01.702','Sulfeto de níquel'),
        ('02.01.703','Sulfometuron metil'),
        ('02.01.704','Sulfotep (TEDP)'),
        ('02.01.705','Sulprofos'),
        ('02.01.706','2,4,5-T'),
        ('02.01.707','Talco'),
        ('02.01.708','Tálio'),
        ('02.01.709','Tamoxifeno '),
        ('02.01.710','Telureto de bismuto - não aditivado, como Bi2Te3 '),
        ('02.01.711','Telureto de bismuto - aditivado com Se, como Bi2Te3'),
        ('02.01.712','Telúrio e compostos (NOS), como Te, excluído telureto de hidrogênio'),
        ('02.01.713','Temefós'),
        ('02.01.714','Terbufos'),
        ('02.01.715','Terebentina e monoterpenos selecionados'),
        ('02.01.716','Terfenilas (o,m,p-isômeros)'),
        ('02.01.717','Terfenilas hidrogenadas (não irradiadas)'),
        ('02.01.718','Tetrabrometo de acetileno (1,1,2,2-Tetrabromoetano)'),
        ('02.01.719','Tetrabrometo de carbono'),
        ('02.01.720','Tetracloreto de carbono'),
        ('02.01.721','2,3,7,8-Tetraclorodibenzo-para-dioxina'),
        ('02.01.722','1,1,1,2-Tetracloro-2,2-difluoretano'),
        ('02.01.723','1,1,2,2-Tetracloro-1,2-difluoretano'),
        ('02.01.724','Tetracloroetano (1,1,2,2-Tetracloroetano)'),
        ('02.01.725','Tetracloronaftaleno'),
        ('02.01.726','Tetrafluoretileno'),
        ('02.01.727','Tetrafluoreto de enxofre'),
        ('02.01.728','Tetrahidreto de germânio'),
        ('02.01.729','Tetrahidreto de silício'),
        ('02.01.730','Tetrahidrofurano'),
        ('02.01.731','Tetraquis (hidroximetil) fosfônio, sais - Cloreto de tetraquis (hidroximetil) fosfônio'),
        ('02.01.732','Tetraquis (hidroximetil) fosfônio, sais - Sulfato de tetraquis (hidroximetil) fosfônio'),
        ('02.01.733','Tetrametil succinonitrila'),
        ('02.01.734','Tetranitrometano'),
        ('02.01.735','Tetril'),
        ('02.01.736','Tetróxido de ósmio'),
        ('02.01.737','Thiram'),
        ('02.01.738','Tiotepa'),
        ('02.01.739','Titânio'),
        ('02.01.740','4,4''-Tiobis (6-terc-butil-m-cresol)'),
        ('02.01.741','o-Tolidina'),
        ('02.01.742','Tolueno (toluol)'),
        ('02.01.743','m-Toluidina'),
        ('02.01.744','p-Toluidina'),
        ('02.01.745','Tório-232 e seus produtos de decaimento'),
        ('02.01.746','Tribrometo de boro'),
        ('02.01.747','Tricloreto de boro'),
        ('02.01.748','Tribromometano (Bromofórmio)'),
        ('02.01.749','Tricloreto de fósforo'),
        ('02.01.750','Triclorfon'),
        ('02.01.751','Triclorometil benzeno'),
        ('02.01.752','1,1,2-Tricloro-1,2,2-trifluoretano (freon 113)'),
        ('02.01.753','1,2,4-Triclorobenzeno'),
        ('02.01.754','1,1,1 Tricloroetano (Metilclorofórmio)'),
        ('02.01.755','1,1,2-Tricloroetano (Tricloreto de vinila)'),
        ('02.01.756','Tricloroetileno'),
        ('02.01.758','Tricloronaftaleno'),
        ('02.01.759','1,2,3-Tricloropropano'),
        ('02.01.760','Trietanolamina'),
        ('02.01.761','Trietilamina'),
        ('02.01.762','Trifluorbromometano'),
        ('02.01.763','Trifluoreto de boro'),
        ('02.01.764','Trifluoreto de cloro'),
        ('02.01.765','Trifluoreto de nitrogênio'),
        ('02.01.767','1,3,5-Triglicidil-s-triazinetriona'),
        ('02.01.768','Trimetilamina'),
        ('02.01.769','Trimetil benzeno (mistura de isômeros)'),
        ('02.01.770','2,4,6-Trinitrotolueno'),
        ('02.01.771','Trióxido de antimônio'),
        ('02.01.772','Tungstênio - compostos solúveis'),
        ('02.01.773','Tungstênio - metal e compostos insolúveis'),
        ('02.01.774','Urânio (natural) compostos solúveis e insolúveis'),
        ('02.01.775','n-Valeraldeído'),
        ('02.01.776','4-Vinilciclohexeno'),
        ('02.01.777','n-Vinil-2-pirrolidone'),
        ('02.01.778','Vinil tolueno'),
        ('02.01.779','Warfarin (Varfarina)'),
        ('02.01.780','Xileno (xilol)'),
        ('02.01.781','Xilidina (mistura de isômeros)'),
        ('02.01.782','Xisto betuminoso e seus derivados'),
        ('02.01.783','Zircônio e compostos'),
        ('02.01.785','Hormônios sexuais femininos (apenas para homens)'),
        ('02.01.786','4-Dimetil-aminoazobenzeno'),
        ('02.01.787','N''-Nitrosonornicotina (NNN)'),
        ('02.01.788','Sílica livre (sílica livre cristalizada) - poeira total'),
        ('02.01.789','Particulados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS) - não respiráveis'),
        ('02.01.999','Outros'),
        ('03.01.001','Agentes biológicos infecciosos e infectocontagiosos (bactérias, vírus, protozoários, fungos, príons, parasitas e outros)'),
        ('03.01.999','Outros'),
        ('04.01.001','Trabalho em posturas incômodas ou pouco confortáveis por longos períodos'),
        ('04.01.002','Postura sentada por longos períodos'),
        ('04.01.003','Postura de pé por longos períodos'),
        ('04.01.004','Frequente deslocamento a pé durante a jornada de trabalho'),
        ('04.01.005','Trabalho com esforço físico intenso'),
        ('04.01.006','Levantamento e transporte manual de cargas ou volumes'),
        ('04.01.007','Frequente ação de puxar/empurrar cargas ou volumes'),
        ('04.01.008','Frequente execução de movimentos repetitivos'),
        ('04.01.009','Manuseio de ferramentas e/ou objetos pesados por longos períodos'),
        ('04.01.010','Exigência de uso frequente de força, pressão, preensão, flexão, extensão ou torção dos segmentos corporais'),
        ('04.01.011','Compressão de partes do corpo por superfícies rígidas ou com quinas'),
        ('04.01.012','Exigência de flexões de coluna vertebral frequentes'),
        ('04.01.013','Uso frequente de pedais'),
        ('04.01.014','Uso frequente de alavancas'),
        ('04.01.015','Exigência de elevação frequente de membros superiores'),
        ('04.01.016','Manuseio ou movimentação de cargas e volumes sem pega ou com “pega pobre”'),
        ('04.01.017','Exposição a vibração de corpo inteiro'),
        ('04.01.018','Exposição a vibrações localizadas (mão-braço)'),
        ('04.01.019','Uso frequente de escadas'),
        ('04.01.020','Trabalho intensivo com teclado ou outros dispositivos de entrada de dados'),
        ('04.01.999','Outros'),
        ('04.02.001','Posto de trabalho improvisado'),
        ('04.02.002','Mobiliário sem meios de regulagem de ajuste'),
        ('04.02.003','Equipamentos e/ou máquinas sem meios de regulagem de ajuste ou sem condições de uso'),
        ('04.02.004','Posto de trabalho não planejado/adaptado para a posição sentada'),
        ('04.02.005','Assento inadequado '),
        ('04.02.006','Encosto do assento inadequado ou ausente'),
        ('04.02.007','Mobiliário ou equipamento sem espaço para movimentação de segmentos corporais'),
        ('04.02.008','Trabalho com necessidade de alcançar objetos, documentos, controles ou qualquer ponto além das zonas de alcance ideais para as características antropométricas do trabalhador'),
        ('04.02.009','Equipamentos ou mobiliários não adaptados à antropometria do trabalhador'),
        ('04.02.999','Outros'),
        ('04.03.001','Trabalho realizado sem pausas pré-definidas para descanso'),
        ('04.03.002','Necessidade de manter ritmos intensos de trabalho'),
        ('04.03.003','Trabalho com necessidade de variação de turnos '),
        ('04.03.004','Monotonia '),
        ('04.03.005','Trabalho noturno'),
        ('04.03.006','Insuficiência de capacitação para execução da tarefa'),
        ('04.03.007','Trabalho com utilização rigorosa de metas de produção'),
        ('04.03.008','Trabalho remunerado por produção'),
        ('04.03.009','Cadência do trabalho imposta por um equipamento'),
        ('04.03.010','Desequilíbrio entre tempo de trabalho e tempo de repouso'),
        ('04.03.999','Outros'),
        ('04.04.001','Condições de trabalho com níveis de pressão sonora fora dos parâmetros de conforto'),
        ('04.04.002','Condições de trabalho com índice de temperatura efetiva fora dos parâmetros de conforto'),
        ('04.04.003','Condições de trabalho com velocidade do ar fora dos parâmetros de conforto'),
        ('04.04.004','Condições de trabalho com umidade do ar fora dos parâmetros de conforto'),
        ('04.04.005','Condições de trabalho com Iluminação diurna inadequada '),
        ('04.04.006','Condições de trabalho com Iluminação noturna inadequada '),
        ('04.04.007','Presença de reflexos em telas, painéis, vidros, monitores ou qualquer superfície, que causem desconforto ou prejudiquem a visualização'),
        ('04.04.008','Piso escorregadio e/ou irregular'),
        ('04.04.999','Outros'),
        ('04.05.001','Excesso de situações de estresse'),
        ('04.05.002','Situações de sobrecarga de trabalho mental'),
        ('04.05.003','Exigência de alto nível de concentração, atenção e memória'),
        ('04.05.004','Trabalho em condições de difícil comunicação'),
        ('04.05.005','Excesso de conflitos hierárquicos no trabalho'),
        ('04.05.006','Excesso de demandas emocionais/afetivas no trabalho'),
        ('04.05.007','Assédio de qualquer natureza no trabalho'),
        ('04.05.008','Trabalho com demandas divergentes (ordens divergentes, metas incompatíveis entre si, exigência de qualidade X quantidade, entre outras)'),
        ('04.05.009','Exigência de realização de múltiplas tarefas, com alta demanda cognitiva'),
        ('04.05.010','Insatisfação no trabalho'),
        ('04.05.011','Falta de autonomia no trabalho'),
        ('04.05.999','Outros'),
        ('05.01.001','Diferença de nível menor ou igual a dois metros'),
        ('05.01.002','Diferença de nível maior que dois metros'),
        ('05.01.003','Iluminação diurna inadequada '),
        ('05.01.004','Iluminação noturna inadequada '),
        ('05.01.005','Condições ou procedimentos que possam provocar contato com eletricidade'),
        ('05.01.006','Arranjo físico deficiente ou inadequado'),
        ('05.01.007','Máquinas e equipamentos sem proteção'),
        ('05.01.008','Armazenamento inadequado'),
        ('05.01.009','Ferramentas necessitando de ajustes e manutenção'),
        ('05.01.010','Ferramentas inadequadas'),
        ('05.01.011','Ambientes com risco de engolfamento'),
        ('05.01.012','Ambientes com risco de afogamento'),
        ('05.01.013','Áreas classificadas'),
        ('05.01.014','Queda de objetos'),
        ('05.01.015','Intempéries'),
        ('05.01.016','Ambientes com risco de soterramento'),
        ('05.01.017','Animais peçonhentos'),
        ('05.01.018','Animais domésticos'),
        ('05.01.019','Animais selvagens'),
        ('05.01.020','Mobiliário e/ou superfícies com quinas vivas, rebarbas ou elementos de fixação expostos'),
        ('05.01.021','Pisos, passagens, passarelas, plataformas, rampas e corredores com saliências, descontinuidades, aberturas ou obstruções, ou escorregadios'),
        ('05.01.022','Escadas e rampas inadequadas'),
        ('05.01.023','Superfícies e/ou materiais aquecidos expostos'),
        ('05.01.024','Superfícies e/ou materiais em baixa temperatura expostos'),
        ('05.01.025','Áreas de trânsito de pedestres sem demarcação'),
        ('05.01.026','Áreas de trânsito de veículos sem demarcação'),
        ('05.01.027','Áreas de movimentação de materiais sem demarcação'),
        ('05.01.028','Condução de veículos de qualquer natureza em vias públicas'),
        ('05.01.029','Objetos cortantes e/ou perfurocortantes'),
        ('05.01.030','Movimentação de materiais'),
        ('05.01.031','Máquinas e equipamentos necessitando ajustes e manutenção'),
        ('05.01.032','Procedimentos de ajuste, limpeza, manutenção e inspeção deficientes ou inexistentes'),
        ('05.01.999','Outros'),
        ('06.01.001','Condições perigosas previstas na legislação trabalhista'),
        ('07.01.001','Associação de fatores de risco prevista na legislação previdenciária para fins de aposentadoria especial'),
        ('08.01.001','Umidade'),
        ('09.01.001','Ausência de Fator de Risco'),
    )
    
    choice_tipo_risco = (
        ('F','FÍSICOS'),
        ('Q','QUÍMICOS'),
        ('B','BIOLÓGICOS'),
        ('EB','ERGONÔMICOS-BIOMECÂNICOS'),
        ('EM','ERGONÔMICOS-MOBILIÁRIO E EQUIPAMENTOS'),
        ('EO','ERGONÔMICOS-ORGANIZACIONAIS'),
        ('EA','ERGONÔMICOS-AMBIENTAIS'),
        ('EP','ERGONÔMICOS-PSICOSSOCIAIS/COGNITIVOS'),
        ('A','MECÂNICOS/ACIDENTES'),
        ('P','PERIGOSOS'),
        ('AS','ASSOCIAÇÃO DE FATORES DE RISCO'),
        ('O','OUTROS FATORES DE RISCO'),
        ('NO','AUSÊNCIA DE FATORES DE RISCO'),  
    )

    tipo_risco = models.CharField(max_length=10, choices=choice_tipo_risco)
    fator_risco = models.CharField(max_length=10, choices=choice_riscos)
    
    def __str__(self):
        return self.tipo_risco
    class Meta:
        verbose_name_plural = "Tipos de Risco"

    
class Descricaoperigo(models.Model):

    IMPACTO0 = '200004300'
    IMPACTO1 = '200004600'
    IMPACTO2 = '200008300'
    IMPACTO3 = '200008600'
    IMPACTO4 = '200008900'
    QUEDA0 = '200012200'
    QUEDA1 = '200012300'
    QUEDA2 = '200012400'
    QUEDA3 = '200012500'
    QUEDA4 = '200012600'
    QUEDA5 = '200012700'
    QUEDA6 = '200012900'
    QUEDA7 = '200016300'
    QUEDA8 = '200016600'
    QUEDA9 = '200016900'
    APRISIONAMENTO0 = '200020100'
    APRISIONAMENTO1 = '200020300'
    APRISIONAMENTO2 = '200020500'
    APRISIONAMENTO3 = '200020700'
    APRISIONAMENTO4 = '200020900'
    ATRITO0 = '200024300'
    ATRITO1 = '200024400'
    ATRITO2 = '200024500'
    ATRITO3 = '200024600'
    ATRITO4 = '200024700'
    ATRITO5= '200024900'
    REAÇÃO0 = '200028300'
    REAÇÃO1 = '200028600'
    ESFORÇO0 = '200032200'
    ESFORÇO1 = '200032400'
    ESFORÇO2 = '200032600'
    ESFORÇO3 = '200032900'
    ELÉTRICA0 = '200036000'
    TEMPERATURA0 = '200040300'
    TEMPERATURA1 = '200040600'
    TEMPERATURA2 = '200044300'
    TEMPERATURA3 = '200044600'
    INALAÇÃO0 = '200048200'
    INGESTÃO = '200048400'
    ABSORÇÃO = '200048600'
    INALAÇÃO1 = '200048900'
    IMERSÃO0 = '200052000'
    RADIAÇÃO0 = '200056000'
    RADIAÇÃO1 = '200060000'
    RUÍDO = '200064000'
    VIBRAÇÃO = '200068000'
    PRESSÃO = '200072000'
    EXPOSIÇÃO0 = '200072300'
    EXPOSIÇÃO1 = '200072600'
    POLUIÇÃO0 = '200076200'
    POLUIÇÃO1 = '200076400'
    POLUIÇÃO2 = '200076600'
    POLUIÇÃO3 = '200076900'
    ATAQUE0 = '200080200'
    ATAQUE1 = '200080400'
    ATAQUE2 = '200080600'
    ATAQUE3 = '200080900'
    TIPO0 = '209000000'
    TIPO1 = '209500000'
    
    
    choice_perigos = (
        (IMPACTO0,'Impacto de pessoa contra objeto parado'),
        (IMPACTO1,'Impacto de pessoa contra objeto em movimento'),
        (IMPACTO2,'Impacto sofrido por pessoa de objeto que cai'),
        (IMPACTO3,'Impacto sofrido por pessoa de objeto projetado'),
        (IMPACTO4,'Impacto sofrido por pessoa, NIC'),
        (QUEDA0,'Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc.'),
        (QUEDA1,'Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus'),
        (QUEDA2,'Queda de pessoa com diferença de nível de material empilhado'),
        (QUEDA3,'Queda de pessoa com diferença de nível de veículo'),
        (QUEDA4,'Queda de pessoa com diferença de nível em escada permanente'),
        (QUEDA5,'Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc.'),
        (QUEDA6,'Queda de pessoa com diferença de nível, NIC'),
        (QUEDA7,'Queda de pessoa em mesmo nível em passagem ou superfície de sustentação'),
        (QUEDA8,'Queda de pessoa em mesmo nível sobre ou contra alguma coisa'),
        (QUEDA9,'Queda de pessoa em mesmo nível, NIC'),
        (APRISIONAMENTO0,'Aprisionamento em, sobre ou entre objetos em movimento convergente'),
        (APRISIONAMENTO1,'Aprisionamento em, sobre ou entre objeto parado e outro em movimento'),
        (APRISIONAMENTO2,'Aprisionamento em, sobre ou entre dois ou mais objetos em movimento'),
        (APRISIONAMENTO3,'Aprisionamento em, sobre ou entre desabamento ou desmoronamento'),
        (APRISIONAMENTO4,'Aprisionamento em, sob ou entre, NIC'),
        (ATRITO0,'Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto'),
        (ATRITO1,'Atrito ou abrasão por manusear objeto'),
        (ATRITO2,'Atrito ou abrasão por objeto em vibração'),
        (ATRITO3,'Atrito ou abrasão por corpo estranho no olho'),
        (ATRITO4,'Atrito ou abrasão por compressão repetitiva'),
        (ATRITO5,'Atrito ou abrasão, NIC'),
        (REAÇÃO0,'Reação do corpo a movimento involuntário'),
        (REAÇÃO1,'Reação do corpo a movimento voluntário'),
        (ESFORÇO0,'Esforço excessivo ao erguer objeto'),
        (ESFORÇO1,'Esforço excessivo ao empurrar ou puxar objeto'),
        (ESFORÇO2,'Esforço excessivo ao manejar, sacudir ou arremessar objeto'),
        (ESFORÇO3,'Esforço excessivo, NIC'),
        (ELÉTRICA0,'Elétrica, exposição a energia'),
        (TEMPERATURA0,'Temperatura muito alta, contato com objeto ou substância a'),
        (TEMPERATURA1,'Temperatura muito baixa, contato com objeto ou substância a'),
        (TEMPERATURA2,'Temperatura ambiente elevada, exposição a'),
        (TEMPERATURA3,'Temperatura ambiente baixa, exposição a'),
        (INALAÇÃO0,'Inalação de substância cáustica, tóxica ou nociva'),
        (INGESTÃO,'Ingestão de substância cáustica'),
        (ABSORÇÃO,'Absorção de substância cáustica'),
        (INALAÇÃO1,'Inalação, ingestão ou absorção, NIC'),
        (IMERSÃO0,'Imersão'),
        (RADIAÇÃO0,'Radiação não ionizante, exposição a'),
        (RADIAÇÃO1,'Radiação ionizante, exposição a'),
        (RUÍDO,'Ruído, exposição a'),
        (VIBRAÇÃO,'Vibração, exposição a'),
        (PRESSÃO,'Pressão ambiente, exposição a'),
        (EXPOSIÇÃO0,'Exposição à pressão ambiente elevada'),
        (EXPOSIÇÃO1,'Exposição à pressão ambiente baixa'),
        (POLUIÇÃO0,'Poluição da água, ação da (exposição à poluição da água)'),
        (POLUIÇÃO1,'Poluição do ar, ação da (exposição à poluição do ar)'),
        (POLUIÇÃO2,'Poluição do solo, ação da (exposição à poluição do solo)'),
        (POLUIÇÃO3,'Poluição, NIC, exposição a (exposição à poluição, NIC)'),
        (ATAQUE0,'Ataque de ser vivo por mordedura, picada, chifrada, coice, etc.'),
        (ATAQUE1,'Ataque de ser vivo com peçonha'),
        (ATAQUE2,'Ataque de ser vivo com transmissão de doença'),
        (ATAQUE3,'Ataque de ser vivo, NIC'),
        (TIPO0,'Tipo, NIC  '),
        (TIPO1,'Tipo inexistente'),
    )
    
    descricao_perigo = models.CharField(max_length=2000, choices=choice_perigos)
    def __str__(self):
        return self.descricao_perigo
        
    class Meta:
        verbose_name_plural = "Tipos de Perigo"
        
class Lesoes(models.Model):
    choice_lesao = (
            ('702000000','Lesão imediata'),
            ('702005000','Escoriação, abrasão (ferimento superficial)'),
            ('702010000','Corte, laceração, ferida contusa, punctura (ferida aberta)'),
            ('702015000','Contusão, esmagamento (superfície cutânea intacta)'),
            ('702020000','Distensão, torção'),
            ('702025000','Inflamação de articulação, tendão ou músculo - inclui sinovite, tenossionovite, etc. Não inclui distensão, torção ou suas consequências'),
            ('702030000','Luxação'),
            ('702035000','Fratura'),
            ('702040000','Queimadura ou escaldadura - efeito de temperatura elevada. Efeito do contato com substância quente. Inclui queimadura por eletricidade, mas não inclui choque elétrico. Não inclui queimadura por substância química, efeito de radiação, queimadura de sol, incapacidade sistêmica como intermação, queimadura por atrito, etc.'),
            ('702042000','Queimadura química (lesão de tecido provocada pela ação corrosiva de produto químico, suas emanações, etc.)'),
            ('702045000','Efeito de radiação (imediato) - queimadura de sol e toda forma de lesão de tecido, osso ou fluido orgânico, por exposição à radiação'),
            ('702048000','Congelamento, geladura e outros efeitos da exposição à baixa temperatura'),
            ('702050000','Asfixia, estrangulamento, afogamento'),
            ('702055000','Intermação, insolação, cãibra, exaustão e outros efeitos da temperatura ambiente elevada - não inclui queimadura de sol ou outros efeitos de radiação'),
            ('702060000','Choque elétrico e eletroplessão (eletrocussão)'),
            ('702065000','Hérnia de qualquer natureza, ruptura'),
            ('702070000','Amputação ou enucleação'),
            ('702075000','Perda ou diminuição de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
            ('702080000','Concussão cerebral'),
            ('702090000','Lesão imediata, NIC'),
            ('704020000','Doença contagiosa ou infecciosa (tuberculose, brucelose, etc.)'),
            ('704030000','Pneumoconiose (silicose, asbestose, etc.)'),
            ('704040000','Dermatose (erupção, inflamação da pele, inclusive furúnculo, etc.). Geralmente provocada pelo contato direto com substâncias ou agentes sensibilizantes ou irritantes, tais como medicamentos, óleos, agentes biológicos, plantas, madeiras ou metais. Não inclui lesão provocada pela ação corrosiva de produtos químicos, queimadura por contato com substâncias quentes, efeito de exposição à radiação, efeito de exposição a baixas temperaturas ou inflamação ou irritação causada por fricção ou impacto'),
            ('704050000','Envenenamento sistêmico - condição mórbida sistêmica provocada por inalação, ingestão ou absorção cutânea de substância tóxica, que afete o metabolismo, o funcionamento do sistema nervoso, do aparelho circulatório, do aparelho digestivo, do aparelho respiratório, dos órgãos de excreção, do sistema músculoesquelético, etc., inclui ação de produto químico, medicamento, metal ou peçonha. Não inclui efeito de radiação, pneumoconiose, efeito corrosivo de produto químico, irritação cutânea, septicemia ou caso de ferida infectada'),
            ('704060000','Perda ou diminuição mediatas de sentido (audição, visão, olfato, paladar e tato, desde que não seja sequela de outra lesão)'),
            ('704070000','Efeito de radiação (mediato) - queimadura do sol e toda forma de lesão de tecido, osso, ou fluido orgânico por exposição à radiação.'),
            ('704090000','Doença, NIC'),
            ('706050000','Lesões múltiplas'),
            ('706090000','Outras lesões, NIC'),
    )
        
    descricao_lesao = models.CharField(max_length=1000, choices=choice_lesao)
    def __str__(self):
        return self.descricao_lesao
    
    class Meta:
        verbose_name_plural = "Tipos de Lesão"

class Fonterisco(models.Model):
    
    choice_fonte = (
        ('200004300','Impacto de pessoa contra objeto parado. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'),
        ('200004600','Impacto de pessoa contra objeto em movimento. Aplica-se a casos em que a lesão foi produzida por impacto da pessoa acidentada contra a fonte da lesão, tendo sido o movimento que produziu o contato originalmente o da pessoa e não o da fonte da lesão, exceto quando o movimento do acidentado tiver sido provocado por queda. Inclui casos de alguém chocar-se contra alguma coisa, tropeçar em alguma coisa, ser empurrado ou projetado contra alguma coisa, etc. Não inclui casos de salto para nível inferior.'),
        ('200008300','Impacto sofrido por pessoa, de objeto que cai. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
        ('200008600','Impacto sofrido por pessoa, de objeto projetado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
        ('200008900','Impacto sofrido por pessoa, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido da fonte da lesão e não do acidentado o movimento que originou o contato.'),
        ('200012200','Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200012300','Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus não permitem o apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200012400','Queda de pessoa com diferença de nível de material empilhado. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200012500','Queda de pessoa com diferença de nível de veículo. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200012600','Queda de pessoa com diferença de nível em escada permanente cujos degraus permitem apoio integral do pé. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200012700','Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc. (da borda da abertura). Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200012900','Queda de pessoa com diferença de nível, NIC. Aplica-se a casos em que a lesão foi produzida por impacto entre o acidentado e a fonte da lesão, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade. 2) O ponto de contato com a fonte da lesão estava abaixo da superfície que suportava o acidentado no início da queda. Inclui salto para nível inferior.'),
        ('200016300','Queda de pessoa em mesmo nível em passagem ou superfície de sustentação. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
        ('200016600','Queda de pessoa em mesmo nível sobre ou contra alguma coisa. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
        ('200016900','Queda de pessoa em mesmo nível, NIC. Aplica-se a casos em que a lesão foi produzida por Impacto entre o acidentado e um objeto externo, tendo sido do acidentado o movimento que produziu o contato, nas seguintes circunstâncias: 1) O movimento do acidentado foi devido à ação da gravidade com perda do equilíbrio e impossibilidade de manter-se de pé. 2) O ponto de contato com a fonte da lesão estava, no momento do início da queda, ao nível ou acima da superfície que suportava o acidentado.'),
        ('200020100','Aprisionamento em, sob ou entre objetos em movimento convergente (calandra) ou de encaixe. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('200020300','Aprisionamento em, sob ou entre um objeto parado e outro em movimento. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('200020500','Aprisionamento em, sob ou entre dois ou mais objetos em movimento (sem encaixe). Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('200020700','Aprisionamento em, sob ou entre desabamento ou desmoronamento de edificação, barreira, etc. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('200020900','Aprisionamento em, sob ou entre, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por compressão, pinçamento ou esmagamento entre um objeto em movimento e outro parado, entre dois objetos em movimento ou entre partes de um mesmo objeto. Não se aplica quando a fonte da lesão for um objeto livremente projetado ou em queda livre.'),
        ('200024300','Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto (não em vibração). Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('200024400','Atrito ou abrasão por manusear objeto (não em vibração).  Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('200024500','Atrito ou abrasão por objeto em vibração. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('200024600','Atrito ou abrasão por corpo estranho no olho. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('200024700','Atrito ou abrasão por compressão repetitiva Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('200024900','Atrito ou abrasão, NIC. Aplica-se a casos, sem impacto, em que a lesão foi produzida por pressão, vibração ou atrito entre o acidentado e a fonte da lesão.'),
        ('200028300','Reação do corpo a seus movimentos - movimento involuntário (escorregão sem queda, etc.). Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'),
        ('200028600','Reação do corpo a seus movimentos - movimento voluntário. Aplica-se a casos, sem impacto, em que a lesão foi causada exclusivamente por movimento livre do corpo humano que causou tensão ou torção em alguma parte do corpo. Geralmente, aplica-se à ocorrência de torções, distensões, rupturas ou outras lesões internas, resultantes da adoção de uma posição forçada ou de movimentos involuntários provocados por sustos ou esforços de recuperação da posição normal em casos de escorregão ou perda de equilíbrio. Inclui casos de lesão muscular ou interna resultantes de movimentos individuais como andar, subir, correr, tentar alcançar algo, voltar-se, curvar-se, etc., quando tais movimentos forem a própria fonte da lesão. Não se aplica a esforço excessivo ao erguer, puxar ou empurrar objetos ou a casos em que o movimento do corpo, voluntário ou involuntário, tenha tido por resultado contato violento com algum objeto.'),
        ('200032200','Esforço excessivo ao erguer objeto. Ver explicações da classificação anterior (200028000).'),
        ('200032400','Esforço excessivo ao empurrar ou puxar objeto. Ver explicações da classificação anterior (200028000).'),
        ('200032600','Esforço excessivo ao manejar, sacudir ou arremessar objeto. Ver explicações da classificação anterior (200028000).'),
        ('200032900','Esforço excessivo, NIC. Ver explicações da classificação anterior (200028000).'),
        ('200036000','Exposição a energia elétrica. Aplica-se somente a casos sem impacto, em que a lesão consiste em choque elétrico, queimadura ou eletroplessão (eletrocussão).'),
        ('200040300','Contato com objeto ou substância a temperatura muito alta. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'),
        ('200040600','Contato com objeto ou substância a temperatura muito baixa. Aplica-se somente a casos, sem impacto, em que a lesão consiste em queimadura, geladura, etc., resultante queimadura, geladura, etc., resultante de contato com objetos, ar, gases, vapores ou líquidos quentes ou frios. Não se aplica a casos em que a lesão foi provocada pelas características tóxicas ou cáusticas de produtos químicos ou a queimadura por descarga elétrica.'),
        ('200044300','Exposição à temperatura ambiente elevada. Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'),
        ('200044600','Não se aplica aos casos de lesão proveniente de exposição à radiação solar ou outras radiações. Também não se aplica a casos de queimadura ou geladura provocada por contato com objeto ou substância a temperaturas extremas ou queimadura devida à energia elétrica.'),
        ('200048200','Inalação de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('200048400','Ingestão de substancia cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('200048600','Absorção (por contato) de substância cáustica, tóxica ou nociva. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('200048900','Inalação, ingestão e absorção, NIC. Aplica-se somente a casos, sem impacto, em que a lesão foi provocada por inalação, absorção ou ingestão de substâncias nocivas. Geralmente, refere-se a intoxicações, envenenamentos, queimaduras, irritações ou reações alérgicas por produtos químicos.'),
        ('200052000','Imersão. Aplica-se aos acidentes que têm por consequência o afogamento.'),
        ('200056000','Exposição à radiação não ionizante. Aplica-se a casos em que as lesões são provocadas por exposição à radiação solar ou outras radiações não ionizantes (por exemplo: ultravioleta e infravermelho).'),
        ('200060000','Exposição à radiação ionizante.'),
        ('200064000','Exposição ao ruído.'),
        ('200068000','Exposição à vibração.'),
        ('200072300','Exposição à pressão ambiente elevada.'),
        ('200072600','Exposição à pressão ambiente baixa.'),
        ('200076200','Exposição à poluição da água.'),
        ('200076400','Exposição à poluição do ar.'),
        ('200076600','Exposição à poluição do solo.'),
        ('200076900','Exposição à poluição, NIC.'),
        ('200080200','Ataque de ser vivo por mordedura, picada, chifrada, coice, etc., não se aplicando no caso de haver peçonha ou transmissão de doença.'),
        ('200080400','Ataque de ser vivo com peçonha.'),
        ('200080600','Ataque de ser vivo com transmissão de doença.'),
        ('200080900','Ataque de ser vivo (inclusive do homem), NIC.'),
        ('200080901','Contato com pessoas doentes ou material infecto-contagiante - agentes biológicos.'),
        ('209000000','Tipo, NIC'),
        ('209500000','Tipo inexistente'),
    )
    
    fonte_risco = models.CharField(max_length=500, choices=choice_fonte)
    
    def __str__(self):
        return self.fonte_risco
    
    class Meta:
        verbose_name_plural = "Fontes de Risco"


class Medidasimplementadas(models.Model):
    medidas_implementadas = models.CharField(max_length=200)
    def __str__(self):
        return self.medidas_implementadas
    class Meta:
        verbose_name_plural = "Medidas Implementadas"
    
class Tempoexposicao(models.Model):
    
    HH0 = '0'
    HH1 = '1'
    HH2 = '2'
    HH3 = '3'
    HH4 = '4'
                    
    choice_exposicao = (
        (HH0,'Até 1 hora por dia'),
        (HH1,'Até 2 horas por dia'),
        (HH2,'Até 4 horas por dia'),
        (HH3,'Até 6 horas por dia'),
        (HH4,'Até 8 horas por dia'),
        )
    
    tempo_exposicao = models.CharField(max_length=200, choices=choice_exposicao)
    def __str__(self):
        return self.tempo_exposicao
    class Meta:
        verbose_name_plural = "Tempos de exposição"
    
class Inventario(models.Model):
    tipo_risco = models.ForeignKey(Tiporisco, verbose_name=("tipo_risco"), on_delete=models.CASCADE)
    descricao_perigo = models.ForeignKey(Descricaoperigo, verbose_name=("descricao_perigo"), on_delete=models.CASCADE)
    descricao_lesao = models.ForeignKey(Lesoes, verbose_name=("lesoes"), on_delete=models.CASCADE)
    fonte_risco = models.ForeignKey(Fonterisco, verbose_name=("fonte"), on_delete=models.CASCADE)
    medidas_implementadas = models.ForeignKey(Medidasimplementadas, verbose_name=("medidas"), on_delete=models.CASCADE)
    tempo_exposicao = models.ForeignKey(Tempoexposicao, verbose_name=("exposicao"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao_perigo

    class Meta:
        verbose_name_plural = "Inventários de Risco"

class Medidascontrole(models.Model):
    
    choice_medidas_controle = (
        ('A','Aceitável'),
        ('I','Ineficiente'),
        ('D','Deficiente'),
        ('MD','Muito Deficiente'),
        ('DT','Deficiência Total'),
        )
    
    choice_nmc = (
        ('1','1'),
        ('2','2'),
        ('6','6'),
        ('10','10'),
        ('14','14'),
        )
    
    choice_significado = (
        ('1','Não Foram detectadas anomalias'),
        ('1','O perigo está controlado'),
        ('2','Foram detectados fatores de risco de menor importancia'),
        ('2','O dano pode ocorrer algumas vezes'),
        ('6','Foram detectados alguns fatores de risco significativos'),
        ('6','As medidas preventivas existentes tem sua eficávia reduzida'),
        ('10','Foram detectados fatores de risco significativos'),
        ('10','As medidas preventivas existentes são ineficazes'),
        ('10','O dano ocorerá na maior parte das circunstâncias'),
        ('14','Medidas preventivas inexistentes ou desadequadas'),
        ('14','São esperados danos na maior parte das situações'),
        )

    
    medidas_controle = models.CharField(max_length=200, choices=choice_medidas_controle)
    nmc = models.CharField(max_length=200, choices=choice_nmc)
    significado = models.CharField(max_length=200, choices=choice_significado)
    def __str__(self):
        return self.medidas_controle
    class Meta:
        verbose_name_plural = "Medidas de Controle"

class Nivelexposicao(models.Model):
    choice_nivel_exposicao = (
    ('E','Exporádica'),
    ('P','Pouco Frequente'),
    ('O','Ocasional'),
    ('F','Frequente'),
    ('C','Continuada'),
    )
    
    choice_ne = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        )

    choice_significado = (
        ('1','Uma vez por ano, por pouco tempo(minutos)'),
        ('2','Algumas vezes por ano e por período de tempo determinado'),
        ('3','Algumas vezes por mês'),
        ('4','Várias vezes durante o período laboral, ainda que com tempos curtos'),
        ('4','Várias vezes por semana ou diário'),
        ('5','Várias vezes por dia com tempo prolongado ou continuamente'),
        )

    nivel_exposicao = models.CharField(max_length=200, choices=choice_nivel_exposicao)
    ne = models.CharField(max_length=200, choices=choice_ne)
    significado = models.CharField(max_length=200, choices=choice_significado)
    def __str__(self):
        return self.nivel_exposicao
    class Meta:
        verbose_name_plural = "Níveis de Exposição"

class Nivelprobabilidade(models.Model):
    choice_nivel_probabilidade = (
    ('MB','Muito Baixa'),
    ('PF','Pouco Frequente'),
    ('M','Média'),
    ('A','Alta'),
    ('MA','Muito Alta'),
    )
    
    choice_np = (
        ('1','1 a 3'),
        ('4','4 a 6'),
        ('8','8 a 20'),
        ('24','24 a 30'),
        ('40','40 a 70'),
        )
    
    choice_significado = (
        ('1','Não é de se esperar que a situação perigosa se materialize, ainda que possa ser concebida'),
        ('4','A materialização da situação perigosa pode ocorrer'),
        ('8','A materialização da situação perigosa é passível de ocorrer pelo menos uma vez com danos'),
        ('24','A materizalização da situação perigosa pode ocorrer várias vezes durante o peródo de trabalho'),
        ('40','Normalmente a materizalização da situação perigosa ocorre com frequência'),
        )

    
    nivel_probabilidade = models.CharField(max_length=200, choices=choice_nivel_probabilidade)
    np = models.CharField(max_length=200, choices=choice_np)
    significado = models.CharField(max_length=200, choices=choice_significado)
    def __str__(self):
        return self.nivel_probabilidade
    class Meta:
        verbose_name_plural = "Níveis de Probabilidade"
            
class Nivelgravidade(models.Model):
    choice_nivel_gravidade = (
    ('I','Insignificante'),
    ('L','Leve'),
    ('M','Moderado'),
    ('G','Grave'),
    ('M','Mortal'),
    )
    
    choice_ng = (
        ('10','10'),
        ('25','25'),
        ('60','60'),
        ('90','90'),
        ('155','155'),
        )

    choice_significado = (
        ('10','Não há danos pessoais'),
        ('25','Pequenas lesões que não requerem hospitalização. Apenas primeiros socorros'),
        ('60','Lesões com incapacidade transitória. REquerem tratamento médico'),
        ('90','Lesões graves que podem ser irreparáveis'),
        ('155','Morte ou incapacidade permanente'),
        )

    nivel_gravidade = models.CharField(max_length=200, choices=choice_nivel_gravidade)
    ng = models.CharField(max_length=200, choices=choice_ng)
    significado = models.CharField(max_length=200, choices=choice_significado)

    def __str__(self):
        return self.nivel_gravidade
    class Meta:
        verbose_name_plural = "Níveis de Gravidade"    

class Nivelrisco(models.Model):
    ng = models.ForeignKey(Nivelgravidade, on_delete=models.CASCADE)
    np = models.ForeignKey(Nivelprobabilidade, on_delete=models.CASCADE)
    nivel_risco = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nivel_risco
    class Meta:
        verbose_name_plural = "Níveis de Risco" 

class Classificacaorisco(models.Model):

    choice_classificacao_risco = (
    ('C','Crítico'),
    ('A','Alto'),
    ('M','Moderado'),
    ('B','Baixo'),
    ('I','Irrelevante'),
    )
    
    choice_nr = (
        ('10850','3360 a 10850'),
        ('3100','1240 a 3100'),
        ('1200','360 a 1200'),
        ('300','90 a 300'),
        ('80','10 a 80'),
        )

    choice_significado = (
        ('10850','Situação CRITÍCA'),
        ('10850','Intervenção imediata'),
        ('10850','Isolar o perigo até serem adaptadas às medidas de controle'),
        ('3100','Situação a CORRIGIR'),
        ('3100','Adaptar medidas de controle enquanto a situação perigosa não for eliminada ou reduzida'),
        ('1200','Situação a MELHORAR'),
        ('1200','Deverão ser elaborados planos, programas ou procedimentos, documentados de intervenção'),
        ('300','MELHORAR SE POSSÍVEL, justificando a intervenção'),
        ('80','Intervir apenas se uma análise mais pormenorizada o justificar'),
        )

    
    nr = models.CharField(max_length=200, choices=choice_nr)
    classificacao_risco = models.CharField(max_length=200, choices=choice_classificacao_risco)
    significado = models.CharField(max_length=200, choices=choice_significado)
    
    def __str__(self):
        return self.classificacao_risco
    class Meta:
        verbose_name_plural = "Classificação de Riscos"

class Avaliacaorisco(models.Model):
    medidas_controle = models.ForeignKey(Medidascontrole, verbose_name=('medidas_controle'), on_delete=models.CASCADE)
    nivel_exposicao = models.ForeignKey(Nivelexposicao, verbose_name=('nivel_exposicao'), on_delete=models.CASCADE)
    nivel_probabilidade = models.ForeignKey(Nivelprobabilidade, verbose_name=('nivel_probabilidade'), on_delete=models.CASCADE)
    nivel_gravidade = models.ForeignKey(Nivelgravidade, verbose_name=('nivel_gravidade'), on_delete=models.CASCADE)
    nivel_risco = models.ForeignKey(Nivelrisco, verbose_name=('nivel_risco'), on_delete=models.CASCADE)
    classificacao_risco = models.ForeignKey(Classificacaorisco, verbose_name=('classificacao_risco'), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.classificacao_risco
    class Meta:
        verbose_name_plural = "Avaliações de Risco"
        
class PlanoAcao(models.Model):
    oque = models.CharField(max_length=200)
    porque = models.CharField(max_length=200)
    quando = models.CharField(max_length=200)
    quem = models.CharField(max_length=200)
    onde = models.CharField(max_length=200)
    como = models.CharField(max_length=200)
    quanto = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return {self.oque}
    
    class Meta:
        verbose_name_plural = "Planos de Ação"

# Gravação dos registros    
class UsuarioInventario(models.Model):
    usuario = models.ForeignKey(Usuario, verbose_name=("usuario"), on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, verbose_name=("inventario"), on_delete=models.CASCADE)

class UsuarioPlano(models.Model):
    usuario = models.ForeignKey(Usuario, verbose_name=("usuario"), on_delete=models.CASCADE)
    plano_acao = models.ForeignKey(PlanoAcao, verbose_name=("planoacao"), on_delete=models.CASCADE)