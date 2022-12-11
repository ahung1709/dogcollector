from django.shortcuts import render
from django.http import HttpResponse

# Add the Dog class & list and view function below the imports
class Dog: # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Mango', 'Golden Retriever', 'Scottish breed of retriever dog of medium size', 5), 
    Dog('Yeti', 'Husky', 'Medium-sized working sled dog breed', 3), 
    Dog('Ranger', 'Rough Collie', 'Sable and white, where the "sable" ranges from pale tan to a mahogany', 3), 
    Dog('Quicksilver', 'German Shepherd', 'Domed forehead, a long square-cut muzzle with strong jaws and a black nose', 4)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello 🐕🐕🐕</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { "dogs": dogs })