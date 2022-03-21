from decimal import Decimal
from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

## SKILLS
#  HARD SKILLS
class Hard_Skill (models.Model):
    PL = 'PL' # Programming Language
    DL = 'DL' # Non-programming developing language
    FL = 'FL' # Framework or Library
    DB = 'DB' # Database
    HL = 'HL' # Human Speaking/Writing language
    OS = 'OS' # Operating System
    VT = 'VT' # Virtualization technology
    SW = 'SW' # Software skill
    OT = 'OT' # Other hard skill
    type_skill_choices = [
        (PL, 'Programming Language'),
        (DL, 'Non-programming developing language'),
        (FL, 'Framework or Library'),
        (DB, 'Database'),
        (HL, 'Human Speaking/Writing language'),
        (OS, 'Operating System'),
        (VT, 'Virtualization technology'),
        (SW, 'Software Skill'),
        (OT, 'Other hard skill')
    ]
    type_skill = models.CharField(
        max_length=2,
        choices=type_skill_choices,
        default=PL
    )
    name = models.CharField(max_length=50, verbose_name='Name', blank=False, null=False)
    percentage = models.IntegerField(verbose_name='Percentage', default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], blank=False, null=False)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Hard Skill'
        verbose_name_plural = 'Hard Skills'

#  SOFT SKILLS
class Soft_Skill (models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', blank=False, null=False)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Soft Skill'
        verbose_name_plural = 'Soft Skills'

## CREDENTIALS
#  CREDENTIAL EMITTERS
class Credential_Emitter (models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    picture = models.ImageField(upload_to='portfolio/pictures/', verbose_name='Picture', null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Credential Emitter'
        verbose_name_plural = 'Credential Emitters'

#  CREDENTIALS
class Credential (models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    date_earned = models.DateField(verbose_name='Date earned', default=now)
    date_expiration = models.DateField(verbose_name='Date of expiration', blank=True, null=True)
    description = models.TextField(verbose_name='Description', default="", blank=True, null=True)
    embed = models.TextField(verbose_name='Embed Code', default="", blank=True, null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    document = models.FileField(upload_to='portfolio/documents/', verbose_name='Document', null=True)
    picture = models.ImageField(upload_to='portfolio/pictures/', verbose_name='Picture', null=True)
    hard_skills = models.ManyToManyField(Hard_Skill)
    emitter_credential = models.ManyToManyField(Credential_Emitter)

    P = 'P' # Professional Universitty Title
    T = 'T' # Technician Title
    C = 'C' # Professional Certification
    B = 'B' # Badge
    L = 'L' # Human Language Official Test Certification
    type_credential_choices = [
        (P, 'Professional University Title'),
        (T, 'Technician Title'),
        (C, 'Professional certification'),
        (B, 'Badge'),
        (L, 'Human Language Official Test Certification')
    ]
    type_credential = models.CharField(
        max_length=1,
        choices=type_credential_choices,
        default=B
    )

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Credential'
        verbose_name_plural = 'Credentials'

## PROJECTS
class Project (models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', blank=False, null=False)
    publication_date = models.DateField(verbose_name='Publication Date', default=now)
    start_date = models.DateField(verbose_name='Project Start Date', blank=True, null=True)
    end_date = models.DateField(verbose_name='Project End Date', blank=True, null=True)
    short_description = models.CharField(max_length=100, verbose_name='Short Description', default="", blank=True, null=True)
    long_description = models.TextField(verbose_name='Long Description', default="", blank=True, null=True)
    project_url = models.URLField(verbose_name='Project URL', blank=True, null=True)
    code_url = models.URLField(verbose_name='Code URL', blank=True, null=True)
    picture = models.ImageField(upload_to='portfolio/pictures/', verbose_name='Picture', null=True)
    hard_skills = models.ManyToManyField(Hard_Skill)
    soft_skills = models.ManyToManyField(Soft_Skill)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-publication_date']

