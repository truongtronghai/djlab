from django.urls import path
from .views.serialization_sample import SampleSerializationApiView

urlpatterns = [
    path("/", SampleSerializationApiView.as_view(), name="sample_serialization")
]
