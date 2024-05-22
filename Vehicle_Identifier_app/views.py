import os
import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleImageForm
from .models import VehicleImage
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials


#defines the function for the index view.
def index(request):
    if request.method == 'POST': #Index or the home page has a form submission so requires a POST request
        form = VehicleImageForm(request.POST, request.FILES) #creating the form instance
        # if statement checks is the form is valid and then calls on the custom vision model to predict type and save details to database
        if form.is_valid():
            vehicle_image = form.save(commit=False)
            vehicle_image.image = request.FILES['image']
            vehicle_image.save()

            image_path = vehicle_image.image.path

            prediction = get_vehicle_type(image_path)
            vehicle_image.vehicle_type = prediction
            vehicle_image.insurance_price = generate_insurance_price()
            vehicle_image.save()
            return redirect('result', pk=vehicle_image.pk)
    else:
        form = VehicleImageForm() #creates an empty instance if not a POST request
    return render(request, 'index.html', {'form': form}) #renders the index.html file with the form

#Defines the result view
def result(request, pk):
    vehicle_image = get_object_or_404(VehicleImage, pk=pk) #retrieves the the VehicleImage object using a primary key or a 404 error if not found
    return render(request, 'result.html', {'vehicle_image': vehicle_image}) #renders result.html with vehicle_image

#defines the search_page view
def search_page(request):
    return render(request, 'search_page.html') #rendering

#defines the search function
def search(request):
    reference_number = request.GET.get('reference_number') #uses a GET request to retrieve a ref number saved in db
    return redirect('reference', reference_number=reference_number)

#defines the reference view with error handling
def reference(request, reference_number):
    try:
        vehicle_image = VehicleImage.objects.get(reference_number=reference_number) #retrieves the VehicleImage object using the reference number entered in search
        return render(request, 'reference.html', {'vehicle_image': vehicle_image})
    except VehicleImage.DoesNotExist:
        return render(request, 'NoQuote.html') #renders the no quote found page if the object doesn't exist

#defines the function to get identify the vehicle type
def get_vehicle_type(image_path):
    prediction_key = os.getenv('PREDICTION_KEY')
    endpoint = os.getenv('PREDICTION_ENDPOINT')
    project_id = os.getenv('PROJECT_ID')
    iteration_name = os.getenv('ITERATION_NAME')

    credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key}) #API key credentials
    predictor = CustomVisionPredictionClient(endpoint, credentials) #creates a prediction client

    with open(image_path, 'rb') as image_data: #open image file in binary mode
        results = predictor.classify_image(project_id, iteration_name, image_data.read()) #sending image to client for classification

    top_prediction = max(results.predictions, key=lambda p: p.probability) #assigns the prediction with the highest probability
    return top_prediction.tag_name #returns tag name of top prediction


#Random number generator for the insurance price of the vehicle
def generate_insurance_price():
    return round(random.uniform(500, 2000), 2)
