from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
# from .models import Dog
# from django.http import HttpResponse

# Add the Dog class & list and view function below the imports
# class Dog: # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# dogs = [
#     Dog('Mango', 'Golden Retriever', 'Scottish breed of retriever dog of medium size', 5), 
#     Dog('Yeti', 'Husky', 'Medium-sized working sled dog breed', 3), 
#     Dog('Ranger', 'Rough Collie', 'Sable and white, where the "sable" ranges from pale tan to a mahogany', 3), 
#     Dog('Quicksilver', 'German Shepherd', 'Domed forehead, a long square-cut muzzle with strong jaws and a black nose', 4)
# ]

# Create your views here.

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    # Let's disallow the renaming of a dog by excluding the name field!
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

def home(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>Hello 🐕🐕🐕</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { "dogs": dogs })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog':dog })

