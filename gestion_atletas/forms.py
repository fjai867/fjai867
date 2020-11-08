from django import forms
from gestion_atletas.models import Atleta,Inscripcion
from django.contrib.auth.forms import PasswordChangeForm





class fmrAtletas(forms.ModelForm):
    class Meta:
        model=Atleta

        fields=[

            'Id_Atleta',
            'Num_Matri',
            'Nom',
            'Ape',
            'Dire',
            'Pobla',
            'Cod_Pos',
            'Tel',
            'Fecha_Nac',
            'email',
            
            
            ]
        labels={
            'Num_Matri': 'Numero de Matricula',
            'Nom':'Nombre',
            'Ape':'Apellidos',
            'Dire': 'Diereccion',
            'Pobla': 'Poblacion',
            'Cod_Pos': 'Codigo Postal',
            'Tel': 'Telefono',  
            'Fecha_Nac': 'Fecha Nacimiento',
            'email': 'E-mail',
            
            
            
            
             }
       

        widgets={
            'Num_Matri': forms.TextInput(attrs={'class':'form-control'}),
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
            'Ape':forms.TextInput(attrs={'class':'form-control'}),
            'Dire': forms.TextInput(attrs={'class':'form-control'}),
            'Pobla': forms.TextInput(attrs={'class':'form-control'}),
            'Cod_Pos':forms.TextInput(attrs={'class':'form-control'}), 
            'Tel': forms.TextInput(attrs={'class':'form-control'}),  
            'Fecha_Nac': forms.DateInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            
            }

class fmrAtletasEdit(forms.ModelForm):
    class Meta:
        model=Atleta
        


        fields=[

            'Id_Atleta',
            'Num_Matri',
            'Nom',
            'Ape',
            'Dire',
            'Pobla',
            'Cod_Pos',
            'Tel',
            'Fecha_Nac',
            'email',
            
            
            ]
        labels={
            'Num_Matri': 'Numero de Matricula',
            'Nom':'Nombre',
            'Ape':'Apellidos',
            'Dire': 'Diereccion',
            'Pobla': 'Poblacion',
            'Cod_Pos': 'Codigo Postal',
            'Tel': 'Telefono',  
            'Fecha_Nac': 'Fecha Nacimiento',
            'email': 'E-mail',
            
            
            
            
             }
       

        widgets={
            'Num_Matri': forms.TextInput(attrs={'class':'form-control'}),
            'Nom':forms.TextInput(attrs={'class':'form-control'}),
            'Ape':forms.TextInput(attrs={'class':'form-control'}),
            'Dire': forms.TextInput(attrs={'class':'form-control'}),
            'Pobla': forms.TextInput(attrs={'class':'form-control'}),
            'Cod_Pos':forms.TextInput(attrs={'class':'form-control'}), 
            'Tel': forms.TextInput(attrs={'class':'form-control'}),  
            'Fecha_Nac': forms.DateInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            
            }

    def __init__(self, *args, **kwargs):

        super(fmrAtletasEdit, self).__init__(*args, **kwargs)
       
        self.fields['Nom'].widget.attrs['readonly'] = 'readonly'
        
        self.fields['Ape'].widget.attrs['readonly'] = 'readonly'
        
        self.fields['email'].widget.attrs['readonly'] = 'readonly'

        self.fields['Fecha_Nac'].widget.attrs['readonly'] = 'readonly'



class Nuevo_PasswordChangeForm(PasswordChangeForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class':'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control'})
        