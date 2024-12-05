
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import numpy as np

# Charger le modèle
with open('prediction/model/Appartment_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@api_view(['POST'])
def predict_price(request):
    data = request.data
    try:
        # Extraire les attributs
        category = int(data.get('category'))
        surface = float(data.get('surface'))
        meublee = int(data.get('meublee'))  # 1 pour Oui, 0 pour Non
        chambre = int(data.get('nombre_de_chambres'))
       
        # Préparer les données pour la prédiction
        features = np.array([[category, surface, meublee, chambre]])
        predicted_price = model.predict(features)[0]

        # Retourner la prédiction
        return Response({'predicted_price': predicted_price})
    except Exception as e:
        return Response({'error': str(e)}, status=400)