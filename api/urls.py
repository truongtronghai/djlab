from sys import api_version
from django.urls import path
import mimetypes

from .views.index import IndexView # restruct Dj structrure in folder so I import index like this

app_name = "api"

urlpatterns = [
    path("", IndexView.as_view() , name="index"), # using class view rather than function view
]

# add minetype for Js in case of browser prevent from a disallowed MIME type
mimetypes.add_type("application/javascript", ".js", True)