from django import forms
from django.forms import ModelForm
from .models import Golfer

class ScoreForm(ModelForm):
    class Meta:
        model = Golfer
        fields = (
            "do_dodge",
            "elbow_room",
            "wigwam",
            "depot",
            "sports_page",
            "reboot",
            "mouse_trap",
            "clancys",
            "dooleys",
            "gi",
            "brothers",
            "pio",
            "pickle",
            "shenanns",
            "brat"
        )

        labels = {
            "do_dodge": 'Do Dodge',
            "elbow_room": 'Elbow Room',
            "wigwam": 'Wigwam',
            "depot": 'Depot',
            "sports_page": 'Sports Page',
            "reboot": 'Reboot',
            "mouse_trap": 'Mouse Trap',
            "clancys": 'Clancy\'s',
            "dooleys": 'Dooleys',
            "gi": 'GI',
            "brothers": 'Brothers',
            "pio": 'Pio',
            "pickle": 'Pickle',
            "shenanns": 'She-Nanns',
            "brat": 'Brat'
        }

        widgets = {
            "do_dodge": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "elbow_room": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "wigwam": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "depot": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "sports_page": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "reboot": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "mouse_trap": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "clancys": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "dooleys": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "gi": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "brothers": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "pio": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "pickle": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "shenanns": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'}),
            "brat": forms.NumberInput(attrs={'class':'score-input rounded', 'readonly': 'readonly'})
        }