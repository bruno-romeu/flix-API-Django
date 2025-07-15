from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('CHILE', 'Chile'),
    ('ARGENTINA', 'Argentina'),
    ('MEXICO', 'México'),
    ('SPAIN', 'Espanha'),
    ('ITALY', 'Itália'),
    ('PORTUGAL', 'Portugal'),
    ('RUSSIA', 'Rússia'),
    ('SOUTH_KOREA', 'Coreia do Sul'),
    ('SOUTH_AFRICA', 'África do Sul'),
    ('SWEDEN', 'Suécia'),
    ('NORWAY', 'Noruega'),
    ('FINLAND', 'Finlândia'),
    ('DENMARK', 'Dinamarca'),
    ('NETHERLANDS', 'Países Baixos'),
    ('BELGIUM', 'Bélgica'),
    ('SWITZERLAND', 'Suíça'),
    ('UK', 'Reino Unido'),
    ('FRANCE', 'França'),
    ('GERMANY', 'Alemanha'),
    ('CANADA', 'Canadá'),
    ('AUSTRALIA', 'Austrália'),
    ('INDIA', 'Índia'),
    ('JAPAN', 'Japão'),
    ('CHINA', 'China'),
    ('OTHER', 'Outro'),
    ('NOT_SPECIFIED', 'Não Especificado'),

)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
