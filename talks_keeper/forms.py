from django import forms

from .models import Label, Talk


class TalkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TalkForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        labels = Label.objects.all()
        for label_ in labels:
            if instance is None:
                initial = False
            else:
                initial = label_.talks.filter(id=instance.id).exists()
            self.fields.update({
                'label_{}'.format(label_.id): forms.BooleanField(
                    label=label_.name,
                    required=False,
                    initial=initial,
                )})

    class Meta:
        model = Talk
        exclude = ['company']

    def save(self, commit=True):
        talk = super(TalkForm, self).save()
        for label_ in Label.objects.all():
            if self.cleaned_data['label_{}'.format(label_.id)]:
                label_.talks.add(talk)
