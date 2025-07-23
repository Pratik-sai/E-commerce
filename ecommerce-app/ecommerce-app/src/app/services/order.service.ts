import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private apiUrl = 'http://127.0.0.1:8000/od_app/orders';  // Replace with your Django API URL

  constructor(private http: HttpClient) { }

  // Get orders
  getOrders(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  // Place an order
  placeOrder(orderData: any): Observable<any> {
    return this.http.post(this.apiUrl, orderData);
  }
}
