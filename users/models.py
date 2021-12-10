from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import FileExtensionValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from partners.models import Category


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


GENDER = (("male", "male"), ("female", "female"), ("other", "other"))

LAN = (
    ("AF", "Afrikaans"),
    ("SQ", "Albanian"),
    ("AR", "Arabic"),
    ("HY", "Armenian"),
    ("EU", "Basque"),
    ("BN", "Bengali"),
    ("BG", "Bulgarian"),
    ("CA", "Catalan"),
    ("KM", "Cambodian"),
    ("ZH", "Chinese"),
    ("HR", "Croatian"),
    ("CS", "Czech"),
    ("DA", "Danish"),
    ("NL", "Dutch"),
    ("EN", "English"),
    ("ET", "Estonian"),
    ("FJ", "Fiji"),
    ("FI", "Finnish"),
    ("FR", "French"),
    ("KA", "Georgian"),
    ("DE", "German"),
    ("EL", "Greek"),
    ("GU", "Gujarati"),
    ("HE", "Hebrew"),
    ("HI", "Hindi"),
    ("HU", "Hungarian"),
    ("IS", "Icelandic"),
    ("ID", "Indonesia"),
    ("GA", "Irish"),
    ("IT", "Italian"),
    ("JA", "Japanese"),
    ("JW", "Javanese"),
    ("KO", "Korean"),
    ("LA", "Latin"),
    ("LV", "Latvian"),
    ("LT", "Lithuania"),
    ("MK", "Macedonia"),
    ("MS", "Malay"),
    ("ML", "Malayalam"),
    ("MT", "Maltese"),
    ("MI", "Maori"),
    ("MR", "Marathi"),
    ("MN", "Mongolian"),
    ("NE", "Nepali"),
    ("NO", "Norwegian"),
    ("FA", "Persian"),
    ("PL", "Polish"),
    ("PT", "Portugues"),
    ("PA", "Punjabi"),
    ("QU", "Quechua"),
    ("RO", "Romanian"),
    ("RU", "Russian"),
    ("SM", "Samoan"),
    ("SR", "Serbian"),
    ("SK", "Slovak"),
    ("SL", "Slovenian"),
    ("ES", "Spanish"),
    ("SW", "Swahili"),
    ("SV", "Swedish"),
    ("TA", "Tamil"),
    ("TT", "Tatar"),
    ("TE", "Telugu"),
    ("TH", "Thai"),
    ("BO", "Tibetan"),
    ("TO", "Tonga"),
    ("TR", "Turkish"),
    ("UK", "Ukrainian"),
    ("UR", "Urdu"),
    ("UZ", "Uzbek"),
    ("VI", "Vietnames"),
    ("CY", "Welsh"),
    ("XH", "Xhosa"),
)


class UserProfile(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default=None, null=True
    )
    user_name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[UnicodeUsernameValidator()]
    )
    last_name = models.CharField(
        max_length=75, null=True, blank=True, validators=[UnicodeUsernameValidator()]
    )
    profile_image = models.ImageField(
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
        blank=True,
    )
    id_card_front = models.ImageField(
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
        blank=True,
    )
    id_card_back = models.ImageField(
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
        blank=True,
    )
    birth_date = models.DateField(null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    degree = models.CharField(null=True, max_length=100, blank=True)
    degree_image = models.ImageField(
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
        blank=True,
    )
    gender = models.CharField(null=True, choices=GENDER, default="male", max_length=9)
    address = models.CharField(null=True, max_length=75)
    organization = models.CharField(null=True, max_length=75, blank=True)
    phone_number = models.CharField(null=True, max_length=75)
    language = models.CharField(null=True, choices=LAN, default="EN", max_length=75)
    bio = models.CharField(null=True, blank=True, max_length=20)
    description = models.TextField(null=True, blank=True, max_length=2500)
    seller = models.BooleanField(default=False)
    valid = models.BooleanField(default=False)
    reject = models.BooleanField(null=True)
    admin_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_name}"
