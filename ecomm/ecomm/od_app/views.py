from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, Sum
import datetime
from .models import Cart, Order
from .serializers import CartSerializer, OrderSerializer

# Create your views here.

def index(request):
    return render(request,'od_app/index.html')

class CartView(APIView):
    def get(self,request):
        orders = Cart.objects.all()
        serializer = CartSerializer(orders, many= True)
        return Response(
            {
                "status": "success",
                "data": serializer.data
            },
            status = status.HTTP_200_OK
        )
    def post(self, request):
        
        total_amount = float(request.data.get('quantity')) * float(request.data.get('amount'))
        order = Order.objects.create(cust_id=1,order_amount = total_amount, order_date = datetime.datetime.now().strftime("%Y-%m-%d"))
        #mutable = request.data._mutable
        #request.data._mutable = True
        req = request.data.copy()
        req['order_id'] = str(order.id)
        #request.data['cust_id'] = 300
        print(req)
        serializer = CartSerializer(data=req)
        #serializer = self.get_serializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "status": "success",
                "data": serializer.data
            },
            status = status.HTTP_200_OK
        )
        else:
            return Response(
                {
                  "status": "error",
                  "data": serializer.error
                },
                status = status.HTTP_400_BAD_REQUEST
            )
'''        
    def create(self, request, *arg, **kwargs):
        total_amount = 0
        if isinstance(request.data, list):
            for item in request.data:
                total_amount += request.data.get('quantity') * request.data.get('amount')
            cart = Cart.objects.create(order_amount = total_amount, order_date = datetime.datetime.now().strftime("%Y-%m-%d"))
            mutable = request.data._mutable
            request.data._mutable = True
            request.data['order_id_id'] = str(cart.id)
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            new_data={}
            total_amount = float(request.data.get('quantity') * request.data.get('amount'))
            cart = Cart.objects.create(order_amount = total_amount, order_date = datetime.datetime.now().strftime("%Y-%m-%d"))
            mutable = request.data._mutable
            request.data._mutable = True
            request.data['order_id_id'] = str(cart.id)
            print(request.data)
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid()
        self.perform_create(serializer)
        headers = self.get_success_header(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, header=headers)
'''


class OrderView(APIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many= True)
        return Response(
            {
                "status": "success",
                "data": serializer.data
            },
            status = status.HTTP_200_OK
        )
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        #total = Cart.objects.filter(Order= Order).aggregate(total=Sum(F('quantity')* F('amount')))['total'] or 0
        #Order.order_amount = total
        #Order.save()
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "status": "success",
                "data": serializer.data
            },
            status = status.HTTP_200_OK
        )
        else:
            return Response(
                {
                  "status": "error",
                  "data": serializer.error
                },
                status = status.HTTP_400_BAD_REQUEST
            )
    