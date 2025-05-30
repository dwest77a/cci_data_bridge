"""cci_data_bridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from data_bridge_app import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("admin/", admin.site.urls),
    path("dataset/", views.DatasetListView.as_view(), name="dataset-list"),
    path("dataset/<int:pk>", views.DatasetDetailView.as_view(), name="dataset-detail"),
    path("dataset/<path:url>", views.DatasetUrlDetailView.as_view()),
    path("project/", views.ProjectListView.as_view(), name="project-list"),
    path(
        "relationtype/", views.RelationTypeListView.as_view(), name="relation-type-list"
    ),
    path("sankey/", views.SankeyView.as_view(), name="sankey"),
    path("sankey/<slug:project>", views.SankeyProjectView.as_view(), name="sankey"),
    path("sankey/<path:url>", views.SankeyDatasetView.as_view(), name="sankey"),
    path("docs/api", views.DocsApiView.as_view(), name="docs-api"),
]
