from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for adding or editing a review.
    """

    class Meta:
        model = Review  # Specifies the model to use for the form
        # Specifies the fields to include in the form
        fields = ('title', 'content', 'rating',)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor

        # Define placeholders for form fields
        placeholders = {
            'title': 'Title',
            'content': 'Your Review',
            'rating': 0
        }

        # Set attributes for title field
        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['aria-label'] = 'Review Title'

        # Set attribute for content field
        self.fields['content'].widget.attrs['aria-label'] = 'Review Content'

        # Loop through fields to set placeholders, classes, and labels
        for field in self.fields:
            if self.fields[field].required:
                # Add '*' to required fields
                placeholder = f'{placeholders[field]} *'  
            else:
                placeholder = placeholders[field]
            # Set placeholder and class attributes for the field
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = \
                'border-black rounded-0 mt-3 mb-3'                 
            # Hide the field labels in the form
            self.fields[field].label = False
