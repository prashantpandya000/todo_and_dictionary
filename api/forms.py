from django import forms
import requests

class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://owlbot.info/api/v4/dictionary/{word}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'Authorization': 'Token 8d1301b449cf197316984ff5b92d274439c69c90'}
        response = requests.get("GET",url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The  API is not available at the moment. Please try again later.'
        print(result)
        return result

DictionaryForm('hello')