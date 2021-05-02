from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1>Vítej v autopůjčovně trpasličích aut!</h1>"
                            "<h2>Máme auta těch nejmenších velikostí:</h2>"
                            "<ul>"
                                "<li>Opravdu malá auta</li>"
                                "<li>Opravdu hodně malá auta</li>"
                                "<li>Ty opravdu nejvíc nejmenší auta. Skutečná autíčka</li>"
                            "<p>Na katalog se můžeš podívat zde:<br></p>"
                            "<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>")

class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam trpasličích aut.")