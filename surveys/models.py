from django.db import models
from uuid import uuid4
from django.utils.translation import gettext as _
from base.models import User


class EndScreenSocialMedia(models.Model):
    
    class SocialMediaType(models.TextChoices):
        INSTAGRAM = 'instagram',_('INSTAGRAM'),
        FACEBOOK = 'facebook',_('FACEBOOK'),
        WHATSAPP = 'whatsapp',_('WHATSAPP'),
        TWITTER = 'twitter',_('TWITTER'),
        EMAIL = 'email',_('EMAIL'),
        TIKTOK = 'tiktok',_('TIKTOK'),
    
    id = models.UUIDField(default=uuid4, primary_key=True)
    social_media_link = models.URLField()
    media_type = models.TextField(choices=SocialMediaType.choices, default=SocialMediaType.EMAIL, max_length=20)
    end_screen = models.ForeignKey('EndScreen',on_delete=models.CASCADE)



class Surveys(models.Model):

    class Status(models.TextChoices):
        DEVELOPMENT = 'DEVELOPMENT', _('DEVELOPMENT')
        PRODUCTION = 'PRODUCTION', _('PRODUCTION')

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.TextField(max_length=250)
    status = models.TextField(choices=Status.choices, default=Status.DEVELOPMENT, max_length=15)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    
    show_time_to_complete = models.BooleanField(default=False)
    show_number_of_submissions = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def am_i_d_owner(self, user:User):
        if self.host.id != user.id: raise ValueError('You are not authorize to access this action')
        
    
    def __str__(self):
        return self.name

class Background(models.Model):
    background_color = models.CharField(max_length=50, null=True)
    background_image = models.URLField(null=True)
    survey_block = models.ForeignKey('SurveyBlockType', on_delete=models.CASCADE, null=True, blank=True)

class PhoneNumbers(models.Model):
    check_number = models.BooleanField(default=False)
    format_number = models.BooleanField(default=True)
    placeholder = models.CharField(max_length=500, default='Placeholder')
    
class PictureChoice(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    label = models.TextField(max_length=1000, null=True, blank=True)
    super_size = models.BooleanField(default=False)
    multiple_selection = models.BooleanField(default=True)
    
class PictureChoiceImages(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    picture = models.ForeignKey(PictureChoice, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField()
    alt_tag = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    saturation = models.PositiveIntegerField(default=0)
    contrast = models.PositiveIntegerField(default=0)
    brightness = models.PositiveIntegerField(default=0)
    blur = models.PositiveIntegerField(default=0)
    x = models.PositiveIntegerField(default=1)
    y = models.PositiveIntegerField(default=1)
    hue = models.PositiveIntegerField(default=1)
    grayscale = models.PositiveIntegerField(default=0)
    pixelate = models.PositiveIntegerField(default=0)
    rotationIndex = models.PositiveIntegerField(default=0)

class Date(models.Model):
   class Seperator(models.TextChoices):
       DASH = '-',_('-')
       DOT = '.',_('.')
       SLASH = '/',_('/')

   class Format(models.TextChoices):
       YEARFIRST = 'yyyy-MM-dd',_('yyyy-MM-dd')
       DAYFIRST = 'dd-MM-yyyy',_('dd-MM-yyyy')
       MONTHFIRST = 'MM-yyyy-dd',_('MM-yyyy-dd')
       DEFAULT = 'PPP', _('PPP')

   

   date = models.DateField(null=True, blank=True)
   label = models.TextField(max_length=1000, null=True, blank=True)
   seperator = models.TextField(choices=Seperator.choices, default=Seperator.SLASH, max_length=30)
   format = models.TextField(choices=Format.choices, default=Format.DAYFIRST, max_length=30)
   class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    domain = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    
class Number(models.Model):
    min = models.PositiveIntegerField(null=True, blank=True)
    max = models.PositiveIntegerField(null=True, blank=True)
    
class ShortText(models.Model):
    max_character = models.PositiveIntegerField(default=100)
    label = models.TextField(max_length=1000, null=True, blank=True)
    place_holder = models.CharField(max_length=500, default='PlaceHolder')

class LongText(models.Model):
    max_character = models.PositiveIntegerField(default=100)
    label = models.TextField(max_length=1000, null=True, blank=True)
    place_holder = models.CharField(max_length=500, default='PlaceHolder')
    
class DropDown(models.Model):
    label = models.TextField(max_length=1000, null=True, blank=True)
    alphabetically = models.BooleanField(default=False)
    multiple_selection = models.BooleanField(default=True)
    allow_search = models.BooleanField(default=False)
    
class DropDownOpions(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    drop_down = models.ForeignKey(DropDown, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=1000)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model):
    ratings_length = models.PositiveIntegerField(default=5)
    label = models.TextField(max_length=1000, null=True, blank=True)
    
class Choices(models.Model):
    multiple_selection = models.BooleanField(default=True)
    vertical_alignment = models.BooleanField(default=False)
    label = models.TextField(max_length=1000, null=True, blank=True)
    randomize = models.BooleanField(default=False)

class Email(models.Model):
    check_email = models.BooleanField(default=False)
    label = models.TextField(max_length=1000, null=True, blank=True)
    
class YesNo(models.Model):
    allow_reselect = models.BooleanField(default=True)
    
class Website(models.Model):
    accept_url_with = models.TextField(null=True, blank=True)
    label = models.TextField(max_length=1000, null=True, blank=True)
    
class RedirectWithUrl(models.Model):
    url = models.URLField()
    message = models.TextField(max_length=1000, null=True, blank=True, default="Redirect to url")
    custom_html = models.TextField(max_length=10000, null=True, blank=True)
    click_option = models.BooleanField(default=True)
    button_text = models.CharField(default="Click here if you are not redirected.", max_length=500)
    


class WelcomeScreen(models.Model):
    
    message = models.CharField(max_length=500)
    label = models.TextField(max_length=2000, null=True)
    have_continue_button = models.BooleanField(default=True)
    button_text = models.CharField(max_length=50, null=True, default='Start Questionaire.')
    background_image = models.URLField(null=True)
    custom_html = models.TextField(max_length=20000, null=True)
    time_to_complete = models.PositiveIntegerField(null=True)
    

class EndScreen(models.Model):
    button_link = models.URLField()
    message = models.CharField(max_length=500)
    label = models.TextField(max_length=2000, null=True)
    button_text = models.TextField(max_length=50, null=True, default='Button')
    

class ChoicesOptions(models.Model):
    choices = models.ForeignKey(Choices, on_delete=models.CASCADE)
    option = models.CharField(max_length=1000)
    id = models.UUIDField(primary_key=True, default=uuid4)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class UserReponse(models.Model):
    user_id = models.UUIDField(default=uuid4)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(null=True, blank=True)
    block = models.ForeignKey('SurveyBlockType', on_delete=models.CASCADE, null=True)
    response = models.CharField(max_length=2000)
    browser_type = models.TextField(null=True, blank=True)



    # Validation here!
    pass

class SurveySettings(models.Model):
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    show_progress_bar = models.BooleanField(default=True)
    show_question_number = models.BooleanField(default=True)

class Design(models.Model):

    class Colors(models.TextChoices):
        BLUE = 'BLUE',_('BLUE')
        GREEN = 'GREEN',_('GREEN')
        YELLOW = 'YELLOW',_('YELLOW')

    class FontSize(models.TextChoices):
        SMALL = 'SMALL',_('SMALL')
        MEDIUM = 'MEDIUM',_('MEDIUM')
        LARGE = 'LARGE',_('LARGE')

    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    color = models.TextField(choices=Colors.choices, default=Colors.GREEN, max_length=10)
    font_size = models.TextField(choices=FontSize.choices, default=FontSize.MEDIUM, max_length=10)
    background_img = models.URLField()



class SurveyBlockType(models.Model):

    class BlockType(models.TextChoices):
        ContactInfo = "ConatctInfo", _('ContactInfo')
        Email = 'Email', _("Email")
        PhoneNumber = 'PhoneNumber', _('PhoneNumber')
        Website = "Website", _('Website')
        Choices = "Choices", _('Choices')
        Dropdown = "DropDown", _('DropDown')
        PictureChoice = "PictureChoice", _('PictureChoice')
        YesNo = "YesNo", _("YesNo")
        Rating = "Rating", _('Rating')
        LongText = "LongText", _("LongText")
        ShortText = "ShortText", _("ShortText")
        Time = "Time", _("Time")
        Date ="Date",_("Date")
        Number = "Number",_("Number")
        QuestionGroup = "QuestionGroup",('QuestionGroup')
        EndScreen= "EndScreen",_("EndScreen")
        RedirectToURL = "RedirectToURL", _("RedirectToURL")
        WelcomeScreen = "WelcomeScreen", _("WelcomeScreen")

    
    id = models.UUIDField(default=uuid4, primary_key=True)
    question = models.TextField(max_length=250, null=True)
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE, related_name='survey_blocks')
    block_type = models.TextField(choices=BlockType.choices, default=BlockType.ShortText)
    is_required = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    label = models.TextField(max_length=5000, null=True, blank=True)
    dropdown = models.ForeignKey(DropDown, on_delete=models.CASCADE, null=True, blank=True, related_name='dropdown_blocks')
    ratings = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True, blank=True, related_name='rating_blocks')
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, blank=True, related_name='email_blocks')
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE, null=True, blank=True, related_name='phone_number_blocks')
    picture_choice = models.ForeignKey(PictureChoice, on_delete=models.CASCADE, null=True, blank=True, related_name='picture_choice_blocks')
    date = models.ForeignKey(Date, on_delete=models.CASCADE, null=True, blank=True, related_name='date_blocks')
    number = models.ForeignKey(Number, on_delete=models.CASCADE, null=True, blank=True, related_name='number_blocks')
    short_text = models.ForeignKey(ShortText, on_delete=models.CASCADE, null=True, blank=True, related_name='short_text_blocks')
    long_text = models.ForeignKey(LongText, on_delete=models.CASCADE, null=True, blank=True, related_name='long_text_blocks')
    choices = models.ForeignKey(Choices, on_delete=models.CASCADE, null=True, blank=True, related_name='choices_blocks')
    yes_no = models.ForeignKey(YesNo, on_delete=models.CASCADE, null=True, blank=True, related_name='yes_no_blocks')
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True, blank=True, related_name='website_blocks')
    redirect_with_url = models.ForeignKey(RedirectWithUrl, on_delete=models.CASCADE, null=True, blank=True, related_name='redirect_with_url_blocks')
    welcome_screen = models.ForeignKey(WelcomeScreen, on_delete=models.CASCADE, null=True, blank=True, related_name='welcome_screen_blocks')
    end_screen = models.ForeignKey(EndScreen, on_delete=models.CASCADE, null=True, blank=True, related_name='end_screen_blocks')
    index = models.PositiveIntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.survey.name + ' ' + self.block_type
    
    # def correct_all_index(self):
    #     all_blocks_gt_current_index = SurveyBlockType.objects.filter(survey__id=self.survey.id, index__gt=self.index)
    #     print(all_blocks_gt_current_index)
    #     for i in all_blocks_gt_current_index:
    #         all_blocks_gt_current_index[i].index += 1
    #         all_blocks_gt_current_index[i].save()
            
    # def save(self, *arg, **kwarg):
    #     self.correct_all_index()
    #     super().save(*arg, **kwarg)





