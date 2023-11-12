from django.db import models
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    """Profile model"""

    username = models.CharField(_('username'), max_length=100, unique=True, db_index=True)
    user_id = models.CharField(_('user_id'), max_length=20, unique=True, db_index=True)
    full_name = models.CharField(max_length=200,blank=True)
    points = models.IntegerField(default=0)
    profile_image_url = models.URLField(_("profile_image_url"),default = 'https://img.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_138676-2387.jpg?w=740&t=st=1699500630~exp=1699501230~hmac=b24973b64cc2f563099c02f0f0d0fde3caa3611bcf086fc17674934db52b887f', max_length=1000)
    bg_image_url = models.URLField(_("bg_image_url"),default = 'https://img.freepik.com/free-photo/free-photo-black-grunge-abstract-background-pattern-wallpaper_1340-34108.jpg?t=st=1699500772~exp=1699504372~hmac=658dd763edb14036f4525432330b4e7a8eaaf237430b17d952d1572cd64eadeb&w=740', max_length=1000)
    is_mentor = models.BooleanField(_("is_mentor"),default=False)
    bio = models.TextField(blank=True)
    company = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        indexes = [
            models.Index(fields=['username', 'user_id'])
        ]
        

class MentorProfile(models.Model):
    """ Mentor Profile model"""
    profile = models.ForeignKey("profiles.UserProfile", verbose_name=_("Mentor Profile"), on_delete=models.CASCADE)
    position = models.IntegerField(_("position"),null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.username

        
class Topics(models.Model):
    """
    This model is designed for users to add topics in there intrests and to find peoples with common intrests
    """
    subject = models.CharField(_("subject"), max_length=50,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class UserIntrests(models.Model):
    """ Modles for users for adding there intrests  """
    topic = models.ForeignKey("profiles.Topics", verbose_name="Intrested Topics", on_delete=models.CASCADE)
    user = models.ForeignKey("profiles.UserProfile", verbose_name=_("Intrested users"), on_delete=models.CASCADE)


class UserLinks(models.Model):
    """Service type model"""
    profile = models.ForeignKey("profiles.UserProfile", verbose_name=_("User Links"), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=100,null=True)
    url = models.URLField(_('url'))

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        db_table = 'user_links'
    def __str__(self) -> str:
        return self.profile.username + ' ' + 'title'
