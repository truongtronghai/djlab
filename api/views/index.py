from django.shortcuts import render
from django.views import View

# Create your view of index here.
class IndexView(View):
    template_name = "api/index.html"

    def get(self,req):
        context = {
            "title" : "Django Lab",
            "content": "Hello Django. I\'m back. Working with backend technology."
        }
        return render(req, self.template_name, context)