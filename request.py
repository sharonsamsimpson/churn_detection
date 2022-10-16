import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url,json={'credit_score':608,
                            'country':0,
                            'gender':0,
                            'age':21,
                            'tenure':0,
                            'balance':0,
                            'products_number':0,
                            'credit_card':0,
                            'active_member':0,
                            'estimated_salary':0 })

print(r.json())
