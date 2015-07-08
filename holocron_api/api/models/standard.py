from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_key = models.CharField(max_length=100, blank=True, null=True,
                                    unique=True)
    campaign_name = models.CharField(max_length=100)
    campaign_description = models.CharField(max_length=140)
    created_by = models.CharField(max_length=100)
    campaign_notes = models.CharField(max_length=140, blank=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_key


# method for updating the key to match the id if it is null/blank
def update_key(sender, *args, **kwargs):
    i = kwargs['instance']
    if i.campaign_key is None or i.campaign_key == "":
        i.campaign_key = i.campaign_id
        i.save()
    else:
        i2 = slugify(i.campaign_key)
        if i.campaign_key != i2:
            i.campaign_key = i2
            i.save()
        else:
            pass


# register the signal
post_save.connect(update_key, sender=Campaign)


class Medium(models.Model):
    medium_key = models.SlugField(max_length=100, primary_key=True)
    medium_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medium_key


class Source(models.Model):
    source_key = models.SlugField(max_length=100, primary_key=True)
    source_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_key


class Creative(models.Model):
    creative_id = models.AutoField(primary_key=True)
    creative_name = models.CharField(max_length=100)
    creative_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creative_name


class Placement(models.Model):
    placement_id = models.AutoField(primary_key=True)
    placement_name = models.CharField(max_length=100)
    placement_url = models.CharField(max_length=250)
    campaign = models.ForeignKey(Campaign)
    medium = models.ForeignKey(Medium)
    source = models.ForeignKey(Source)
    creative = models.ForeignKey(Creative)
    catid = models.IntegerField(blank=True, null=True)
    pageCat = models.CharField(max_length=100, blank=True, null=True)
    pageID = models.CharField(max_length=100, blank=True, null=True)
    jira_ticket = models.CharField(max_length=20, blank=True, default="")
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placement_id
