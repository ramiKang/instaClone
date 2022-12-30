from rest_framework.views import APIView
from django.shortcuts import render

class Sub(APIView):
    def get(self,request):
        print("겟으로 호출")
        return render(request,"ramstargram/main.html")

    def post(self,request):
        print("포스트로 호출")
        return render(request,"ramstargram/main.html")
