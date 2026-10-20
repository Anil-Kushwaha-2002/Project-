# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Insight
from .serializers import InsightSerializer

# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # This assumes you have an index.html template


class InsightAPI(APIView):
    def get(self, request):
        # Fetching filters from the request
        year = request.GET.get('year', None)
        sector = request.GET.get('sector', None)

        # Query the database and apply filters
        insights = Insight.objects.all()
        
        if year:
            insights = insights.filter(end_year=year)  # Apply the year filter
        if sector:
            insights = insights.filter(sector=sector)  # Apply the sector filter

        # Serialize and return the filtered data
        serializer = InsightSerializer(insights, many=True)
        return Response(serializer.data)

