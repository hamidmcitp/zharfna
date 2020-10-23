from django.shortcuts import render
from .models import Singer,Owner,RbtMusic

def rbt(request):

    # Farakhani az Database = az RbtMusic be rbts
    rbts = RbtMusic.objects.all()

    return render(request,'rbt/rbt.html', {'rbts': rbts} )

# for Page home
def home(request):
    return render(request,'rbt/home.html')