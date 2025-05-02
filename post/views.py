from django.shortcuts import render


# Main
def main(request):
    return render(request,'main.html')