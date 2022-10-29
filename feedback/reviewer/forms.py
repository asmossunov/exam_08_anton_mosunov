#
#
# class TaskForm(forms.ModelForm):
#     text = forms.CharField(
#         label='Текст',
#         validators=(MinLengthValidator(5), max_length_validator, first_number_validator, )
#     )
#     status = forms.ModelChoiceField(
#         label='Статус',
#         queryset=Status.objects.all(),
#         initial='New'
#     )
#     types = forms.ModelMultipleChoiceField(
#         label='Тип',
#         queryset=Type.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
#
#     class Meta:
#         model = Task
#         fields = ('text', 'description', 'status', 'types')
#         widgets = {
#             'text': forms.TextInput(attrs={'class': 'form-input'}),
#             'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),
#
#             }
