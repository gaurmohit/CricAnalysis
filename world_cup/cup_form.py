from django import forms

class world_cup_form(forms.Form):
    conti = forms.CharField(label = "conti",
                             max_length=25,
                             required = False,)
    
    group_type = forms.IntegerField(label = "group_type",
                                 required = False,)

    num_of_teams_a = forms.IntegerField(label = "num_of_teams",
                                  required = False,)
        
    num_of_teams_b = forms.IntegerField(label = "num_of_teams",
                                  required = False,)
        
    num_of_teams = forms.IntegerField(label = "num_of_teams",
                                  required = False,)

    team_a = forms.CharField(label = "teams_a",
                            required = False,)
            
    team_b = forms.CharField(label = "team_b",
                            required = False,)

    teams = forms.CharField(label = "teams",
                            required = False,)